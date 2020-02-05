from app import list_of_characters
from database.databasemodel import Base, UserTB, CesarTB, MonoAlphabeticSubstitutionTB, EncodedStringTB, \
    EncryptionTypeTB
from encryption import Cesar, MonoAlphabetic
from flask import Flask, render_template, redirect, request, session, flash
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from forms import LoginForm, EncryptionForm, RegisterForm
from functools import wraps
import requests
from userinput import offset

webapp = Flask(__name__,
               template_folder="templates",
               static_folder="static")
# Storing our configuration settings in config.py
webapp.config.from_object('config.Config')

# Create database session
db = SQLAlchemy(webapp)
# Creates session cookie
sess = Session(webapp)
# CSRFProtection
csrf = CSRFProtect(webapp)


# Own decorators
def check_user_is_logged_in(func):
    """ Checks if a user is logged in,
    if not the user is redirected to the login page.
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'current_user' in session:
            return func(*args, **kwargs)
        else:
            flash("Please login first.", "error")
            return redirect('/login')

    return wrapper


def check_if_the_user_has_encrypted_text(func):
    """ Checks if the user is trying to enter the result page from somewhere else then the encryption page.
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'encryptiontype' in session:
            return func(*args, **kwargs)
        else:
            flash("Let us first encrypt some text.", "error")
            return redirect('/encryption')

    return wrapper


@webapp.before_first_request
def setup():
    # Create the database, if it isn't existing
    Base.metadata.create_all(bind=db.engine)


# Routing
@webapp.route("/login", methods=['GET', 'POST'])
@webapp.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if 'current_user' in session:
        flash("You are already logged in.\nIf you want to login as an other user, you first have to logout.", "error")
        return render_template('login.html', form=form)

    if form.validate_on_submit():
        username = request.form['username']
        username = username.lower()
        password = request.form['password']

        existing_user = db.session.query(UserTB).filter(UserTB.user_name == username).first()
        if existing_user:
            # Last part added so that user, who already registered in the console app, can use the website.
            if existing_user.user_password == password or existing_user.user_password is None and password == '':
                # Save to session
                session['current_user'] = str(username)
                return redirect("/encryption")
            elif existing_user:
                flash("Wrong password", "error")
                return redirect('/login')
        flash("Please register first", "error")
        return redirect('/login')

    return render_template('login.html', form=form)


@webapp.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = request.form['username']
        username = username.lower()
        password = request.form['password']

        # # Save to session, if a person isn't logged in already.
        # if not 'current_user' in session:
        #     session['current_user'] = str(username)

        existing_user = db.session.query(UserTB).filter(UserTB.user_name == username).first()
        if existing_user:
            flash("Your are already registered, please login", "error")
            return redirect("/register")

        new_user = UserTB(username, password)
        db.session.add(new_user)
        db.session.commit()
        flash("Successfully registered.", "session")
        return redirect("/register")

    return render_template('register.html', form=form)


@webapp.route("/encryption", methods=['GET', 'POST'])
@check_user_is_logged_in
def display_encryption_page():
    form = EncryptionForm()
    if form.validate_on_submit():
        string_to_encrypt = request.form['string_to_encrypt']
        encryptiontype = request.form['encryptiontype']
        new_encodedstring = ''

        if encryptiontype == 'cesar':
            offsetfactor = offset.get_offset(request.form['offset'])
            # Save to session
            session['offset'] = str(offsetfactor)
            # Shorten offset factor
            short_offsetfactor= Cesar.shorten_cesar_offset(offsetfactor, list_of_characters)
            for letter in string_to_encrypt:
                new_encodedstring += Cesar.cesar_encrypter(short_offsetfactor, letter, list_of_characters)
            new_cesar = CesarTB(offsetfactor)
            db.session.add(new_cesar)
            db.session.commit()
        else:
            new_mono = MonoAlphabeticSubstitutionTB()
            db.session.add(new_mono)
            db.session.commit()
            list_of_characters_reverse = MonoAlphabetic.reverse_text(list_of_characters)
            for letter in string_to_encrypt:
                new_encodedstring += MonoAlphabetic.mono_encrypter(letter, list_of_characters,
                                                                   list_of_characters_reverse)

        # Get the encryptiontype from the database -- It searches for the last item
        encryption_type = db.session.query(EncryptionTypeTB) \
            .order_by(EncryptionTypeTB.encryption_type_id.desc()) \
            .first()

        # Get the user from the database
        username = str(session['current_user'])
        user = db.session.query(UserTB).filter(UserTB.user_name == username).first()

        new_string = EncodedStringTB(new_encodedstring, user.user_id, encryption_type.encryption_type_id)
        db.session.add(new_string)
        db.session.commit()

        # Save to session
        session['encryptiontype'] = str(encryptiontype)
        session['unencoded_string'] = str(string_to_encrypt)
        session['encoded_string'] = str(new_encodedstring)
        return redirect("/result")

    return render_template('encryption.html', form=form, current_user=str(session['current_user']))


@webapp.route("/result", methods=['GET', 'POST'])
@check_user_is_logged_in
@check_if_the_user_has_encrypted_text
def display_result_page():
    encryptiontype = str(session['encryptiontype'])
    # .pop deletes the content
    session.pop('encryptiontype', None)

    if encryptiontype == 'cesar':
        offsetfactor = str(session['offset'])
    else:
        offsetfactor = ''
    session.pop('offset', None)

    unencoded_string = str(session['unencoded_string'])
    session.pop('unencoded_string', None)

    encoded_string = str(session['encoded_string'])
    session.pop('encoded_string', None)

    return render_template('result.html',
                           encryptiontype=encryptiontype, offset=offsetfactor,
                           unencoded_string=unencoded_string, encoded_string=encoded_string)


@webapp.route("/users", methods=['GET'])
@check_user_is_logged_in
def show_users():
    all_users = db.session.query(UserTB).order_by(UserTB.user_name).all()
    return render_template('users.html', useroutput=all_users)


@webapp.route("/logout", methods=['GET'])
@check_user_is_logged_in
def logout():
    session.clear()
    flash("Successfully logged out.", "session")
    return redirect('/')


@webapp.route("/catfact", methods=['GET'])
@check_user_is_logged_in
def catfact():
    # Api documentation: https://alexwohlbruck.github.io/cat-facts/docs/
    response = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1")
    # parse response into json dictionary
    response_body = response.json()
    return render_template('catfact.html', catfact=response_body)


@webapp.route("/joke", methods=['GET'])
@check_user_is_logged_in
def joke():
    # Api documentation: http://www.icndb.com/api/
    # The results are escaped to html --> " = &quot;
    response = requests.get("http://api.icndb.com/jokes/random?escape=html")
    # parse response into json dictionary
    response_body = response.json()
    return render_template('joke.html', joke=response_body)


# Just for debugging!
if __name__ == "__main__":
    webapp.run(debug=True)
