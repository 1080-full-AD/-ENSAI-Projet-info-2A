from src.utils.singleton import Singleton
from src.business_objet.manga_physique import MangaPhysique
from src.dao.manga_physique_dao import MangaPhysiqueDao
from src.utils.log_decorator import log
from src.dao.utilisateur_dao import UtilisateurDao


class MangaPhysiqueService(metaclass=Singleton):
    """Classe permettant d'avoir des informations à propos des Mangas"""

    @log
    def creer_manga_physique(self, manga: MangaPhysique) -> bool:
        """Créer un manga physique dans la base de données"""
        if MangaPhysiqueDao().creer(manga):
            print("Création de la mangathèque réussie :)")
            return True
        else:
            return False
    @log
    def supprimer_manga_physique(self, manga: MangaPhysique) -> bool:
        """Supprimer un manga de la base de données"""
        if MangaPhysiqueDao().supprimer_manga_physique(manga):
            print("Suppression de la mangathèque réussie :)")
            return True
        else:
            return False

    @log
    def ajouter_tome(self, manga: MangaPhysique, new_tome: int) -> bool:
        """
        ajouter un nouveau tome au manga physique

        parameters
        -----------
        manga:manga
        new_tome:tome à ajouter

        return
        ---------
        bool
        True si l'ajout c'est bien passée
        False sinon
        """
        if not isinstance(new_tome, int):
            raise TypeError("Le tome ajouté doit être un entier")
        if new_tome in manga.tomes_manquants:
            manga.tomes_manquants.remove(new_tome)
            return MangaPhysiqueDao().modifier_manga_physique(manga)
        elif new_tome > manga.dernier_tome:
            for i in range(1, new_tome - manga.dernier_tome):
                manga.tomes_manquants.append(manga.dernier_tome + i)
            manga.dernier_tome = new_tome
            return MangaPhysiqueDao().modifier_manga_physique(manga)
        else:
            raise ValueError("Vous possédez déjà ce tome")

    @log
    def enlever_tome(self, manga: MangaPhysique, tome) -> bool:
        """
        elever un  tome au manga physique

        parameters
        -----------
        manga:manga
        tome:tome à elever

        return
        ---------
        bool
        True si le tome a bien été enlever
        False sinon
        """
        if not isinstance(tome, int):
            raise TypeError(f"{tome},doit être un entier")

        if tome == manga.dernier_tome:
            manga.tomes_manquants.append(tome)
            manga.tomes_manquants.sort()  # Trier pour garantir l'ordre croissant

            # On cherche le nouveau dernier tome qui n'est pas manquant
            nouveau_dernier_tome = tome - 1
            while (
                nouveau_dernier_tome in manga.tomes_manquants
                and nouveau_dernier_tome > 0
            ):
                nouveau_dernier_tome -= 1
                manga.dernier_tome = nouveau_dernier_tome
            return MangaPhysiqueDao().modifier_manga_physique(manga)

        elif tome < manga.dernier_tome and tome not in manga.tomes_manquants:
            manga.tomes_manquants.append(tome)
            return MangaPhysiqueDao().modifier_manga_physique(manga)
        else:
            raise ValueError("vous ne disposez pas de ce tome :/")

    @log
    def modifier_manga_physique(self, manga):
        "modifier un manga physique enregisté dans la base de donnnées"
        return MangaPhysiqueDao().modifier_manga_physique(manga)

    @log
    def lister_manga_physique(self, id_utilisateur):
        "lister tous les mangas physique d'un utilisateur"
        if not isinstance(id_utilisateur, int):
            raise TypeError(f"{id_utilisateur} n'est pas un identifiant")
        if UtilisateurDao().trouver_par_id(id_utilisateur) is None:
            raise ValueError("ce identifiant n'est associé à aucun utilisateur")
        return MangaPhysiqueDao().liste_manga_physique(id_utilisateur)

    @log
    def rechercher_manga_physique(self, id_utilisateur: int, id_manga: int):
        """rechercher un manga physique à partir de l'identifiant d'un utilisateur
        et de celui du manga"""
        if not isinstance(id_utilisateur, int) or not isinstance(id_manga, int):
            raise TypeError("les informations renseignés ne sont pas correctes")
        else:
            if UtilisateurDao().trouver_par_id(id_utilisateur) is None:
                raise ValueError("cet identifiant n'est associé à aucun utilisateur")
            else:
                if (
                    MangaPhysiqueDao().rechercher_manga_physique(id_utilisateur, id_manga)
                    is None
                    ):
                    raise ValueError("aucun manga trouvé :/")
                else:
                    return MangaPhysiqueDao().rechercher_manga_physique(
                        id_utilisateur, id_manga
                         )
