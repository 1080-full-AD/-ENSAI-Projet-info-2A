from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.collection_service import CollectionVirtuelleService
from src.service.utilisateur_service import UtilisateurService
from src.views.session import Session
from src.views.users.main_collection_view import MainCollectionView


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
                "Consulter vos collections",
                "Consulter les collections d'un utilisateur",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Consulter vos collections":
                user = Session().getuser()
                id_utilisateur = user.id_utilisateur

############################## IL FAUT UN EMETHODE POUR LISTER LES COLLECTIONS DES USER###############################

                return ConsulterCollectionView("\n" + "=" * 50 + " Consultation des collections"
                                    " :) " + "=" * 50 + "\n")

            case "Consulter les collections d'un utilisateur":
                pseudo = inquirer.text(
                 "Entrez le pseudo de l'utilisateur en question :)"
                ).execute()
                try:
                    user = UtilisateurService(
                    ).trouver_par_pseudo_utilisateur(pseudo=pseudo)
                    id_utilisateur = user.id_utilisateur
                except Exception as e:
                    print("\n", e)
############################## IL FAUT UN EMETHODE POUR LISTER LES COLLECTIONS DES USER###############################
                return ConsulterCollectionView("\n" + "=" * 50 + " Consultation des collections"
                                    " :) " + "=" * 50 + "\n")
            case "Retour":
                return MainCollectionView("\n" + "=" * 50 + " Menu des"
                                            " collections " + "=" * 50 + "\n")