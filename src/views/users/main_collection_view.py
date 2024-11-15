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
                "Créer une Collection",
                "Modifier une Collection",
                "Supprimer une Collection",
                "Consulter les Collections",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Créer une Collection":                
                from src.views.collection.creer_collection_view import CreateCollectionView

                return CreateCollectionView("\n" + "=" * 50 + " Création de Collection"
                                         " :) " + "=" * 50 + "\n")

            case "Modifier une Collection":
                from src.views.collection.modification_collection_view import ModificationCollectionView

                return ModificationCollectionView("\n" + "=" * 50 + " Modification de Collection"
                                         " :) " + "=" * 50 + "\n")

            case "Supprimer une Collection":
                from src.views.collection.supprimer_collection_view import SupprimerCollectionView

                return CreateCollectionView("\n" + "=" * 50 + " Création d'avis"
                                         " :) " + "=" * 50 + "\n")

            case "Consulter les Collections":
                from src.views.collection.consulter_collection_view import ConsulterCollectionView

                return ConsulterCollectionView("\n" + "=" * 50 + " Consultation d'avis"
                                         " :) " + "=" * 50 + "\n")
            case "Retour":
                from src.views.users.main_user_view import MainUserView

                return MainUserView("Retour au menu utilisateur :)")
