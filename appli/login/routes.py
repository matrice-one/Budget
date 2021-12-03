
import requests
from numpy import random
from functools import wraps
from flask import render_template, url_for, request, redirect
from flask import flash, Blueprint

from flask_login import LoginManager, login_required
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from flask import current_app as app
from sqlalchemy.exc import SQLAlchemyError

from appli.budget.classes import db, User


# Routes pour le login
# Pour la suite, ca servira à chaque page à
# voir si l'utilisateur est connecté
# afin qu'il est le droit d'aller sur
# la page ou non


login_bp = Blueprint('login_bp', __name__,
                     template_folder='templates',
                     static_folder='static',
                     static_url_path='/appli/login/static')


login_manager = LoginManager()
login_manager.login_view = 'login'     # Page name to log in
login_manager.login_message = u"Sorry ! You cannot access to this page..."
login_manager.init_app(app)


# Gère les erreurs plus facilement
def add_db(element, kind):
    db.session.add(element)
    try:
        db.session.commit()
        print("{} : {} added to the database".format(element.id, kind))
    except SQLAlchemyError as err:
        print('e = ', err)
        error = str(err.__dict__['orig'])
        print("Erreur :", error)
        raise Exception("Erreur : {}".format(error))

# Fonction à part pour remplir la DB avec des Users
# (Sera sûrement modifiée à l'avenir)
def fill_db(name, email=None, password=None):
    if not email:
        email = name+"@etu.unige.ch"
    if not password:
        password = "123"

    # create a new user with the form data.
    # Hash the password so the plaintext version isn't saved.
    new_user = User(email=email,
                    name=name,
                    password=generate_password_hash(
                        password, method='sha256'))

    add_db(new_user, "User {}".format(new_user.name))

    return 0


# Nécessaire, mais pas important à comprendre
@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table,
    # use it in the query for the user
    return User.query.get(int(user_id))


# Template pour le login (merci Internet)
@login_bp.route('/login')
def login():
    return render_template('login.html')


# Login page
@login_bp.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it,
    # and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        # if the user doesn't exist or password is wrong, reload the page
        return redirect(url_for('login_bp.login'))

    # if the above check passes, then we know
    # the user has the right credentials
    login_user(user, remember=remember)
    # r = requests.post('/login', auth=(email, password))
    # user.token = r.json()['token']
    db.session.commit()
    return redirect(url_for('budget_bp.seedb'))



# Pour créer un compte
@login_bp.route('/signup')
def signup():
    return render_template('signup.html')


# Création du nouveau User
@login_bp.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    username = request.form.get('name')
    password = request.form.get('password')

    # if this returns a user, then the email already exists in database
    user = User.query.filter_by(email=email).first()

    # if a user is found, we want to redirect back to signup page
    # so user can try again
    if user:
        flash('Email address already exists')
        return redirect(url_for('login_bp.signup'))

    fill_db(username, email, password)

    return redirect(url_for('login_bp.login'))
