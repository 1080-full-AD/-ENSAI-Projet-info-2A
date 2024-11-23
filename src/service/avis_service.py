from src.dao.avis_dao import AvisDao
from src.dao.manga_dao import MangaDao
from src.business_objet.avis import Avis


class AvisService:
    def creer(
        self, id_manga: int, id_utilisateur: int, texte: str, spoiler=False
    ) -> bool:
        """Création d'un avis

        Parameters
        ----------
        id_manga : int
        id_utilisateur : int
        texte : str

        Returns
        -------
        bool
            True si l'avis a été créé avec succès, False sinon
        """
        if isinstance(id_manga, int) is False:
            raise TypeError(
                "L'identifiant du manga doit être un entier :/"
                )
        if isinstance(id_utilisateur, int) is False:
            raise TypeError(
                "L'identifiant de l'utilisateur doit être un entier :/"
                )
        if isinstance(texte, str) is False:
            raise TypeError(
                "L'avis doit être une chaîne de caractère :/"
                )

        avisuser = AvisService().trouver_tous_par_id(id_utilisateur)
        for i in avisuser:
            if i.id_manga == id_manga and i.texte is not None:
                raise ValueError(
                    "Vous avez déjà donné un avis sur ce manga."
                    " Si vous souhaitez le modifier,"
                    " sélectionnez le menu modifier :)"
                )

        avis = Avis(
            id_manga=id_manga,
            id_utilisateur=id_utilisateur,
            texte=texte,
            spoiler=spoiler,
        )
        res = AvisDao().creer(avis)
        print("Votre avis a bien été créé :)")
        return res

    def trouver_tous_par_id(
        self, id_utilisateur: int, include_spoilers=True
    ) -> list[Avis]:
        """Trouver les avis d'un utilisateur

        Parameters
        ----------
        id_utilisateur : int

        Returns
        -------
        list[Avis]
            Liste des avis de l'utilisateur
        """

        return AvisDao().trouver_tous_par_id(
            id_utilisateur, 
            include_spoilers
            )

    def trouver_avis_par_manga(
        self, id_manga: int, include_spoilers=True
    ) -> list[Avis]:
        """Trouver les avis pour un manga

        Parameters
        ----------
        id_manga : int

        Returns
        -------
        list[Avis]
            Liste des avis pour ce manga
        """
        if MangaDao().trouver_par_id(id_manga) is None:
            raise ValueError(
                "Auncun manga ne possède ce nom :/"
                )
        elif AvisDao().trouver_avis_par_manga(
            id_manga, 
            include_spoilers
            ) == []:
            raise ValueError(
                "Auncun avis à afficher pour ce manga :/"
                )
        else:
            return AvisDao().trouver_avis_par_manga(
                id_manga, 
                include_spoilers
                )

    def supprimer_avis(self, id_manga: int, id_utilisateur: int) -> bool:
        """Supprimer un avis

        Parameters
        ----------
        id_manga : int
        id_utilisateur : int

        Returns
        -------
        bool
            True si l'avis a été supprimé avec succès, False sinon
        """
        if isinstance(id_manga, int) is False:
            raise TypeError(
                "L'identifiant du manga doit être un entier :/"
                )
        if isinstance(id_utilisateur, int) is False:
            raise TypeError(
                "L'identifiant de l'utilisateur doit être un entier :/"
                )

        avisuser = AvisService().trouver_tous_par_id(id_utilisateur)
        for i in avisuser:
            if i.id_manga == id_manga and i.texte is not None:
                avis = Avis(
                    id_manga=id_manga, 
                    id_utilisateur=id_utilisateur, 
                    texte=""
                    )
                print("Votre avis a bien été supprimé :)")
                return AvisDao().supprimer_avis(avis)

            else:
                raise ValueError(
                    "Vous n'avez pas donné d'avis sur ce manga :/"
                    )
        return False

    def supprimer_note(
        self, id_manga: int, id_utilisateur: int
    ) -> bool:
        """Supprimer une note

        Parameters
        ----------
        id_manga : int
        id_utilisateur : int

        Returns
        -------
        bool
            True si l'avis a été supprimé avec succès, False sinon
        """
        if isinstance(id_manga, int) is False:
            raise TypeError(
                "L'identifiant du manga doit être un entier :/"
                )
        if isinstance(id_utilisateur, int) is False:
            raise TypeError(
                "L'identifiant de l'utilisateur doit être un entier :/"
                )

        avisuser = AvisService().trouver_tous_par_id(id_utilisateur)
        for i in avisuser:
            if i.id_manga == id_manga and i.note is not None:
                avis = Avis(
                    id_manga=id_manga, 
                    id_utilisateur=id_utilisateur, 
                    texte="")
                print("Votre note a bien été supprimée :)")
                return AvisDao().supprimer_note(avis)

            else:
                raise ValueError(
                    "Vous n'avez pas donné de note sur ce manga :/"
                    )

    def modifier(
        self, id_manga: int, id_utilisateur: int, newtexte: str, spoiler=False
    ) -> bool:
        """Modifier un avis

        Parameters
        ----------
        id_manga : int
        id_utilisateur : int
        newtexte : str

        Returns
        -------
        bool
            True si la modification a été un succès, False sinon
        """
        if isinstance(id_manga, int) is False:
            raise TypeError(
                "L'identifiant du manga doit être un entier :/"
                )
        if isinstance(id_utilisateur, int) is False:
            raise TypeError(
                "L'identifiant de l'utilisateur doit être un entier :/"
                )
        if isinstance(newtexte, str) is False:
            raise TypeError(
                "L'avis doit être une chaîne de caractère :/"
                )

        avisuser = AvisService().trouver_tous_par_id(id_utilisateur)
        for i in avisuser:
            if i.id_manga == id_manga and i.texte is not None:
                avis = Avis(
                    id_manga=id_manga, 
                    id_utilisateur=id_utilisateur, 
                    texte=""
                    )
                print("Votre avis a bien été modifié :)")
                return AvisDao().modifier(avis, newtexte, spoiler)

            else:
                raise ValueError(
                    "Vous n'avez pas donné d'avis sur ce manga."
                    " Si vous souhaitez en créer un,"
                    " sélectionnez le menu Rédiger un avis/donner"
                    " une note :)"
                )

    def noter(
        self, id_manga: int, id_utilisateur: int, note: int
    ) -> bool:
        """Noter un manga

        Parameters
        ----------
        id_manga : int
        id_utilisateur : int
        note : int

        Returns
        -------
        bool
            True si la modification a été un succès, False sinon
        """
        if isinstance(id_manga, int) is False:
            raise TypeError(
                "L'identifiant du manga doit être un entier :/"
                )
        if isinstance(id_utilisateur, int) is False:
            raise TypeError(
                "L'identifiant de l'utilisateur doit être un entier :/"
                )
        if isinstance(note, int) is False:
            raise TypeError(
                "La note doit êre un entier :/"
                )
        if note < 0 or note > 5:
            raise ValueError(
                "Même si vous avez beaucoup apprécié (ou détesté)"
                " ce manga, la note doit être comprise entre 0 et 5 :)"
            )

        avisuser = AvisService().trouver_tous_par_id(id_utilisateur)
        for i in avisuser:
            if i.id_manga == id_manga and i.note is not None:
                raise ValueError(
                    "Vous avez déjà donné noté ce manga."
                    " Si vous souhaitez la modifier,"
                    " sélectionnez le menu modifier :)"
                )

        avis = Avis(
            id_manga=id_manga, id_utilisateur=id_utilisateur, texte=""
            )
        print("Votre note a bien été ajoutée :)")
        return AvisDao().noter(avis, note)

    def modifier_note(
        self, id_manga: int, id_utilisateur: int, newnote: int
    ) -> bool:
        """Modifier une note

        Parameters
        ----------
        id_manga : int
        id_utilisateur : int
        newnote : int

        Returns
        -------
        bool
            True si la modification a été un succès, False sinon
        """
        if isinstance(id_manga, int) is False:
            raise TypeError(
                "L'identifiant du manga doit être un entier :/"
                )
        if isinstance(id_utilisateur, int) is False:
            raise TypeError(
                "L'identifiant de l'utilisateur doit être un entier :/"
                )
        if isinstance(newnote, int) is False:
            raise TypeError("La note doit être un entier :/")

        avisuser = AvisService().trouver_tous_par_id(id_utilisateur)
        for i in avisuser:
            if i.id_manga == id_manga and i.note is not None:
                avis = Avis(
                    id_manga=id_manga, 
                    id_utilisateur=id_utilisateur, 
                    texte=""
                    )
                print("Votre note a bien été modifiée :)")
                return AvisDao().modifier_note(avis, newnote)

            else:
                raise ValueError(
                    "Vous n'avez pas donné de note à ce manga."
                    " Si vous souhaitez en donner une,"
                    " sélectionnez le menu Rédiger un avis/donner"
                    " une note :)"
                )
