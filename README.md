# ENSAI-Projet-info-2A

Code source pour le projet d'info du cours à l'ENSAI [Compléments d'informatique](https://ludo2ne.github.io/
ENSAI-2A-Projet-info/).

Auteurs : Attig Chahine, Gibert Adrien, Kambou Hery Ruth, Madec Jeanne, Saleck Mohamed

## Objectifs

Cette Application sert à intéragir avec des mangas issus d'une API open source

- Rechercher un manga par son titre ou son mangaka
- Partager des avis sur ces mangas
- Partager des collections de mangas

## Installation

Installez les packages requis avec les commandes bash suivantes:

```bash
pip install -r requirements.txt     # installer tout les packages listés dans les fichier
pip list                            # obtenir la liste des packages installé
```


- **inquirerPy** : Librairie permettant de créer des menus textuels interactifs avec des questions et des options pour les usagers.
- **pytest** : Structure de tests python puissant.
- **python-dotenv** : Librairie permettant de charger des variables d'environnement de fichiers .env.
- **requests** : designé pour rendre les requetes HTTP plus accessible pour l'humain.


## Tests Unitaires

```bash
python -m pytest -v
```

## Lancer l'application

```bash
python src/__main__.py
```