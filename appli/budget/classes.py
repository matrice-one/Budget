from flask_login import UserMixin
from appli import db


# Contient les Tables
# Puis les classes si on en fait

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    token = db.Column(db.String(500))

    def __repr__(self):
        return '<User %r>' % self.name


# Creating & maintain the database
class Depense(db.Model):
    # Defines the column of the db
    id = db.Column(db.Integer, primary_key=True, )
    amount = db.Column(db.Integer, nullable=False)
    categorie = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)

    #  ?
    def __init__(self, amount=None, categorie=None, date=None):
        self.amount = amount
        self.categorie = categorie
        self.date = date

    def __repr__(self):
        return '<Depense %r>' % self.id
