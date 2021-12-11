from flask_login import UserMixin
from appli import db


# Contient les Tables
# Puis les classes si on en fait


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    money = db.Column(db.Integer)
    piggy_bank = db.Column(db.Integer)
    debt = db.Column(db.Integer)

    def __init__(self, email, password, name=None, money=0,
                 piggy_bank=None, debt=None):
        self.name = name
        self.password = password
        self.email = email
        self.money = money
        self.piggy_bank = piggy_bank
        self.debt = debt

    def __repr__(self):
        return '<User %r>' % self.name


class List(db.Model):
    __tablename__ = 'list'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)

    def __repr__(self):
        return '<List %r>' % self.category_id


class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    comment = db.Column(db.String(50))
    # category = user_id = db.Column(db.Integer, db.ForeignKey('list.category_id'),
    #                                nullable=False)
    date = db.Column(db.String(50))
    category = db.Column(db.String(50))

    def __init__(self, amount, date, comment=None):
        self.amount = amount
        self.date = date
        self.comment = comment

    def __repr__(self):
        return '<Transaction %r>' % self.id
