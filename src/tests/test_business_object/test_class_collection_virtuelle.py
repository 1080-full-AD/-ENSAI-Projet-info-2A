import pytest
from src.business_objet.manga import Manga
from src.business_objet.manga_physique import MangaPhysique
from src.business_objet.collection.collection_virtuelle import CollectionVirtuelle


def test_collection_virtuelle_creation_ok():
    # GIVEN
    manga1 = Manga(1, "Titre 1", "Auteur 1", "Synopsis 1")
    manga2 = Manga(2, "Titre 2", "Auteur 2", "Synopsis 2")
    list_manga = [manga1, manga2]

    # WHEN
    collection = CollectionVirtuelle(1, "Ma Collection Virtuelle", 1, list_manga)

    # THEN
    assert collection.id_collection == 1
    assert collection.titre == "Ma Collection Virtuelle"
    assert collection.id_utilisateur == 1
    assert collection.list_manga == list_manga
    assert collection.type == "virtuelle"


def test_collection_virtuelle_creation_erreur_manga_physique():
    # GIVEN
    manga_physique = MangaPhysique(1, 1, "Titre 1", "Auteur 1", "Synopsis 1", [], 10, "Complet")
    list_manga = [manga_physique]

    # WHEN/THEN
    with pytest.raises(ValueError, match="les collection virtuelles ne peuvent contenir des collections physique"):
        CollectionVirtuelle(1, "Ma Collection Virtuelle", 1, list_manga)


def test_collection_virtuelle_creation_erreur_pas_manga():
    # GIVEN 
    list_manga = ["manga"]

    # WHEN/THEN
    with pytest.raises(ValueError, match="les collections virtuelles ne conteniennent que des mangas virtuelles"):
        CollectionVirtuelle(1, "Ma Collection Virtuelle", 1, list_manga)





def test_ajouter_manga_ok():
    # GIVEN
    collection = CollectionVirtuelle(1, "Ma Collection Virtuelle", 1, [])
    new_manga = Manga(3, "Nouveau Manga", "Auteur", "Synopsis")

    # WHEN
    collection.ajouter_manga(new_manga)

    # THEN
    assert len(collection.list_manga) == 1
    assert collection.list_manga[0] == new_manga


def test_ajouter_manga_erreur_manga_physique():
    # GIVEN
    collection = CollectionVirtuelle(1, "Ma Collection Virtuelle", 1, [])
    new_manga = MangaPhysique(1, 1, "Manga Physique", "Auteur", "Synopsis", [], 5, "Complet")

    # WHEN/THEN
    with pytest.raises(ValueError, match="les collections virtuelle ne contiennent que des mangas virtuelles"):
        collection.ajouter_manga(new_manga)


def test_ajouter_manga_erreur_pas_manga():
    # GIVEN
    collection = CollectionVirtuelle(1, "Ma Collection Virtuelle", 1, [])
    
    # WHEN/THEN
    with pytest.raises(ValueError, match="manga n'est pas un manga"):
        collection.ajouter_manga("manga")


def test_supprimer_manga_ok():
    # GIVEN
    manga1 = Manga(1, "Titre 1", "Auteur 1", "Synopsis 1")
    collection = CollectionVirtuelle(1, "Ma Collection Virtuelle", 1, [manga1])

    # WHEN
    collection.supprimer_manga(manga1)

    # THEN
    assert len(collection.list_manga) == 0


def test_supprimer_manga_non_existant():
    # GIVEN
    manga1 = Manga(1, "Titre 1", "Auteur 1", "Synopsis 1")
    manga2 = Manga(2, "Titre 2", "Auteur 2", "Synopsis 2")
    collection = CollectionVirtuelle(1, "Ma Collection Virtuelle", 1, [manga1])

    # WHEN/THEN
    with pytest.raises(ValueError, match="ce manga ne fait pas partir de cette collection"):
        collection.supprimer_manga(manga2)


if __name__ == "__main__":
    pytest.main([__file__])
