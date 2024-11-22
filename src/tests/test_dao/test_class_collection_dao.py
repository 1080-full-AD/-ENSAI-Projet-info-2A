import os
import pytest
from unittest.mock import patch
from src.utils.reset_database import ResetDatabase
from src.business_objet.collection_virtuelle import CollectionVirtuelle
from src.business_objet.manga import Manga
from src.dao.collection_dao import CollectionDao
from src.business_objet.utilisateur import Utilisateur

@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test"""
    with patch.dict(os.environ, {"SCHEMA": "projet_test_dao"}):
        ResetDatabase().lancer()
        yield


def test_creer_collection_ok():
    """Création d'une collection virtuelle réussie"""
    # GIVEN
    collection = CollectionVirtuelle("Ma Collection", 1, [], "Collection de test")

    # WHEN
    created = CollectionDao().creer(collection)

    # THEN
    assert created


def test_creer_collection_ko():
    """Échec de la création d'une collection (ex. titre manquant)"""
    # GIVEN
    collection = CollectionVirtuelle(None, 1, [], "Collection sans titre")

    # WHEN
    created = CollectionDao().creer(collection)

    # THEN
    assert not created


def test_ajouter_manga_virtuel_ok():
    """Ajout d'un manga dans une collection virtuelle réussie"""
    # GIVEN
    collection = CollectionVirtuelle("Ma Collection", 1, [], "Collection de test")
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
    )

    # WHEN
    ajout = CollectionDao().ajouter_manga(collection, manga)

    # THEN
    assert ajout


def test_rechercher_collection_ok():
    #GIVEN
    id_utilisateur = 1
    titre_collec = "Ma Collection"

    #WHEN
    resultat = CollectionDao().recherhcer_collection(
               id_utilisateur=id_utilisateur, titre_collec=titre_collec)

    #THEN
    assert resultat is not None
    assert resultat.titre == "Ma Collection"
    assert resultat.liste_manga[0].id_manga == 13


def test_rechercher_collection_none():
    #GIVEN
    id_utilisateur = 4
    titre_collec = "Ma Collection"

    #WHEN
    resultat = CollectionDao().recherhcer_collection(
               id_utilisateur=id_utilisateur, titre_collec=titre_collec)

    #THEN
    assert resultat is None
    



def test_supprimer_manga_virtuel_ok():
    """Suppression d'un manga dans une collection virtuelle réussie"""
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
    )
    collection = CollectionVirtuelle("Ma Collection", 2, [], "Collection de test")
    CollectionDao().ajouter_manga(collection, manga)


    # WHEN
    suppression = CollectionDao().supprimer_manga(collection, manga)

    # THEN
    assert suppression


def test_supprimer_manga_virtuel_ko():
    """Échec de suppression d'un manga non existant dans une collection virtuelle"""
    # GIVEN
    collection = CollectionVirtuelle("Ma Collection", 2, [], "Collection de test")
    manga = Manga("999", "Manga Inexistant", "Auteur Inconnu", "Synopsis Inconnu")

    # WHEN
    suppression = CollectionDao().supprimer_manga(collection, manga)

    # THEN
    assert not suppression


def test_modifier_collection_ok():
    """Modification réussie d'une collection virtuelle"""
    # GIVEN
    collection = CollectionVirtuelle("Ma Collec", 1, [], "Description de test")
    CollectionDao().creer(collection)
    collection.description = "Nouvelle description"

    # WHEN
    modification = CollectionDao().modifier(collection)

    # THEN
    assert modification



def test_modifier_titre_ok():
    """Modification réussie d'une collection virtuelle"""
    # GIVEN
    collection = CollectionVirtuelle("Ma new_Collec", 1, [], "Description de test")
    CollectionDao().creer(collection)
    new_titre = "Nouvelle collec"

    # WHEN
    modification = CollectionDao().modifier_titre(collection, new_titre)

    # THEN
    assert modification


def test_modifier_collection_ko():
    """Échec de modification d'une collection (ex. id utilisateur incorrect)"""
    # GIVEN
    collection = CollectionVirtuelle("Ma Collection", 999, [], "Description de test")

    # WHEN
    
    modification = CollectionDao().modifier(collection)

    # THEN
    assert not modification


