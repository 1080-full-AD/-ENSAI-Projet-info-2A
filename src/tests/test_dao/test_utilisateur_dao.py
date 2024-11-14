import time
import pytest
import os
from unittest.mock import patch
from src.utils.reset_database import ResetDatabase
from src.business_objet.utilisateur import Utilisateur
from src.dao.utilisateur_dao import UtilisateurDao
from src.utils import securite
from src.dao.avis_dao import AvisDao


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test"""
    with patch.dict(os.environ, {"SCHEMA": "projet_test_dao"}):
        ResetDatabase().lancer()
        yield


def test_creer_ok():
    """Création d'un utilisateur réussie"""

    # GIVEN
    user = Utilisateur(pseudo="LoveMangaMax", age=23)

    # WHEN
    created = UtilisateurDao().creer(user)

    # THEN
    assert created is not None


def test_creer_echec():
    """Création d'un utilisateur échouée"""

    # GIVEN
    user = Utilisateur(pseudo="LoveMangaMax", age=23)

    # WHEN
    created = UtilisateurDao().creer(user)

    # THEN
    assert not created


def test_trouver_par_pseudo_existant():
    """Méthode permettant de tester la méthode qui cherche un utilisateur par
    pseudo. Ici, elle teste si la méthode fonctionne avec un pseudo existant
    dans la base"""
    # GIVEN
    pseudo = "user1"

    # WHEN
    res = UtilisateurDao().trouver_par_pseudo(pseudo)

    # THEN
    assert res is not None


def teste_trouver_par_pseudo_non_existant():
    """Méthode permettant de tester la méthode qui cherche un utilisateur par
    pseudo. Ici, elle teste si la méthode fonctionne avec un pseudo qui
    n'existe pas dans la base. Elle doit renvoyer None si le pseudo
    n'existe pas dans la base"""
    # GIVEN
    pseudo = "AbsentBDD"

    # WHEN
    res = UtilisateurDao().trouver_par_pseudo(pseudo)

    # THEN
    assert res is None


def test_lister_tous():
    """Vérifie que la méthode renvoie une liste d'utilisateurs
    de taille supérieure ou égale à 2
    """

    # GIVEN

    # WHEN
    utilisateurs = UtilisateurDao().lister_tous()

    # THEN
    assert isinstance(utilisateurs, list)
    for j in utilisateurs:
        assert isinstance(j, (Utilisateur))
    assert len(utilisateurs) >= 2


def test_supprimer_echec():
    """Suppression d'un utilisateur non réussie"""

    # GIVEN
    user = Utilisateur(pseudo="LoveMangaMax", age=23, id_utilisateur=33333)

    # WHEN
    suppression = UtilisateurDao().supprimer(user)

    # THEN
    assert not suppression


def test_supprimer_ok():
    """Suppression d'un utilisateur réussie'"""

    # GIVEN
    user = Utilisateur(pseudo="LoveMangaMax", age=23, id_utilisateur=1)

    # WHEN
    suppression = UtilisateurDao().supprimer(user)

    # THEN
    assert suppression


def test_modifier_ok():
    """Modification d'un utilisateur réussie"""

    # GIVEN
    new_age = 24
    user = Utilisateur(pseudo="LoveMangaMax", age=23)

    # WHEN
    modification = UtilisateurDao().modifier(user)

    # THEN
    assert modification is not None


def test_modifier_echec():
    """Modification d'un utilisateur échouée"""

    # GIVEN
    user = Utilisateur(pseudo="LoveMangaMax", age=23)

    # WHEN
    modification = UtilisateurDao().modifier(user)

    # THEN
    assert not modification


def test_se_connecter_ok():
    """Connexion d' utilisateur' réussie"""

    # GIVEN
    pseudo = "user1"
    mdp = "password1"

    # WHEN
    UtilisateurDao().se_connecter(pseudo, securite.hash_password(mdp, pseudo))

    # THEN
    assert True


def test_se_connecter_echec():
    """Connexion d'un utilisateur échouée (pseudo ou mdp incorrect)"""

    # GIVEN
    pseudo = "tototata"
    mdp = "password2"

    # WHEN
    user = UtilisateurDao().se_connecter(pseudo, securite.hash_password(mdp, pseudo))

    # THEN
    assert not user


def test_trouver_par_id_existant():
    """Recherche par id d'un utilisateur existant"""

    # GIVEN
    id_utilisateur = 1

    # WHEN
    user = UtilisateurDao().trouver_par_id(id_utilisateur)

    # THEN
    assert user is not None


def test_trouver_par_id_non_existant():
    """Recherche par id d'un utilisateur n'existant pas"""

    # GIVEN
    id_utilisateur = 9999999999999

    # WHEN
    user = UtilisateurDao().trouver_par_id(id_utilisateur)

    # THEN
    assert user is None


if __name__ == "__main__":
    pytest.main([__file__])
