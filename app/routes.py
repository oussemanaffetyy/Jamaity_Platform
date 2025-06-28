from flask import Blueprint, render_template, request, current_app, jsonify
import pandas as pd

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    df = current_app.config.get('PROJECT_DF')
    if df is None:
        return "<h1>Erreur Critique : Le fichier de données n'a pas pu être chargé. Vérifiez la console.</h1>", 500

    df = df.copy()
    df['Nom_appel'] = df['Nom_appel'].replace('', pd.NA)
    df = df.dropna(subset=['Nom_appel'])
    df['Lien_details'] = df['Lien_details'].fillna('')
    df['Association'] = df['Association'].fillna('').astype(str)

    regions = sorted(df['region'].dropna().unique())
    thematiques = sorted(df['thematique'].dropna().unique())

    # Paramètres GET
    selected_name = request.args.get('search_name', default="", type=str).strip()
    selected_region = request.args.get('region', default="", type=str).strip()
    selected_thematique = request.args.get('thematique', default="", type=str).strip()

    # Condition : si aucun filtre n'est actif, on ne renvoie rien
    no_filters_applied = not selected_name and not selected_region and not selected_thematique

    projets = []
    if not no_filters_applied:
        filtered_df = df.copy()

        if selected_name:
            filtered_df = filtered_df[filtered_df['Association'].str.contains(selected_name, case=False, na=False)]

        if selected_region:
            filtered_df = filtered_df[filtered_df['region'] == selected_region]

        if selected_thematique:
            filtered_df = filtered_df[filtered_df['thematique'] == selected_thematique]

        projets = filtered_df.to_dict('records')

    return render_template(
        'index.html',
        regions=regions,
        thematiques=thematiques,
        projets=projets,
        nombre_projets=len(projets),
        selected_name=selected_name,
        selected_region=selected_region,
        selected_thematique=selected_thematique,
        filters_applied=not no_filters_applied
    )

# ✅ Cette route est maintenant définie correctement
@main_bp.route('/search_nom')
def search_nom():
    df = current_app.config.get('PROJECT_DF')
    search_query = request.args.get('q', '').lower()
    if not search_query or df is None:
        return jsonify([])

    results = df[
        df['Nom_appel'].str.lower().str.contains(search_query, na=False) |
        df['Association'].str.lower().str.contains(search_query, na=False)
    ]

    projets = results.head(10).to_dict(orient='records')
    return jsonify(projets)
