from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.collection_service import CollectionVirtuelleService
from src.service.manga_service import MangaService
from src.views.session import Session
from src.views.users.main_collection_view import MainCollectionView


class ModificationCollectionView(AbstractView):
    """Menu principal des avis"""

    def choisir_menu(self):
        """Choix du menu suivant

        Return
        ------
        view
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        titre = inquirer.text(
            message="Bonnez le titre de la collection que vous souhaitez modifier :)",
        ).execute()

        user = Session().getuser()
        id_utilisateur = user.id_utilisateur

        try:
            collection = CollectionVirtuelleService().trouverMACHIN(titre, id_utilisateur)
#############METHODE POUR AVOIR ACC7S A UNE COLLECTION AVEC LE TITRE ET LID DE LUSER#######################
        except Exception as e:
            print("\n", e)
            return ModificationCollectionView("\n" + "=" * 50 + " Modification de collection"
                                         " :) " + "=" * 50 + "\n")


        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                f"Modifier le titre de NOM COLLECTION",
                f"Modifier la dscription de NOM COLLECTION",
                f"Ajouter un manga a NOM COLLECTION",
                f"Enlever un manga a NOM COLLECTION",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Modifier le titre de NOM COLLECTION":
                texte = inquirer.text(
                    "Rédigez votre nouvel avis :)"
                ).execute()

                AvisService().creer(id_manga=id_manga,
                                    id_utilisateur=id_utilisateur, texte=texte)
                from src.views.users.main_opinion_view import MainOpinionView

                return MainOpinionView("\n" + "=" * 50 + " Menu des avis"
                                       " :) " + "=" * 50 + "\n")
            
            case "Modifier la dscription de NOM COLLECTION":

                note = int(inquirer.number(
                    f"Donnez votre nouvelle note à {manga.titre_manga} :)",
                    min_allowed=0,
                    max_allowed=5
                ).execute())
                AvisService().noter(id_manga=id_manga,
                                    id_utilisateur=id_utilisateur, note=note)

                from src.views.users.main_opinion_view import MainOpinionView

                return MainOpinionView("\n" + "=" * 50 + " Menu des avis"
                                       " :) " + "=" * 50 + "\n")

            case "Ajouter un manga a NOM COLLECTION":
                
                note = int(inquirer.number(
                    f"Donnez votre nouvelle note à {manga.titre_manga} :)",
                    min_allowed=0,
                    max_allowed=5
                ).execute())
                AvisService().noter(id_manga=id_manga,
                                    id_utilisateur=id_utilisateur, note=note)

                from src.views.users.main_opinion_view import MainOpinionView

                return MainOpinionView("\n" + "=" * 50 + " Menu des avis"
                                       " :) " + "=" * 50 + "\n")

            case "Enlever un manga a NOM COLLECTION":
                
                note = int(inquirer.number(
                    f"Donnez votre nouvelle note à {manga.titre_manga} :)",
                    min_allowed=0,
                    max_allowed=5
                ).execute())
                AvisService().noter(id_manga=id_manga,
                                    id_utilisateur=id_utilisateur, note=note)

                from src.views.users.main_opinion_view import MainOpinionView

                return MainOpinionView("\n" + "=" * 50 + " Menu des avis"
                                       " :) " + "=" * 50 + "\n")

            case "Retour":
                from src.views.users.main_opinion_view import MainOpinionView

                return MainOpinionView("\n" + "=" * 50 + " Menu des avis"
                                       " :) " + "=" * 50 + "\n")
