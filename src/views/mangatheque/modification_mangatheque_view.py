from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.collection_service import CollectionVirtuelleService
from src.service.manga_service import MangaService
from src.views.session import Session
from src.views.users.main_collection_view import MainCollectionView


class ModificationMangathequeView(AbstractView):
    """Menu principal des avis"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        titre = inquirer.text(
            message="Donnez le titre de la mangathèque que vous souhaitez modifier :)",
        ).execute()

        user = Session().getuser()
        id_utilisateur = user.id_utilisateur

        try:
            collection = CollectionVirtuelleService().rechercher_collection(id_utilisateur=id_utilisateur, titre_collec=titre)

        except Exception as e:
            print("\n", e)
            return MainCollectionView("\n" + "=" * 50 + " Menu des collection"
                                         " :) " + "=" * 50 + "\n")


        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Modifier le titre",
                "Modifier la description",
                "Ajouter un manga",
                "Enlever un manga",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Modifier le titre":
                new_titre = inquirer.text(
                    "Rédigez votre nouveau titre :)"
                ).execute()
                try:
                    CollectionVirtuelleService().modifier_titre(collection=collection, new_titre=new_titre)
                except Exception as e:
                    print("\n", e)

                return MainCollectionView(("\n" + "=" * 50 + " Menu des collections"
                                        " :) " + "=" * 50 + "\n"))

            case "Modifier la description":
                desc = inquirer.text(
                    "Rédigez votre nouvelle description :)"
                ).execute()
                try:
                    CollectionVirtuelleService().modifier_description(collection=collection, new_description=desc)
                except Exception as e:
                    print("\n", e)

                return MainCollectionView(("\n" + "=" * 50 + " Menu des collections"
                                        " :) " + "=" * 50 + "\n"))

            case "Ajouter un manga":
                
                titre_manga = inquirer.text(
                    "Entrez le nom du manga que vous voulez ajouter :)"
                ).execute()
                try:
                    manga = MangaService().rechercher_un_manga(
                        titre_manga=titre_manga
                        )
                    CollectionVirtuelleService().ajouter_manga(collection=collection, new_manga=manga)
                except Exception as e:
                    print("\n", e)

                return MainCollectionView(("\n" + "=" * 50 + " Modification Menu des collections"
                                        " :) " + "=" * 50 + "\n"))

            case "Enlever un manga":
                titre_manga = inquirer.text(
                    "Entrez le nom du manga que vous voulez enlever :)"
                ).execute()

                try:
                    manga = MangaService().rechercher_un_manga(
                        titre_manga=titre_manga
                    )
                    CollectionVirtuelleService().supprimer_manga(collection=collection, manga=manga)
                except Exception as e:
                    print("\n", e)

                return MainCollectionView("\n" + "=" * 50 + " Menu des collections"
                                        " :) " + "=" * 50 + "\n")               

            case "Retour":
                from src.views.users.main_opinion_view import MainOpinionView

                return MainCollectionView("\n" + "=" * 50 + " Menu des collections"
                                       " :) " + "=" * 50 + "\n")
