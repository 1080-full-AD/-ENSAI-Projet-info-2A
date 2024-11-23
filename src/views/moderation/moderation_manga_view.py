from InquirerPy import inquirer
from src.views.abstract_view import AbstractView
from src.service.manga_service import MangaService
from src.business_objet.manga import Manga


class ModerationMangaView(AbstractView):
    """Menu principal des collections"""

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
                "Ajouter un manga",
                "Supprimer un manga",
                "Modifier un manga",
                "Gestion des collections",
                "Retour",
            ],
        ).execute()

        match choix:
            case "Ajouter un manga":
                titre_manga = inquirer.text(message="Entrez le titre du manga").execute()
                auteurs = inquirer.text(message="Entrez le(s) auteur(s) du manga").execute()
                nb_volumes = int(inquirer.number(message="Entrez le nombre de volumes").execute())
                nb_chapitres = int(inquirer.number(message="Entrez le nombre de chapitres").execute())
                id_manga= 99
                synopsis = inquirer.text(message="Entrez le synopsis").execute()
                manga = Manga(id_manga=id_manga, titre_manga=titre_manga, auteurs=auteurs, synopsis=synopsis, nb_volumes=nb_volumes, nb_chapitres=nb_chapitres)
                try:
                    MangaService().creer_manga(manga)
                except Exception as e:
                    print("\n", e)
            
                return ModerationMangaView("\n" + "=" * 50 + " Modération de manga "
                                      + "=" * 50 + "\n")

            case "Supprimer un manga":
                id_manga = int(inquirer.number(message="Entrez l'identifiant du manga à supprimer").execute())
                supp = inquirer.confirm(message="Confirmer ?").execute()
                try:
                    if supp is True:
                        manga = MangaService().rechercher_un_id_manga(id_manga=id_manga)
                        s = manga.__str__()
                        print(s)
                        MangaService().supprimer_un_manga(manga=manga)
                except Exception as e:
                    print("\n", e)

                return ModerationMangaView("\n" + "=" * 50 + " Modération de manga "
                                      + "=" * 50 + "\n")

            case "Modifier un manga":
                id_manga = int(inquirer.number(message="Entrez l'identifiant du manga à modifier").execute())
                manga = MangaService().rechercher_un_id_manga(id_manga=id_manga)
                modif = inquirer.select(
                    message="Choisissez l'atribut à modifier",
                    choices=[
                        "Titre",
                        "Synopsis",
                        "Auteur(s)",
                        "Nombre de volumes",
                        "Nombre de chapitres"
                    ]
                ).execute()
                match modif:
                    case "Titre":
                        new_titre = inquirer.text("Entrez le nouveau titre").execute()
                        manga.titre = new_titre
                        mod = inquirer.confirm(message="Confirmer ?").execute()
                        if mod is True:
                            try:
                                MangaService().modifier_un_manga(manga=manga)
                            except Exception as e:
                                print("\n", e)

                        return ModerationMangaView("\n" + "=" * 50 + " Modération de manga "
                                            + "=" * 50 + "\n")


            case "Consulter les mangathèques":
                from src.views.collection.consulter_mangatheque_view import ConsulterMangathequeView

                return ConsulterMangathequeView("\n" + "=" * 50 + " Consultation des collections"
                                         " :) " + "=" * 50 + "\n")
            case "Retour":
                from src.views.users.main_user_view import MainUserView

                return MainUserView("Retour au menu utilisateur :)")
