from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.manga_physique_service import MangaPhysiqueService
from src.service.utilisateur_service import UtilisateurService
from src.views.session import Session
from src.views.users.main_mangatheque_view import MainMangathequeView


class ConsulterMangathequeView(AbstractView):
    """Menu pour consulter les avis"""

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
                "Consulter vos mangathèques",
                "Consulter les mangathèques d'un utilisateur",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Consulter vos mangathèques":
                user = Session().getuser()
                id_utilisateur = user.id_utilisateur

                liste_collec = MangaPhysiqueService().lister_manga_physique(
                    id_utilisateur=id_utilisateur
                )
                for i in liste_collec:
                    print(i.__str__())

                return ConsulterMangathequeView(
                    "\n" + "=" * 50 + " Consultation des collections"
                    " :) " + "=" * 50 + "\n"
                )

            case "Consulter les mangathèques d'un utilisateur":
                pseudo = inquirer.text(
                    "Entrez le pseudo de l'utilisateur en question :)"
                ).execute()
                try:
                    user = UtilisateurService().trouver_par_pseudo_utilisateur(
                        pseudo=pseudo
                    )
                    id_utilisateur = user.id_utilisateur
                    liste_collec = MangaPhysiqueService().lister_manga_physique(
                        id_utilisateur=id_utilisateur
                    )
                    for i in liste_collec:
                        print(i.__str__())
                except Exception as e:
                    print("\n", e)

                return ConsulterMangathequeView(
                    "\n" + "=" * 50 + " Consultation des collections"
                    " :) " + "=" * 50 + "\n"
                )
            case "Retour":
                return MainMangathequeView(
                    "\n" + "=" * 50 + " Menu des mangatheques " + "=" * 50 + "\n"
                )
