from unittest.mock import MagicMock

from src.service.utilisateur_service import UtilisateurService
from src.dao.utilisateur_dao import UtilisateurDao
from src.business_objet.utilisateur import Utilisateur

# Exemple d'utilisateur: 
# "liste_utilisateur[
Utilisateur(pseudo="Naruto54", age=16, mdp=("mdpmanga", "Naruto54"), collections=["Favoris"], id_utilisateur=1),
Utilisateur(pseudo="missmanga", age=18, mdp=("126OnePiece", "missmanga"), collections=["Favoris"], id_utilisateur=2),
Utilisateur(pseudo="23One", age=22, mdp=("78Naruto", "23One"), collections=["Favoris"], id_utilisateur=5),
]

def pseudo_existe_deja_ok():

    # GIVEN
    utilisateur = UtilisateurDao()

    # WHEN
    utilisateur = dao.utilisateur_dao.trouver_par_pseudo()
