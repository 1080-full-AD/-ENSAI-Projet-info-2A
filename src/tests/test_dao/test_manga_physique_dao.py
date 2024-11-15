import pytest
from unittest.mock import patch
from src.business_objet.manga_physique import MangaPhysique
from src.dao.manga_physique_dao import MangaPhysiqueDao
from src.utils.reset_database import ResetDatabase
import os


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test"""
    with patch.dict(os.environ, {"SCHEMA": "projet_test_dao"}):
        ResetDatabase().lancer()
        yield


def test_creer_manga_physique_ok():
    """Tester la création d'un manga physique"""
    # GIVEN
    manga_physique = MangaPhysique(
        id_manga=1,
        titre_manga="Dragon Ball",
        auteurs="Akira Toriyama",
        synopsis="Un manga sur les aventures de Goku.",
        statut="Terminé",
        nb_tomes=42
    )

    # WHEN
    created = MangaPhysiqueDao().creer_manga_physique(manga_physique)

    # THEN
    assert created is not None
    assert created.id_manga == 1


def test_creer_manga_physique_echec():
    """Tester la création d'un manga physique échouée si données invalides"""
    # GIVEN
    manga_physique = MangaPhysique(
        id_manga=None,
        titre_manga="Dragon Ball Z",
        auteurs="Akira Toriyama",
        synopsis="Suivi de Dragon Ball.",
        statut="En cours",
        nb_tomes=20
    )

    # WHEN
    created = MangaPhysiqueDao().creer_manga_physique(manga_physique)

    # THEN
    assert created is None



def test_trouver_manga_physique_par_utilisateur_existant():
    """Tester la recherche d'un manga physique par identifiant d'utilisateur existant"""
    # GIVEN
    utilisateur=Utilisateur(pseudo="USER1", age=25, mot_de_passe=None, id_utilisateur=None)

    # WHEN
    manga = MangaPhysiqueDao().liste_manga_physique(utilisateur)

    # THEN
    assert manga is not None
    assert manga.id_manga == id_manga


def test_trouver_manga_physique_par_id_non_existant():
    """Tester la recherche d'un manga physique par identifiant non existant"""
    # GIVEN
    id_manga = 9999

    # WHEN
    manga = MangaPhysiqueDao().trouver_par_id(id_manga)

    # THEN
    assert manga is None


def test_modifier_manga_physique():
    """Tester la modification d'un manga physique existant"""
    # GIVEN
    manga_physique = MangaPhysique(
        id_manga=1,
        titre_manga="Dragon Ball Z",
        auteurs="Akira Toriyama",
        synopsis="Les aventures de Goku et ses amis.",
        statut="Terminé",
        nb_tomes=42
    )

    # WHEN
    modified = MangaPhysiqueDao().modifier_manga_physique(manga_physique)

    # THEN
    assert modified is not None
    assert modified.titre_manga == "Dragon Ball Z"


def test_supprimer_manga_physique():
    """Tester la suppression d'un manga physique existant"""
    # GIVEN
    manga_physique = MangaPhysique(
        id_manga=1,
        titre_manga="Dragon Ball",
        auteurs="Akira Toriyama",
        synopsis="Un manga sur les aventures de Goku.",
        statut="Terminé",
        nb_tomes=42
    )

    # WHEN
    deleted = MangaPhysiqueDao().supprimer_manga_physique(manga_physique)

    # THEN
    assert deleted


def test_supprimer_manga_physique_non_existant():
    """Tester la suppression d'un manga physique non existant"""
    # GIVEN
    manga_physique = MangaPhysique(
        id_manga=9999,
        titre_manga="Inexistant",
        auteurs="Auteur Inconnu",
        synopsis="Synopsis inexistant.",
        statut="Non défini",
        nb_tomes=0
    )

    # WHEN
    deleted = MangaPhysiqueDao().supprimer_manga_physique(manga_physique)

    # THEN
    assert not deleted


if __name__ == "__main__":
    pytest.main([__file__])
