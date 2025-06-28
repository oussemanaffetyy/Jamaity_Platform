from flask import Flask
import pandas as pd

def create_app():
    app = Flask(__name__)

    # Chargement du fichier Excel
    try:
        df = pd.read_excel("data/recommandations_BERT_final.xlsx")
        print("✅ Données chargées avec succès.")
        print("Colonnes disponibles :", df.columns.tolist())
        app.config['PROJECT_DF'] = df
    except Exception as e:
        print("❌ Erreur de chargement des données :", e)
        app.config['PROJECT_DF'] = None

    # Import du blueprint correctement
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
