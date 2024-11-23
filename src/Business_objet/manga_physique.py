from src.business_objet.manga import Manga
from src.service.utilisateur_service import UtilisateurService


class MangaPhysique(Manga):

    """Classe représentant un Manga physique

     Attributs
    ----------
    id_manga : str
        identifiant
    titre : str
        titre du manga
    auteurs: str
        l'auteur du manga
    synopsis : int
        synopsis du manga
    id_utilisateur : int
        identifiant de l'utilisateur qui possède ce manga
    tomes_manquants: list[int]
        liste des tomes de ce manga que l'utilisateur ne possède pas
    dernier_tome: int
        dernier tome de ce manga possédé par ce utilisateur
    status: str
        status actuelle du manga
    """

    def __init__(
        self,
        id_manga,
        id_utilisateur,
        titre_manga,
        auteurs,
        synopsis,
        tomes_manquants,
        dernier_tome,
        status,
        nb_volumes,
        nb_chapitres,
    ):
        "constructeur"
        super().__init__(
            id_manga, titre_manga, auteurs, synopsis, nb_volumes, nb_chapitres
        )
        self.id_utilisateur = id_utilisateur
        self.tomes_manquants = tomes_manquants
        self.dernier_tome = dernier_tome
        self.status = status

    def __str__(self):
        """Représentation graphique d'une mangathèque"""
        utilisateur = UtilisateurService().trouver_par_id_utilisateur(
            self.id_utilisateur
        )
        return (
            f"Mangathèque personelle du manga {self.titre_manga} de {utilisateur.pseudo} :)\n"
            f"Identifiant: {self.id_manga}\n"
            f"Titre: {self.titre_manga}\n"
            f"Auteur(s): {self.auteurs}\n"
            f"Nombre de volumes: {self.nb_volumes}\n"
            f"Nombre de chapitres: {self.nb_chapitres}\n"
            f"Tomes manqants: {self.tomes_manquants}\n"
            f"Dernier tome: {self.dernier_tome}\n"
            f"Statut: {self.status}\n \n"
        )
