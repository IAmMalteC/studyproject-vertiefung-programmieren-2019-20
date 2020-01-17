from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField, SubmitField
from wtforms.validators import InputRequired, Regexp, Length


# Form blueprint
# [VARIABLE] = [FIELD TYPE]('[LABEL]', [
#         validators=[VALIDATOR TYPE](message=('[ERROR MESSAGE'))
#     ])


class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('Username', validators=[InputRequired(),
                                                   Length(max=80, message="Your username may not be longer then 80 characters"),
                                                   Regexp('^[a-zA-Z]+$', message="Your username must just contain letters.")])
    password = PasswordField("Password", validators=[InputRequired(),
                                                     Length(max=160, message="Your password may not be longer then 160 characters")])
    submit = SubmitField('Login')

class LogoutForm(LoginForm):
    """Logout Form"""
    submit = SubmitField('Register')


class EncryptionForm(FlaskForm):
    """Encryption Form"""
    encryptiontype = RadioField('Type of encryption', validators=[InputRequired()],
                                choices=[('cesar', 'Cäsar Verschlüsselung'),
                                         ('monoalphabeticsubstitution', 'Monoalphabetische Substitution')],
                                default='cesar')
    offset = StringField('Offsetfactor')  # IntegerField
    string_to_encrypt = TextAreaField('Text to encode', validators=[InputRequired(),
                                                                    Regexp('[!-~]+$', # = !"#$%&'()*+,-./0-9:;<=>?@A-Z[\]^_`a-z{|}~
                                                                           message="Just use following characters: a-z, A-Z, 0-9 oder !\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~")])
    submit = SubmitField('Encode and save')
