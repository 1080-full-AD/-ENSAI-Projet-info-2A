from InquirerPy import inquirer
from src.views.abstract_view import AbstractView


class MainCollectionView(AbstractView):
    """Menu principal des collections"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Créer une collection",
                "Modifier une collection",
                "Supprimer une collection",
                "Consulter les collections",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Créer une collection":
                from src.views.collection.creer_collection_view import CreateCollectionView

                return CreateCollectionView("\n" + "=" * 50 + " Création de Collection"
                                         " :) " + "=" * 50 + "\n")

            case "Modifier une collection":
                from src.views.collection.modification_collection_view import ModificationCollectionView

                return ModificationCollectionView("\n" + "=" * 50 + " Modification de Collection"
                                         " :) " + "=" * 50 + "\n")

            case "Supprimer une collection":
                from src.views.collection.supprimer_collection_view import SupprimerCollectionView

                return CreateCollectionView("\n" + "=" * 50 + " Création d'avis"
                                         " :) " + "=" * 50 + "\n")

            case "Consulter les collections":
                from src.views.collection.consulter_collection_view import ConsulterCollectionView

                return ConsulterCollectionView("\n" + "=" * 50 + " Consultation d'avis"
                                         " :) " + "=" * 50 + "\n")
            case "Retour":
                from src.views.users.main_user_view import MainUserView

                return MainUserView("Retour au menu utilisateur :)")
