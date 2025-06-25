# app/routes.py
from flask import Blueprint, render_template, request, current_app
import pandas as pd

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    df = current_app.config.get('PROJECT_DF')
    if df is None:
        return "<h1>Erreur Critique : Le fichier de données n'a pas pu être chargé. Vérifiez la console.</h1>", 500

    df = df.copy()

    # Supprimer uniquement les projets sans nom d'appel
    df['Nom_appel'].replace('', pd.NA, inplace=True)
    df = df.dropna(subset=['Nom_appel'])

    # Garder les projets même sans lien (pas de suppression ici)
    df['Lien_details'].fillna('', inplace=True)  # Remplace nan par chaîne vide

    # Préparation des filtres
    regions = sorted(list(set(df['region'].dropna())))
    thematiques = sorted(list(set(df['thematique'].dropna())))

    selected_name = request.args.get('search_name', default="", type=str)
    selected_region = request.args.get('region', default="", type=str)
    selected_thematique = request.args.get('thematique', default="", type=str)

    filtered_df = df

    if selected_name:
        filtered_df = filtered_df[filtered_df['Association'].str.contains(selected_name, case=False, na=False)]

    if selected_region:
        filtered_df = filtered_df[filtered_df['region'] == selected_region]

    if selected_thematique:
        filtered_df = filtered_df[filtered_df['thematique'] == selected_thematique]

    projets = filtered_df.to_dict('records')

    return render_template('index.html',
                           regions=regions,
                           thematiques=thematiques,
                           projets=projets,
                           nombre_projets=len(projets),
                           selected_name=selected_name,
                           selected_region=selected_region,
                           selected_thematique=selected_thematique)
