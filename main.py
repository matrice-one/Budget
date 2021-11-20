from flask import Flask
from flask.templating import render_template
from flask import Flask, render_template, url_for, request, redirect, make_response
from flask import jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///essai.db'
db = SQLAlchemy(app)


class Depense(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    amount = db.Column(db.Integer, nullable=False)
    categorie = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)

    def __init__(self, amount=None, categorie=None, date=None):
        self.amount = amount
        self.categorie = categorie
        self.date = date

    def __repr__(self):
        return '<Depense %r>' % self.id

@app.route('/')
def hello():
    print("Nice try")
    return render_template('home.html')

@app.route("/postdata", methods=['POST'])
def postdata():
    valeur = request.json
    newdep = Depense(valeur['montant'], valeur['categorie'], valeur['date'])
    db.session.add(newdep)
    db.session.commit()
    return make_response("OK")

@app.route("/seedb")
def seedb():
    depenses = Depense.query.all()
    deps = []
    for depense in depenses:
        print("Amount = " + str(depense.amount) + " categorie = " + str(depense.categorie) + " Date = " + str(depense.date))
        dep = {"amount": depense.amount, "categorie": depense.categorie, "date": depense.date}
        deps.append(dep)
    print(deps)
    return render_template("seedb.html", depenses=deps)


if __name__ == '__main__':
    app.run(debug=True)
