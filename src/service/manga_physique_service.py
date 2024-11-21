from src.utils.singleton import Singleton
from src.business_objet.manga_physique import MangaPhysique
from src.dao.manga_physique_dao import MangaPhysiqueDao
from src.utils.log_decorator import log
from src.dao.manga_physique_dao import MangaPhysiqueDao


class MangaPhysiqueService(metaclass=Singleton):
    """Classe permettant d'avoir des informations à propos des Mangas"""


    @log
    def creer_manga_physique(self, manga) -> bool:
        """Créer un manga physique dans la base de données"""
        return MangaPhysiqueDao().creer(manga)

    @log
    def supprimer_manga_physique(self, manga) -> bool:
        """Supprimer un manga de la base de données"""
        return MangaPhysiqueDao().supprimer_manga_physique(manga)

    @log
    def ajouter_tome(self, manga,new_tome):
        """
        ajouter un nouveau tome au manga physique

        parameters
        manga:manga 
        new_tome:tome à ajouter 

        return
        """
        if not isinstance(new_tome, int):
            raise TypeError("Le tome ajouté doit être un entier")
        if new_tome in manga.tomes_manquants:
            manga.tomes_manquants.remove(new_tome)
            return MangaPhysiqueDao().modifier_manga_physique(manga)
        elif new_tome > manga.dernier_tome:
            for i in range(1, new_tome-manga.dernier_tome):
                manga.tomes_manquants.append(manga.dernier_tome+i)
            manga.dernier_tome = new_tome
            return MangaPhysiqueDao().modifier_manga_physique(manga)
        else:
            raise ValueError("tome deja existant")

    @log
    def enlever_tome(self,manga, tome):
        if not isinstance(tome, int):
            raise TypeError(f"{tome},doit être un entier")

        if tome == manga.dernier_tome:
            manga.tomes_manquants.append(tome)
            manga.tomes_manquants.sort()  # Trier pour garantir l'ordre croissant
            
        # On cherche le nouveau dernier tome qui n'est pas manquant
            nouveau_dernier_tome = tome - 1
            while nouveau_dernier_tome in manga.tomes_manquants and nouveau_dernier_tome > 0:
                nouveau_dernier_tome -= 1
                manga.dernier_tome = nouveau_dernier_tome
            return MangaPhysiqueDao().modifier_manga_physique(manga)
        elif tome < manga.dernier_tome and tome not in manga.tomes_manquants:
            manga.tomes_manquants.append(tome)
            return MangaPhysiqueDao().modifier_manga_physique(manga)
        else:
            raise ValueError("vous ne disposez pas de ce tome")

    @log
    def modifier_manga_physique(self, manga):
        "modifier un manga physique enregisté dans la base de donnnées"
        return MangaPhysiqueDao().modifier_manga_physique(manga)