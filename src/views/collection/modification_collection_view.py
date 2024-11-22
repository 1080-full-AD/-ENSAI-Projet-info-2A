from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.collection_service import CollectionVirtuelleService
from src.service.manga_service import MangaService
from src.views.session import Session
from src.views.users.main_collection_view import MainCollectionView


class ModificationCollectionView(AbstractView):
    """Menu principal des avis"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        titre = inquirer.text(
            message="Donnez le titre de la collection que vous souhaitez modifier :)",
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
                titre = inquirer.text(
                    "Rédigez votre nouveau titre :)"
                ).execute()
                try:
                    CollectionVirtuelleService().modifier_titre(collection=collection, new_titre=titre)
                except Exception as e:
                    print("\n", e)

                return ModificationCollectionView(("\n" + "=" * 50 + " Modification de collection"
                                        " :) " + "=" * 50 + "\n"))

            case "Modifier la description":
                desc = inquirer.text(
                    "Rédigez votre nouvelle description :)"
                ).execute()
                try:
                    CollectionVirtuelleService().modifier_description(collection=collection, new_description=desc)
                except Exception as e:
                    print("\n", e)

                return ModificationCollectionView(("\n" + "=" * 50 + " Modification de collection"
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

                return ModificationCollectionView(("\n" + "=" * 50 + " Modification de collection"
                                        " :) " + "=" * 50 + "\n"))

            case "Enlever un manga":
                
                note = int(inquirer.number(
                    f"Donnez votre nouvelle note à {manga.titre_manga} :)",
                    min_allowed=0,
                    max_allowed=5
                ).execute())
                AvisService().noter(id_manga=id_manga,
                                    id_utilisateur=id_utilisateur, note=note)

                from src.views.users.main_opinion_view import MainOpinionView

                return MainOpinionView("\n" + "=" * 50 + " Menu des avis"
                                       " :) " + "=" * 50 + "\n")

            case "Retour":
                from src.views.users.main_opinion_view import MainOpinionView

                return MainOpinionView("\n" + "=" * 50 + " Menu des avis"
                                       " :) " + "=" * 50 + "\n")
