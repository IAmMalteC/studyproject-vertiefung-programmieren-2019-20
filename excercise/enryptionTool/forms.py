from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, TextField, RadioField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length
# Form blueprint
# [VARIABLE] = [FIELD TYPE]('[LABEL]', [
#         validators=[VALIDATOR TYPE](message=('[ERROR MESSAGE'))
#     ])


class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('Benutzername', [DataRequired()])
    submit = SubmitField('Login')


class EncryptionForm(FlaskForm):
    """Encryption Form"""
    encryptiontype = RadioField('Verschlüsselungstyp', [DataRequired()], choices=[('cesar', 'Cäsar Verschlüsselung'), ('monoalphabeticsubstitution', 'Monoalphabetische Substitution')], default='cesar')
    offset = IntegerField('Offset Faktor')
    string_to_encrypt = TextAreaField('Zu verschlüsselnder Text', [DataRequired()])
    submit = SubmitField('Verschlüsseln und speichern')


class ResultForm(FlaskForm):
    """Result Form"""
    unencryptedString = TextAreaField('Unverschlüsselter Text')
    encryptedString = TextAreaField('Verschlüsselter Text')
