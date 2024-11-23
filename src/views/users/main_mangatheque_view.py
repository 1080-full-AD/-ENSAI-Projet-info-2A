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
                from src.views.mangatheque.creer_mangatheque_view import (
                    CreateMangathequeView,
                )

                return CreateMangathequeView(
                    "\n" + "=" * 50 + " Création de collection" " :) " + "=" * 50 + "\n"
                )

            case "Modifier une mangathèque":
                from src.views.collection.modification_mangatheque_view import (
                    ModificationMangathequeView,
                )

                return ModificationMangathequeView(
                    "\n" + "=" * 50 + " Modification de collection"
                    " :) " + "=" * 50 + "\n"
                )

            case "Supprimer une mangathèque":
                from src.views.mangatheque.supprimer_mangatheque_view import (
                    SupprimerMangathequeView,
                )

                return SupprimerMangathequeView(
                    "\n" + "=" * 50 + " Suppression de mangathèque"
                    " :) " + "=" * 50 + "\n"
                )

            case "Consulter les mangathèques":
                from src.views.collection.consulter_mangatheque_view import (
                    ConsulterMangathequeView,
                )

                return ConsulterMangathequeView(
                    "\n" + "=" * 50 + " Consultation des collections"
                    " :) " + "=" * 50 + "\n"
                )
            case "Retour":
                from src.views.users.main_user_view import MainUserView

                return MainUserView("Retour au menu utilisateur :)")
