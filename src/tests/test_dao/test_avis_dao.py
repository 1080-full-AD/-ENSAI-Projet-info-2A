import pytest

import os

from unittest.mock import patch

from src.utils.reset_database import ResetDatabase

from src.dao.avis_dao import AvisDao

from src.business_objet.avis import Avis


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test"""
    with patch.dict(os.environ, {"SCHEMA": "projet"}):
        ResetDatabase().lancer()
        yield

def test_creer_ok():
    """Création d'avis réussie"""

    # GIVEN
    avis = Avis(id_manga=3, id_utilisateur=2, texte="Masterpiece")

    # WHEN
    creation_ok = AvisDao().creer(avis)

    # THEN
    assert creation_ok
    assert avis.id_utilisateur == 2
    assert avis.id_manga == 3


def test_creer_ko():
    """Création d'avis échouée """

    # GIVEN
    avis = Avis(id_manga=None, id_utilisateur=2, texte='l')

    # WHEN
    creation_ok = AvisDao().creer(avis)

    # THEN
    assert not creation_ok



def test_trouver_tous_par_id_existant():
    """Recherche les avis par id d'un joueur existant"""

    # GIVEN
    id_utilisateur = 1

    # WHEN
    avis = AvisDao().trouver_tous_par_id(id_utilisateur)

    # THEN
    assert isinstance(avis, list)
    assert all(isinstance(a, Avis) for a in avis)


def test_trouver_par_id_non_existant():
    """Recherche les avis par id d'un joueur n'existant pas"""

    # GIVEN
    id_utilisateur = 999999999

    # WHEN
    avis = AvisDao().trouver_tous_par_id(id_utilisateur)

    # THEN
    assert isinstance(avis, list)
    assert len(avis) == 0


def test_supprimer_avis_ok():
    """Suppression d'un avis réussie"""

    # GIVEN
    avis = Avis(id_manga=1, id_utilisateur=1, texte="test")

    # WHEN
    suppression_ok = AvisDao().supprimer_avis(avis)

    # THEN
    assert suppression_ok


def test_supprimer_avis_ko():
    """Suppression d'un avis échouée (avis non existant)"""

    # GIVEN
    avis = Avis(id_manga=9999, id_utilisateur=9999, texte="non existant")

    # WHEN
    suppression_ok = AvisDao().supprimer_avis(avis)

    # THEN
    assert not suppression_ok



def test_modifier_ok():
    """Modification d'avis réussie"""

    # GIVEN
    new_texte = "test_lol"
    avis = Avis(id_manga=1, id_utilisateur=1, texte='Amazing manga!')

    # WHEN
    modification_ok = AvisDao().modifier(avis, new_texte)

    # THEN
    assert modification_ok


def test_modifier_ko():
    """Modification d'avis échouée """

    # GIVEN
    new_texte = "test_lol"
    avis = Avis(id_manga=99999, id_utilisateur=999999, texte="test")

    # WHEN
    modification_ok = AvisDao().modifier(avis, new_texte)

    # THEN
    assert not modification_ok


if __name__ == "__main__":
    pytest.main([__file__])
