from flask import Flask
import pandas as pd
import os

def create_app():
    # Crée l'instance de l'application Flask
    app = Flask(__name__)

    # Chemin absolu vers le fichier de données pour éviter les erreurs
    data_path = os.path.join(os.path.dirname(app.root_path), 'data', 'recommandations_BERT_final.xlsx')

    try:
        # Charger les données une seule fois au démarrage
        df = pd.read_excel(data_path)
        # Stocker le dataframe dans la configuration de l'app pour y accéder partout
        app.config['PROJECT_DF'] = df
    except FileNotFoundError:
        print(f"ERREUR : Fichier de données introuvable. Vérifiez le chemin : {data_path}")
        app.config['PROJECT_DF'] = None

    # Importer et enregistrer les routes définies dans routes.py
    with app.app_context():
        from . import routes
        app.register_blueprint(routes.main_bp)

    return app