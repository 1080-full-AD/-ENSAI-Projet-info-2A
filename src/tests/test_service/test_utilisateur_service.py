from unittest.mock import MagicMock

from src.service.utilisateur_service import UtilisateurService
from src.dao.utilisateur_dao import UtilisateurDao
from src.business_objet.utilisateur import Utilisateur

# Exemple d'utilisateur: 
liste_utilisateur=[
Utilisateur(pseudo="Naruto54", age=16, mdp=("mdpManga4#", "Naruto54"), collections=["Favoris"], id_utilisateur=1),
Utilisateur(pseudo="missmanga", age=18, mdp=("126OnePiece#", "missmanga"), collections=["Favoris"], id_utilisateur=2),
Utilisateur(pseudo="23One", age=22, mdp=("78Naruto#", "23One"), collections=["Favoris"], id_utilisateur=5),
]

def test_pseudo_existe_deja_ok():
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


def test_pseudo_existe_déjà_echec():
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


def test_creer_utilisateur_ok():
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


def test_creer_utilisateur_echec():
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


def test_modifier_utilisateur_ok():
    """Vérifier que la méthode modifier_utilisateur fonctionne correctement"""

    # GIVEN
    pseudo, age, mdp, collections, id_utilisateur = "fanmang", 22, "Monste_R12", ["Monster", "One Piece", "Naruto"], 678
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.modifier_utilisateur.return_value = True

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    utilisateur = utilisateur_service.modifier_utilisateur(pseudo, age, mdp, collections, id_utilisateur )

    # THEN
    assert utilisateur is True


def test_modifier_utilisateur_echec():
    """Vérifier que la méthode modifier_utilisateur renvoie bien une erreur"""

    # GIVEN
    pseudo, age, mdp, collections, id_utilisateur = "fanmang", 22, "Monste_R12", ["Monster", "One Piece", "Naruto"], 678
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.modifier_utilisateur.return_value = False

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    utilisateur = utilisateur_service.modifier_utilisateur(pseudo, age, mdp, collections, id_utilisateur )

    # THEN
    assert utilisateur is False


def test_supprimer_utilisateur_ok():
    """Vérifier que la méthode supprimer_utilsiateur fonctionne correctement"""

    # GIVEN
    pseudo, age, mdp, collections, id_utilisateur = "fanmang", 22, "Monste_R12", ["Monster", "One Piece", "Naruto"], 678
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.supprimer_utilisateur.return_value = True

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    utilisateur = utilisateur_service.supprimer_utilisateur(pseudo, age, mdp, collections, id_utilisateur )

    # THEN
    assert utilisateur is True


def test_supprimer_utilisateur_echec():
    """Vérifier que la méthode supprimer_utilsiateur renvoie bien une erreur"""

    # GIVEN
    pseudo, age, mdp, collections, id_utilisateur = "fanmang", 22, "Monste_R12", ["Monster", "One Piece", "Naruto"], 678
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.supprimer_utilisateur.return_value = False

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    utilisateur = utilisateur_service.supprimer_utilisateur(pseudo, age, mdp, collections, id_utilisateur )

    # THEN
    assert utilisateur is False


def test_trouver_par_pseudo_utilisateur_ok():
    """Vérifier que la méthode qui liste tous les utilisateurs grâce à leur pseudo fonctionne"""

    # GIVEN
    pseudo = pseudo.utilisateur_service()
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.trouver_tous_utilisateur.return_value = [pseudo for pseudo in liste_utilisateur if pseudo.id_utilisateur == pseudo]

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    res = utilisateur_service.trouver_tous_utilisateur(pseudo)

    # THEN
    assert len(res) == 2
    for pseudo in res:
        assert pseudo.id_utilisateur == pseudo


def test_trouver_par_pseudo_utilisateur_echec():
    """Vérifier que la méthode qui renvoie tous les utilisateurs renvoie bien un échec"""

    # GIVEN
    pseudo = pseudo.utilisateur_service()
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.trouver_tous_utilisateur.side_effect = Exception("Erreur de base de données")

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    res = utilisateur_service.trouver_tous_utilisateur(pseudo)

    # THEN
    assert res == []


def test_lister_tous_utilisateur_ok():
    """Lister tous les utilisateurs avec succès"""

    # GIVEN
    id_utilisateur = id_utilisateur.utilisateur_service()
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.lister_tous_utilisateur.return_value = [pseudo for pseudo in liste_utilisateur if pseudo.id_utilisateur == id_utilisateur]

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    res = utilisateur_service.lister_tous_utilisateur(id_utilisateur)

    # THEN
    assert len(res) == 2
    for pseudo in res:
        assert pseudo.id_utilisateur == id_utilisateur


def test_lister_tous_utilisateur_echec():
    """Vérifier que la méthode qui liste tous les utilisateurs grâce à leur identifiant renvoie bien un échec"""

    # GIVEN
    id_utilisateur = id_utilisateur.utilisateur_service()
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.lister_tous_utilisateur.side_effect = Exception("Erreur de base de données")

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    res = utilisateur_service.lister_tous_utilisateur(id_utilisateur)

    # THEN
    assert res == []


def test_se_connecter_ok():
    """Vérifier que la méthode se_connecter fonctionne correctement"""

    # GIVEN
    pseudo, age, mdp, collections, id_utilisateur = "Naruto54", 16, "mdpManga7#", ["Monster", "One Piece", "Naruto"], 678
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.se_connecter.return_value = True

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    utilisateur = utilisateur_service.se_connecter(pseudo, age, mdp, collections, id_utilisateur )

    # THEN
    assert utilisateur is True 


def test_se_connecter_echec():
    """Vérifier que la méthod se connecter renvoie bien une erreur"""

    # GIVEN
    pseudo, age, mdp, collections, id_utilisateur = "Naruto54", 16, "mdpManga7#", ["Monster", "One Piece", "Naruto"], 678
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.se_connecter.return_value = False

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    utilisateur = utilisateur_service.se_connecter(pseudo, age, mdp, collections, id_utilisateur )

    # THEN
    assert utilisateur is False


def test_se_deconecter_ok():
    """Vérifier que la méthode se déconnecter fonctionne comme il le faut"""

    # GIVEN
    pseudo, age, mdp, collections, id_utilisateur = "Naruto54", 16, "mdpManga7#", ["Monster", "One Piece", "Naruto"], 678
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.se_connecter.return_value = True

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    utilisateur = utilisateur_service.se_connecter(pseudo, age, mdp, collections, id_utilisateur )

    # THEN
    assert utilisateur is True


def test_se_deconecter_echec():
    """Vérifier que la méthode se déconnecter renvoie bien une erreur"""

    # GIVEN
    pseudo, age, mdp, collections, id_utilisateur = "Naruto54", 16, "mdpManga7#", ["Monster", "One Piece", "Naruto"], 678
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.se_connecter.return_value = False

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    utilisateur = utilisateur_service.se_connecter(pseudo, age, mdp, collections, id_utilisateur )

    # THEN
    assert utilisateur is False

    



      







if __name__ == "__main__":
    import pytest

    pytest.main([__file__])


