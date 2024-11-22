from unittest.mock import MagicMock

from src.service.avis_service import AvisService
from src.dao.avis_dao import AvisDao
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
    id_manga, id_utilisateur, texte = 1, 5, "C'est un super manga !"
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.creer.return_value = True

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao 

    # WHEN
    avis = avis_service.creer(id_manga, id_utilisateur, texte)
    avis_service.supprimer_avis(id_manga,id_utilisateur)
    # THEN
    assert avis is True


def test_creer_echec():
    """Création d'un avis échouée """

    # GIVEN
    id_manga, id_utilisateur, texte = 1, 4, "C'est un super manga !"
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.creer.return_value = False

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao  

    # WHEN
    avis = avis_service.creer(id_manga, id_utilisateur, texte)
    avis_service.supprimer_avis(id_manga,id_utilisateur)
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
    res = avis_service.trouver_tous_par_id(id_utilisateur)

    # THEN
    assert len(res) == 2
    for avis in res:
        assert avis.id_utilisateur == id_utilisateur


def test_trouver_tous_par_id_echec():
    """Lister les avis d'un utilisateur échoué"""

    # GIVEN
    id_utilisateur = 999
    mock_dao = MagicMock(spec=AvisDao)

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao 

    # WHEN
    res = avis_service.trouver_tous_par_id(id_utilisateur)

    # THEN
    assert res == []

def test_trouver_avis_par_manga_ok():
    """Lister les avis pour un manga avec succès"""

    # GIVEN
    id_manga = 1
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.trouver_avis_par_manga.return_value = [avis for avis in liste_avis if avis.id_manga == id_manga]

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao 

    # WHEN
    res = avis_service.trouver_avis_par_manga(id_manga)

    # THEN
    assert len(res) == 1
    for avis in res:
        assert avis.id_manga == id_manga


def test_trouver_avis_par_manga_echec():
    """Lister les avis pour un manga échoué"""

    # GIVEN
    id_manga = 999
    mock_dao = MagicMock(spec=AvisDao)

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao 

    # WHEN
    res = avis_service.trouver_avis_par_manga(id_manga)

    # THEN
    assert res == []

def test_supprimer_avis_ok():
    """Suppression d'un avis réussie"""

    # GIVEN
    id_manga, id_utilisateur = 1, 5
    mock_dao = MagicMock(spec=AvisDao)

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao

    # WHEN
    avis_service.creer(id_manga,id_utilisateur,"a")
    result = avis_service.supprimer_avis(id_manga, id_utilisateur)

    # THEN
    assert result is True


def test_supprimer_avis_echec():
    """Suppression d'un avis échouée"""

    # GIVEN
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.supprimer_avis.return_value = False

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao 

    # WHEN
    result = avis_service.supprimer_avis(9999, 9999)

    # THEN
    assert result is False


def test_supprimer_note_ok():
    """Suppression d'un avis réussie"""

    # GIVEN
    id_manga, id_utilisateur = 1, 5
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.supprimer_note.return_value = True

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao

    # WHEN
    avis_service.noter(1,5,3)
    result = avis_service.supprimer_note(id_manga, id_utilisateur)

    # THEN
    assert result is True


def test_supprimer_note_echec():
    """Suppression d'une note échouée"""

    # GIVEN
    id_manga, id_utilisateur = 1, 5
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.supprimer_note.return_value = False

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao
    # WHEN
    avis_service.noter(1,5,3) 
    result = avis_service.supprimer_note(id_manga, id_utilisateur)

    # THEN
    self.assertEqual(str(context.exception), "Vous n'avez pas donné de note sur ce manga :/")

def test_modifier_avis_ok():
    """Modification d'un avis réussie"""

    # GIVEN
    id_manga, id_utilisateur, newtexte = 1, 5, "Manga très intéressant"
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.modifier.return_value = True

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao 

    # WHEN
    avis_service.creer(1,5,"lol")
    result = avis_service.modifier(id_manga, id_utilisateur, newtexte)
    avis_service.supprimer_avis(1,5)

    # THEN
    assert result is True


def test_modifier_avis_echec():
    """Modification d'un avis échouée"""


    # GIVEN
    id_manga, id_utilisateur, newtexte = 1, 5, "Manga très intéressant"
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.modifier.return_value = False

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao 

    # WHEN
    avis_service.creer(1,5,"lol")
    result = avis_service.modifier(id_manga, id_utilisateur, newtexte)
    avis_service.supprimer_avis(1,5)

    # THEN
    assert result is False



def test_noter_ok():
    """Notation d'un manga réussie"""

    # GIVEN
    id_manga, id_utilisateur, note = 1, 5, 3
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.noter.return_value = True

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao 

    # WHEN
    result = avis_service.noter(id_manga, id_utilisateur, note)
    avis_service.supprimer_note(id_manga,id_utilisateur)

    # THEN
    assert result is True


def test_noter_echec():
    """Notation d'un manga échouée"""


    # GIVEN
    id_manga, id_utilisateur, note = 1, 5, 3
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.noter.return_value = False

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao 

    # WHEN
    result = avis_service.noter(id_manga, id_utilisateur, note)
    avis_service.supprimer_note(id_manga,id_utilisateur)

    # THEN
    assert result is False


def test_modifier_note_ok():
    """Modification d'un avis réussie"""

    # GIVEN
    id_manga, id_utilisateur, newnote = 1, 5, 3
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.modifier_note.return_value = True

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao 

    # WHEN
    avis_service.noter(1,5,4)
    result = avis_service.modifier_note(id_manga, id_utilisateur, newnote)
    avis_service.supprimer_note(1,5)

    # THEN
    assert result is True


def test_modifier_note_echec():
    """Modification d'un avis échouée"""


    # GIVEN
    id_manga, id_utilisateur, newnote = 1, 1, 3
    mock_dao = MagicMock(spec=AvisDao)
    mock_dao.modifier_note.return_value = False

    avis_service = AvisService()
    avis_service.AvisDao = mock_dao 

    # WHEN
    avis_service.noter(1,5,4)
    result = avis_service.modifier_note(id_manga, id_utilisateur, newnote)
    avis_service.supprimer_note(1,5)

    # THEN
    assertEqual(str(context.exception), "Vous n'avez pas donné de note à ce manga. Si vous souhaitez en donner une, sélectionnez le menu Rédiger un avis/donner une note :)")


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
