from unittest.mock import MagicMock

from src.service.utilisateur_service import UtilisateurService
from src.dao.utilisateur_dao import UtilisateurDao
from src.business_objet.utilisateur import Utilisateur

# Exemple d'utilisateur: 
# "liste_utilisateur
[
Utilisateur(pseudo="Naruto54", age=16, mdp=("mdpManga4#", "Naruto54"), collections=["Favoris"], id_utilisateur=1),
Utilisateur(pseudo="missmanga", age=18, mdp=("126OnePiece#", "missmanga"), collections=["Favoris"], id_utilisateur=2),
Utilisateur(pseudo="23One", age=22, mdp=("78Naruto#", "23One"), collections=["Favoris"], id_utilisateur=5),
]

def pseudo_existe_deja_ok():
    """Vérifier que la méthode pseudo_existe_déjà fonctionne correctement"""

    # GIVEN
    pseudo, age, mdp, collections, id_utilisateur = "Naruto54", 16, "mdpManga7#", ["Monster", "One Piece", "Naruto"], 678
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.pseudo_existe_deja.return_value = True

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    utilisateur = utilisateur_service.pseudo_existe_deja(pseudo, age, mdp, collections, id_utilisateur )

    # THEN
    assert utilisateur is True


def pseudo_existe_déjà_echec():
    """Vérifier que la méthode pseudo_existe_déjà renvoie bien une erreur"""

    # GIVEN
    pseudo, age, mdp, collections, id_utilisateur = "Naruto54", 16, "mdpManga7#", ["Monster", "One Piece", "Naruto"], 678
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.pseudo_existe_deja.return_value = False

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    utilisateur = utilisateur_service.pseudo_existe_deja(pseudo, age, mdp, collections, id_utilisateur )

    # THEN
    assert utilisateur is False


def creer_utilisateur_ok():
    """Vérifier que la méthode creer_utilisateur fonctionne bien"""

    # GIVEN
    pseudo, age, mdp, collections, id_utilisateur = "fanmang", 22, "Monste_R12", ["Monster", "One Piece", "Naruto"], 678
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.creer_utilisateur.return_value = True

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    utilisateur = utilisateur_service.creer_utilisateur(pseudo, age, mdp, collections, id_utilisateur )

    # THEN
    assert utilisateur is True


def creer_utilisateur_echec():
    """Vérifier que la méthode creer_utilisateur renvoie bien un échec"""

    # GIVEN
    pseudo, age, mdp, collections, id_utilisateur = "fanmang", 22, "Monste_R12", ["Monster", "One Piece", "Naruto"], 678
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.creer_utilisateur.return_value = False

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    utilisateur = utilisateur_service.creer_utilisateur(pseudo, age, mdp, collections, id_utilisateur )

    # THEN
    assert utilisateur is False


def modifier_utilisateur_ok():
    """Vérifier que la méthode modifier_utilisateur fonctionne correctement"""

    # GIVEN
    
#test de test
if __name__ == "__main__":
    import pytest

    pytest.main([__file__])


