from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Regexp


# Form blueprint
# [VARIABLE] = [FIELD TYPE]('[LABEL]', [
#         validators=[VALIDATOR TYPE](message=('[ERROR MESSAGE'))
#     ])


class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('Username', validators=[DataRequired()]) # , Regexp('^[a-zA-Z]+$', message="Username must just contain letters.")])
    submit = SubmitField('Login')


class EncryptionForm(FlaskForm):
    """Encryption Form"""
    encryptiontype = RadioField('Type of encryption', validators=[DataRequired()],
                                choices=[('cesar', 'Cäsar Verschlüsselung'),
                                         ('monoalphabeticsubstitution', 'Monoalphabetische Substitution')],
                                default='cesar')
    offset = IntegerField('Offsetfactor')
    string_to_encrypt = TextAreaField('Text to encode', validators=[DataRequired()])
    submit = SubmitField('Encode and save')
