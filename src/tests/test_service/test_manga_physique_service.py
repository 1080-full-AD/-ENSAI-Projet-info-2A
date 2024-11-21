import logging
from unittest.mock import MagicMock
from src.service.manga_physique_service import MangaPhysiqueService
from src.dao.manga_physique_dao import MangaPhysiqueDao
from src.business_objet.manga_physique import MangaPhysique
import unittest


class TestMangaPhysiqueService(unittest.TestCase):

    manga = MangaPhysique(
            id_manga=26,
            id_utilisateur=1,
            titre_manga="Naruto",
            auteurs="Masashi Kishimoto",
            synopsis="Histoire d'un ninja ambitieux.",
            tomes_manquants=[5, 6],
            dernier_tome=10,
            status="incomplet"
            )


    def test_creer_manga_physique_ok(self):
        """Test pour vérifier la création d'un manga physique réussie"""
        #GIVEN
        manga = MangaPhysique(
            id_manga=26,
            id_utilisateur=1,
            titre_manga="Naruto",
            auteurs="Masashi Kishimoto",
            synopsis="Histoire d'un ninja ambitieux.",
            tomes_manquants=[5, 6],
            dernier_tome=10,
            status="incomplet"
            )
        mock_dao = MagicMock(spec=MangaPhysiqueDao)
        mock_dao.creer.return_value = True

        manga_service = MangaPhysiqueService()
        manga_service.MangaPhysiqueDao = mock_dao

        # WHEN
        result = manga_service.creer_manga_physique(manga)

        # THEN
        self.assertTrue(result)

    
    def test_ajouter_tome_ok(self):
        """Test pour vérifier l'ajout d'un tome manquant"""
        # GIVEN
        manga = MangaPhysique(
            id_manga=26,
            id_utilisateur=1,
            titre_manga="Naruto",
            auteurs="Masashi Kishimoto",
            synopsis="Histoire d'un ninja ambitieux.",
            tomes_manquants=[5, 6],
            dernier_tome=10,
            status="incomplet"
            )

        new_tome = 5
        mock_dao = MagicMock(spec=MangaPhysiqueDao)
        mock_dao.modifier_manga_physique.return_value = True

        manga_service = MangaPhysiqueService()
        manga_service.MangaPhysiqueDao = mock_dao
        

        # WHEN
        
        result = manga_service.ajouter_tome(manga, new_tome)

        # THEN
        self.assertTrue(result)

    def test_enlever_tome_ok(self):
        """Test pour vérifier la suppression d'un tome existant"""
        # GIVEN
        manga = MangaPhysique(
            id_manga=26,
            id_utilisateur=1,
            titre_manga="Naruto",
            auteurs="Masashi Kishimoto",
            synopsis="Histoire d'un ninja ambitieux.",
            tomes_manquants=[5, 6],
            dernier_tome=10,
            status="incomplet"
            )

        tome_to_remove = 10
        mock_dao = MagicMock(spec=MangaPhysiqueDao)
        mock_dao.modifier_manga_physique.return_value = True

        manga_service = MangaPhysiqueService()
        manga_service.MangaPhysiqueDao = mock_dao

        # WHEN
        result = manga_service.enlever_tome(manga, tome_to_remove)

        # THEN
        self.assertTrue(result)

    def test_modifier_manga_physique_ok(self):
        """Test pour vérifier la modification d'un manga physique"""
        # GIVEN
        logging.info("Test : test_modifier_tome_ok")
        manga = MangaPhysique(
            id_manga=26,
            id_utilisateur=1,
            titre_manga="Naruto",
            auteurs="Masashi Kishimoto",
            synopsis="Histoire d'un ninja ambitieux.",
            tomes_manquants=[5, 6],
            dernier_tome=10,
            status="incomplet"
            )
        new_status = "complet"
        mock_dao = MagicMock(spec=MangaPhysiqueDao)
        mock_dao.modifier_manga_physique.return_value = True

        manga_service = MangaPhysiqueService()
        manga_service.MangaPhysiqueDao = mock_dao

        # WHEN
        manga.status = new_status
        result = manga_service.modifier_manga_physique(manga)

        # THEN
        logging.info(f"Résultat : {result}")
        self.assertTrue(result)

    def test_supprimer_manga_physique_ok(self):
        """Test pour vérifier la suppression réussie d'un manga physique"""
        # GIVEN
        manga = MangaPhysique(
            id_manga=26,
            id_utilisateur=1,
            titre_manga="Naruto",
            auteurs="Masashi Kishimoto",
            synopsis="Histoire d'un ninja ambitieux.",
            tomes_manquants=[5, 6],
            dernier_tome=10,
            status="incomplet"
            )
        mock_dao = MagicMock(spec=MangaPhysiqueDao)
        mock_dao.supprimer_manga_physique.return_value = True

        manga_service = MangaPhysiqueService()
        manga_service.MangaPhysiqueDao = mock_dao

        # WHEN
        result = manga_service.supprimer_manga_physique(manga)

        # THEN
        self.assertTrue(result)

        
if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
