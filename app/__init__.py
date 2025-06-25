# app/__init__.py
from flask import Flask
import pandas as pd
import os

def create_app():
    app = Flask(__name__)

    # On charge le seul fichier de données nécessaire
    data_file = os.path.join(os.path.dirname(app.root_path), 'data', 'recommandations_BERT_final.xlsx')

    try:
        df = pd.read_excel(data_file)
        app.config['PROJECT_DF'] = df
        print(f"✅ Fichier {data_file} chargé avec succès.")

    except FileNotFoundError:
        app.config['PROJECT_DF'] = None
        print(f"!!! ERREUR CRITIQUE : Le fichier {data_file} est introuvable.")
    except Exception as e:
        app.config['PROJECT_DF'] = None
        print(f"!!! ERREUR CRITIQUE LORS DU CHARGEMENT : {e}")

    # Importer et enregistrer les routes
    with app.app_context():
        from . import routes
        app.register_blueprint(routes.main_bp)

    return app