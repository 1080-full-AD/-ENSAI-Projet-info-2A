from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.avis_service import AvisService
from src.service.utilisateur_service import UtilisateurService
from src.service.manga_service import MangaService


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

                afficher_spoilers = inquirer.select(
                    message="Voulez-vous afficher les spoilers ?",
                    choices=["Oui", "Non"],
                ).execute()

                afficher_spoilers = afficher_spoilers == "Oui"

                pseudo = inquirer.text(
                    "Entrez le pseudo de l'utilisateur en question"
                ).execute()
                try:
                    user = UtilisateurService().trouver_par_pseudo_utilisateur(pseudo=pseudo)
                    id_utilisateur = user.id_utilisateur
                except Exception as e:
                    print("\n", e)
                    return ConsulterAvisView("\n" + "=" * 50 + " Consultation d'avis"
                                             " :) " + "=" * 50 + "\n")

                avis = AvisService().trouver_tous_par_id(id_utilisateur=id_utilisateur, include_spoilers=afficher_spoilers)

                # Filtrer les avis en fonction du choix de l'utilisateur sur les spoilers
                for i in avis:
                    if afficher_spoilers or not i.spoiler:  # Si l'utilisateur veut voir les spoilers ou l'avis n'est pas un spoiler
                        print(i.__str__())
                    else:
                        print("Avis marqué comme spoiler, non affiché.")  # Message si l'avis est un spoiler

                return ConsulterAvisView("\n" + "=" * 50 + " Consultation d'avis"
                                         " :) " + "=" * 50 + "\n")

            case "Consulter les avis sur un manga":

                afficher_spoilers = inquirer.select(
                    message="Voulez-vous afficher les spoilers ?",
                    choices=["Oui", "Non"],
                ).execute()

                afficher_spoilers = afficher_spoilers == "Oui"
                name = inquirer.text(
                    "Entrez le nom du manga en question"
                ).execute()
                try:
                    manga = MangaService().rechercher_un_manga(titre_manga=name)
                except Exception as e:
                    print("\n", e)
                    return ConsulterAvisView("\n" + "=" * 50 + " Consultation d'avis"
                                             " :) " + "=" * 50 + "\n")

                id_manga = manga.id_manga
                avis = AvisService().trouver_avis_par_manga(id_manga=id_manga, include_spoilers=afficher_spoilers)


                for i in avis:
                    if afficher_spoilers or not i.spoiler:
                        print(i.__str__())
                    else:
                        print("Avis marqué comme spoiler, non affiché.")

                return ConsulterAvisView("\n" + "=" * 50 + " Consultation d'avis"
                                         " :) " + "=" * 50 + "\n")

            case "Consulter vos avis":
                from src.views.session import Session
                user = Session().getuser()
                id_utilisateur = user.id_utilisateur
                avis = AvisService().trouver_tous_par_id(id_utilisateur=id_utilisateur)

                for i in avis:
                    print(i.__str__())


                return ConsulterAvisView("\n" + "=" * 50 + " Consultation d'avis"
                                         " :) " + "=" * 50 + "\n")

            case "Retour":
                from src.views.users.main_user_view import MainUserView
                return MainUserView("Retour au menu utilisateur")
