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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///essai.db'
db = SQLAlchemy(app)


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


# What happens at the end point
@app.route('/')
def hello():
    print("Nice try")
    return render_template('home.html')

#  Time to make requests

# Here you're saying what happens to the data you assigned to the url /postdata in home.html


@app.route("/postdata", methods=['POST'])
def postdata():
    valeur = request.json
    newdep = Depense(valeur['montant'], valeur['categorie'], valeur['date'])
    db.session.add(newdep)
    db.session.commit()
    return make_response("OK", 200)

# And to show what will be displayed after?


@app.route("/seedb")
def seedb():
    # SQL Query to get all data. as df..? tuple?
    depenses = Depense.query.all()
    deps = []
    for depense in depenses:
        print("Amount = " + str(depense.amount) + " categorie = " + str(depense.categorie) + " Date = " + str(depense.date))
        dep = {"id" : depense.id, "amount": depense.amount, "categorie": depense.categorie, "date": depense.date}
        deps.append(dep)
    print(deps)
    return render_template("seedb.html", depenses=deps)


@app.route("/delete", methods=["POST"])
def delete():
    to_delete = request.json
    print("A supprimer : ", to_delete)
    for index in to_delete['todelete']:
        depense = Depense.query.filter_by(id = index).first()
        db.session.delete(depense)
        db.session.commit()
    return make_response("OK", 200)

@app.route("/truc", methods=[])
def truc():
    print(request.form)
    return make_response("OK", 200)


if __name__ == '__main__':
    # Debug mode as long as we are in production mode.
    app.run(debug=True)
