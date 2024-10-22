import os
import pytest

from unittest.mock import patch

from utils.reset_database import ResetDatabase
from utils.securite import hash_password

from dao.avis_dao import AvisDAO

from business_objet.avis import Avis


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test"""
    with patch.dict(os.environ, {"SCHEMA": "projet_test_dao"}):
        ResetDatabase().lancer(test_dao=True)
        yield

def test_creer_ok():
    """Création d'avis réussie"""

    # GIVEN
    avis = Avis(id_manga=22, id_utilisateur=44, texte="Masterpiece")

    # WHEN
    creation_ok = AvisDAO().creer(avis)

    # THEN
    assert creation_ok
    assert avis.id_utilisateur


#def test_creer_ko():
#    """Création d'avis échouée """

    # GIVEN
#    avis = Avis(id_manga=22, id_utilisateur=44, texte="Masterpiece")

    # WHEN
#    creation_ok = AvisDao().creer(avis)

    # THEN
#    assert not creation_ok



def test_trouver_tous_par_id_existant():
    """Recherche les avis par id d'un joueur existant"""

    # GIVEN
    id_utilisateur = 44

    # WHEN
    avis = AvisDAO().trouver_tous_par_id(id_utilisateur)

    # THEN
    assert isinstance(avis, list)
    assert all(isinstance(a, Avis) for a in avis)


def test_trouver_par_id_non_existant():
    """Recherche les avis par id d'un joueur n'existant pas"""

    # GIVEN
    id_utilisateur = 999999999

    # WHEN
    avis = AvisDAO().trouver_tous_par_id(id_utilisateur)

    # THEN
    assert isinstance(avis, list)
    assert len(avis) == 0


def test_supprimer_avis_ok():
    """Suppression d'un avis réussie"""

    # GIVEN
    avis = Avis(id_manga=1, id_utilisateur=1, texte="test")

    # WHEN
    suppression_ok = AvisDAO().supprimer_avis(avis)

    # THEN
    assert suppression_ok


def test_supprimer_avis_ko():
    """Suppression d'un avis échouée (avis non existant)"""

    # GIVEN
    avis = Avis(id_manga=9999, id_utilisateur=9999, texte="non existant")

    # WHEN
    suppression_ok = AvisDAO().supprimer_avis(avis)

    # THEN
    assert not suppression_ok



def test_modifier_ok():
    """Modification de Joueur réussie"""

    # GIVEN
    new_mail = "maurice@mail.com"
    joueur = Joueur(id_joueur=997, pseudo="maurice", age=20, mail=new_mail)

    # WHEN
    modification_ok = JoueurDao().modifier(joueur)

    # THEN
    assert modification_ok


def test_modifier_ko():
    """Modification de Joueur échouée (id inconnu)"""

    # GIVEN
    joueur = Joueur(id_joueur=8888, pseudo="id inconnu", age=1, mail="no@mail.com")

    # WHEN
    modification_ok = JoueurDao().modifier(joueur)

    # THEN
    assert not modification_ok


def test_supprimer_ok():
    """Suppression de Joueur réussie"""

    # GIVEN
    joueur = Joueur(id_joueur=995, pseudo="miguel", age=1, mail="miguel@projet.fr")

    # WHEN
    suppression_ok = JoueurDao().supprimer(joueur)

    # THEN
    assert suppression_ok


def test_supprimer_ko():
    """Suppression de Joueur échouée (id inconnu)"""

    # GIVEN
    joueur = Joueur(id_joueur=8888, pseudo="id inconnu", age=1, mail="no@z.fr")

    # WHEN
    suppression_ok = JoueurDao().supprimer(joueur)

    # THEN
    assert not suppression_ok


def test_se_connecter_ok():
    """Connexion de Joueur réussie"""

    # GIVEN
    pseudo = "batricia"
    mdp = "9876"

    # WHEN
    joueur = JoueurDao().se_connecter(pseudo, hash_password(mdp, pseudo))

    # THEN
    assert isinstance(joueur, Joueur)


def test_se_connecter_ko():
    """Connexion de Joueur échouée (pseudo ou mdp incorrect)"""

    # GIVEN
    pseudo = "toto"
    mdp = "poiuytreza"

    # WHEN
    joueur = JoueurDao().se_connecter(pseudo, hash_password(mdp, pseudo))

    # THEN
    assert not joueur


if __name__ == "__main__":
    pytest.main([__file__])
