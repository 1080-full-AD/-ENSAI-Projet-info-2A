import logging

from utils.singleton import Singleton

from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.avis import Avis


class AvisDAO(metaclass=Singleton):
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
                        "INSERT INTO manga(id_manga, id_utilisateur, texte)VALUES"
                        "(%(id_manga)s, %(id_utilisateur)s, %(texte)s)         "
                        "  RETURNING id_manga, id_utilisateur, texte;                    ",
                        {
                            "id_manga": avis.id_manga,
                            "id_utilisateur": avis.id_utilisateur,
                            "avis": avis.texte
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            avis.id_manga = res["id_manga"]
            avis.id_utilisateur = res["id_utilisateur"]
            avis.texte = res["texte"]
            created = True

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
                        "SELECT *,"
                        "FROM avis"
                        "WHERE id_utilisateur = %(id)s",
                        {"id":id}
                        )
                    avis_rows = cursor.fetchall()
                for row in avis_rows:
                    avis = Avis(
                        id_manga=row["id_manga"],
                        id_utilisateur=row["id_utilisateur"],
                        texte=row["texte"]
                        )
                    res_avis.append(avis)
                
        except Exception as e:
            logging.error(f"Erreur lors de la récupération des avis: {e}")
            raise

    @log        
    def supprimer_avis(self, avis) -> bool:
        """Suppression d'un avis dans la base de données

        Parameters
        ----------
        avis : Avis
            avis à supprimer de la base de données

        Returns
        -------
            True si l'avis a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer un manga de la base de données
                    cursor.execute(
                        "DELETE FROM avis                  "
                        " WHERE id_manga=%(id_manga)s      ",
                        " AND id_utilisateur=%(id_utilisateur)s      ",
                        {"id_manga": avis.id_manga,
                         "id_utilisateur": avis.id_utilisateur},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0
    
    @log
    def modifier(self, avis, texte: str) -> bool:
        """Modification d'un avis dans la base de données

        Parameters
        ----------
        manga : Avis

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
                        "UPDATE avis                                "
                        "   SET texte      = %(texte)s,        "
                        " WHERE id_manga = %(id_manga)s,             ",
                        " AND id_utilisateur = %(id_utilisateur)s;             ",
                        {
                            "id_manga": avis.id_manga,
                            "id_utilisateur": avis.id_utilisateur,
                            "texte": texte
                        }
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res == 1
