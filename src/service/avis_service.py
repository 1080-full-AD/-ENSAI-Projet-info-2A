import logging
import dotenv

from src.dao.avis_dao import AvisDao
from src.business_objet.avis import Avis


class AvisService:

    def creer(self, id_manga: int, id_utilisateur: int, texte: str) -> None:
        """Création d'un avis

        Parameters
        ----------
        id_manga : int
        id_utilisateur : int
        texte : str

        Returns
        -------
        bool
            True si l'avis a été créé avec succès, False sinon
        """
        avis = Avis(id_manga=id_manga, id_utilisateur=id_utilisateur, texte=texte)
        if AvisDao().creer(avis):
            AvisDao().creer(avis)
        else:
            raise ValueError("Erreur lors de la création de l'avis :/ ")


    def trouver_tous_par_id(self, id_utilisateur: int) -> list[Avis]:
        """Trouver les avis d'un utilisateur

        Parameters
        ----------
        id_utilisateur : int

        Returns
        -------
        list[Avis]
            Liste des avis de l'utilisateur
        """
        try:
            return AvisDao().trouver_tous_par_id(id_utilisateur)
        except Exception as e:
            logging.error(f"Erreur lors de la récupération des avis pour l'utilisateur {id_utilisateur}: {e}")
            return []

    def trouver_avis_par_manga(self, id_manga: int) -> list[Avis]:
        """Trouver les avis pour un manga

        Parameters
        ----------
        id_manga : int

        Returns
        -------
        list[Avis]
            Liste des avis pour ce manga
        """
        try:
            return AvisDao().trouver_avis_par_manga(id_manga)
        except Exception as e:
            logging.error(f"Erreur lors de la récupération des avis pour le manga {id_manga}: {e}")
            return []

    def supprimer_avis(self, id_manga: int, id_utilisateur: int) -> bool:
        """Supprimer un avis

        Parameters
        ----------
        id_manga : int
        id_utilisateur : int

        Returns
        -------
        bool
            True si l'avis a été supprimé avec succès, False sinon
        """
        avis = Avis(id_manga=id_manga, id_utilisateur=id_utilisateur, texte="")
        try:
            return AvisDao().supprimer_avis(avis)
        except Exception as e:
            logging.error(f"Erreur lors de la suppression de l'avis: {e}")
            return False

    def modifier(self, id_manga: int, id_utilisateur: int, newtexte: str) -> bool:
        """Modifier un avis

        Parameters
        ----------
        id_manga : int
        id_utilisateur : int
        newtexte : str

        Returns
        -------
        bool
            True si la modification a été un succès, False sinon
        """
        avis = Avis(id_manga=id_manga, id_utilisateur=id_utilisateur, texte="")
        try:
            return AvisDao().modifier(avis, newtexte)
        except Exception as e:
            logging.error(f"Erreur lors de la modification de l'avis: {e}")
            return False

    def noter(self, id_manga: int, id_utilisateur: int, note: int) -> bool:
        """Noter un manga

        Parameters
        ----------
        id_manga : int
        id_utilisateur : int
        note : int

        Returns
        -------
        bool
            True si la modification a été un succès, False sinon
        """
        if note < 0 or note > 5:
            logging.error(f"Note invalide: {note}. La note doit être comprise entre 0 et 5.")
            return False
        avis = Avis(id_manga=id_manga, id_utilisateur=id_utilisateur, texte="")
        try:
            return AvisDao().noter(avis, note)
        except Exception as e:
            logging.error(f"Erreur lors de la notation du manga: {e}")
            return False

    def modifier_note(self, id_manga: int, id_utilisateur: int, newnote: int) -> bool:
        """Modifier une note

        Parameters
        ----------
        id_manga : int
        id_utilisateur : int
        newnote : int

        Returns
        -------
        bool
            True si la modification a été un succès, False sinon
        """
        avis = Avis(id_manga=id_manga, id_utilisateur=id_utilisateur, texte="")
        try:
            return AvisDao().modifier_note(avis, newnote)
        except Exception as e:
            logging.error(f"Erreur lors de la modification de la note: {e}")
            return False
