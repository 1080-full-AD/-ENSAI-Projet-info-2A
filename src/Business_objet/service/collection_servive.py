from business_objet.collection.collection_virtuelle import CollectionVirtuelle
from dao.collection_dao import CollectionDao
from utils.log_decorator import log 


class CollectionVirtuelleService:
    "classe contenant les services des collections virtuelles"

    @log
    def creer(self, titre, id_utilisateur, list_manga)-> CollectionVirtuelle:
        "création d'une collection virtuelle a partir de ses attributs"

        nouvelle_collection = CollectionVirtuelle(    
            titre=titre,
            id_utilisateur=id_utilisateur,
            list_manga=list_manga,
            )

        return nouvelle_collection if CollectionDao().creer(nouvelle_collection) else none

    @log   
    def trouver_par_titre(self,titre)->CollectionVirtuelle:
        "trouver un manga à partir de son titre"
        return CollectionDao().trouver_par_titre(titre)



    @log
    def modifier_collection(self,collection)->collection:
        "modifier une collection"
        return collection if CollectionDao().modifier(collection) else none




    @log
    def supprimer(self, collection) -> bool :
        "supprimer la collection de l'utilisateur"

        return CollectionDao().supprimer(collection)


    @log
    def liste_manga(self, collection):
        "lister tous les mangas qui composent la collection"
        return CollectionDao().liste_manga(collection)
        
       