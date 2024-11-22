import logging

from src.utils.singleton import Singleton

from src.utils.log_decorator import log

from src.dao.db_connection import DBConnection

from src.business_objet.avis import Avis


class AvisDao(metaclass=Singleton):
    def creer(self, avis) -> bool:
        """Creation d'un avis dans la base de données

        Parameters
        ----------
        avis : Avis

        Returns
        -------
        created : bool
            True si la création est un succès
            False sinon
        """
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet.avis(id_manga, id_utilisateur, texte, spoiler) VALUES (%s, %s, %s, %s) RETURNING id_manga, id_utilisateur, texte, spoiler;",
                        (avis.id_manga, avis.id_utilisateur, avis.texte, avis.spoiler),
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.error(f"Erreur lors de la création de l'avis: {e}")
            raise

        print("res=",res)
        created = res is not None
        if created:
            avis.id_manga = res["id_manga"]
            avis.id_utilisateur = res["id_utilisateur"]
            avis.texte = res["texte"]
            avis.avis = res["avis"]

        return created

    @log
    def trouver_tous_par_id(self, id: int) -> list[Avis]:
        """Trouver les avis par son id

        Parameters
        ----------
        id : l'id de l'utilisateur : int

        Returns
        -------
        res_avis : tous les avis de l'utilisateur
        """
        res_avis = []
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * " 
                        "FROM projet.avis " 
                        f"WHERE id_utilisateur = {id}",
                        {"id": id},
                    )
                    avis_rows = cursor.fetchall()
                for row in avis_rows:
                    avis = Avis(
                        id_manga=row["id_manga"],
                        id_utilisateur=row["id_utilisateur"],
                        texte=row["texte"],
                        note=row["note"]
                    )
                    res_avis.append(avis)
            return res_avis

        except Exception as e:
            logging.error(f"Erreur lors de la récupération des avis: {e}")
            return []


    @log
    def trouver_avis_par_manga(self, id_manga: int, include_spoilers=False) -> list[Avis]:
        """Trouver les avis pour un manga

        Parameters
        ----------
        id : l'id du manga : int

        Returns
        -------
        res_avis : tous les avis pour ce manga
        """
        res_avis = []
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    if include_spoilers:
                        cursor.execute(
                            "SELECT * " 
                            "FROM projet.avis " 
                            f"WHERE id_manga = {id_manga}",
                            {"id_manga": id_manga},
                        )
                        avis_rows = cursor.fetchall()
                    else:
                        cursor.execute(
                            "SELECT * " 
                            "FROM projet.avis " 
                            f"WHERE id_manga = {id_manga}"
                            f" AND spoiler = True ;     ",
                            {"id_manga": id_manga},
                        )
                        avis_rows = cursor.fetchall()                        
                for row in avis_rows:
                    avis = Avis(
                        id_manga=row["id_manga"],
                        id_utilisateur=row["id_utilisateur"],
                        texte=row["texte"],
                        note=row["note"]
                    )
                    res_avis.append(avis)
            return res_avis

        except Exception as e:
            logging.error(f"Erreur lors de la récupération des avis: {e}")
            return []
            raise

    @log
    def supprimer_avis(self, avis: Avis) -> bool:
        """Suppression d'un avis dans la base de données

        Parameters
        ----------
        avis : Avis
            avis à supprimer de la base de données

        Returns
        -------
            True si l'avis a bien été supprimé
        """
        L = AvisDao().trouver_tous_par_id(avis.id_utilisateur)
        for avis_exist in L:
            if (avis_exist.id_utilisateur == avis.id_utilisateur) and (avis_exist.id_manga == avis.id_manga) and (avis_exist.note is None):
                try:
                    with DBConnection().connection as connection:
                        with connection.cursor() as cursor:
                            # Supprimer un avis de la base de données
                            cursor.execute(
                                "DELETE FROM projet.avis                  "
                                f" WHERE id_manga={avis.id_manga}      "
                                f" AND id_utilisateur={avis.id_utilisateur} ;     "
                            )
                            res = cursor.rowcount
                except Exception as e:
                    logging.info(e)
                    raise
                return res > 0
            elif (avis_exist.id_utilisateur == avis.id_utilisateur) and (avis_exist.id_manga == avis.id_manga) and (avis_exist.note is not None):
                try:
                    with DBConnection().connection as connection:
                        with connection.cursor() as cursor:
                            cursor.execute(
                                "UPDATE projet.avis                                "
                                f"   SET texte      = NULL        "
                                f" WHERE id_manga = {avis.id_manga}             "
                                f" AND id_utilisateur = {avis.id_utilisateur};             "
                            )
                            res = cursor.rowcount
                            return res == 1

                except Exception as e:
                    logging.info(e)
                    return False

    @log
    def supprimer_note(self, avis: Avis) -> bool:
        """Suppression d'une note dans la base de données

        Parameters
        ----------
        avis : Avis
            avis à supprimer de la base de données

        Returns
        -------
            True si l'avis a bien été supprimé
        """
        L = AvisDao().trouver_tous_par_id(avis.id_utilisateur)
        for avis_exist in L:
            if (avis_exist.id_utilisateur == avis.id_utilisateur) and (avis_exist.id_manga == avis.id_manga) and (avis_exist.texte is None):
                try:
                    with DBConnection().connection as connection:
                        with connection.cursor() as cursor:
                            # Supprimer un avis de la base de données
                            cursor.execute(
                                "DELETE FROM projet.avis                  "
                                f" WHERE id_manga={avis.id_manga}      "
                                f" AND id_utilisateur={avis.id_utilisateur} ;     "
                            )
                            res = cursor.rowcount
                except Exception as e:
                    logging.info(e)
                    raise
                return res > 0
            elif (avis_exist.id_utilisateur == avis.id_utilisateur) and (avis_exist.id_manga == avis.id_manga) and (avis_exist.texte is not None):
                try:
                    with DBConnection().connection as connection:
                        with connection.cursor() as cursor:
                            cursor.execute(
                                "UPDATE projet.avis                                "
                                f"   SET note      = NULL        "
                                f" WHERE id_manga = {avis.id_manga}             "
                                f" AND id_utilisateur = {avis.id_utilisateur};             "
                            )
                            res = cursor.rowcount
                            return res == 1
            

                except Exception as e:
                    logging.info(e)
                return res == 1

    @log
    def modifier(self, avis: Avis, newtexte: str, spoiler=False) -> bool:
        """Modification d'un avis dans la base de données

        Parameters
        ----------
        avis : Avis
        newtexte : str
        spoiler : bool

        Returns
        -------
        created : bool
            True si la modification est un succès
            False sinon
        """

        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE projet.avis                                "
                        f"   SET texte      = '{newtexte}' AND spoiler = {spoiler}        "
                        f" WHERE id_manga = {avis.id_manga}             "
                        f" AND id_utilisateur = {avis.id_utilisateur};             "
                    )
                    res = cursor.rowcount

        except Exception as e:
            logging.info(e)
        return res == 1

    @log
    def noter(self, avis: Avis, note: int) -> bool:
        """Notation d'un manga dans la base de données

        Parameters
        ----------
        avis : Avis
        note: int

        Returns
        -------
        created : bool
            True si la notation est un succès
            False sinon
        """
        L = AvisDao().trouver_tous_par_id(avis.id_utilisateur)
        for avis_exist in L:
            if (avis_exist.id_utilisateur == avis.id_utilisateur) and (avis_exist.id_manga == avis.id_manga) and (avis_exist.note is not None):
                raise ValueError("Une note existe déjà pour ce manga :/")
            elif (avis_exist.id_utilisateur == avis.id_utilisateur) and (avis_exist.id_manga == avis.id_manga) and (avis_exist.note is None):
                try:
                    with DBConnection().connection as connection:
                        with connection.cursor() as cursor:
                            cursor.execute(
                                "UPDATE projet.avis                                "
                                f"   SET note      = '{note}'        "
                                f" WHERE id_manga = {avis.id_manga}             "
                                f" AND id_utilisateur = {avis.id_utilisateur};             "
                            )
                            res = cursor.rowcount
                            return res == 1

                except Exception as e:
                    logging.info(e)
                return res == 1
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projet.avis(id_manga, id_utilisateur, note) VALUES (%s, %s, %s) RETURNING id_manga, id_utilisateur, note;",
                        (avis.id_manga, avis.id_utilisateur, note),
                    )
                    res = cursor.fetchone()
                    return res is not None
        except Exception as e:
            logging.error(f"Erreur lors de la notation: {e}")
            raise

    @log
    def modifier_note(self, avis: Avis, newnote: int) -> bool:
        """Modification d'une note dans la base de données

        Parameters
        ----------
        avis : Avis
        newnote : int

        Returns
        -------
        created : bool
            True si la modification est un succès
            False sinon
        """

        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE projet.avis                                "
                        f"   SET note      = '{newnote}'        "
                        f" WHERE id_manga = {avis.id_manga}             "
                        f" AND id_utilisateur = {avis.id_utilisateur};             "
                    )
                    res = cursor.rowcount

        except Exception as e:
            logging.info(e)
        return res == 1

