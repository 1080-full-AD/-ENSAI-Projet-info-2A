import time
import pytest
import os
from unittest.mock import patch
from src.utils.reset_database import ResetDatabase
from src.business_objet.manga import Manga
from src.dao.manga_dao import MangaDao


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test"""
    with patch.dict(os.environ, {"SCHEMA": "projet_test_dao"}):
        ResetDatabase().lancer()
        yield


def test_trouver_par_titre_existant():
    """Méthode permettant de tester la méthode qui cherche un manga par
    titre. Ici, elle teste si la méthode fonctionne avec un titre existant
    dans la base"""
    # GIVEN
    titre = "Monster"

    # WHEN
    res = MangaDao().trouver_par_titre(titre)

    # THEN
    assert res is not None


def teste_trouver_par_titre_non_existant():
    """Méthode permettant de tester la méthode qui cherche un manga par
    titre. Ici, elle teste si la méthode fonctionne avec un titre qui
    n'existe pas dans la base. Elle doit renvoyer None si le titre
    n'existe pas dans la base"""
    # GIVEN
    titre = "AbsentBDD"

    # WHEN
    res = MangaDao().trouver_par_titre(titre)

    # THEN
    assert res is None


# teser identifiant
def test_trouver_par_id_existant():
    """Méthode permettant de tester la méthode qui cherche un manga par
    identifiant. Ici, elle teste si la méthode fonctionne avec un identifiant existant
    dans la base"""
    # GIVEN
    id = 11

    # WHEN
    res = MangaDao().trouver_par_titre(id)

    # THEN
    assert res is None


def test_trouver_par_id_non_existant():
    """Méthode permettant de tester la méthode qui cherche un manga par
    identifiant. Ici, elle teste si la méthode fonctionne avec un
    identifiant qui n'existe pas dans la base. Elle doit renvoyer None
    si l'identifiant n'existe pas dans la base"""
    # GIVEN
    id = 999

    # WHEN
    res = MangaDao().trouver_par_titre(id)

    # THEN
    assert res is None


def test_creer_ok():
    """Création d'un manga réussie"""

    # GIVEN
    manga = Manga(
        9999,
        "Le12",
        "Eiichirō Oda",
        "Manga génial qui raconte la vie de 12 personnes",
        None,
        None,
    )

    # WHEN
    created = MangaDao().creer_manga(manga)

    # THEN
    assert created is not None
    assert manga.id_manga == 9999


def test_creer_echec():
    """Création d'un manga échouée"""

    # GIVEN
    manga = Manga(
        id_manga=None,
        titre_manga="gd",
        synopsis="manga génial sur la vie de gg",
        auteurs="Urasawa, Naoki",
        nb_volumes=4,
        nb_chapitres=12,
    )

    # WHEN
    created = MangaDao().creer_manga(manga)

    # THEN
    assert not created


def test_supprimer_echec():
    """Suppression d'un manga réussie"""

    # GIVEN
    manga = Manga(
        id_manga=995,
        titre_manga="miguel",
        synopsis="manga qui raconte la vie de miguel étudiant en art",
        auteurs="Urasawa, Naoki",
        nb_volumes=6,
        nb_chapitres=12,
    )

    # WHEN
    suppression = MangaDao().supprimer_manga(manga)

    # THEN
    assert not suppression


def test_supprimer_ok():
    """Suppression d'un manga réussie"""

    # GIVEN
    manga = Manga(
        id_manga=13,
        titre_manga="One Piece",
        synopsis="Gol D. Roger, a man referred to as the King of the Pirates,"
        "is set to be executed by the World Government. But just before his demise, he confirms the existence of a great treasure,"
        " One Piece, located somewhere within the vast ocean known as the Grand Line. Announcing that One Piece can be claimed by"
        "anyone worthy enough to reach it, the King of the Pirates is executed and the Great Age of Pirates begins."
        "Twenty-two years later, a young man by the name of Monkey D. Luffy is ready to embark on his own adventure"
        ", searching for One Piece and striving to become the new King of the Pirates. Armed with just a straw hat, a small boat,"
        "and an elastic body, he sets out on a fantastic journey to gather his own crew and a worthy ship that will take them across"
        "the Grand Line to claim the greatest status on the high seas.[Written by MAL Rewrite]",
        auteurs="Oda, Eiichiro",
        nb_volumes=None,
        nb_chapitres=None,
    )

    # WHEN
    suppression = MangaDao().supprimer_manga(manga)

    # THEN
    assert suppression


def test_modifier_ok():
    """Modification d'un manga réussie"""

    # GIVEN
    new_titre = "One Piece Test"
    manga = Manga(
        id_manga=13,
        titre_manga="One Piece",
        synopsis="Gol D. Roger, a man referred to as the King of the Pirates,"
        "is set to be executed by the World Government. But just before his demise, he confirms the existence of a great treasure,"
        " One Piece, located somewhere within the vast ocean known as the Grand Line. Announcing that One Piece can be claimed by"
        "anyone worthy enough to reach it, the King of the Pirates is executed and the Great Age of Pirates begins."
        "Twenty-two years later, a young man by the name of Monkey D. Luffy is ready to embark on his own adventure"
        ", searching for One Piece and striving to become the new King of the Pirates. Armed with just a straw hat, a small boat,"
        "and an elastic body, he sets out on a fantastic journey to gather his own crew and a worthy ship that will take them across"
        "the Grand Line to claim the greatest status on the high seas.[Written by MAL Rewrite]",
        auteurs="Oda, Eiichiro",
        nb_volumes=None,
        nb_chapitres=None,
    )

    # WHEN
    modification = MangaDao().modifier(manga)

    # THEN
    assert modification is not None


def test_modifier_echec():
    """Modification d'un manga échouée (id inconnu)"""

    # GIVEN
    manga = Manga(
        id_manga=8888,
        titre_manga="id inconnu",
        auteurs="Miguel",
        synopsis="Manga racontant la vie de Miguel",
        nb_volumes=56,
        nb_chapitres=134,
    )

    # WHEN
    modification = MangaDao().modifier(manga)

    # THEN
    assert not modification


def test_trouver_par_auteur_existant():
    """Rechercher un manga grâce à son/ses auteur/s existant"""

    # GIVEN
    auteurs = "Urasawa, Naoki"

    # WHEN
    manga = MangaDao().trouver_par_auteur(auteurs)

    # THEN
    assert manga is not None


def test_trouver_par_id_non_existant():
    """Rechercher un manga grâce à son/ses auteur/s n'existant pas"""

    # GIVEN
    auteurs = "Urasawa"

    # WHEN
    manga = MangaDao().trouver_par_auteur(auteurs)

    # THEN
    assert manga is None


def test_trouver_serie_par_titre_existant():
    """Rechercher une série grâce à son titre existant"""

    # GIVEN
    manga = "Naruto"

    # WHEN
    res = MangaDao().trouver_serie_par_titre(manga)

    # THEN
    assert res is not None


def test_trouver_serie_par_titre_non_existant():
    """Rechercher une série de mangas grâce à son titre n'existant pas"""

    # GIVEN
    manga = "NarutO"

    # WHEN
    res = MangaDao().trouver_serie_par_titre(manga)

    # THEN
    assert res is None


if __name__ == "__main__":
    pytest.main([__file__])