def test_liste_manga_virtuel():
    """Vérifie que la liste des mangas d'une collection virtuelle est correcte."""
    
    # GIVEN: Création d'une collection virtuelle et ajout de mangas
    collection = CollectionVirtuelle(titre="Ma Collection préfèrée", id_utilisateur=1, liste_manga=[], description="Une collection test")
    manga1 = Manga(
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
    )
    manga2 = Manga(
        id_manga=1, 
        titre_manga="Monster", 
        auteurs="Urasawa, Naoki", 
        synopsis="Guts, a former mercenary now known as the Black Swordsman, is out for revenge. After"
        " a tumultuous childhood, he finally finds someone he respects and believes he can trust, only to "
        "have everything fall apart when this person takes away everything important to Guts for the purpose "
        "of fulfilling his own desires. Now marked for death, Guts becomes condemned to a fate in which he is "
        "relentlessly pursued by demonic beings." 
        "Setting out on a dreadful quest riddled with misfortune, Guts, armed with a massive sword and monstrous strength, "
        "will let nothing stop him, not even death itself, until he is finally able to take the head of the one who stripped him�and "
        "his loved one�of their humanity."

        "[Written by MAL Rewrite]"

        "Included one-shot:"
        "Volume 14: Berserk: The Prototype"
        "And so when he is assigned to Team 7�along with his new teammates Sasuke Uchiha and Sakura Haruno, under the "
        "mentorship of veteran ninja Kakashi Hatake�Naruto is forced to work together with other people for the first time "
        "in his life. Through undergoing vigorous training and taking on challenging missions, Naruto must learn what it means"
        " to work in a team and carve his own route toward becoming a full-fledged ninja recognized by his village."

        "[Written by MAL Rewrite])"
        )

    CollectionDao().creer(collection)
    CollectionDao().ajouter_manga(collection, manga1)
    CollectionDao().ajouter_manga(collection, manga2)
    
    # WHEN: Appel de la méthode liste_manga_virtuelle
    liste_manga = CollectionDao().liste_manga(id_utilisateur=1 ,titre_collec="Ma Collection préfèrée")

    # THEN: Vérification que la liste des mangas est correcte
    assert len(liste_manga) == 2
    assert any(m.titre_manga == "One Piece" for m in liste_manga)
    assert any(m.titre_manga == "Monster" for m in liste_manga)


def test_liste_collection_ok():
    #given
    id_utilisateur = 1

    #WHEN
    result = CollectionDao().liste_collection(id_utilisateur)

    #THEN 
    assert len(result)>0


def test_supprimer_collection_virtuelle_ok():
    """Suppression réussie d'une collection virtuelle"""
    # GIVEN
    collection = CollectionVirtuelle("Ma Collection", 1, [], "Description de test")

    # WHEN
    suppression = CollectionDao().supprimer_collection(collection)

    # THEN
    assert suppression




def test_supprimer_collection_virtuelle_ko():
    """Échec de suppression d'une collection virtuelle non existante"""
    # GIVEN
    collection = CollectionVirtuelle("Collection Inexistante", 1, [], "Description de test")

    # WHEN
    suppression = CollectionDao().supprimer_collection(collection)

    # THEN
    assert not suppression

    
def test_titre_existant_True():
    """test pour vérifier que la methode titre_existant retourne True 
    lorsque le titre est déja enregistrer dans la base de données pour 
    utilisateur """
        # GIVEN
    collection_1 = CollectionVirtuelle("Collection 1", 2, [], "Description de test")
    id_utilisateur = 2
    titre = "Collection 1"
        # WHEN
    CollectionDao().creer(collection_1)
    result = CollectionDao().titre_existant(id_utilisateur=id_utilisateur, titre=titre)
        # THEN
    assert result == True


def test_titre_existant_false():
    """test pour vérifier que la méthode titre_existant retourne false lorsque le titre 
    n'est pas enregister dans la base de données pour un utilisateur """
    # GIVEN
    id_utilisateur = 2
    titre = "Collection merveilleuse"
    # WHEN
    result = CollectionDao().titre_existant(id_utilisateur=id_utilisateur, titre=titre)
    
    #THEN
    assert result == False 


   

if __name__ == "__main__":
    pytest.main([__file__])