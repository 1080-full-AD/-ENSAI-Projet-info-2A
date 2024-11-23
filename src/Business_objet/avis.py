from src.service.utilisateur_service import UtilisateurService
from src.service.manga_service import MangaService

class Avis:
    """Classe représentant un avis

     Attributs
    ----------
    id_manga : int
        identifiant du manga
    id_utilisateur : int
        identifiant de l'utilisateur
    avis: str
        l'avis de l'utilisateur
    spoiler: bool
        si l'avis contient un spoiler ou pas
    """
    def __init__(self, id_manga, id_utilisateur, texte=None, note=None, spoiler =False):
        """Constructeur"""
        self.id_manga = id_manga
        self.id_utilisateur = id_utilisateur
        self.texte = texte
        self.note = note
        self.spoiler = spoiler

    def __str__(self):

        try:
            utilisateur = UtilisateurService().trouver_par_id_utilisateur(self.id_utilisateur)
            pseudo_utilisateur = utilisateur.pseudo
        except Exception as e:
            pseudo_utilisateur = "Utilisateur inconnu"
            print(f"Erreur lors de la récupération du pseudo de l'utilisateur : {e}")

        try:
            manga = MangaService().rechercher_un_id_manga(self.id_manga)
            nom_manga = manga.titre_manga
        except Exception as e:
            nom_manga = "Manga inconnu"
            print(f"Erreur lors de la récupération du nom du manga : {e}")
        
        return (
            f"Avis de l'utilisateur {pseudo_utilisateur}"
            f" sur le manga {nom_manga}:"
            f"\n{self.texte}"
            "\n"
            f"\nNote donnée: {self.note}"
            "\n\n"
        )
