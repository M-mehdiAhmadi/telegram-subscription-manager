fr = {
    "starthandler": {
        "text": "Bienvenue ! Veuillez choisir une option :",
        "keyboard": [
            {"text": "Acheter un abonnement à un canal", "callback_data": "buychannelsubscriptions"},
            {"text": "Changer la langue", "callback_data": "select_language"}
        ]
    },
    "selectlanguagehandler": {
        "text": "Veuillez choisir votre langue :",
        "keyboard": [
            {"text": "English", "callback_data": "en"},
            {"text": "فارسی", "callback_data": "fa"},
            {"text": "Español", "callback_data": "es"},
            {"text": "Deutsch", "callback_data": "de"},
            {"text": "Русский", "callback_data": "ru"},
            {"text": "日本語", "callback_data": "ja"},
            {"text": "中文", "callback_data": "zh"},
            {"text": "Français", "callback_data": "fr"},
            {"text": "Türkçe", "callback_data": "tr"},
            {"text": "Italiano", "callback_data": "it"},
            {"text": "Português", "callback_data": "pt"},
            {"text": "Nederlands", "callback_data": "nl"}
        ]
    },
    "setlanguagehandler": {"text": "Votre langue a été changée en français."},
    "selectchannelsubscriptionstate": {"text": "Veuillez sélectionner votre canal :"},
    "selectsubscriptionsstate": {"text": "Veuillez sélectionner le type d’abonnement :"},
    "selectcryptostate": {"text": "Veuillez choisir votre cryptomonnaie :"},
    "sendpaymentlinkstate": {"text": "Veuillez utiliser le lien suivant pour effectuer le paiement :"},
    "checkpaymentstatusstate": {
        "text": "Cliquez sur le bouton ci-dessous pour vérifier l’état de votre paiement.\nID de la facture :",
        "keyboard": [{"text": "Vérifier l’état du paiement", "callback_data": ""}]
    },
    "cancel": {"text": "Votre paiement a été annulé ou a expiré en raison de l'inactivité.\nVeuillez réessayer."},
    "joinrequesthandler": {"text": "Votre demande d’adhésion a été reçue. Veuillez attendre l’approbation."},
    "addadminhandler": {"text": "Veuillez entrer l’identifiant de l’utilisateur à qui attribuer les droits administrateur."},
    "addspecialuserhandler": {"text": "Veuillez entrer l’identifiant de l’utilisateur à marquer comme spécial."},
    "banuserhandler": {"text": "Veuillez entrer l’identifiant de l’utilisateur à bloquer."},
    "checkpaymentstatushandler": {"text": "Vérification de l’état du paiement en cours. Veuillez patienter..."},
    "adminpannelhandler": {
        "text": """
Liste des commandes d’administration :

1. **Ajouter un canal obligatoire** : /addjoinforcechannel
2. **Supprimer un canal obligatoire** : /deletejoinforcechannel
3. **Ajouter un canal** : /addchannel
4. **Supprimer un canal** : /deletechannel
5. **Ajouter un abonnement** : /addsubscription
6. **Supprimer un abonnement** : /deletesubscription
7. **Bloquer un utilisateur** : /banuser
8. **Débloquer un utilisateur** : /unbanuser
9. **Ajouter un administrateur** : /addadmin
10. **Supprimer un administrateur** : /removeadmin
11. **Afficher tous les administrateurs** : /showalladmin
12. **Ajouter un utilisateur spécial** : /addspecialuser
13. **Supprimer un utilisateur spécial** : /removespecialuser
14. **Exporter une table en CSV** : /exporttabletocsv

Veuillez entrer la commande correspondante à l’action souhaitée.
"""
    },
    "selectchannelsubscriptions": {"text": "Veuillez sélectionner votre canal :"},
    "unbanuserhandler": {"text": "Veuillez entrer l’identifiant de l’utilisateur à débloquer."},
    "removeadminhandler": {"text": "Veuillez entrer l’identifiant de l’utilisateur à retirer des administrateurs."},
    "showalladminhandler": {"text": "Voici la liste de tous les administrateurs du système :"},
    "removespecialuserhandler": {"text": "Veuillez entrer l’identifiant de l’utilisateur à retirer de la liste spéciale."},
    "exporttabletocsvhandler": {"text": "Veuillez indiquer le nom de la table à exporter au format CSV."},
    "addforcedjoinchannelhandler": {"text": "Veuillez entrer les détails du canal à ajouter comme canal obligatoire."},
    "deleteforcedjoinchannelhandler": {"text": "Veuillez entrer les détails du canal à supprimer de la liste obligatoire."},
    "addchannelhandler": {"text": "Veuillez entrer les détails du canal à ajouter."},
    "deletechannelhandler": {"text": "Veuillez entrer les détails du canal à supprimer."},
    "addsubscriptionhandler": {"text": "Veuillez entrer les détails de l’abonnement à ajouter."},
    "deletesubscriptionhandler": {"text": "Veuillez entrer les détails de l’abonnement à supprimer."},
    "forcejoincheckerhandler": {"text": "Vérification de l’adhésion au canal en cours..."},
    "confirmdeletestate": {"text": "Êtes-vous sûr de vouloir supprimer cela ?"},
    "deleteforcedjoinchannelstate": {"text": "Sélectionnez le canal obligatoire à supprimer :"},
    "confirmdeletechannelstate": {"text": "Confirmez-vous la suppression de ce canal ?"},
    "deletechannelstate": {"text": "Sélectionnez le canal à supprimer :"},
    "deletesubscriptionstate": {"text": "Sélectionnez l’abonnement à supprimer :"},
    "listsubscriptionsstate": {"text": "Voici la liste de tous les abonnements disponibles :"},
    "confirmdeleteanotherstate": {"text": "Voulez-vous supprimer un autre abonnement ?"},
    "DeleteAnotherSubscriptionState": {"text": "Voulez-vous en supprimer un autre ?"},
    "showlistoftableshandler": {"text": "Voici la liste des tables disponibles :"},
    "addchannelstate": {"text": "Entrez les détails du canal à ajouter :"},
    "getchatidstate": {"text": "Entrez l’ID du chat du canal :"},
    "addforcedjoinchannelstate": {"text": "Entrez les détails du canal obligatoire à ajouter :"},
    "getchannellinkstate": {"text": "Entrez le lien du canal :"},
    "getchannelhandler": {"text": "Récupération des informations du canal..."},
    "addsubscriptionstate": {"text": "Entrez les détails de l’abonnement à ajouter :"},
    "getnamestate": {"text": "Entrez le nom de l’abonnement :"},
    "getpriceState": {"text": "Entrez le prix de l’abonnement :"},
    "getdaystate": {"text": "Entrez la durée (en jours) de l’abonnement :"},
    "confirmaddanotherstate": {"text": "Souhaitez-vous en ajouter un autre ?"},
    "selectsubscriptionstate": {"text": "Veuillez choisir un abonnement :"}
}
