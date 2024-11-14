from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.avis_service import AvisService
from src.service.utilisateur_service import UtilisateurService

class ConsulterAvisView(AbstractView):
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
                "Consulter les avis d'un utilisateur",
                "Consulter les avis sur un manga",
                "Consulter vos avis",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Consulter les avis d'un utilisateur":
                pseudo = inquirer.text(
                    "Entrez le peuso de l'utiisateur en question"
                    ).execute()
                user = UtilisateurService().trouver_par_pseudo_utilisateur(pseudo)
                id = user.id_utilisateur
                avis = AvisService().trouver_tous_par_id(id)
                for i in avis:
                    print(i.__str__())
                
                return ConsulterAvisView("\n" + "=" * 50 + " Consultation d'avis"
                            " :) " + "=" * 50 + "\n")

            case "Consulter les avis sur un manga":
                pass

            case "Supprimer un avis":
                pass

            case "Consulter vos avis":
                pass

            case "Retour":
                from src.views.users.main_user_view import MainUserView

                return MainUserView("Retour au menu utilisateur :)")


ConsulterAvisView().choisir_menu()
