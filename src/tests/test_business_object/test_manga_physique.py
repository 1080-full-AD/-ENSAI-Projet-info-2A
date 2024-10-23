
import pytest
from src.business_objet.manga_physique import MangaPhysique


def test_liste_tome_ok():
    # GIVEN
    manga = MangaPhysique(1, 1, "Titre", "Auteur", "Synopsis", [], 5, "En cours")

    # WHEN
    res = manga.liste_tome()

    # THEN
    expected = [1, 2, 3, 4, 5]
    assert res == expected

def test_liste_tome_avec_tomes_manquants():
    # GIVEN
    manga = MangaPhysique(1, 1, "Titre", "Auteur", "Synopsis", [2, 4], 5, "En cours")

    # WHEN
    res = manga.liste_tome()

    # THEN
    expected = [1, 3, 5]
    assert res== expected

def test_ajouter_tome_manquant():
    # GIVEN
    manga = MangaPhysique(1, 1, "Titre", "Auteur", "Synopsis", [2, 4], 5, "En cours")

    # WHEN
    manga.ajouter_tome(2)

    # THEN
    expected = [4]
    assert manga.tomes_manquants == expected

def test_ajouter_tome_sup():
    "tester la methode ajouter un nouveau tome pour un tome après le dernier tome enregistré"
    # GIVEN
    manga = MangaPhysique(1, 1, "Titre", "Auteur", "Synopsis", [3], 5, "En cours")

    # WHEN
    manga.ajouter_tome(7)

    # THEN
    expected = [3, 6]
    assert manga.tomes_manquants == expected and manga.dernier_tome == 7
        

def test_ajouter_tome_existant():
    # GIVEN
    manga = MangaPhysique(1, 1, "Titre", "Auteur", "Synopsis", [], 5, "En cours")

    # WHEN
    manga.ajouter_tome(3)

    # THEN
    assert manga.tomes_manquants == [] and manga.dernier_tome == 5
        

def test_ajouter_tome_type_invalide():
    # GIVEN
    manga = MangaPhysique(1, 1, "Titre", "Auteur", "Synopsis", [], 5, "En cours")
        
    # WHEN/THEN
    with pytest.raises(TypeError):
        manga.ajouter_tome("deux")








def test_enlever_tome_dernier():
    "tester la fonction enlever tome pour le dernier tome"
    # GIVEN
    manga = MangaPhysique(1, 1, "Titre", "Auteur", "Synopsis", [3], 5, "En cours")

    # WHEN
    manga.enlever_tome(5)

    # THEN
    expected = [3, 5]
    assert manga.tomes_manquants == expected and manga.dernier_tome == 4
        
def test_enlever_tome_existant():
    "teste la fonction enlever un tome pour un tome existant et différent du dernier tome"
    # GIVEN
    manga = MangaPhysique(1, 1, "Titre", "Auteur", "Synopsis", [], 5, "En cours")

    # WHEN
    manga.enlever_tome(3)

    # THEN
    assert manga.tomes_manquants == [3] and manga.dernier_tome == 5
        

def test_enlever_tome_non_existant():
    # GIVEN
    manga = MangaPhysique(1, 1, "Titre", "Auteur", "Synopsis", [], 5, "En cours")

    # WHEN/THEN
    manga.enlever_tome(6)

    # THEN
    assert manga.tomes_manquants == [] and manga.dernier_tome == 5


def test_elever_tome_type_invalide():
    # GIVEN
    manga = MangaPhysique(1, 1, "Titre", "Auteur", "Synopsis", [], 5, "En cours")
        
    # WHEN/THEN
    with pytest.raises(TypeError):
        manga.enlever_tome("deux")

       

if __name__ == "__main__":
    pytest.main([__file__])