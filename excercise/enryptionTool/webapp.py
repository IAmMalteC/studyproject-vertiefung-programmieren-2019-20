import string
from flask import Flask, render_template, session, redirect, url_for, escape, request, make_response
from sqlalchemy.orm import relationship
from forms import LoginForm, EncryptionForm, ResultForm
from flask_sqlalchemy import SQLAlchemy
from database.databasemodel import Base, User_TB, Cesar_TB, MonoAlphabeticSubstitution_TB, EncodedString_TB, EncryptionType_TB
from encryption import Cesar, MonoAlphabetic

webapp = Flask(__name__,
               template_folder="templates",
               static_folder="static")
# Storing our configuration settings in config.py
webapp.config.from_object('config.Config')

db = SQLAlchemy(webapp)


@webapp.before_first_request
def setup():
    # to add the relationship
    User_TB.encrypted_string = relationship("EncodedString", order_by=EncodedString_TB.id, back_populates="userstr")
    EncryptionType_TB.encrypted_string = relationship("EncodedString", order_by=EncodedString_TB.id, back_populates="encryptiontyperelation")
    # creates the table
    Base.metadata.create_all(bind=db.engine)


# Routing
@webapp.route("/login", methods=['GET', 'POST'])
@webapp.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        username = username.lower()
        existing_user = db.session.query(User_TB).filter(User_TB.name == username).first()
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


@webapp.route("/encryption/<username>", methods=['GET', 'POST'])
def display_encryption_page():
    if request.method == 'POST':
        string_to_encrypt = request.form['string_to_encrypt']
        encryptiontype = request.form['encryptiontype']
        new_encodedstring = ''
        if encryptiontype == 'cesar':
            offset = request.form['offset']
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

        # TODO Get the username from Login
        new_string = EncodedString_TB(new_encodedstring, username, encryptiontype)
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
    return render_template('encryption.html', form=form)


@webapp.route("/result", methods=['GET', 'POST'])
def display_result_page():
    # TODO Print the encrypted stuff from /encryption, use same method as for the username
    if request.method == 'POST':
        form = ResultForm()
        if form.validate_on_submit():
            return redirect(url_for('success'))
        return render_template('result.html', form=form)
    return redirect("/login")


# Just for debugging!
if __name__ == "__main__":
    webapp.run(debug=True)
