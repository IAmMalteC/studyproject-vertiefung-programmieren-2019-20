from app import list_of_characters
from database.databasemodel import Base, User_TB, Cesar_TB, MonoAlphabeticSubstitution_TB, EncodedString_TB, EncryptionType_TB
from encryption import Cesar, MonoAlphabetic
from flask import Flask, render_template, redirect, request, session, flash
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from forms import LoginForm, EncryptionForm, LogoutForm
from functools import wraps
from userinput import offset

webapp = Flask(__name__,
               template_folder="templates",
               static_folder="static")
# Storing our configuration settings in config.py
webapp.config.from_object('config.Config')

db = SQLAlchemy(webapp)
sess = Session(webapp)
csrf = CSRFProtect(webapp) # CSRFProtection

# Todo add password to App.py


# Own decorators
def check_user_is_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'current_user' in session:
            return func(*args, **kwargs)
        else:
            flash("Please login first.", "error")
            return redirect('/login')
    return wrapper


def check_if_the_user_has_encrypted_text(func):
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
    # creates the database if it isn't existing
    Base.metadata.create_all(bind=db.engine)


# Routing
@webapp.route("/login", methods=['GET', 'POST'])
@webapp.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form['username']
        username = username.lower()
        password = request.form['password']
        # save to session
        session['current_user'] = str(username)
        existing_user = db.session.query(User_TB).filter(User_TB.user_name == username).first()
        if existing_user.user_password == password:
            return redirect("/encryption")
        elif existing_user:
            flash("Wrong password","error")
            return redirect('/login')
        flash("Please register first","error")
        return redirect('/register')
    return render_template('login.html', form=form)


@webapp.route("/register", methods=['GET', 'POST'])
def register():
    form = LogoutForm()
    if form.validate_on_submit():
        username = request.form['username']
        username = username.lower()
        password = request.form['password']
        # save to session
        session['current_user'] = str(username)
        existing_user = db.session.query(User_TB).filter(User_TB.user_name == username).first()
        if existing_user:
            flash("Your are already registerd, please login", "error")
            return redirect("/register")
        new_user = User_TB(username, password)
        db.session.add(new_user)
        db.session.commit()
        flash("Succesfully registered.", "session")
        return redirect("/register")
    return render_template('register.html', form=form)


@webapp.route("/encryption", methods=['GET', 'POST'])
@check_user_is_logged_in
def display_encryption_page():
    form = EncryptionForm()
    # if request.method == 'POST':
    if form.validate_on_submit():
        string_to_encrypt = request.form['string_to_encrypt']
        encryptiontype = request.form['encryptiontype']
        new_encodedstring = ''
        if encryptiontype == 'cesar':
            offsetfactor = offset.get_offset(request.form['offset'])
            # save to session
            session['offset'] = str(offsetfactor)
            for letter in string_to_encrypt:
                new_encodedstring += Cesar.encrypter(offsetfactor, letter, list_of_characters)
            new_cesar = Cesar_TB(offsetfactor)
            db.session.add(new_cesar)
            db.session.commit()
        else:
            new_mono = MonoAlphabeticSubstitution_TB()
            db.session.add(new_mono)
            db.session.commit()
            list_of_characters_reverse = MonoAlphabetic.reverse_text(list_of_characters)
            for letter in string_to_encrypt:
                new_encodedstring += MonoAlphabetic.encrypter(letter, list_of_characters, list_of_characters_reverse)

        # to get the encryptiontype from the DB -- It searches for the last item
        type = db.session.query(EncryptionType_TB).filter(EncryptionType_TB.encryption_type_type == encryptiontype).order_by(EncryptionType_TB.encryption_type_id.desc()).first()
        # to get the user from the DB
        username = str(session['current_user'])
        user = db.session.query(User_TB).filter(User_TB.user_name == username).first()
        new_string = EncodedString_TB(new_encodedstring, user.user_id, type.encryption_type_id)
        db.session.add(new_string)
        db.session.commit()
        # save to session
        session['encryptiontype'] = str(encryptiontype)
        session['unencoded_string'] = str(string_to_encrypt)
        session['encoded_string'] = str(new_encodedstring)
        return redirect("/result")
    return render_template('encryption.html', form=form, current_user=str(session['current_user']))


@webapp.route("/result", methods=['GET', 'POST'])
@check_user_is_logged_in
@check_if_the_user_has_encrypted_text
def display_result_page():
    # .pop deletes the content
    encryptiontype = str(session['encryptiontype'])
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
    return render_template('result.html', encryptiontype=encryptiontype, offset=offsetfactor, unencoded_string = unencoded_string, encoded_string=encoded_string)


@webapp.route("/users", methods=['GET'])
@check_user_is_logged_in
def show_users():
    all_users = db.session.query(User_TB).order_by(User_TB.user_name).all()
    return render_template('users.html', useroutput=all_users)


@webapp.route("/logout", methods=['GET'])
@check_user_is_logged_in
def logout():
    session.clear()
    flash("Successfully logged out.", "session")
    return redirect('/')

# Just for debugging!
if __name__ == "__main__":
    webapp.run(debug=True)
