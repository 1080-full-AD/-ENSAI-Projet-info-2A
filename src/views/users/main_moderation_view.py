from InquirerPy import inquirer
from src.views.abstract_view import AbstractView


class MainModerationView(AbstractView):
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
                "Gestion de la base de manga",
                "Gestion des avis",
                "Gestion des utilisateurs",
                "Gestion des collections",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Gestion de la base de manga":
                from src.views.moderation.moderation_manga_view import ModerationMangaView

                return ModerationMangaView("\n" + "=" * 50 + " Modération de manga"
                                         + "=" * 50 + "\n")

            case "Modifier une mangathèque":
                from src.views.collection.modification_mangatheque_view import ModificationMangathequeView

                return ModificationMangathequeView("\n" + "=" * 50 + " Modification de collection"
                                         " :) " + "=" * 50 + "\n")

            case "Supprimer une mangathèque":
                from src.views.collection.supprimer_mangatheque_view import SupprimerCollectionView

                return SupprimerCollectionView("\n" + "=" * 50 + " Suppression de collections"
                                         " :) " + "=" * 50 + "\n")

            case "Consulter les mangathèques":
                from src.views.collection.consulter_mangatheque_view import ConsulterMangathequeView

                return ConsulterMangathequeView("\n" + "=" * 50 + " Consultation des collections"
                                         " :) " + "=" * 50 + "\n")
            case "Retour":
                from src.views.users.main_user_view import MainUserView

                return MainUserView("Retour au menu utilisateur :)")
