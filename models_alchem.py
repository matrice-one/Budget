
from app2 import db


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    account_money = db.Column(db.Integer)
    amount_piggy_bank = db.Column(db.Integer)
    amount_debt = db.Column(db.Integer)

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
