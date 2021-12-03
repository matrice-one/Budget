from appli import init_app

# Point de départ de l'appli
# Il faut lancer python run.py, et tout se lance
# (comme par magie ;)

# Les dossiers se trouvent dans le dossier 'appli'
# Ils sont divisés selon leur rôle
# Pour l'instant, 'login' et 'budget'

app = init_app()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, threaded=True, port=8080)
