from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.utilisateur_service import UtilisateurService
from src.views.session import Session


class MainUserView(AbstractView):
    """Vue d'accueil des utilisateurs"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "=" * 50 + " Bienvenue :) " + "=" * 50 + "\n")

        user = Session().getuser()

        if user.is_admin is False:
            choices = [
                "Rechercher des mangas",
                "Accéder au menu des collections",
                "Accéder au menu des mangathèques",
                "Accéder au menu des avis",
                "Se déconnecter",
                "Supprimer son compte :(",
            ]
        else:
            choices = [
                "Rechercher des mangas",
                "Accéder au menu des collections",
                "Accéder au menu des mangathèques",
                "Accéder au menu des avis",
                "Accéder au menu de modération",
                "Se déconnecter",
            ]

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=choices,
        ).execute()

        match choix:
            case "Rechercher des mangas":
                from src.views.accueil.search_manga_view import MangaSearchView

                return MangaSearchView(
                    "\n" + "=" * 50 + " Recherche" " de mangas " + "=" * 50 + "\n"
                )

            case "Accéder au menu des collections":
                from src.views.users.main_collection_view import MainCollectionView

                return MainCollectionView(
                    "\n" + "=" * 50 + " Menu des" " collections " + "=" * 50 + "\n"
                )

            case "Accéder au menu des mangathèques":
                from src.views.users.main_mangatheque_view import MainMangathequeView

                return MainMangathequeView(
                    "\n" + "=" * 50 + " Menu des" " Mangathèques :) " + "=" * 50 + "\n"
                )

            case "Accéder au menu des avis":
                from src.views.users.main_opinion_view import MainOpinionView

                return MainOpinionView(
                    "\n" + "=" * 50 + " Menu des " "avis " + "=" * 50 + "\n"
                )

            case "Se déconnecter":
                from src.views.accueil.main_menu_view import MainView

                UtilisateurService().se_deconnecter()
                return MainView("Retour au menu principal")

            case "Supprimer son compte :(":
                from src.views.accueil.main_menu_view import MainView
                from src.service.manga_physique_service import MangaPhysiqueService
                from src.service.collection_service import CollectionVirtuelleService
                from src.service.avis_service import AvisService
                from src.service.utilisateur_service import UtilisateurService
                try:
                    supp = inquirer.confirm(
                        message=f"Confirmer la suppression "
                                f"de de l'utilisateur {user.id_utilisateur} ?"
                    ).execute()

                    if supp is True:
                        id_utilisateur = user.id_utilisateur
                        Lc = CollectionVirtuelleService().liste_collection(id_utilisateur=id_utilisateur)
                        La = AvisService().trouver_tous_par_id(id_utilisateur=id_utilisateur)
                        Lm = MangaPhysiqueService().lister_manga_physique(id_utilisateur=id_utilisateur)
                        for i in Lc:
                            CollectionVirtuelleService().supprimer(i)
                        for i in La:
                            AvisService().supprimer_avis(id_utilisateur=id_utilisateur, id_manga=i.id_manga)
                            AvisService().supprimer_note(id_manga=i.id_manga, id_utilisateur=id_utilisateur)
                        for i in Lm:
                            MangaPhysiqueService().supprimer_manga_physique(manga=i)
                        UtilisateurService().supprimer_utilisateur(utilisateur=user)
                        UtilisateurService().supprimer_utilisateur(
                            utilisateur=Session().getuser()
                        )
                except Exception as e:
                    print("\n", e)
        
                return MainView("Retour au menu principal")

            case "Accéder au menu de modération":
                from src.views.users.main_moderation_view import MainModerationView

                return MainModerationView(
                    "\n" + "=" * 50 + " Menu des modérateurs" + "=" * 50 + "\n"
                )
