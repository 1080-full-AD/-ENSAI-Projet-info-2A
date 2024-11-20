from unittest.mock import patch, MagicMock

from src.service.utilisateur_service import UtilisateurService
from src.dao.utilisateur_dao import UtilisateurDao
from src.business_objet.utilisateur import Utilisateur

import unittest

# Exemple d'utilisateur:
liste_utilisateur = [
    Utilisateur(
        pseudo="Naruto54",
        age=16,
        mot_de_passe=("mdpManga4#", "Naruto54"),
        id_utilisateur=1,
    ),
    Utilisateur(
        pseudo="missmanga",
        age=18,
        mot_de_passe=("126OnePiece#", "missmanga"),
        id_utilisateur=2,
    ),
    Utilisateur(
        pseudo="23One", age=22, mot_de_passe=("78Naruto#", "23One"), id_utilisateur=5
    ),
]


def test_pseudo_existe_deja_ok():
    """Vérifier que la méthode pseudo_existe_déjà fonctionne correctement"""

    # GIVEN
    pseudo, age, mot_de_passe, id_utilisateur = (
        "user2",
        16,
        "mdpManga7#",
        678,
    )
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.lister_tous.return_value = True

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao

    # WHEN
    utilisateur = utilisateur_service.pseudo_deja_utilise(pseudo)

    # THEN
    assert utilisateur is True


def test_pseudo_existe_déjà_echec():
    """Vérifier que la méthode pseudo_existe_déjà renvoie bien une erreur"""

    # GIVEN
    pseudo, age, mot_de_passe, id_utilisateur = (
        "Naruto54",
        16,
        "mdpManga7#",
        678,
    )
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.lister_tous.return_value = False

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao

    # WHEN
    utilisateur = utilisateur_service.pseudo_deja_utilise(pseudo)

    # THEN
    assert utilisateur is False


def test_creer_utilisateur_ok():
    """Vérifier que la méthode creer_utilisateur fonctionne bien"""

    # GIVEN
    pseudo, age, mot_de_passe, id_utilisateur = (
        "fanmanga3",
        22,
        "Monste_R12",
        678,
    )
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.creer.return_value = True

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao
    utilisateur_service.pseudo_deja_utilise = MagicMock(return_value=False)

    # WHEN
    utilisateur = utilisateur_service.creer_utilisateur(
        pseudo, age, mot_de_passe, id_utilisateur
    )

    # THEN
    assert utilisateur is not None


def test_creer_utilisateur_echec(self):
    """Vérifier que la méthode creer_utilisateur renvoie bien un échec"""

    # GIVEN
    pseudo, age, mot_de_passe, id_utilisateur = (
        "FanManga",
        22,
        "Monste_R12",
        678,
    )
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.creer.return_value.side_effet = ValueError(
        "Ce nom d'utilisateur est déjà pris."
    )

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao

    # WHEN
    utilisateur = utilisateur_service.creer_utilisateur(
        pseudo, age, mot_de_passe, id_utilisateur
    )

    # THEN
    self.assertEqual(utilisateur, "Ce nom d'utilisateur est déjà pris.")


def test_modifier_utilisateur_ok():
    """Vérifier que la méthode modifier_utilisateur fonctionne correctement"""

    # GIVEN
    user = Utilisateur(
        "fanmang",
        22,
        "Monste_R12",
        678,
    )
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.modifier.return_value = True

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao

    # WHEN
    utilisateur = utilisateur_service.modifier_utilisateur(user)

    # THEN
    assert utilisateur is not None


def test_modifier_utilisateur_echec():
    """Vérifier que la méthode modifier_utilisateur renvoie bien une erreur"""

    # GIVEN
    user = Utilisateur(
        "fanmang",
        22,
        "Monste_R12",
        678,
    )
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.modifier.return_value = False

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao

    # WHEN
    utilisateur = utilisateur_service.modifier_utilisateur(user)

    # THEN
    assert utilisateur is None


def test_supprimer_utilisateur_ok():
    """Vérifier que la méthode supprimer_utilsiateur fonctionne correctement"""

    # GIVEN
    user = Utilisateur(
        "fanmang",
        22,
        "Monste_R12",
        678,
    )
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.supprimer.return_value = True

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao

    # WHEN
    utilisateur = utilisateur_service.supprimer_utilisateur(user)

    # THEN
    assert utilisateur is not None


def test_supprimer_utilisateur_echec():
    """Vérifier que la méthode supprimer_utilsiateur renvoie bien une erreur"""

    # GIVEN
    user = Utilisateur(
        "fanmang",
        22,
        "Monste_R12",
        678,
    )
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.supprimer.return_value = False

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao

    # WHEN
    utilisateur = utilisateur_service.supprimer_utilisateur(user)

    # THEN
    assert utilisateur is False


def test_trouver_par_pseudo_utilisateur_ok():
    """Vérifier que la méthode qui liste tous les utilisateurs grâce à leur pseudo fonctionne"""

    # GIVEN
    utilisateur_service = UtilisateurService()

    pseudo = "user2"
    mock_dao = MagicMock(spec=UtilisateurDao)
    utilisateur_service.UtilisateurDao = mock_dao

    utilisateurs_simules = [
        {
            "id_utilisateur": 2,
            "pseudo": "user2",
            "mot_de_passe": "password2",
            "age": 30,
        },
        {
            "id_utilisateur": 2,
            "pseudo": "user2",
            "mot_de_passe": "password2",
            "age": 30,
        },
        {
            "id_utilisateur": 3,
            "pseudo": "user1",
            "mot_de_passe": "password3",
            "age": 22,
        },
    ]

    mock_dao.lister_tous.return_value = utilisateurs_simules
    # WHEN
    res = utilisateur_service.trouver_par_pseudo_utilisateur(pseudo)

    # THEN
    assert res.pseudo == pseudo


