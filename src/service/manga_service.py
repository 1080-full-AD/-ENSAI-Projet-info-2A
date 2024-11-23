from src.utils.singleton import Singleton
from src.business_objet.manga import Manga
from src.dao.manga_dao import MangaDao
from src.utils.log_decorator import log


class MangaService(metaclass=Singleton):
    """Classe permettant d'avoir des informations à propos des Mangas"""

    @log
    def rechercher_un_manga(self, titre_manga) -> Manga:
        """Trouver un manga à partir de son titre

        Retourne TypeError, si le manga demandé n'est pas une chaîne de caractère
        Retourne ValueError, si le manga recherché n'est pas trouvé

        """
        if isinstance(titre_manga, str) is False:
            raise TypeError("Le titre doit être une chaîne de caractère :/")
        manga = MangaDao().trouver_par_titre(titre_manga)
        if manga:
            return manga
        else:
            raise ValueError("Aucun manga ne possède ce titre :/")

    @log
    def rechercher_un_id_manga(self, id_manga) -> Manga:
        """Trouver un manga à partir de son id

        Retourne TypeError si l'identifiant saisi n'est pas un entier
        Retourne ValueError si le manga recherché n'est pas trouvé

        """
        if isinstance(id_manga, int) is False:
            raise TypeError("L'indentifiant doit être un entier :/")
        manga = MangaDao().trouver_par_id(id_manga)
        if manga:
            return manga
        else:
            raise ValueError("Aucun manga ne possède cet identifiant :/")

    @log
    def creer_manga(self, manga) -> bool:
        """Créer un manga dans la base de données"""
        if MangaDao().creer_manga(manga):
            print("Manga ajouté à la base")
            return True
        else:
            print("echec de l'ajout")
            return False

    @log
    def supprimer_un_manga(self, manga) -> bool:
        MangaService().rechercher_un_id_manga(id_manga=manga.id_manga)
        """Supprimer un manga de la base de données"""
        if MangaDao().supprimer_manga(manga):
            print("Manga supprimé de la base")
            return True
        else:
            return False

    @log
    def modifier_un_manga(self, manga) -> bool:
        """Modifier un manga de la base de données"""
        if MangaDao().modifier(manga):
            print("Modification effectuée")
            return True
        else:
            print("echec de la modification")
            return False

    @log
    def rechercher_un_auteur(self, auteurs) -> Manga:
        """Trouver un manga à partir de son auteur"""
        if isinstance(auteurs, str) is False:
            raise TypeError("Le nom de l'auteur doit être une chaîne de caractère :/")
        manga = MangaDao().trouver_par_auteur(auteurs)
        if manga:
            return manga
        else:
            raise ValueError("Aucun auteur ne s'apelle comme ça :/")

    @log
    def rechercher_une_serie(self, manga) -> Manga:
        """Trouver une série de mangas à partir du nom de la saga"""
        return MangaDao().trouver_serie_par_titre(manga)


manga = Manga(1, "aa","aaaa", "a", 1, 1)

MangaService().creer_manga(manga=manga)
