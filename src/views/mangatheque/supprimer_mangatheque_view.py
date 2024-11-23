from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.collection_service import CollectionVirtuelleService
from src.service.manga_physique_service import MangaPhysiqueService
from src.service.manga_service import MangaService
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

        try:
            manga = MangaService().rechercher_un_manga(titre_manga=titre)

            user = Session().getuser()
            id_utilisateur = user.id_utilisateur

            L = MangaPhysiqueService().rechercher_manga_physique(id_utilisateur=id_utilisateur, id_manga=manga.id_manga)
            MangaPhysiqueService().supprimer_manga_physique(L)

        except Exception as e:
            print("\n", e)

        return MainCollectionView(
            "\n" + "=" * 50 + " Menu des collection" " :) " + "=" * 50 + "\n"
        )
