from src.utils.singleton import Singleton
from src.business_objet.manga import Manga
from src.dao.manga_dao import MangaDao
from src.utils.log_decorator import log


class MangaService(metaclass=Singleton):
    """Classe permettant d'avoir des informations à propos des Mangas"""

    @log
    def rechercher_un_manga(self, titre) -> Manga:
        """Trouver un manga à partir de son titre"""
        return MangaDao().trouver_par_id(titre)

    @log
    def rechercher_un_id_manga(self, id_manga) -> Manga:
        """Trouver un manga à partir de son id"""
        return MangaDao().trouver_par_id(id_manga)

    @log
    def creer_manga(self, manga) -> bool:
        """Créer un manga dans la base de données"""
        return MangaDao().creer_manga(manga)

    @log
    def supprimer_un_manga(self, manga) -> bool:
        """Supprimer un manga de la base de données"""
        return MangaDao().supprimer_manga(manga)

    @log
    def modifier_un_manga(self, manga) -> bool:
        """Modifier un manga de la base de données"""
        return MangaDao().modifier(manga)

    @log
    def rechercher_un_auteur(self, auteur) -> Manga:
        """Trouver un manga à partir de son auteur"""
        return MangaDao().trouver_par_auteur(auteur)

    @log
    def rechercher_une_serie(self, manga) -> Manga:
        """Trouver une série de mangas à partir du nom de la saga"""
        return MangaDao().trouver_serie_par_titre(manga)
