from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS # utile peut-être plus tard

# Fichier qui centralise les sous-dossiers
# Ils sont importés ici, pour que chaque
# sous-dossier puisse accéder au informations
# d'un autre, par l'intermédiaire de ce lieu

db = SQLAlchemy()


def init_app():
    app = Flask(__name__, instance_relative_config=False, static_folder=None)
    app.config.from_pyfile('settings.py')
    # CORS(app, supports_credentials=True)

    db.init_app(app)

    # On importe les plans (blueprint, ou bp)
    # puis on les incorpore à l'app
    # et on crée la DB au passage, comme ca
    # plus besoin d'y faire à la main
    # (si elle existe déjà, ça n'en crée pas une autre)
    with app.app_context():
        from .login.routes import login_bp
        from .budget.routes import budget_bp

        # Register Blueprints
        app.register_blueprint(login_bp)
        app.register_blueprint(budget_bp)

        db.create_all()
        print("\n***********\nDatabase created\n")

        return app
