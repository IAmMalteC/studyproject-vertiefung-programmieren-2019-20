from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, IntegerField, SubmitField
from wtforms.validators import InputRequired, Regexp


# Form blueprint
# [VARIABLE] = [FIELD TYPE]('[LABEL]', [
#         validators=[VALIDATOR TYPE](message=('[ERROR MESSAGE'))
#     ])


class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('Username', validators=[InputRequired(), Regexp('^[a-zA-Z]+$',
                                                                           message="Username must just contain letters.")])
    submit = SubmitField('Login')


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
