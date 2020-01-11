from flask import Flask, render_template, session, redirect, url_for, escape, request
from forms import LoginForm, EncryptionForm, ResultForm
from flask_login import LoginManager
# THIS WEBAPP IS BUILD BY THE HELP OF https://hackersandslackers.com/your-first-flask-application
webapp = Flask(__name__,
               template_folder="templates",
               static_folder="static")
# Session from = https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions
# Secret Key for session
webapp.secret_key = b'ayTAyD2feEGDS6P9eZwj'

# # Login from https://flask-login.readthedocs.io/en/latest/#flask_login.LoginManager
# # Login
# login_manager = LoginManager()
# login_manager.init_app(webapp)
# @login_manager.user_loader()
# def load_user(user_id):
#     return User.get(user_id)


# Routing
@webapp.route("/login", methods=['GET', 'POST'])
@webapp.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('login.html', form=form)
    # # / is in general the indexsite, but we shall start with a login. So here we go.
    # if request.method == 'POST':
    #     session['username'] = request.form['username']
    #     return redirect(url_for('login'))
    # return render_template('login.html')


@webapp.route("/encryption", methods=['GET', 'POST'])
# @login_required
def display_encryption_page():
    # if 'username' in session:
    #     return 'Logged in as %s' % escape(session['username'])
    # return 'You are not logged in'
    form = EncryptionForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('encryption.html', form=form)


@webapp.route("/result", methods=['GET', 'POST'])
# @login_required
def display_result_page():
    form = ResultForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('result.html', form=form)


# @webapp.route('/logout') # gibt es noch nicht als html seite
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('login'))


# Just for debuging -- REMOVE before delivering
if __name__ == "__main__":
    webapp.run(debug=True)
