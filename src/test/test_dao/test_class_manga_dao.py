import time
import pytest
from unittest import TestCase, TextTestRunner, TestLoader
from business_object.manga import Manga

from dao.manga_dao import MangaDao


class TestMangaDao(TestCase):
    """Classe permettant de réaliser des tests unitaires sur chaque 
        méthode de la classe MangaDao"""
# teste titre
    def trouver_par_titre_existant(self):
        """Méthode permettant de tester la méthode qui cherche un manga par 
        titre. Ici, elle teste si la méthode fonctionne avec un titre existant
        dans la base"""
        # GIVEN
        titre = "mettre le nom d'un manga de la base"

        # WHEN
        res = MangaDao().trouver_par_titre(titre)

        # THEN
        assert res is not None

    def trouver_par_titre_non_existant(self):
        """Méthode permettant de tester la méthode qui cherche un manga par
        titre. Ici, elle teste si la méthode fonctionne avec un titre qui 
        n'existe pas dans la base. Elle doit renvoyer None si le titre
        n'existe pas dans la base"""
        # GIVEN
        titre = 'mettre titre non existant dans bdd'

        # WHEN
        res = MangaDao().trouver_par_titre(titre)

        # THEN
        assert res is None
    
    def trouver_par_titre_erreur(self):
        """Méthode permettant de tester la méthode qui cherche un manga par
        titre. Ici, elle teste si la méthode relève une erreur de typer avec
        en entrée, un type différent de celui qui doit être donné en entrée."""
        # GIVEN
        titre = 999999999

        # WHEN/THEN
        with pytest.raises(TypeError):
            MangaDao().trouver_par_titre(titre)

# teser identifiant
    def trouver_par_id_existant(self):
        """Méthode permettant de tester la méthode qui cherche un manga par 
        identifiant. Ici, elle teste si la méthode fonctionne avec un identifiant existant
        dans la base"""
        # GIVEN
        id = "mettre l'id'd'un manga de la base"

        # WHEN
        res = MangaDao().trouver_par_titre(id)

        # THEN
        assert res is not None

    def trouver_par_id_non_existant(self):
        """Méthode permettant de tester la méthode qui cherche un manga par
        identifiant. Ici, elle teste si la méthode fonctionne avec un 
        identifiant qui n'existe pas dans la base. Elle doit renvoyer None 
        si l'identifiant n'existe pas dans la base"""
        # GIVEN
        id = 'mettre id non existant dans bdd'

        # WHEN
        res = MangaDao().trouver_par_titre(titre)

        # THEN
        assert res is None
    
    def trouver_par_titre_erreur(self):
        """Méthode permettant de tester la méthode qui cherche un manga par
        titre. Ici, elle teste si la méthode relève une erreur de typer avec
        en entrée, un type différent de celui qui doit être donné en entrée."""
        # GIVEN
        titre = 999999999

        # WHEN/THEN
        with pytest.raises(TypeError):
            MangaDao().trouver_par_titre(titre)

        