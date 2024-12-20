from src.business_objet.collection_virtuelle import CollectionVirtuelle
from src.dao.collection_dao import CollectionDao
from src.dao.utilisateur_dao import UtilisateurDao
from src.utils.log_decorator import log
from src.business_objet.manga_physique import MangaPhysique
from src.business_objet.manga import Manga


class CollectionVirtuelleService:
    "classe contenant les services des collections virtuelles"

    @log
    def creer(
        self,
        titre: str,
        id_utilisateur: int,
        liste_manga: list[Manga],
        description: str,
    ) -> CollectionVirtuelle:
        "création d'une collection virtuelle a partir de ses attributs"

        if not all(isinstance(i, Manga) for i in liste_manga):
            raise TypeError(
                "Les collections virtuelles ne"
                "conteniennent que des mangas virtuelles :/"
            )

        for i in liste_manga:
            if isinstance(i, MangaPhysique):
                raise TypeError(
                    "les collection virtuelles"
                    "ne peuvent contenir des mangas physique"
                )

        if (
            CollectionDao().titre_existant(
                titre=titre, id_utilisateur=id_utilisateur
                ) is True
        ):
            raise ValueError(
                "Vous avez déja une collection avec ce titre :/"
                )
        for i in liste_manga:
            if isinstance(i, MangaPhysique):
                raise ValueError(
                    "les collection virtuelles ne peuvent"
                    " contenir des collections physique"
                )
                break

        nouvelle_collection = CollectionVirtuelle(
            titre=titre,
            id_utilisateur=id_utilisateur,
            liste_manga=liste_manga,
            description=description,
        )

        if CollectionDao().creer(
            collection=nouvelle_collection
            ) and all(
            CollectionDao().ajouter_manga(
                collection=nouvelle_collection, manga=manga
                )
            for manga in liste_manga
        ):
            return nouvelle_collection
        else:
            return None

    @log
    def modifier_description(
        self, collection, new_description
    ) -> CollectionVirtuelle:
        "modifier la description d'une collection"
        collection.description = new_description
        if CollectionDao().modifier(collection) is True:
            return collection
        else:
            return None

    @log
    def modifier_titre(self, collection, new_titre):
        "modifier le titre d'une collection dans la base de données"
        if (
            CollectionDao().titre_existant(
                titre=new_titre,
                id_utilisateur=collection.id_utilisateur
            )
            is True
        ):
            raise ValueError(
                "Vous avez déja une collection avec ce titre :/"
                )

        else:
            modifiee = CollectionDao().modifier_titre(
                collection=collection, new_titre=new_titre
            )
            collection.titre = new_titre
            return collection if modifiee else None

    @log
    def supprimer(self, collection) -> bool:
        "supprimer la collection de l'utilisateur"
        print(f"Suppresion de la collection {collection.titre} réussie :)")

        return CollectionDao().supprimer_collection(collection)

    @log
    def liste_manga(self, id_utilisateur, titre_collec):
        "lister tous les mangas qui composent la collection"
        return CollectionDao().liste_manga(
            id_utilisateur, titre_collec
            )

    @log
    def ajouter_manga(self, collection, new_manga):
        if not isinstance(new_manga, Manga):
            raise ValueError(
                f"{new_manga} n'est pas un manga"
                )
        if isinstance(new_manga, MangaPhysique):
            raise ValueError(
                "les collections virtuelle"
                "ne contiennent que des mangas virtuelles"
            )
        if new_manga in CollectionDao().liste_manga(
            id_utilisateur=collection.id_utilisateur,
            titre_collec=collection.titre
        ):
            raise ValueError(
                f"Ce manga appartient déja à {collection.titre} :/"
                )
        if new_manga in CollectionDao().liste_manga(
            id_utilisateur=collection.id_utilisateur,
            titre_collec=collection.titre
        ):
            raise ValueError(
                "ce manga appartient déja à cette collection"
                )
        print(f"{new_manga} a été ajouté à {collection.titre} :)")
        return CollectionDao().ajouter_manga(
            collection=collection, manga=new_manga
            )

    @log
    def supprimer_manga(self, collection, manga):
        if manga not in CollectionDao().liste_manga(
            collection.id_utilisateur, collection.titre
        ):
            raise ValueError(
                f"{manga.titre_manga} ne fait pas"
                f" partit de {collection.titre} :/"
            )
        else:
            print(f"{manga} a été supprimé"
                  f" de {collection.titre} avec succès :)")
            return CollectionDao().supprimer_manga(
                manga=manga, collection=collection
                )

    @log
    def liste_collection(self, id_utilisateur: int):
        "lister toutes les collections virtuelles de l'utilisateur"
        if not isinstance(id_utilisateur, int):
            raise TypeError(
                f"{id_utilisateur} n'est pas un identifiant"
                )
        if UtilisateurDao().trouver_par_id(id_utilisateur) is None:
            raise ValueError(
                "cet identifiant n'est associé à aucun utilisateur"
                )
        return CollectionDao().liste_collection(id_utilisateur)

    @log
    def rechercher_collection(
        self, id_utilisateur: int, titre_collec: str
    ):
        """rechercher une collection
        à partir de l'identifiant d'un utilisateur
        et du titre de la collection"""
        if CollectionDao().recherhcer_collection(
            id_utilisateur, titre_collec
             ) is None:
            raise ValueError(
                "Vous ne possédez pas de collection avec ce nom :/"
                )
        else:
            return CollectionDao().recherhcer_collection(
                id_utilisateur, titre_collec
                )
