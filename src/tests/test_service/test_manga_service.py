from unittest.mock import MagicMock

from src.service.manga_service import MangaService
from src.dao.manga_dao import MangaDao
from src.business_objet.manga import Manga

import unittest


# Liste de mangas :
Liste_Manga = [
    Manga(
        id_manga=13,
        titre_manga="One Piece",
        auteurs="Eiichirō Oda",
        synopsis="Gol D. Roger, a man referred to as the King of the Pirates, is set to be executed by the World Government. But just before his demise,"
        " he confirms the existence of a great treasure, One Piece, located somewhere within the vast ocean known as the Grand Line. Announcing that One Piece can be claimed by anyone worthy enough to reach it,"
        "the King of the Pirates is executed and the Great Age of Pirates begins.\n\nTwenty-two years later, a young man by the name of Monkey D. Luffy is ready to embark on his own adventure, searching for One "
        "Piece and striving to become the new King of the Pirates. Armed with just a straw hat, a small boat, and an elastic body, he sets out on a fantastic journey to gather his own crew and a worthy ship that"
        " will take them across the Grand Line to claim the greatest status on the high seas.\n\n[Written by MAL Rewrite]",
    )
]


def test_creer_manga_ok():
    """Création d'un manga dans la BDD réussie"""

    # GIVEN
    manga = Manga(
        9999,
        "Le12",
        "Eiichirō Oda",
        "Manga génial qui raconte la vie de 12 personnes",
    )
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.creer_manga.return_value = True

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao

    # WHEN
    manga = manga_service.creer_manga(manga)

    # THEN
    assert manga is not None


def test_creer_manga_echec():
    """Création d'un manga dans la BDD réussie"""

    # GIVEN
    manga = Manga(
        9999,
        "Le12",
        "Eiichirō Oda",
        "Manga génial qui raconte la vie de 12 personnes",
    )
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.creer_manga.return_value = False

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao

    # WHEN
    manga = manga_service.creer_manga(manga)

    # THEN
    assert manga is False


def test_recherche_manga_ok():
    """Tester la recherche d'un manga à partir de son titre"""

    # GIVEN
    titre_manga = "Monster"
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.trouver_par_titre.return_value = True

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao

    # WHEN
    manga = manga_service.rechercher_un_manga(titre_manga)

    # THEN
    assert isinstance(manga, Manga)


def test_recherche_manga_echec(self):
    """Tester si la recherche de manga à partir de son titre renvoie bien un échec"""

    # GIVEN
    titre_manga = "AbsentBDD"
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.trouver_par_titre.return_value.side_effect = ValueError(
        "Aucun manga ne possède ce titre :/"
    )

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao

    # WHEN
    manga = manga_service.rechercher_un_manga(titre_manga)

    # THEN
    self.assertEqual(manga, "Aucun manga ne possède ce titre :/")


def test_recherche_id_manga_ok():
    """Tester si la recherche de manga à partir de son id fonctionne"""

    # GIVEN
    id_manga = 11
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.trouver_par_id.return_value = True

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao

    # WHEN
    manga = manga_service.rechercher_un_id_manga(id_manga)

    # THEN
    assert manga is not None


def test_recherche_id_manga_echec(self):
    """Tester si la recherche de manga à partir de son id renvoie bien un échec"""

    # GIVEN
    id_manga = 9998
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.trouver_par_id.return_value.side_effect = ValueError(
        "Aucun manga ne possède cet identifiant :/"
    )

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao

    # WHEN
    manga = manga_service.rechercher_un_id_manga(id_manga)

    # THEN
    self.assertEqual(manga, "Aucun manga ne possède cet identifiant :/")


def test_supprimer_manga_ok():
    """Tester si la suppression d'un manga de la base fonctionne"""

    # GIVEN
    manga = Manga(
        9999,
        "Le12",
        "Eiichirō Oda",
        "Manga génial qui raconte la vie de 12 personnes",
    )
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.supprimer_manga.return_value = True

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao

    # WHEN
    res = manga_service.supprimer_un_manga(manga)

    # THEN
    assert res is not None


def test_supprimer_manga_echec():
    """Tester la méthode pour voir si elle renvoie bien un échec"""
    # GIVEN
    manga = Manga(
        9999,
        "Le12",
        "Eiichirō Oda",
        "Manga génial qui raconte la vie de 12 personnes",
    )
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.supprimer_manga.return_value = False

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao

    # WHEN
    manga = manga_service.supprimer_un_manga(manga)

    # THEN
    assert manga is False


def test_modifier_manga_ok():
    """Tester si la modification d'un manga est réussie"""

    # GIVEN
    manga = Manga(
        9999,
        "Le12",
        "Eiichirō Oda",
        "Manga génial qui raconte la vie de 12 personnes",
    )
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.modifier.return_value = True

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao

    # WHEN
    result = manga_service.modifier_un_manga(manga)

    # THEN
    assert result is not None


def test_modifier_manga_echec():
    """Tester si la modification d'un manga est un échec"""

    # GIVEN
    manga = Manga(
        9999,
        "Le12",
        "Eiichirō Oda",
        "Manga génial qui raconte la vie de 12 personnes",
    )
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.modifier.return_value = False

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao

    # WHEN
    result = manga_service.modifier_un_manga(manga)

    # THEN
    assert result is False


def test_rechercher_un_auteur_ok():
    """Tester si la recherche d'un manga par le nom de son auteur fonctionne"""

    # GIVEN
    auteurs = "Urasawa, Naoki"
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.trouver_par_auteur.return_value = True

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao

    # WHEN
    result = manga_service.rechercher_un_auteur(auteurs)

    # THEN
    assert result is not None


def test_rechercher_un_auteur_echec():
    """Tester si la recherches d'un manga grâce au nom de son auteur est un échec"""

    # GIVEN
    auteurs = "Urasawa, Naoki"
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.trouver_par_auteur.return_value.side_effect = ValueError(
        "Aucun auteur ne s'apelle comme ça :/"
    )

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao

    # WHEN
    result = manga_service.rechercher_un_auteur(auteurs)

    # THEN
    assert result, "Aucun auteur ne s'apelle comme ça :/"


def test_rechercher_une_serie_ok():
    """Tester si la recherche de la saga d'un manga fonctionne"""

    # GIVEN
    titre = "One Piece"
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.trouver_serie_par_titre.return_value = True

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao

    # WHEN
    result = manga_service.rechercher_une_serie(titre)

    # THEN
    assert result is True


def test_rechercher_une_serie_echec():
    """Tester si la recherche de la saga d'un manga ne fonctionne pas"""

    # GIVEN
    titre = "One Piece"
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.trouver_serie_par_titre.return_value = False

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao

    # WHEN
    result = manga_service.rechercher_une_serie(titre)

    # THEN
    assert result is None


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
