from app import db
from sqlalchemy.dialects.postgresql import JSON

class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    
    amount = db.Column(db.Integer)
    comment = db.Column(db.String(50))
    category = db.Column(db.String(50))

    def __init__(self, amount, created_on, updated_on, comment=None):
        self.amount = amount

        self.comment = comment
        self.created_on = created_on,
        self.updated_on = updated_on,

    def __repr__(self):
        return '<Transaction %r>' % self.id