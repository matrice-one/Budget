from flask import Flask
from flask.templating import render_template
from flask import Flask, render_template, url_for, request, redirect, make_response
from flask import jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import request
from flask import flash, Blueprint
from flask import current_app as app
from .classes import db, User, Transaction


# Partie lié au budget
# Modifies-y comme tu le sens
# Vu que c'est surtout toi,
# moi je vais pas trop y touché

# Pour l'instant, il y a une page pour
# ajouter une entrée, et une pour les
# afficher


budget_bp = Blueprint('budget_bp', __name__,
                      template_folder='templates',
                      static_folder='static',
                      static_url_path='/appli/budget/static')


# Connect to a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///essai.db'


# What happens at the end point
@budget_bp.route('/')
def hello():
    print("Nice try")
    return render_template('home.html')


@budget_bp.route("/seedb")
def seedb():
    depenses = Transaction.query.all()
    deps = []
    for depense in depenses:
        print("Amount = " + str(depense.amount) + " categorie = " +
              str(depense.category) + " Date = " + str(depense.date))
        dep = {"id": depense.id, "amount": depense.amount,
               "categorie": depense.category, "date": depense.date}
        deps.append(dep)
    print(deps)
    return render_template("seedb.html", depenses=deps)


@budget_bp.route("/delete", methods=["POST"])
def delete():
    to_delete = request.json
    print("A supprimer : ", to_delete)
    for index in to_delete['todelete']:
        depense = Transaction.query.filter_by(id=index).first()
        db.session.delete(depense)
        db.session.commit()
    return make_response("OK", 200)


@budget_bp.route("/addentry", methods=["POST"])
def truc():
    print(request.form)
    valeur = request.form
    newdep = Transaction(
        valeur['montant'], valeur['categorie'], valeur['date'])
    db.session.add(newdep)
    db.session.commit()
    return redirect(url_for('budget_bp.seedb'))


@budget_bp.route("/budget")
def budget():
    depenses = Transaction.query.all()
    deps = []
    for depense in depenses:
        print("Amount = " + str(depense.amount) + " categorie = " +
              str(depense.category) + " Date = " + str(depense.date))
        dep = {"id": depense.id, "amount": depense.amount,
               "categorie": depense.category, "date": depense.date}
        deps.append(dep)
    return render_template("budget.html", depenses=deps)
