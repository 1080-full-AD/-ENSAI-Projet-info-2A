from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.avis_service import AvisService
from src.service.utilisateur_service import UtilisateurService
from src.service.manga_service import MangaService


class ConsulterCollectionView(AbstractView):
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
                    "Entrez le peuso de l'utilisateur en question"
                    ).execute()
                user = UtilisateurService(

                ).trouver_par_pseudo_utilisateur(pseudo=pseudo)
                id_utilisateur = user.id_utilisateur
                avis = AvisService(
                ).trouver_tous_par_id(id_utilisateur=id_utilisateur)
                for i in avis:
                    print(i.__str__())

                return ConsulterAvisView("\n" + "=" * 50 + " Consultation d'avis"
                                         " :) " + "=" * 50 + "\n")

            case "Consulter les avis sur un manga":
                name = inquirer.text(
                 "Entrez le nom du manga en question"
                ).execute()
                manga = MangaService().rechercher_un_manga(titre_manga=name)
                id_manga = manga.id_manga
                avis = AvisService().trouver_avis_par_manga(id_manga=id_manga)
                for i in avis:
                    print(i.__str__())

                return ConsulterAvisView("\n" + "=" * 50 + " Consultation d'avis"
                                         " :) " + "=" * 50 + "\n")

            case "Consulter vos avis":
                from src.views.session import Session
                user = Session().getuser()
                id_utilisateur = user.id_utilisateur
                avis = AvisService(
                ).trouver_tous_par_id(id_utilisateur=id_utilisateur)
                for i in avis:
                    print(i.__str__())

                return ConsulterAvisView("\n" + "=" * 50 + " Consultation d'avis"
                                         " :) " + "=" * 50 + "\n")

            case "Retour":
                from src.views.users.main_user_view import MainUserView

                return MainUserView("Retour au menu utilisateur")
