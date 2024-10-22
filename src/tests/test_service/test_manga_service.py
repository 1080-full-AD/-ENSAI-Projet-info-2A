from unittest.mock import MagicMock

from src.service.manga_service import MangaService
from src.dao.manga_dao import MangaDao
from src.business_objet.manga import Manga


# Liste de mangas :
Liste_Manga = [
    Manga(id_manga=13, titre="One Piece", auteur="Eiichirō Oda", synopsis="Gol D. Roger, a man referred to as the King of the Pirates, is set to be executed by the World Government. But just before his demise,"
          " he confirms the existence of a great treasure, One Piece, located somewhere within the vast ocean known as the Grand Line. Announcing that One Piece can be claimed by anyone worthy enough to reach it,"
          "the King of the Pirates is executed and the Great Age of Pirates begins.\n\nTwenty-two years later, a young man by the name of Monkey D. Luffy is ready to embark on his own adventure, searching for One "
          "Piece and striving to become the new King of the Pirates. Armed with just a straw hat, a small boat, and an elastic body, he sets out on a fantastic journey to gather his own crew and a worthy ship that"
          " will take them across the Grand Line to claim the greatest status on the high seas.\n\n[Written by MAL Rewrite]")
]


def creer_manga_ok():
    """Création d'un manga dans la BDD réussie"""

    # GIVEN
    id_manga, titre, auteur, synopsis = 9999, "Le12", "Eiichirō Oda", "Manga génial qui raconte la vie de 12 personnes" 
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.creer.return_value = True

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao 

    # WHEN
    manga = manga_service.creer_un_manga(id_manga, titre, auteur, synopsis)

    # THEN
    assert manga is True


def creer_manga_echec():
    """Création d'un manga dans la BDD réussie"""

    # GIVEN
    id_manga, titre, auteur, synopsis = 9999, "Le12", "Eiichirō Oda", "Manga génial qui raconte la vie de 12 personnes" 
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.creer.return_value = False

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao 

    # WHEN
    manga = manga_service.creer_un_manga(id_manga, titre, auteur, synopsis)

    # THEN
    assert manga is False


def recherche_manga_ok():
    """Tester la recherche d'un manga à partir de son titre"""

    # GIVEN
    titre = "One Piece"
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.rechercher_un_manga.return_value = True

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao 

    # WHEN
    manga = manga_service.rechercher_un_manga(titre)

    # THEN
    assert manga is True


def recherche_manga_echec():
    """Tester si la recherche de manga à partir de son titre renvoie bien un échec"""

    # GIVEN
    titre = ["titre"]
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.rechercher_un_manga.return_value = False

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao 

    # WHEN
    manga = manga_service.rechercher_un_manga(titre)

    # THEN
    assert manga is False


def recherche_id_manga_ok():
    """Tester si la recherche de manga à partir de son id fonctionne"""

    # GIVEN
    id_manga = 13
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.rechercher_un_id_manga.return_value = True

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao 

    # WHEN
    manga = manga_service.rechercher_un_id_manga(id_manga)

    # THEN
    assert manga is True


def recherche_id_manga_echec():
    """Tester si la recherche de manga à partir de son id renvoie bien un échec"""

    # GIVEN
    id = "One Piece"
    mock_dao = MagicMock(spec=MangaDao)
    mock_dao.rechercher_un_id_manga.return_value = False

    manga_service = MangaService()
    manga_service.MangaDao = mock_dao 

    # WHEN
    manga = manga_service.rechercher_un_id_manga(id)

    # THEN
    assert manga is False






if __name__ == "__main__":
    import pytest

    pytest.main([__file__])