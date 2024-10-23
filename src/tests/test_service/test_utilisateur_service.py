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

def pseudo_existe_deja_ok():
    """Vérifier que la méthode pseudo_existe_déjà fonctionne correctement"""

    # GIVEN
    pseudo = "Naruto54"
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.pseudo_existe_deja.return_value = True

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    utilisateur = utilisateur_service.pseudo_existe_deja(pseudo)

    # THEN
    assert utilisateur is True


def pseudo_existe_déjà_echec():
    """Vérifier que la méthode pseudo_existe_déjà renvoie bien une erreur"""

    # GIVEN
    pseudo = "Naruto54"
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.pseudo_existe_deja.return_value = False

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    utilisateur = utilisateur_service.pseudo_existe_deja(pseudo)

    # THEN
    assert utilisateur is False



def creer_utilisateur_ok():
    """Vérifier que la méthode creer_utilisateur fonctionne bien"""

    # GIVEN
    pseudo, age, mdp, collections, id_utilisateur = "fanmang", 22, "Monster_R12", ["Monster", "One Piece", "Naruto"], 678
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.creer_utilisateur.return_value = True

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    utilisateur = utilisateur_service.creer_utilisateur(pseudo, age, mdp,
                                                        collections,
                                                        id_utilisateur)

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
    utilisateur = utilisateur_service.creer_utilisateur(pseudo, age, mdp,
                                                        collections,
                                                        id_utilisateur)

    # THEN
    assert utilisateur is False


def modifier_utilisateur_ok():
    """Vérifier que la méthode modifier_utilisateur fonctionne correctement"""

    # GIVEN
    pseudo, age, mdp, collections, id_utilisateur = "Naruto54", 16, "mdpManga7#", ["Monster", "One Piece", "Naruto"], 1
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.modifier_utilisiateur.return_value = True

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    result = utilisateur_service.modifier_utilisateur(pseudo, age, mdp,
                                                      collections,
                                                      id_utilisateur)

    # THEN
    assert result is True


def modifier_utilisateur_ok():
    """Vérifier que la méthode modifier_utilisateur renvoie bien une erreur"""

    # GIVEN
    pseudo, age, mdp, collections, id_utilisateur = "Naruto54", 16, "mdpManga7#", ["Monster", "One Piece", "Naruto"], 1
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.modifier_utilisiateur.return_value = False

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    result = utilisateur_service.modifier_utilisateur(pseudo, age, mdp,
                                                      collections,
                                                      id_utilisateur)

    # THEN
    assert result is False


def supprimer_utilisateur_ok():
    """Vérifier que la méthode supprimer_utilisateur fonctionne correctement"""

    # GIVEN
    pseudo, age, mdp, collections, id_utilisateur = "Naruto54", 16, "mdpManga7#", ["Monster", "One Piece", "Naruto"], 1
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.supprimer_utilisiateur.return_value = True

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    result = utilisateur_service.supprimer_utilisateur(pseudo, age, mdp,
                                                       collections,
                                                       id_utilisateur)

    # THEN
    assert result is True

    
def supprimer_utilisateur_echec():
    """Vérifier que la méthode supprimer_utilisateur renvoie bien un erreur"""

    # GIVEN
    pseudo, age, mdp, collections, id_utilisateur = "Naruto54", 16, "mdpManga7#", ["Monster", "One Piece", "Naruto"], 1
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.supprimer_utilisiateur.return_value = False

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao 

    # WHEN
    result = utilisateur_service.supprimer_utilisateur(pseudo, age, mdp,
                                                       collections,
                                                       id_utilisateur)

    # THEN
    assert result is False


