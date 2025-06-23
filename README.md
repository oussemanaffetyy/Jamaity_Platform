# 🎯 Plateforme de Recommandation pour la Société Civile Tunisienne

Ce projet est une application web développée avec Flask qui sert de plateforme intelligente pour les associations de la société civile en Tunisie. Elle recommande des appels à projets pertinents en fonction de la région et de la thématique d'une association.


---

## 🚀 Fonctionnalités

* Filtrage des appels à projets par **région**.
* Filtrage par **thématique**.
* Affichage en temps réel des résultats correspondants.
* Lien direct vers le détail de chaque appel à projet.
* Calcul d'un score de pertinence (basé sur un modèle BERT).

---

## 🛠️ Technologies utilisées

* **Backend** : Python, Flask
* **Manipulation de données** : Pandas
* **Frontend** : HTML, CSS
* **Base de données** : Fichier Excel (`.xlsx`)

---

## ⚙️ Installation et Lancement

Suivez ces étapes pour lancer le projet en local.

### Prérequis

* Python 3.8+
* Git

### 1. Cloner le projet

```bash
git clone https://github.com/oussemanaffetyy/Jamaity_Platform
cd Jamaity_Platform
```

### 2. Créer et activer l'environnement virtuel

* **Sur macOS / Linux :**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **Sur Windows :**
  ```bash
  py -m venv venv
  .\venv\Scripts\activate
  ```

### 3. Installer les dépendances

Toutes les bibliothèques nécessaires sont listées dans `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Ajouter le fichier de données

Ce projet nécessite le fichier de données `recommandations_BERT_final.xlsx`. Pour des raisons de bonne pratique, il n'est pas inclus dans ce dépôt.

**Veuillez créer un dossier `data` à la racine du projet et y placer votre fichier `recommandations_BERT_final.xlsx`.**

La structure doit être :

```
Jamaity_Platform/
├── data/
│   └── recommandations_BERT_final.xlsx
└── ... (autres fichiers)
```

### 5. Lancer l'application

Une fois l'installation terminée, vous pouvez démarrer le serveur de développement Flask :

```bash
python run.py
```

Ouvrez votre navigateur et allez à l'adresse **http://127.0.0.1:5000**.

---

## 📂 Structure du projet

```
Jamaity_Platform/
├── app/                  # Package principal de l'application
│   ├── static/           # Fichiers CSS, JS, images
│   ├── templates/        # Fichiers HTML
│   ├── __init__.py       # Factory de l'application Flask
│   └── routes.py         # Logique des pages (routes)
├── data/                 # Données brutes (ignoré par Git)
├── venv/                 # Environnement virtuel (ignoré par Git)
├── requirements.txt      # Dépendances Python
├── run.py                # Point d'entrée pour lancer le serveur
└── README.md             # Ce fichier
```
