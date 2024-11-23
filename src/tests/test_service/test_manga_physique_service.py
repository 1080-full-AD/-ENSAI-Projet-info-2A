import logging
from unittest.mock import MagicMock
from src.service.manga_physique_service import MangaPhysiqueService
from src.dao.manga_physique_dao import MangaPhysiqueDao
from src.business_objet.manga_physique import MangaPhysique

import pytest

# Initialisation des données de test

manga_test = MangaPhysique(
    id_manga=28,
    id_utilisateur=3,
    titre_manga="manga_test",
    synopsis="juste pour tester",
    auteurs="auteur",
    tomes_manquants=[5, 6],
    dernier_tome=10,
    status="incomplet",
    nb_chapitres=10,
    nb_volumes=5,
)


def test_creer_manga_physique_ok():
    """Test pour vérifier la création d'un manga physique réussie"""
    # GIVEN

    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.creer.return_value = True

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao

    # WHEN
    result = service.creer_manga_physique(manga_test)

    # THEN
    assert result is True


def test_creer_manga_physique_echec():
    """Création d'un mangaphysique dans la BDD échec:
    id_manga inexistant dans la base"""

    # GIVEN
    manga = MangaPhysique(
        id_manga=999,
        id_utilisateur=3,
        titre_manga="Naruto",
        auteurs="Masashi Kishimoto",
        synopsis="Histoire d'un ninja ambitieux.",
        tomes_manquants=[5, 6],
        dernier_tome=10,
        status="incomplet",
        nb_chapitres=10,
        nb_volumes=5,
    )

    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.creer.return_value = False

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao

    # WHEN
    manga = service.creer_manga_physique(manga)

    # THEN
    assert manga is False


def test_lister_manga_physique_ok():
    """test pour vérifier  la méthode lister_manga_physique"""
    # GIVEN
    id_utilisateur = 3
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.liste_manga_physique.return_value = True

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao

    # WHEN
    result = service.lister_manga_physique(id_utilisateur)

    # THEN
    assert result is not None
    assert any(m.titre_manga == manga_test.titre_manga for m in result)


def test_lister_manga_physique_id_inexistant():
    """tester la methode lister_manga_physique pour
    un utilisateur non présent dans la base de données"""
    id_utilisateur = 100
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.liste_manga_physique.return_value.side_effect = ValueError(
        "ce identifiant n'est associé à aucun utilisateur"
    )
    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao

    # WHEN\THEN
    with pytest.raises(
        ValueError, match="ce identifiant n'est associé à aucun utilisateur"
    ):
        service.lister_manga_physique(id_utilisateur)


def test_lister_manga_physique_pas_id():
    """tester la methode lister_manga_physique pour
    un argument qui n'est pas un entier"""
    id_utilisateur = "a"
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.liste_manga_physique.return_value.side_effect = TypeError(
        f"{id_utilisateur} n'est pas un identifiant"
    )
    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao

    # WHEN\THEN
    with pytest.raises(TypeError, match=f"{id_utilisateur} n'est pas un identifiant"):
        service.lister_manga_physique(id_utilisateur)


def test_rechercher_manga_ok():
    """test la méthode test_recherche_manga
    fonctionne correction"""

    # GIVEN
    id_utilisateur = 3
    id_manga = manga_test.id_manga
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.rechercher_manga_physique.return_value = True

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao
    # WHEN
    result = service.rechercher_manga_physique(
        id_utilisateur=id_utilisateur, id_manga=id_manga
    )

    # THEN
    assert result is not None
    assert result.titre_manga == manga_test.titre_manga


def test_rechercher_manga_None():
    """test la méthode test_recherche_manga
    pour un manga non posséder par l'utilisateur"""

    # GIVEN
    id_utilisateur = 3
    id_manga = 100
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.rechercher_manga_physique.return_value.side_effect = ValueError(
        "aucun manga trouvé :/"
    )

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao

    # WHEN\THEN
    with pytest.raises(ValueError, match="aucun manga trouvé :/"):
        service.rechercher_manga_physique(
            id_utilisateur=id_utilisateur, id_manga=id_manga
        )


def test_rechercher_manga_utilisateur_inexistant():
    """test la méthode test_recherche_manga
    pour un utilisateur inexistant"""

    # GIVEN
    id_utilisateur = 100
    id_manga = manga_test.id_manga
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.rechercher_manga_physique.return_value.side_effect = ValueError(
        "ce identifiant n'est associé à aucun utilisateur"
    )

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao

    # WHEN\THEN
    with pytest.raises(
        ValueError, match="ce identifiant n'est associé à aucun utilisateur"
    ):
        service.rechercher_manga_physique(
            id_utilisateur=id_utilisateur, id_manga=id_manga
        )


def test_rechercher_manga_valeur_incorrecte():
    """test la méthode test_recherche_manga
    pour des valeurs d'arguments pas correctes"""

    # GIVEN
    id_utilisateur = 3
    id_manga = "b"
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.rechercher_manga_physique.return_value.side_effect = TypeError(
        "les informations renseignés ne sont pas correctes"
    )

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao

    # WHEN\THEN
    with pytest.raises(
        TypeError, match="les informations renseignés ne sont pas correctes"
    ):
        service.rechercher_manga_physique(
            id_utilisateur=id_utilisateur, id_manga=id_manga
        )


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
        "tome deja existant"
    )

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
        "Le tome ajouté doit être un entier"
    )

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao

    # WHEN and THEN
    with pytest.raises(TypeError, match="Le tome ajouté doit être un entier"):
        service.ajouter_tome(manga_test, new_tome)


def test_enlever_dernier_tome_ok():
    """Test pour vérifier la suppression  du dernier tome"""
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
    inférieur au dernier tome"""
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
    posséder l'utilisateur echoue"""
    # GIVEN

    tome_a_supprimer = 76
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.modifier_manga_physique.return_value.side_effect = ValueError(
        "vous ne disposez pas de ce tome"
    )

    service = MangaPhysiqueService()
    service.MangaPhysiqueDao = mock_dao

    # WHEN and THEN
    with pytest.raises(ValueError, match="vous ne disposez pas de ce tome"):
        service.enlever_tome(manga_test, tome_a_supprimer)


def test_enlever_tome_pas_tome_echec():
    """Test pour vérifier la methode enlever_tome appliqué
    à autre chose qu'un entier echoue"""
    # GIVEN

    tome_a_supprimer = "a"
    mock_dao = MagicMock(spec=MangaPhysiqueDao)
    mock_dao.modifier_manga_physique.return_value.side_effect = TypeError(
        "a,doit être un entier"
    )

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


def test_supprimer_manga_physique_ok():
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