def lister_tous_utilisateur_ok():
    """Vérifier que la méthode lister_tous_utilisateur fonctionne correctement"""
        
    # GIVEN
    utilisateur = UtilisateurDao().lister_tous()
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.lister_tous_utilisateur.return_value = [id_utilisateur for id_utilisateur in liste_utilisateur if id_utilisateur.pseudo== utilisateur]

    utilisateur_service = UtilisateurService()
    utilisateur_service.AvisDao = mock_dao 

    # WHEN
    res = utilisateur_service.lister_tous_utilisateur(utilisateur)

    # THEN
    assert len(res) == 2
    for id_utilisateur in res:
        assert id_utilisateur == utilisateur


def lister_tous_utilisateur_echec():
    """Vérifier que la méthode lister_tous_utilisateur renvoie bien une erreur"""

    # GIVEN
    utilisateur = UtilisateurDao().lister_tous()
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.lister_tous_utilisateur.side_effect = Exception("Erreur de base de données")

    utilisateur_service = UtilisateurService()
    utilisateur_service.AvisDao = mock_dao 

    # WHEN
    res = utilisateur_service.lister_tous_utilisateur(utilisateur)

    # THEN
    assert res[]


def trouver_par_pseudo_utilisateur_ok():
    """Vérifier que la méthode trouver_par_pseudo fonctionne correctement"""

    # GIVEN
    utilisateur = UtilisateurDao().lister_tous()
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.lister_tous_utilisateur.return_value = [pseudo for pseudo in liste_utilisateur if pseudo.id_utilisateur == utilisateur]

    utilisateur_service = UtilisateurService()
    utilisateur_service.AvisDao = mock_dao 

    # WHEN
    res = utilisateur_service.lister_tous_utilisateur(utilisateur)

    # THEN
    assert len(res) == 2
    for pseudo in res:
        assert pseudo.id_utilisateur == utilisateur


def trouver_par_pseudo_utilisateur_echec():
    """Vérifier que la méthode trouver_par_pseudo renvoie bien une erreur"""

    # GIVEN
    utilisateur = UtilisateurDao().lister_tous()
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.lister_tous_utilisateur.side_effect = Exception("Erreur de base de données")

    utilisateur_service = UtilisateurService()
    utilisateur_service.AvisDao = mock_dao 

    # WHEN
    res = utilisateur_service.lister_tous_utilisateur(utilisateur)

    # THEN
    assert res[]


def se_connecter_ok():
    """Vérifier que la méthode se_connecter fonctionne correctement"""

    # GIVEN
    utilisateur = UtilisateurDao().se_connecter()
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.connecter.return_value=True

    utilisateur_service = UtilisateurService()
    utilisateur_service.AvisDao = mock_dao 

    # WHEN
    res = utilisateur_service.se_connecter(utilisateur)

    # THEN
    assert res is True


def se_connecter_echec():
    """Vérifier que la méthode se_connecter renvoie bien une erreur"""

    # GIVEN
    utilisateur = UtilisateurDao().se_connecter()
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.se_connecter.return_value=False

    utilisateur_service = UtilisateurService()
    utilisateur_service.AvisDao = mock_dao 

    # WHEN
    res = utilisateur_service.se_connecter(utilisateur)

    # THEN
    assert res is False


def se_deconnecter_ok():
    """Vérifier que la méthode se_deconnecter fonctionne comme il faut"""

    # GIVEN
    utilisateur = UtilisateurService().se_deconnecter()
    mock_dao = MagicMock(spec=UtilisateurService)
    mock_dao.se_deconnecter.UtilisateurService = mock_dao

    # WHEN
    res = utilisateur_service.se_deconnecter(utilisateur)

    # THEN
    assert res is True


def se_deconnecter_echec():
    """Vérifier que la méthode se_déconnecter renvoie bien une erreur"""

    # GIVEN
    utilisateur = UtilisateurService().se_deconnecter()
    mock_dao = MagicMock(spec=UtilisateurService)
    mock_dao.se_deconnecter.UtilisateurService = mock_dao

    # WHEN
    res = utilisateur_service.se_deconnecter(utilisateur)

    # THEN
    assert res is True


