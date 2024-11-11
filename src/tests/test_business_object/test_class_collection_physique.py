import pytest
from src.business_objet.manga_physique import MangaPhysique
from src.business_objet.collection.collection_physique import CollectionPhysique


def test_collection_physique_creation_ok():
    # GIVEN
    manga1 = MangaPhysique(1, 1, "Titre 1", "Auteur 1", "Synopsis 1", [], 10, "Complet")
    manga2 = MangaPhysique(2, 1, "Titre 2", "Auteur 2", "Synopsis 2", [], 15, "En cours")
    list_manga = [manga1, manga2]

    # WHEN
    collection = CollectionPhysique("Ma Collection", 1, list_manga,"description")

    # THEN
    assert collection.titre == "Ma Collection"
    assert collection.id_utilisateur == 1
    assert collection.list_manga == list_manga
    assert collection.type == "physique"


def test_collection_physique_creation_erreur():
    # GIVEN
    manga1 = MangaPhysique(1, 1, "Titre 1", "Auteur 1", "Synopsis 1", [], 10, "Complet")
    manga_invalide = "Manga Invalide"
    list_manga = [manga1, manga_invalide]

    # WHEN/THEN
    with pytest.raises(ValueError):
        CollectionPhysique("Ma Collection", 1, list_manga,"m")


def test_ajouter_manga_ok():
    # GIVEN
    collection = CollectionPhysique("Ma Collection", 1, [],"m")
    new_manga = MangaPhysique(1, 1, "Nouveau Manga", "Auteur", "Synopsis", [], 5, "Complet")

    # WHEN
    collection.ajouter_manga(new_manga)

    # THEN
    assert len(collection.list_manga) == 1
    assert collection.list_manga[0] == new_manga


def test_ajouter_manga_type_invalide():
    # GIVEN
    collection = CollectionPhysique("Ma Collection", 1, [],"m")
    new_manga = "Manga Invalide"  # Ce n'est pas un MangaPhysique

    # WHEN/THEN
    with pytest.raises(TypeError, match="Manga Invalide n'est pas un manga physique"):
        collection.ajouter_manga(new_manga)


def test_supprimer_manga_ok():
    # GIVEN
    manga1 = MangaPhysique(1, 1, "Titre 1", "Auteur 1", "Synopsis 1", [], 10, "Complet")
    collection = CollectionPhysique("Ma Collection", 1, [manga1],"m")

    # WHEN
    collection.supprimer_manga(manga1)

    # THEN
    assert len(collection.list_manga) == 0


def test_supprimer_manga_non_existant():
    # GIVEN
    manga1 = MangaPhysique(1, 1, "Titre 1", "Auteur 1", "Synopsis 1", [], 10, "Complet")
    manga2 = MangaPhysique(2, 1, "Titre 2", "Auteur 2", "Synopsis 2", [], 15, "Complet")
    collection = CollectionPhysique("Ma Collection", 1, [manga1],"m")

    # WHEN/THEN
    with pytest.raises(TypeError, match="ce manga n'est pas dans cette collection"):
        collection.supprimer_manga(manga2)


if __name__ == "__main__":
    pytest.main([__file__])
