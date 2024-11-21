from src.business_objet.manga import Manga 


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

    def __init__(self, id_manga, id_utilisateur, titre_manga, auteurs, 
                 synopsis, tomes_manquants, dernier_tome, status):
        "constructeur"         
        super().__init__(id_manga, titre_manga, auteurs, synopsis)
        self.id_utilisateur = id_utilisateur
        self.tomes_manquants = tomes_manquants
        self.dernier_tome = dernier_tome
        self.status = status

