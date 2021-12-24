from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, redirect, make_response      

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///budgetease.db'
db = SQLAlchemy(app)

#...


#...

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


def init_app():
     db.create_all() 
     return app

app = init_app()

# ROUTES

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/explain")
def about():
    return render_template("explain.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/addentry", methods=["POST"])
def truc():
    print(request.form)
    valeur = request.form
    newdep = Transaction(
        valeur['montant'], 'all good', 'all good')
    db.session.add(newdep)
    db.session.commit()
    return redirect(url_for('budget_bp.seedb'))


@app.route("/dashboard_with_stuff")
def dashboard_with_stuff():
    depenses = Transaction.query.all()
    deps = []
    for depense in depenses:
        print("Amount = " + str(depense.amount))
        dep = {"amount": depense.amount}
        deps.append(dep)
    print(deps)
    return render_template("dashboard_with_stuff.html", depenses=deps)
    
if __name__ == "__main__":
    app.run(debug=True)


# MODEL