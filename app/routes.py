# app/routes.py
from flask import Blueprint, render_template, request, current_app
import pandas as pd

# Un "Blueprint" est un moyen d'organiser un groupe de routes associées.
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Récupérer le dataframe depuis la configuration de l'application
    df = current_app.config['PROJECT_DF']

    if df is None:
        return "<h1>Erreur Critique</h1><p>Le fichier de données n'a pas pu être chargé. Veuillez vérifier les logs du serveur.</p>", 500

    # Préparer les listes pour les menus déroulants
    regions = sorted(list(set(df['region'].dropna())))
    thematiques = sorted(list(set(df['thematique'].dropna())))

    # Récupérer les sélections de l'utilisateur ou utiliser une valeur par défaut
    selected_region = request.args.get('region', default=regions[0] if regions else '', type=str)
    selected_thematique = request.args.get('thematique', default=thematiques[0] if thematiques else '', type=str)

    # Filtrer les données
    if selected_region and selected_thematique:
        filtered_df = df[(df['region'] == selected_region) & (df['thematique'] == selected_thematique)]
    else:
        filtered_df = pd.DataFrame() # Retourne un tableau vide si les filtres ne sont pas valides

    # Convertir les résultats pour l'affichage en HTML
    projets = filtered_df.to_dict('records')

    # Renvoyer le template HTML avec toutes les données nécessaires
    return render_template('index.html',
                           regions=regions,
                           thematiques=thematiques,
                           selected_region=selected_region,
                           selected_thematique=selected_thematique,
                           projets=projets,
                           nombre_projets=len(projets))