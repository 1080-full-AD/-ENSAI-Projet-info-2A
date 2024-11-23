class Manga:
    """Classe représentant un Manga

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
    """

    def __init__(
        self, id_manga, titre_manga, auteurs, synopsis, nb_volumes, nb_chapitres
    ):
        """Constructeur"""
        self.titre_manga = titre_manga
        self.id_manga = id_manga
        self.auteurs = auteurs
        self.synopsis = synopsis
        self.nb_volumes = nb_volumes
        self.nb_chapitres = nb_chapitres

    def __str__(self):
        return (
            f"\n ---> {self.titre_manga}\n"
            f"      Identifiant: {self.id_manga}\n"
            f"      Auteur(s): {self.auteurs}\n"
            f"      Synopsis: {self.synopsis}"
            f"      Nombre de volumes: {self.id_manga}\n"
            f"      Nombre de chapitres: {self.auteurs}\n"
            f"      Synopsis: {self.synopsis}"
        )

    def __eq__(self, autre_manga):
        """
        Compare deux objets Manga pour vérifier s'ils sont égaux.

        param
        autre_manga: manga à comparer avec l'instance actuelle.
        return:
        True si les deux mangas sont égaux, False sinon.
        """
        if isinstance(autre_manga, Manga):
            return (
                self.id_manga == autre_manga.id_manga
                and self.titre_manga == autre_manga.titre_manga
                and self.auteurs == autre_manga.auteurs
                and self.synopsis == autre_manga.synopsis
                and self.nb_volumes == autre_manga.nb_volumes
                and self.nb_chapitres == autre_manga.nb_chapitres
            )
        return False
