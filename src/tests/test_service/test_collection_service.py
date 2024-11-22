

from unittest.mock import MagicMock
from src.service.collection_service import CollectionVirtuelleService
from src.dao.collection_dao import CollectionDao
from src.business_objet.collection_virtuelle import CollectionVirtuelle
from src.business_objet.manga import Manga
from src.business_objet.manga_physique import MangaPhysique
from src.business_objet.utilisateur import Utilisateur
import pytest


# Initialisation des objets pour les tests

manga_virtuel = Manga(
        id_manga=27,
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
    result = service.creer(
        id_utilisateur=collection.id_utilisateur,
        titre=collection.titre,
        liste_manga=collection.liste_manga,
        description=collection.description
        )

    # THEN
    assert result is not None
    
    

def test_creer_collection_echec_manga_physique():
    """Tester la création échoue si un manga physique est présent"""

    # GIVEN
    collection_1 = CollectionVirtuelle("collection virtuelle", 2, [manga_physique],"la meilleure")
    mock_dao = MagicMock(spec=CollectionDao)
    mock_dao.creer.return_value.side_effect = TypeError(
        "les collection virtuelles ne peuvent contenir des mangas physique")

    service = CollectionVirtuelleService()
    service.CollectionDao = mock_dao

    # WHEN / THEN
    with pytest.raises(TypeError, match="les collection virtuelles ne peuvent contenir des mangas physique"):
        service.creer(
        id_utilisateur=collection_1.id_utilisateur,
        titre=collection_1.titre,
        liste_manga=collection_1.liste_manga,
        description=collection_1.description
        )


def test_creer_collection_echec_titre_existant():
    collection_2 = CollectionVirtuelle("collection virtuelle", 2, [manga_virtuel],"la meilleure")
    mock_dao = MagicMock(spec=CollectionDao)
    mock_dao.creer.return_value.side_effect = ValueError(
        "Vous avez déja une collection avec ce titre :/")
    service = CollectionVirtuelleService()
    service.CollectionDao = mock_dao


    # WHEN / THEN
    with pytest.raises(ValueError, match="Vous avez déja une collection avec ce titre :/"):
        service.creer(
                    id_utilisateur = collection_2.id_utilisateur,
                    titre = collection_2.titre,
                    liste_manga = collection_2.liste_manga,
                    description = collection_2.description
                    )
    
def test_recherche_collection():
    #GIVEN
    id_utilisateur = 1
    titre_collec = "Collection Virtuelle"
    mock_dao = MagicMock()
    mock_dao.rechercher_collection.return_value = collection
    service = CollectionVirtuelleService()
    service.CollectionDao = mock_dao

      # WHEN
    result = service.rechercher_collection(id_utilisateur=id_utilisateur, titre_collec=titre_collec)

      #THEN
    assert result is not None
    assert result.titre == collection.titre


def test_liste_manga_ok():
    """Tester le retour de la liste des mangas d'une collection"""

    # GIVEN
    mock_dao = MagicMock()
    mock_dao.liste_manga_virtuelle.return_value = [manga_virtuel]

    service = CollectionVirtuelleService()
    service.CollectionDao = mock_dao

    # WHEN

    result = service.liste_manga(id_utilisateur=1,titre_collec="Collection Virtuelle" )

    # THEN
    assert len(result) == 1
    #assert result[0] == manga_virtuel
    assert result[0].id_manga==manga_virtuel.id_manga
    assert result[0].titre_manga==manga_virtuel.titre_manga
    assert result[0].synopsis==manga_virtuel.synopsis
    assert result[0].auteurs==manga_virtuel.auteurs
    
def liste_collection_ok():

    # GIVEN
    id_utilisateur = 1
    mock_dao = MagicMock()
    mock_dao.liste_manga_virtuelle.return_value = [collection]

    service = CollectionVirtuelleService()
    service.CollectionDao = mock_dao

    # WHEN

    result = service.liste_collection(id_utilisateur)

    # THEN
    assert len(result) == 1
    

    
def test_modifier_description_ok():
    """Tester la modification réussie d'une collection"""

    # GIVEN
    """collection_test = CollectionVirtuelle(
    titre="Collection Virtuelle",
    id_utilisateur=1,
    liste_manga=[manga_virtuel],
    description="Ma première collection virtuelle."
)"""
    new_description="ma new description"
    mock_dao = MagicMock(spec=CollectionDao)
    mock_dao.modifier.return_value = True

    service = CollectionVirtuelleService()
    service.CollectionDao = mock_dao

    # WHEN
    result = service.modifier_description(collection=collection ,new_description=new_description)

    # THEN
    assert result is not None
    assert result.description == collection.description
    
def test_modifier_titre_ok():
    new_titre = "ma new collection"
    mock_dao = MagicMock(spec=CollectionDao)
    mock_dao.modifier_titre.return_value = True

    service = CollectionVirtuelleService()
    service.CollectionDao = mock_dao
    # WHEN
    result = service.modifier_titre(collection=collection, new_titre=new_titre)

    # THEN
    assert result is True
    #assert result.titre == new_titre


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

