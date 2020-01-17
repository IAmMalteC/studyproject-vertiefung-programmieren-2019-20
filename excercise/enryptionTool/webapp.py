import string
from functools import wraps

from flask import Flask, render_template, session, redirect, request, flash
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from database.databasemodel import Base, User_TB, Cesar_TB, MonoAlphabeticSubstitution_TB, EncodedString_TB, EncryptionType_TB
from encryption import Cesar, MonoAlphabetic
from forms import LoginForm, EncryptionForm
from userinput import offset

webapp = Flask(__name__,
               template_folder="templates",
               static_folder="static")
# Storing our configuration settings in config.py
webapp.config.from_object('config.Config')

db = SQLAlchemy(webapp)
sess = Session(webapp)

# TODO add Validation/Requirment to forms


# Own decorators
def user_is_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'current_user' in session:
            return func(*args, **kwargs)
        else:
            flash("Bitte erst einloggen.")
            return redirect('/login')
    return wrapper


@webapp.before_first_request
def setup():
    # creates the table
    Base.metadata.create_all(bind=db.engine)
    # session['testing_login'] = 1


# Routing
# TODO if user exists let him not enter this site redirect to encryption
@webapp.route("/login", methods=['GET', 'POST'])
@webapp.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = request.form['username']
        username = username.lower()
        # save to session
        session['current_user'] = str(username)
        existing_user = db.session.query(User_TB).filter(User_TB.user_name == username).first()
        if existing_user:
            return redirect("/encryption")
        new_user = User_TB(username)
        db.session.add(new_user)
        db.session.commit()
        return redirect("/encryption")
    elif request.method == 'GET':
        return render_template('login.html', form=form)
    # if request.method == 'POST':
    #     # Wieso wird der erste Teil ausgeführt aber der zweite Nicht? Ich verstehe nicht, warum nichts gespeichert wird
    #     if form.validate() == False:
    #         return render_template('login.html', form=form)
    #     else:
    #         username = request.form['username']
    #         username = username.lower()
    #         # save to session
    #         session['current_user'] = str(username)
    #         existing_user = db.session.query(User_TB).filter(User_TB.user_name == username).first()
    #         if existing_user:
    #             return redirect("/encryption")
    #         new_user = User_TB(username)
    #         db.session.add(new_user)
    #         db.session.commit()
    #         return redirect("/encryption")
    # elif request.method == 'GET':
    #     return render_template('login.html', form=form)


# list which defines the scope of values used for encryption
list_of_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation


@webapp.route("/encryption", methods=['GET', 'POST'])
@user_is_logged_in
def display_encryption_page():
    if request.method == 'POST':
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
    # if GET:
    form = EncryptionForm()
    # if form.validate_on_submit():
    #     return redirect(url_for('success'))
    return render_template('encryption.html', form=form, current_user=str(session['current_user']))


@webapp.route("/result", methods=['GET', 'POST'])
@user_is_logged_in
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


# Just for debugging!
if __name__ == "__main__":
    webapp.run(debug=True)
