import os 
import pytest
from src.utils.reset_database import ResetDatabase
from unittest.mock import patch, MagicMock
from src.dao.collection_dao import CollectionDao
from src.business_objet.collection.collection_virtuelle import CollectionVirtuelle
from src.business_objet.collection.collection_physique import CollectionPhysique
from src.business_objet.manga import Manga



@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test"""
    with patch.dict(os.environ, {"SCHEMA": "projet_test_dao"}):
        ResetDatabase().lancer()
        yield



def test_creer_ok():
    """Création de collection réussie"""

    # GIVEN
    collection = CollectionVirtuelle(
        id_collection=1, titre="Ma collection virtuelle", id_utilisateur=123, list_manga=[])

    # WHEN
    creation_ok = CollectionDao().Creer(collection)

    # THEN
    assert creation_ok
    assert collection.titre == "Ma collection virtuelle"


def test_creer_ko():
    """Création d'avis échouée """

    # GIVEN
    collection = CollectionVirtuelle(id_collection=None, titre=None, id_utilisateur=None, list_manga=[])

    # WHEN
    creation_ok = CollectionDao().Creer(collection)

    # THEN
    assert not creation_ok


def test_trouver_tous_par_titre_existant():
    """Test de la recherche d'une collection par titre"""

    # GIVEN
    titre = "Ma collection virtuelle"
    # WHEN
    result = CollectionDao().trouver_par_titre(titre)

    # THEN
    assert result is not None
    assert len(result) == 1
    
    



def test_trouver_par_titre_non_existant():
    """Test recherche d'une collection avec un titre inexistant"""

    # GIVEN
    titre = "Titre inexistant"

    
    # WHEN
    result = CollectionDao().trouver_par_titre(titre)

    # THEN
    assert result is None
    


def test_supprimer_ok():
    """Test suppression d'une collection réussie"""

    # GIVEN
    collection = CollectionVirtuelle(
        id_collection=1, titre="Ma collection virtuelle", id_utilisateur=123, list_manga=[])
    
    # WHEN
    suppression = CollectionDao().supprimer(collection)

    # THEN
    assert suppression



def test_supprimer_ko():
    """Test suppression d'une collection qui n'existe pas dans la base de donnés"""

    # GIVEN
    collection = CollectionVirtuelle(
        id_collection=999999999999999999999, titre="Ma collection virtuelle", id_utilisateur=123, list_manga=[])
    
    # WHEN
    suppression=CollectionDao().supprimer(collection)

    # THEN
    assert not suppression


def test_modifier_ok():
    """Test modification d'une collection réussie"""

    # GIVEN
    new_titre="ma meilleure collection"
    collection = CollectionVirtuelle(
        id_collection="1", titre=new_titre, id_utilisateur="123", list_manga=[]
    )

    # WHEN
    modification_ok = CollectionDao().modifier(collection)

    # THEN
    assert modification_ok
        
def test_modifier_ko():
    """Test modification d'une collection échouée id_collection inconnue"""

    # GIVEN
    collection = CollectionVirtuelle(
        id_collection=9999999999999, titre="Ma collection virtuelle", id_utilisateur=123, list_manga=[]
    )

    # WHEN
    modification_ko = CollectionDao().modifier(collection)

    # THEN
    assert not modification_ko
       


def test_liste_manga_ok():
    """Test de la récupération des mangas d'une collection"""

    # GIVEN
    manga1 = Manga(1, "Titre 1", "Auteur 1", "Synopsis 1")
    manga2 = Manga(2, "Titre 2", "Auteur 2", "Synopsis 2")
    collection = CollectionVirtuelle(
        id_collection=1, titre="Ma collection virtuelle", id_utilisateur=123, list_manga=[manga1,manga2]
    )

    # WHEN
    mangas = CollectionDao().liste_manga(collection)

    # THEN
    assert len(mangas) == 2
    assert mangas[0].titre == "Manga 1"
    

if __name__ == "__main__":
    pytest.main([__file__])