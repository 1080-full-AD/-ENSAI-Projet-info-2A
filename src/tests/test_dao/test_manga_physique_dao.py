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
        # ResetDatabase().lancer()
        yield


def test_creer_manga_physique_ok():
    """Création d'un manga physique réussie"""

    # GIVEN
    manga = MangaPhysique(
        id_manga=3,
        id_utilisateur=3,
        titre_manga="Test Manga",
        auteurs="Auteur Test",
        synopsis="Un test de création de manga physique.",
        tomes_manquants=[1, 3],
        dernier_tome=5,
        status="en cours",
        nb_chapitres=10,
        nb_volumes=5,
    )

    # WHEN
    creation = MangaPhysiqueDao().creer(manga)

    # THEN
    assert creation is True


def test_creer_manga_physique_echec():
    """Création d'un manga physique échouée"""

    # GIVEN
    manga = MangaPhysique(
        id_manga=None,
        id_utilisateur=None,
        titre_manga="Manga Invalide",
        auteurs="Auteur Invalide",
        synopsis="Un manga sans identifiant utilisateur.",
        tomes_manquants=[],
        dernier_tome=0,
        status="inconnu",
        nb_chapitres=10,
        nb_volumes=5,
    )

    # WHEN
    creation = MangaPhysiqueDao().creer(manga)

    # THEN
    assert not creation


def test_supprimer_manga_physique_ok():
    """Suppression d'un manga physique réussie"""

    # GIVEN
    manga = MangaPhysique(
        id_manga=2,
        id_utilisateur=3,
        titre_manga="Test Manga",
        auteurs="Auteur Test",
        synopsis="Un test de suppression de manga physique.",
        tomes_manquants=[1, 3],
        dernier_tome=5,
        status="en cours",
        nb_chapitres=10,
        nb_volumes=5,
    )

    # WHEN
    MangaPhysiqueDao().creer(manga)
    suppression = MangaPhysiqueDao().supprimer_manga_physique(manga)

    # THEN
    assert suppression


def test_supprimer_manga_physique_echec():
    """Suppression d'un manga
    physique échouée (id non existant)"""

    # GIVEN
    manga = MangaPhysique(
        id_manga=999,
        id_utilisateur=3,
        titre_manga="Manga Absent",
        auteurs="Auteur Absent",
        synopsis="Un manga qui n'existe pas dans la base.",
        tomes_manquants=[],
        dernier_tome=0,
        status="inconnu",
        nb_chapitres=10,
        nb_volumes=5,
    )

    # WHEN
    suppression = MangaPhysiqueDao().supprimer_manga_physique(manga)

    # THEN
    assert not suppression


def test_modifier_manga_physique_ok():
    """Modification d'un manga physique réussie"""

    # GIVEN
    manga = MangaPhysique(
        id_manga=1,
        id_utilisateur=3,
        titre_manga="Titre Initial",
        auteurs="Auteur Test",
        synopsis="Synopsis Initial",
        tomes_manquants=[2],
        dernier_tome=10,
        status="en cours",
        nb_chapitres=10,
        nb_volumes=5,
    )
    manga.titre_manga = "Titre Modifié"

    # WHEN
    MangaPhysiqueDao().creer(manga)
    modification = MangaPhysiqueDao().modifier_manga_physique(manga)

    # THEN
    assert modification is not None


def test_modifier_manga_physique_echec():
    """Modification d'un manga
    physique échouée (id non existant)"""

    # GIVEN
    manga = MangaPhysique(
        id_manga=999,
        id_utilisateur=3,
        titre_manga="Titre Inconnu",
        auteurs="Auteur Inconnu",
        synopsis="Un manga inexistant.",
        tomes_manquants=[],
        dernier_tome=0,
        status="inconnu",
        nb_chapitres=10,
        nb_volumes=5,
    )

    # WHEN
    modification = MangaPhysiqueDao().modifier_manga_physique(manga)

    # THEN
    assert not modification


def test_liste_mangas_physiques_utilisateur_existant():
    """Lister tous les mangas physiques d'un utilisateur existant"""

    # GIVEN

    id_utilisateur = 3

    manga_1 = MangaPhysique(
        id_manga=4,
        id_utilisateur=3,
        titre_manga="Titre Inconnu",
        auteurs="Auteur Inconnu",
        synopsis="Un manga inexistant.",
        tomes_manquants=[5],
        dernier_tome=0,
        status="inconnu",
        nb_chapitres=10,
        nb_volumes=5,
    )

    manga_2 = MangaPhysique(
        id_manga=27,
        id_utilisateur=3,
        titre_manga="Titre Inconnu",
        auteurs="Auteur Inconnu",
        synopsis="Un manga inexistant.",
        tomes_manquants=[5],
        dernier_tome=0,
        status="inconnu",
        nb_chapitres=10,
        nb_volumes=5,
    )

    # WHEN
    MangaPhysiqueDao().creer(manga_1)
    MangaPhysiqueDao().creer(manga_2)
    liste_mangas = MangaPhysiqueDao().liste_manga_physique(id_utilisateur)

    # THEN
    assert len(liste_mangas) == 4


def test_liste_mangas_physiques_utilisateur_non_existant():
    """Lister tous les mangas physiques d'un utilisateur non existant"""

    # GIVEN
    id_utilisateur = 999

    # WHEN
    liste_mangas = MangaPhysiqueDao().liste_manga_physique(id_utilisateur)

    # THEN
    assert liste_mangas is not None
    assert len(liste_mangas) == 0


def test_rechercher_manga_physique_ok():
    # GIVEN
    id_utilisateur = 3
    id_manga = 4
    manga_1 = MangaPhysique(
        id_manga=4,
        id_utilisateur=2,
        titre_manga="Titre Inconnu",
        auteurs="Auteur Inconnu",
        synopsis="Un manga inexistant.",
        tomes_manquants=[5],
        dernier_tome=0,
        status="inconnu",
        nb_chapitres=10,
        nb_volumes=5,
    )

    # WHEN
    MangaPhysiqueDao().creer(manga_1)
    liste_mangas = MangaPhysiqueDao().rechercher_manga_physique(
        id_utilisateur=id_utilisateur, id_manga=id_manga
    )

    # THEN
    assert liste_mangas is not None


if __name__ == "__main__":
    pytest.main([__file__])
