from unittest.mock import MagicMock

from src.service.avis_service import AvisService
from src.dao.avis_dao import AvisDAO
from src.business_objet.avis import Avis

# Liste d'exemple d'avis
liste_avis = [
    Avis(id_manga=1, id_utilisateur=1, texte="C'est génial!"),
    Avis(id_manga=2, id_utilisateur=1, texte="Pas mal!"),
    Avis(id_manga=3, id_utilisateur=2, texte="J'ai adoré!"),
]


def test_creer_ok():
    """Création d'un avis réussie"""

    # GIVEN
    id_manga, id_utilisateur, texte = 1, 2, "C'est un super manga !"
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.creer.return_value = True

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao 

    # WHEN
    avis = avis_service.creer_avis(id_manga, id_utilisateur, texte)

    # THEN
    assert avis is True


def test_creer_echec():
    """Création d'un avis échouée """

    # GIVEN
    id_manga, id_utilisateur, texte = 1, 1, "C'est un super manga !"
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.creer.return_value = False

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao  

    # WHEN
    avis = avis_service.creer_avis(id_manga, id_utilisateur, texte)

    # THEN
    assert avis is False


def test_trouver_tous_par_id_ok():
    """Lister les avis d'un utilisateur avec succès"""

    # GIVEN
    id_utilisateur = 1
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.trouver_tous_par_id.return_value = [avis for avis in liste_avis if avis.id_utilisateur == id_utilisateur]

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao 

    # WHEN
    res = avis_service.trouver_avis_par_utilisateur(id_utilisateur)

    # THEN
    assert len(res) == 2
    for avis in res:
        assert avis.id_utilisateur == id_utilisateur


def test_trouver_tous_par_id_echec():
    """Lister les avis d'un utilisateur échoué"""

    # GIVEN
    id_utilisateur = 1
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.trouver_tous_par_id.side_effect = Exception("Erreur de base de données")

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao 

    # WHEN
    res = avis_service.trouver_avis_par_utilisateur(id_utilisateur)

    # THEN
    assert res == []


def test_supprimer_avis_ok():
    """Suppression d'un avis réussie"""

    # GIVEN
    id_manga, id_utilisateur = 1, 1
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.supprimer_avis.return_value = True

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao

    # WHEN
    result = avis_service.supprimer_avis(id_manga, id_utilisateur)

    # THEN
    assert result is True


def test_supprimer_avis_echec():
    """Suppression d'un avis échouée"""

    # GIVEN
    id_manga, id_utilisateur = 1, 1
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.supprimer_avis.return_value = False

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao 

    # WHEN
    result = avis_service.supprimer_avis(id_manga, id_utilisateur)

    # THEN
    assert result is False


def test_modifier_avis_ok():
    """Modification d'un avis réussie"""

    # GIVEN
    id_manga, id_utilisateur, newtexte = 1, 1, "Manga très intéressant"
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.modifier.return_value = True

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao 

    # WHEN
    result = avis_service.modifier(id_manga, id_utilisateur, newtexte)

    # THEN
    assert result is True


def test_modifier_avis_echec():
    """Modification d'un avis échouée"""


    # GIVEN
    id_manga, id_utilisateur, newtexte = 1, 1, "Manga très intéressant"
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.modifier.return_value = False

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao 

    # WHEN
    result = avis_service.modifier(id_manga, id_utilisateur, newtexte)

    # THEN
    assert result is False


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
