from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.collection_service import CollectionVirtuelleService
from src.service.manga_pysique_service import MangaPhysiqueService
from src.views.session import Session
from src.views.users.main_collection_view import MainCollectionView


class SupprimerMangathequeView(AbstractView):
    """Menu principal des avis"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        titre = inquirer.text(
            message="Donnez le titre du manga pour lequel que vous souhaitez supprimer la mangathèque :)",
        ).execute()

        user = Session().getuser()
        id_utilisateur = user.id_utilisateur

        try:
            ######################## IL FAUT LA METHODE POUR TROUUVER LES MANGATHEQUE################################
            MangaPhysiqueService().supprimer_manga_physique(mangatheque)
        except Exception as e:
            print("\n", e)

        return MainCollectionView(
            "\n" + "=" * 50 + " Menu des collection" " :) " + "=" * 50 + "\n"
        )
