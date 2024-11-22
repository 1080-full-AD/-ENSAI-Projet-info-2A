from InquirerPy import inquirer
from src.views.abstract_view import AbstractView


class MainMangathequeView(AbstractView):
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
                "Créer une mangathèque",
                "Modifier une mangathèque",
                "Supprimer une mangathèque",
                "Consulter les mangathèques",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Créer une mangathèque":
                from src.views.collection.creer_mangatheque_view import CreateMangathequeView

                return CreateCollectionView("\n" + "=" * 50 + " Création de collection"
                                         " :) " + "=" * 50 + "\n")

            case "Modifier une mangathèque":
                from src.views.collection.modification_collection_view import ModificationCollectionView

                return ModificationCollectionView("\n" + "=" * 50 + " Modification de collection"
                                         " :) " + "=" * 50 + "\n")

            case "Supprimer une mangathèque":
                from src.views.collection.supprimer_collection_view import SupprimerCollectionView

                return SupprimerCollectionView("\n" + "=" * 50 + " Suppression de collections"
                                         " :) " + "=" * 50 + "\n")

            case "Consulter les mangathèques":
                from src.views.collection.consulter_mangatheque_view import ConsulterCollectionView

                return ConsulterCollectionView("\n" + "=" * 50 + " Consultation des collections"
                                         " :) " + "=" * 50 + "\n")
            case "Retour":
                from src.views.users.main_user_view import MainUserView

                return MainUserView("Retour au menu utilisateur :)")
