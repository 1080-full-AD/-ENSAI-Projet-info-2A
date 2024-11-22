import logging
from unittest.mock import MagicMock
from src.service.manga_physique_service import MangaPhysiqueService
from src.dao.manga_physique_dao import MangaPhysiqueDao
from src.business_objet.manga_physique import MangaPhysique

import pytest



manga_test = MangaPhysique(
                id_manga=26,
                id_utilisateur=1,
                titre_manga="Naruto",
                auteurs="Masashi Kishimoto",
                synopsis="Histoire d'un ninja ambitieux.",
                tomes_manquants=[5, 6],
                dernier_tome=10,
                status="incomplet"
                )


def test_creer_manga_physique_ok():
    """Test pour vérifier la création d'un manga physique réussie"""
    #GIVEN
        
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.creer.return_value = True

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao


    # WHEN
    result = service.creer_manga_physique(manga_test)

    # THEN
    assert result is True

def test_creer_manga_physique_echec():
    """Création d'un mangaphysique dans la BDD échec"""

    # GIVEN
    manga = MangaPhysique(
                id_manga=999,
                id_utilisateur=1,
                titre_manga="Naruto",
                auteurs="Masashi Kishimoto",
                synopsis="Histoire d'un ninja ambitieux.",
                tomes_manquants=[5, 6],
                dernier_tome=10,
                status="incomplet"
                )

    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.creer.return_value = False

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao

    

    # WHEN
    manga = service.creer_manga_physique(manga)

    # THEN
    assert manga is False


def test_ajouter_tome_manquant_ok():
    """Test pour vérifier l'ajout d'un tome manquant"""
    # GIVEN
    new_tome = 5
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.modifier_manga_physique.return_value = True

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao
        

    # WHEN
    result = service.ajouter_tome(manga_test, new_tome)

    # THEN
    assert result is True


def test_ajouter_nouveau_tome_ok():
    """Test pour vérifier l'ajout d'un nouveau tome supérieur 
        supérieur au dernier tome"""
    # GIVEN
    new_tome = 15
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.modifier_manga_physique.return_value = True

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao
        
     # WHEN
    result = service.ajouter_tome(manga_test, new_tome)

    # THEN
    assert result is True
    assert manga_test.tomes_manquants == [6, 11, 12, 13, 14]
    assert manga_test.dernier_tome == 15


def test_ajouter_tome_existant_echec():
    """Test pour vérifier l'ajout d'un tome qui ne fait pas 
    partie des tomes manquants mais qui est inférieur au 
    denier tome echoue"""
    # GIVEN
    new_tome = 2
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.modifier_manga_physique.return_value.side_effect = ValueError(
        "tome deja existant")
    
    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao
        
     # WHEN and THEN
    with pytest.raises(ValueError, match="tome deja existant"):
        service.ajouter_tome(manga_test, new_tome)



def test_ajouter_non_tome_echec():
    """Test pour vérifier l'ajout de autre chose qu'un entier
    avec la methode ajouter_tome echoue"""
    # GIVEN
    new_tome = "a"
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.modifier_manga_physique.return_value.side_effect = TypeError(
        "Le tome ajouté doit être un entier")

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao
        
     # WHEN and THEN
    with pytest.raises(TypeError, match="Le tome ajouté doit être un entier"):
        service.ajouter_tome(manga_test, new_tome)


def test_enlever_dernier_tome_ok():
    """Test pour vérifier la suppression  du dernier tome """
    # GIVEN
    
    tome_a_supprimer = 15
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.modifier_manga_physique.return_value = True

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao

    # WHEN
    result = service.enlever_tome(manga_test, tome_a_supprimer)

    # THEN
    assert result is True 
    assert manga_test.dernier_tome == 10






def test_enlever_tome_pas_dernier_ok():
    """Test pour vérifier la suppression d'un tome existant  
    inférieur au dernier tome """
    # GIVEN
    
    tome_a_supprimer = 8
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.modifier_manga_physique.return_value = True

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao

    # WHEN
    result = service.enlever_tome(manga_test, tome_a_supprimer)

    # THEN
    assert result is True 
    assert 8 in manga_test.tomes_manquants


def test_enlever_tome_non_posséder_echec():
    """Test pour vérifier la suppression d'un tome qui n'est pas 
    posséder l'utilisateur echoue  """
    # GIVEN
    
    tome_a_supprimer = 76
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.modifier_manga_physique.return_value.side_effect = ValueError(
        "vous ne disposez pas de ce tome")

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao

     # WHEN and THEN
    with pytest.raises(ValueError, match="vous ne disposez pas de ce tome"):
        service.enlever_tome(manga_test, tome_a_supprimer)


def test_enlever_tome_pas_tome_echec():
    """Test pour vérifier la methode enlever_tome appliqué 
    à autre chose qu'un entier echoue """
    # GIVEN
    
    tome_a_supprimer = "a"
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.modifier_manga_physique.return_value.side_effect = TypeError(
        "a,doit être un entier")

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao

    # WHEN and THEN
    with pytest.raises(TypeError, match="a,doit être un entier"):
        service.enlever_tome(manga_test, tome_a_supprimer)



def test_modifier_manga_physique_ok():
    """Test pour vérifier la modification d'un manga physique"""
    # GIVEN
    logging.info("Test : test_modifier_tome_ok")
        
    new_status = "complet"
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.modifier_manga_physique.return_value = True

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao

    # WHEN
    manga_test.status = new_status
    result = service.modifier_manga_physique(manga_test)

    # THEN
    logging.info(f"Résultat : {result}")
    assert result is True

def test_supprimer_manga_physique_ok() :
    """Test pour vérifier la suppression réussie d'un manga physique"""
    # GIVEN
        
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.supprimer_manga_physique.return_value = True

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao

    # WHEN
    result = service.supprimer_manga_physique(manga_test)

    # THEN
    assert result is True

        

if __name__ == "__main__":
    pytest.main([__file__])