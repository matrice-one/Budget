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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///final.db'
db = SQLAlchemy(app)


# Creating & maintain the database


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


class List(db.Model):
    __tablename__ = 'list'
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'),
                        nullable=False)

    def __repr__(self):
        return '<List %r>' % self.category_id


class Transation(db.Model):
    __tablename__ = 'transaction'
    transaction_id = db.Column(db.Integer, primary_key=True)
    amount_spent = db.Column(db.Integer)
    comment = db.Column(db.String)
    category = user_id = db.Column(db.Integer, db.ForeignKey('list.category_id'),
                                   nullable=False)

    def __repr__(self):
        return '<Transaction %r>' % self.transaction_id


# What happens at the end point


@app.route('/')
def hello():
    print("Nice try")
    return render_template('index.html')

#  Time to make requests


# on running python main.py, run the flask app
if __name__ == '__main__':
    # Debug mode as long as we are in production mode.
    app.run(debug=True)
