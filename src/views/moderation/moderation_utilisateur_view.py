from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.utilisateur_service import UtilisateurService
from src.service.collection_service import CollectionVirtuelleService
from src.service.avis_service import AvisService
from src.views.users.main_moderation_view import MainModerationView
from src.service.manga_physique_service import MangaPhysiqueService


class ModerationUtilisateurView(AbstractView):
    """Menu principal des collections"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        try:
            id_utilisateur = int(
                inquirer.number(message="Entrez l'identifiant"
                                        " de l'utilisateur que vous"
                                        " voulez supprimer").execute()
            )
            utilisateur = UtilisateurService().trouver_par_id_utilisateur(id=id_utilisateur)

        except Exception as e:
            print("\n", e)
            return MainModerationView(
                        "\n" + "=" * 50 + " Menu de modération " + "=" * 50 + "\n"
                    )
        try:
            supp = inquirer.confirm(
                message=f"Confirmer la suppression "
                        f"de de l'utilisateur {id_utilisateur} ?"
            ).execute()

            if supp is True:
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
                UtilisateurService().supprimer_utilisateur(utilisateur=utilisateur)

        except Exception as e:
            print("\n", e)
            return MainModerationView(
                        "\n" + "=" * 50 + " Menu de modération " + "=" * 50 + "\n"
                    )

        return MainModerationView(
                    "\n" + "=" * 50 + " Menu de modération " + "=" * 50 + "\n"
                )