def test_trouver_par_pseudo_utilisateur_echec():
    """Vérifier que la méthode qui renvoie tous les utilisateurs renvoie bien
    un échec"""

    # GIVEN
    pseudo = "fanmang"
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.lister_tous.side_effect = Exception("Erreur de base de données")

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao

    utilisateurs_simules = [
        {
            "id_utilisateur": 1,
            "pseudo": "user1",
            "mot_de_passe": "password1",
            "age": 25,
        },
        {
            "id_utilisateur": 2,
            "pseudo": "user2",
            "mot_de_passe": "password2",
            "age": 30,
        },
        {
            "id_utilisateur": 3,
            "pseudo": "user1",
            "mot_de_passe": "password3",
            "age": 22,
        },
    ]

    mock_dao.lister_tous.return_value = utilisateurs_simules
    # WHEN
    res = utilisateur_service.trouver_par_pseudo_utilisateur(pseudo)

    # THEN
    assert res == None


def test_lister_tous_utilisateur_ok():
    """Lister tous les utilisateurs avec succès"""

    # GIVEN
    id_utilisateur = 1
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.lister_tous.return_value = [
        pseudo
        for pseudo in liste_utilisateur
        if pseudo.id_utilisateur == id_utilisateur
    ]

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao

    # WHEN
    res = utilisateur_service.lister_tous_utilisateur()

    # THEN
    assert len(res) == 1
    for pseudo in res:
        assert pseudo.id_utilisateur == id_utilisateur


def test_lister_tous_utilisateur_echec(self):
    """Vérifier que la méthode qui liste tous les utilisateurs grâce à leur
    identifiant renvoie bien un échec"""

    # GIVEN
    id_utilisateur = 998
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.lister_tous.side_effect = Exception("Erreur de base de données")

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao

    # WHEN
    res = utilisateur_service.lister_tous_utilisateur(id_utilisateur)

    # THEN
    self.assertEqual(res == [], "Erreur de base de données")


def test_se_connecter_ok():
    """Vérifier que la méthode se_connecter fonctionne correctement"""

    # GIVEN
    user = Utilisateur(pseudo="user2", age=30, mot_de_passe="password2")
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.se_connecter.return_value = True

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao

    # WHEN
    utilisateur = utilisateur_service.se_connecter(
        pseudo=user.pseudo, mot_de_passe=user.mot_de_passe
    )

    # THEN
    assert utilisateur.pseudo == "user2"
    mock_dao.se_connecter.assert_called_once_with(user)


def test_se_connecter_echec():
    """Vérifier que la méthod se connecter renvoie bien une erreur"""

    # GIVEN
    user = Utilisateur(pseudo="NarutO54", mot_de_passe="mdpMAnga7#", age=18)
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.se_connecter.return_value = False

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao

    # WHEN
    utilisateur = utilisateur_service.se_connecter(
        pseudo=user.pseudo, mot_de_passe=user.mot_de_passe
    )

    # THEN
    assert utilisateur is None


def test_se_deconnecter_ok():
    """Vérifier que la méthode se déconnecter fonctionne comme il le faut"""

    # GIVEN
    pseudo, mot_de_passe, age = "user2", "password2", 30
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.se_connecter.return_value = True

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao

    # WHEN
    utilisateur = utilisateur_service.se_connecter(pseudo, mot_de_passe)

    # THEN
    assert utilisateur is None


def test_se_deconnecter_echec():
    """Vérifier que la méthode se déconnecter renvoie bien une erreur"""

    # GIVEN
    user = Utilisateur(pseudo="Naruto54", mot_de_passe="mdpManga72", age=18)
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.se_connecter.return_value = False

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao

    # WHEN
    utilisateur = utilisateur_service.se_connecter(
        pseudo=user.pseudo, mot_de_passe=user.mot_de_passe
    )

    # THEN
    assert utilisateur is None


def test_create_password_ok():
    """Vérifier que la méthode create_password fonctionne correctement"""

    # GIVEN
    user = Utilisateur("password1", age=23)
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.creer.return_value = True
    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao

    # WHEN
    utilisateur = utilisateur_service.create_password(user)
    mock_dao.creer.assert_called_once_with(user)

    # THEN
    assert utilisateur is True


def test_create_password_echec():
    """Vérifier que la méthode create_password renvoie bien une erreur"""

    # GIVEN
    user = "123456##7#"
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.creer.return_value = False

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao

    # WHEN
    utilisateur = utilisateur_service.create_password(user)

    # THEN
    assert utilisateur is False


def test_is_valid_mdp_ok():
    """Vérifier que la méthode is_valid_mdp fonctionne comme il le faut"""

    # GIVEN
    mdp = "A123456aB"
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.modifier.return_value = True

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurService = mock_dao

    # WHEN
    utilisateur = utilisateur_service.is_valid_mdp(mdp)

    # THEN
    assert utilisateur is not None


def test_is_valid_mdp_echec():
    """Vérifier que la méthode is_valid_mdp renvoie bien une erreur"""

    # GIVEN
    mdp = "#123456aN?D"
    mock_dao = MagicMock(spec=UtilisateurDao)
    mock_dao.modifier.return_value = False

    utilisateur_service = UtilisateurService()
    utilisateur_service.UtilisateurDao = mock_dao

    # WHEN
    utilisateur = utilisateur_service.is_valid_mdp(mdp)

    # THEN
    assert utilisateur is False


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
