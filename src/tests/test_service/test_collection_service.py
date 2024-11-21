from unittest.mock import MagicMock
from src.service.collection_servive import CollectionVirtuelleService
from src.dao.collection_dao import CollectionDao
from src.business_objet.collection_virtuelle import CollectionVirtuelle
from src.business_objet.manga import Manga
from src.business_objet.manga_physique import MangaPhysique
from src.business_objet.utilisateur import Utilisateur
import pytest


# Initialisation des objets pour les tests

manga_virtuel = Manga(
        id_manga=28,
        titre_manga="manga_test",
        synopsis='juste pour tester',
        auteurs='auteur',
        )


manga_physique = MangaPhysique(
    id_manga=2,
    titre_manga="One Piece",
    auteurs="Eiichirō Oda",
    synopsis="Aventures de Luffy pour devenir le roi des pirates.",
    id_utilisateur=1,
    tomes_manquants=[],
    dernier_tome=15,
    status="lu"
    )

collection = CollectionVirtuelle(
    titre="Collection Virtuelle",
    id_utilisateur=1,
    liste_manga=[manga_virtuel],
    description="Ma première collection virtuelle."
)


def test_creer_collection_ok():
    """Tester la création d'une collection virtuelle avec des mangas virtuels uniquement"""

    # GIVEN
    mock_dao = MagicMock()
    mock_dao.creer.return_value = True
    mock_dao.ajouter_collection_virtuelle.return_value = True

    service = CollectionVirtuelleService()
    service.CollectionDao = mock_dao

    # WHEN
    result = service.creer(collection=collection)

    # THEN
    assert result is not None
    
    

def test_creer_collection_echec_manga_physique():
    """Tester la création échoue si un manga physique est présent"""

    # GIVEN
    collection_1 = CollectionVirtuelle ("collection virtuelle", 2, [manga_virtuel],"la meilleure")
    mock_dao = MagicMock()
    service = CollectionVirtuelleService()
    service.CollectionDao = mock_dao

    # WHEN / THEN
    with pytest.raises(ValueError):
        service.creer(collection=collection_1)


def test_creer_collection_echec_titre_existant():
    collection = CollectionVirtuelle ("Nouvelle Collection", 2, [manga_physique],"la meilleure")
    mock_dao = MagicMock()
    service = CollectionVirtuelleService()
    service.CollectionDao = mock_dao


    # WHEN / THEN
    with pytest.raises(ValueError):
        service.creer(collection=collection)
    
def test_liste_manga_ok():
    """Tester le retour de la liste des mangas d'une collection"""

    # GIVEN
    mock_dao = MagicMock()
    mock_dao.liste_manga_virtuelle.return_value = [manga_virtuel]

    service = CollectionVirtuelleService()
    service.CollectionDao = mock_dao

    # WHEN

    result = service.liste_manga(collection)

    # THEN
    assert len(result) == 1
    assert result[0] == manga_virtuel
   
    
def test_modifier_collection_ok():
    """Tester la modification réussie d'une collection"""

    # GIVEN
    """collection_test = CollectionVirtuelle(
    titre="Collection Virtuelle",
    id_utilisateur=1,
    liste_manga=[manga_virtuel],
    description="Ma première collection virtuelle."
)"""
    mock_dao = MagicMock()
    mock_dao.modifier.return_value = True

    service = CollectionVirtuelleService()
    service.CollectionDao = mock_dao

    # WHEN
    result = service.modifier_collection(collection)

    # THEN
    assert result is True
    
    
def test_supprimer_manga_ok():
    """Tester la suppression d'un manga virtuel existant dans la collection"""

    # GIVEN
    mock_dao = MagicMock()
    mock_dao.liste_manga_virtuelle.return_value = [manga_virtuel]
    mock_dao.supprimer_manga_virtuel.return_value = True

    service = CollectionVirtuelleService()
    service.CollectionDao = mock_dao

    # WHEN
    result = service.supprimer_manga(collection= collection, manga = manga_virtuel)

    # THEN
    assert result is True


def test_supprimer_manga_echec():
    """Tester la suppression échoue si le manga n'existe pas dans la collection"""

    # GIVEN
    mock_dao = MagicMock()
    mock_dao.liste_manga_virtuelle.return_value = []

    service = CollectionVirtuelleService()
    service.CollectionDao = mock_dao

    # WHEN / THEN
    with pytest.raises(ValueError):
        service.supprimer_manga(collection, manga_virtuel)

def test_ajouter_manga_ok():
    """Tester l'ajout d'un manga virtuel valide à une collection"""

    # GIVEN
    mock_dao = MagicMock()
    mock_dao.ajouter_manga.return_value = True

    service = CollectionVirtuelleService()
    service.CollectionDao = mock_dao

    # WHEN
    result = service.ajouter_manga(collection, manga_virtuel)

    # THEN
    assert result is True
    

def test_ajouter_manga_echec_manga_physique():
    """Tester l'ajout échoue si le manga est physique"""

    # GIVEN
    service = CollectionVirtuelleService()

    # WHEN / THEN
    with pytest.raises(ValueError):
        service.ajouter_manga(collection, manga_physique)


def test_supprimer_collection_ok():
    """Tester la suppression d'une collection réussie"""

    # GIVEN
    mock_dao = MagicMock()
    mock_dao.supprimer.return_value = True

    service = CollectionVirtuelleService()
    service.CollectionDao = mock_dao

    # WHEN
    result = service.supprimer(collection)

    # THEN
    assert result is True
   




if __name__ == "__main__":
    pytest.main([__file__])

