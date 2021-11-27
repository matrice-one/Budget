from flask import Flask
from flask.templating import render_template
from flask import Flask, render_template, url_for, request, redirect, make_response
from flask import jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import request


# Creae an app instance
app = Flask(__name__)

# Connect to a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///neigex.db'
db = SQLAlchemy(app)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    account_money = db.Column(db.Integer)
    amount_piggy_bank = db.Column(db.Integer)
    amount_debt = db.Column(db.Integer)

    def __init__(self, user_id=None, user_name=None, account_money=None,
                 amount_piggy_bank=None, amount_debt=None):
        self.user_id = user_id
        self.user_name = user_name
        self.account_money = account_money
        self.amount_piggy_bank = amount_piggy_bank
        self.amount_debt = amount_debt

    def __repr__(self):
        return '<User %r>' % self.user_name


# What happens at the end point
@app.route('/')
def hello():
    print("Nice try")
    return render_template('home.html')

#  Time to make requests


# on running python main.py, run the flask app
if __name__ == '__main__':
    # Debug mode as long as we are in production mode.
    app.run(debug=True)
