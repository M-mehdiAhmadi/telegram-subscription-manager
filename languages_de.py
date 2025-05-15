de = {
    "starthandler": {
        "text": "Willkommen! Bitte wähle eine Option:",
        "keyboard": [
            {"text": "Kanal-Abonnement auswählen", "callback_data": "buychannelsubscriptions"},
            {"text": "Sprache ändern", "callback_data": "select_language"}
        ]
    },
    "selectlanguagehandler": {
        "text": "Bitte wähle deine Sprache:",
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
    "setlanguagehandler": {
        "text": "Deine Sprache wurde auf Deutsch geändert."
    },
    "selectchannelsubscriptionstate": {
        "text": "Wähle deinen Kanal:"
    },
    "selectsubscriptionsstate": {
        "text": "Wähle dein Abonnement:"
    },
    "selectcryptostate": {
        "text": "Wähle deine Kryptowährung:"
    },
    "sendpaymentlinkstate": {
        "text": "Nutze den folgenden Link zur Bezahlung:"
    },
    "checkpaymentstatusstate": {
        "text": "Klicke auf den untenstehenden Button, um den Zahlungsstatus zu prüfen.\nRechnungs-ID:",
        "keyboard": [
            {"text": "Zahlungsstatus prüfen", "callback_data": ""}
        ]
    },
    "cancel": {
        "text": "Deine Zahlung wurde aufgrund von Inaktivität abgebrochen oder ist abgelaufen.\nBitte versuche es erneut."
    },
    "joinrequesthandler": {
        "text": "Deine Beitrittsanfrage wurde erhalten. Bitte warte auf die Genehmigung."
    },
    "addadminhandler": {
        "text": "Bitte gib die Benutzer-ID ein, um Adminrechte zu vergeben."
    },
    "addspecialuserhandler": {
        "text": "Bitte gib die Benutzer-ID ein, um ihn/sie als besonders zu markieren."
    },
    "banuserhandler": {
        "text": "Bitte gib die Benutzer-ID ein, um den Benutzer zu sperren."
    },
    "checkpaymentstatushandler": {
        "text": "Zahlungsstatus wird überprüft. Bitte warte..."
    },
    "adminpannelhandler": {
        "text": """
Admin-Befehlsübersicht:

1. **Zwangsbeitrittskanal hinzufügen**: `/addjoinforcechannel`
2. **Zwangsbeitrittskanal entfernen**: `/deletejoinforcechannel`
3. **Kanal hinzufügen**: `/addchannel`
4. **Kanal löschen**: `/deletechannel`
5. **Abonnement hinzufügen**: `/addsubscription`
6. **Abonnement löschen**: `/deletesubscription`
7. **Benutzer sperren**: `/banuser`
8. **Benutzer entsperren**: `/unbanuser`
9. **Admin hinzufügen**: `/addadmin`
10. **Admin entfernen**: `/removeadmin`
11. **Alle Admins anzeigen**: `/showalladmin`
12. **Spezialbenutzer hinzufügen**: `/addspecialuser`
13. **Spezialbenutzer entfernen**: `/removespecialuser`
14. **Tabelle als CSV exportieren**: `/exporttabletocsv`

Gib den entsprechenden Befehl ein, um die gewünschte Aktion auszuführen.
"""
    },
    "selectchannelsubscriptions": {
        "text": "Bitte wähle deinen Kanal:"
    },
    "unbanuserhandler": {
        "text": "Bitte gib die Benutzer-ID ein, um die Sperrung aufzuheben."
    },
    "removeadminhandler": {
        "text": "Bitte gib die Benutzer-ID ein, um Adminrechte zu entziehen."
    },
    "showalladminhandler": {
        "text": "Hier ist die Liste aller Admins im System:"
    },
    "removespecialuserhandler": {
        "text": "Bitte gib die Benutzer-ID ein, um den Spezialstatus zu entfernen."
    },
    "exporttabletocsvhandler": {
        "text": "Bitte gib den Tabellennamen an, den du als CSV exportieren möchtest."
    },
    "addforcedjoinchannelhandler": {
        "text": "Bitte gib die Details des Kanals ein, der als Zwangsbeitritt hinzugefügt werden soll."
    },
    "deleteforcedjoinchannelhandler": {
        "text": "Bitte gib die Details des Kanals ein, der aus dem Zwangsbeitritt entfernt werden soll."
    },
    "addchannelhandler": {
        "text": "Bitte gib die Details des hinzuzufügenden Kanals ein."
    },
    "deletechannelhandler": {
        "text": "Bitte gib die Details des zu löschenden Kanals ein."
    },
    "addsubscriptionhandler": {
        "text": "Bitte gib die Details des hinzuzufügenden Abonnements ein."
    },
    "deletesubscriptionhandler": {
        "text": "Bitte gib die Details des zu löschenden Abonnements ein."
    },
    "forcejoincheckerhandler": {
        "text": "Bitte trete zuerst dem Pflichtkanal bei, bevor du fortfährst."
    },
    "confirmdeletestate": {
        "text": "Bist du sicher, dass du dies löschen möchtest?"
    },
    "deleteforcedjoinchannelstate": {
        "text": "Zwangsbeitrittskanal wird gelöscht..."
    },
    "confirmdeletechannelstate": {
        "text": "Bist du sicher, dass du diesen Kanal löschen möchtest?"
    },
    "deletechannelstate": {
        "text": "Kanal wird gelöscht..."
    },
    "deletesubscriptionstate": {
        "text": "Abonnement wird gelöscht..."
    },
    "listsubscriptionsstate": {
        "text": "Liste der verfügbaren Abonnements:"
    },
    "confirmdeleteanotherstate": {
        "text": "Möchtest du ein weiteres Abonnement löschen?"
    },
    "DeleteAnotherSubscriptionState": {
        "text": "Bitte wähle ein weiteres Abonnement zum Löschen."
    },
    "showlistoftableshandler": {
        "text": "Hier ist die Liste der verfügbaren Tabellen:"
    },
    "addchannelstate": {
        "text": "Bitte gib den Kanalnamen ein, den du hinzufügen möchtest:"
    },
    "getchatidstate": {
        "text": "Bitte gib die Chat-ID des Kanals ein:"
    },
    "addforcedjoinchannelstate": {
        "text": "Bitte gib den Namen des Pflichtkanals ein, den du hinzufügen möchtest:"
    },
    "getchannellinkstate": {
        "text": "Bitte gib den Einladungslink des Kanals ein:"
    },
    "getchannelhandler": {
        "text": "Gib die Kanal-ID oder den Benutzernamen ein, um Details zu erhalten:"
    },
    "addsubscriptionstate": {
        "text": "Bitte gib den Namen des neuen Abonnements ein:"
    },
    "getnamestate": {
        "text": "Bitte gib den Namen ein:"
    },
    "getpriceState": {
        "text": "Bitte gib den Preis in USD ein:"
    },
    "getdaystate": {
        "text": "Bitte gib die Gültigkeitsdauer in Tagen ein:"
    },
    "confirmaddanotherstate": {
        "text": "Möchtest du ein weiteres Abonnement hinzufügen?"
    },
    "selectsubscriptionstate": {
        "text": "Bitte wähle ein Abonnement aus:"
    }
}

