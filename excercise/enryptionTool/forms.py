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
                                                   Length(max=80,
                                                          message="Your username may not be longer then 80 characters"),
                                                   Regexp('^[a-zA-Z]+$',
                                                          message="Your username must just contain letters.")
                                                   ]
                           )
    # Not a required field, because a former console user, could be registered without a password
    password = PasswordField("Password")
    submit = SubmitField('Login')


class RegisterForm(LoginForm):
    """Register Form"""
    password = PasswordField("Password", validators=[InputRequired(),
                                                     Length(max=160,
                                                            message="Your password may not be longer then 160 characters")
                                                     ]
                             )
    submit = SubmitField('Register')


class EncryptionForm(FlaskForm):
    """Encryption Form"""
    encryptiontype = RadioField('Type of encryption', validators=[InputRequired()],
                                choices=[('cesar', 'Cesar'),
                                         ('monoalphabeticsubstitution', 'Monoalphabeticsubstitution')],
                                default='cesar')
    offset = StringField('Offsetfactor')  # IntegerField
    string_to_encrypt = TextAreaField('Text to encode', validators=[InputRequired(),
                                                                    # [ -~] are following characters !"#$%&'()*+,-./0-9:;<=>?@A-Z[\]^_`a-z{|}~
                                                                    Regexp('^[ -~]+$',
                                                                           message="Just use following characters: a-z, A-Z, 0-9 oder !\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~")
                                                                    ]
                                      )
    submit = SubmitField('Encode and save')
