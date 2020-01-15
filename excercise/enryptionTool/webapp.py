import string
from flask import Flask, render_template, session, redirect, url_for, escape, request, make_response, flash
from flask_session import Session
from sqlalchemy.orm import relationship
from forms import LoginForm, EncryptionForm, ResultForm
from flask_sqlalchemy import SQLAlchemy
from database.databasemodel import Base, User_TB, Cesar_TB, MonoAlphabeticSubstitution_TB, EncodedString_TB, \
    EncryptionType_TB
from encryption import Cesar, MonoAlphabetic

webapp = Flask(__name__,
               template_folder="templates",
               static_folder="static")
# Storing our configuration settings in config.py
webapp.config.from_object('config.Config')

db = SQLAlchemy(webapp)
sess = Session(webapp)


@webapp.before_first_request
def setup():
    # to add the relationship <-- Can properly be deleted
    # User_TB.encrypted_string = relationship("EncodedString", order_by=EncodedString_TB.id, back_populates="userstr")
    # EncryptionType_TB.encrypted_string = relationship("EncodedString", order_by=EncodedString_TB.id, back_populates="encryptiontyperelation")
    # creates the table
    Base.metadata.create_all(bind=db.engine)
    session['testing_login'] = 1


# Routing
# TODO if user exists let him not enter this site redirect to encryption
@webapp.route("/login", methods=['GET', 'POST'])
@webapp.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        username = username.lower()
        # save to session
        session['current_user'] = str(username)
        existing_user = db.session.query(User_TB).filter(User_TB.user_name == username).first()
        if existing_user:
            return redirect("/encryption")  # hier vielleicht den User/namen übergeben
        new_user = User_TB(username)
        db.session.add(new_user)
        db.session.commit()
        return redirect("/encryption")  # hier vielleicht den User/namen übergeben
    # if GET:
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('login.html', form=form)


# list which defines the scope of values
list_of_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation


@webapp.route("/encryption", methods=['GET', 'POST'])
def display_encryption_page():
    if request.method == 'POST':
        string_to_encrypt = request.form['string_to_encrypt']
        encryptiontype = request.form['encryptiontype']
        # save to session
        session['encryptiontype'] = str(encryptiontype)
        new_encodedstring = ''
        username = str(session['current_user'])
        if encryptiontype == 'cesar':
            offset = request.form['offset']
            # save to session
            session['offset'] = str(offset)
            for letter in string_to_encrypt:
                new_encodedstring = new_encodedstring + Cesar.encrypter(offset, letter, list_of_characters)
            new_cesar = Cesar_TB(offset)
            db.session.add(new_cesar)
        else:
            new_mono = MonoAlphabeticSubstitution_TB()
            db.session.add(new_mono)
            list_of_characters_reverse = MonoAlphabetic.reverse_text(list_of_characters)
            for letter in new_encodedstring:
                new_encodedstring = new_encodedstring + MonoAlphabetic.encrypter(letter, list_of_characters, list_of_characters_reverse)

        new_string = EncodedString_TB(new_encodedstring, username, encryptiontype)
        # save to session
        session['unencoded_string'] = str(string_to_encrypt)
        session['encoded_string'] = str(new_encodedstring)
        # if that is not working add:
        #   EncodedString_TB(new_encodedstring, username, "monoalphabeticsubstitution")
        #   EncodedString_TB(new_encodedstring ,.., "cesar")
        db.session.add(new_string)
        db.session.commit()
        return redirect("/result")
    # if GET:
    form = EncryptionForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('encryption.html', form=form, current_user=str(session['current_user']))


@webapp.route("/result", methods=['GET', 'POST'])
def display_result_page():
    # if not session.get(['current_user']) is None:
    # .pop deletes the content
    encryptiontype = str(session['encryptiontype'])
    session.pop('encryptiontype', None)
    if encryptiontype == 'cesar':
        offset = str(session['offset'])
    else:
        offset = ''
    session.pop('offset', None)
    unencoded_string = str(session['unencoded_string'])
    session.pop('unencoded_string', None)
    encoded_string = str(session['encoded_string'])
    session.pop('encoded_string', None)
    return render_template('result.html', encryptiontype=encryptiontype, offset=offset, unencoded_string = unencoded_string, encoded_string=encoded_string)
    # else:
    #     redirect('/')
    #     # it is possible to use categories : https://pythonise.com/series/learning-flask/flask-message-flashing
    #     flash("Bitte erst einloggen.")



# Just for debugging!
if __name__ == "__main__":
    webapp.run(debug=True)