import logging

from src.utils.log_decorator import log

from src.service.utilisateur_service import UtilisateurService

from src.business_objet.utilisateur import Utilisateur

class UtilisateurClient:
    @log
    def __init__(self, utilisateur_service):
        self.utilisateur_service = utilisateur_service

    @log
    def creer(self, pseudo, mdp, age, collections):
        utilisateur = Utilisateur(pseudo=pseudo, mdp=mdp, age=age, collections=collections)
        if self.UtilisateurService.creer(utilisateur):
            print(f"Utilisateur {pseudo} créé avec succès.")
        else:
            print(f"Erreur lors de la création de l'utilisateur {pseudo}.")

    @log
    def trouver_par_pseudo(self, pseudo):
        utilisateur = self.UtilisateurService.trouver_par_pseudo(pseudo)
        if utilisateur:
            print(f"Utilisateur trouvé : {utilisateur}")
        else:
            print(f"Utilisateur avec le pseudo {pseudo} non trouvé.")
        return utilisateur

    @log
    def lister_tous(self):
        utilisateurs = self.UtilisateurService.lister_tous()
        print(f"Liste de tous les utilisateurs :")
        for utilisateur in utilisateurs:
            print(utilisateur)
        return utilisateurs

    @log
    def modifier(self, utilisateur_id, pseudo, mdp, age, collections):
        utilisateur = Utilisateur(id_utilisateur=utilisateur_id, pseudo=pseudo, mdp=mdp, age=age, collections=collections)
        if self.UtilisateurService.modifier(utilisateur):
            print(f"Utilisateur {pseudo} modifié avec succès.")
        else:
            print(f"Erreur lors de la modification de l'utilisateur {pseudo}.")

    @log
    def supprimer(self, utilisateur_id):
        if self.UtilisateurService.supprimer(utilisateur_id):
            print(f"Utilisateur avec l'ID {utilisateur_id} supprimé avec succès.")
        else:
            print(f"Erreur lors de la suppression de l'utilisateur avec l'ID {utilisateur_id}.")
