nl = {
    "starthandler": {
        "text": "Welkom! Kies een optie:",
        "keyboard": [
            {"text": "Kies kanaalabonnement", "callback_data": "buychannelsubscriptions"},
            {"text": "Kies taal", "callback_data": "select_language"}
        ]
    },
    "selectlanguagehandler": {
        "text": "Selecteer een taal:",
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
        "text": "De taal is gewijzigd naar Nederlands."
    },
    "selectchannelsubscriptionstate": {
        "text": "Selecteer een kanaal:"
    },
    "selectsubscriptionsstate": {
        "text": "Selecteer een abonnement:"
    },
    "selectcryptostate": {
        "text": "Selecteer een cryptovaluta:"
    },
    "sendpaymentlinkstate": {
        "text": "Voer de betaling uit via de onderstaande link:"
    },
    "checkpaymentstatusstate": {
        "text": "Klik op de onderstaande knop om de betalingsstatus te controleren.\nFactuurnummer:",
        "keyboard": [
            {"text": "Controleer betaling", "callback_data": ""}
        ]
    },
    "cancel": {
        "text": "De betaling is geannuleerd of verlopen wegens inactiviteit.\nProbeer het opnieuw."
    },
    "joinrequesthandler": {
        "text": "Verzoek om lid te worden ontvangen. Wacht op goedkeuring."
    },
    "addadminhandler": {
        "text": "Voer de gebruikers-ID in om beheerdersrechten toe te kennen:"
    },
    "addspecialuserhandler": {
        "text": "Voer de gebruikers-ID in om als speciale gebruiker toe te voegen:"
    },
    "banuserhandler": {
        "text": "Voer de gebruikers-ID in om te verbannen:"
    },
    "checkpaymentstatushandler": {
        "text": "Betalingsstatus wordt gecontroleerd. Even geduld..."
    },
    "adminpannelhandler": {
        "text": """
Beheerderspaneel - Commandogids:

1. **Verplicht kanaal toevoegen**: Gebruik `/addjoinforcechannel` om een verplicht kanaal toe te voegen.
2. **Verplicht kanaal verwijderen**: Gebruik `/deletejoinforcechannel` om een verplicht kanaal te verwijderen.
3. **Kanaal toevoegen**: Gebruik `/addchannel` om een nieuw kanaal toe te voegen.
4. **Kanaal verwijderen**: Gebruik `/deletechannel` om een kanaal te verwijderen.
5. **Abonnement toevoegen**: Gebruik `/addsubscription` om een nieuw abonnement toe te voegen.
6. **Abonnement verwijderen**: Gebruik `/deletesubscription` om een abonnement te verwijderen.
7. **Gebruiker verbannen**: Gebruik `/banuser` om een gebruiker te verbannen.
8. **Gebruiker deblokkeren**: Gebruik `/unbanuser` om een gebruiker te deblokkeren.
9. **Beheerder toevoegen**: Gebruik `/addadmin` om beheerdersrechten toe te kennen.
10. **Beheerder verwijderen**: Gebruik `/removeadmin` om beheerdersrechten te verwijderen.
11. **Alle beheerders tonen**: Gebruik `/showalladmin` om alle beheerders weer te geven.
12. **Speciale gebruiker toevoegen**: Gebruik `/addspecialuser` om een gebruiker als speciaal toe te voegen.
13. **Speciale gebruiker verwijderen**: Gebruik `/removespecialuser` om de speciale status te verwijderen.
14. **Exporteer tabel naar CSV**: Gebruik `/exporttabletocsv` om databasegegevens naar CSV te exporteren.

Voer het gewenste commando in:
"""
    },
    "selectchannelsubscriptions": {
        "text": "Selecteer een kanaal:"
    },
    "unbanuserhandler": {
        "text": "Voer de gebruikers-ID in om de ban op te heffen:"
    },
    "removeadminhandler": {
        "text": "Voer de gebruikers-ID in om beheerdersrechten te verwijderen:"
    },
    "showalladminhandler": {
        "text": "Hier is de lijst met alle beheerders in het systeem:"
    },
    "removespecialuserhandler": {
        "text": "Voer de gebruikers-ID in om de speciale status te verwijderen:"
    },
    "exporttabletocsvhandler": {
        "text": "Voer de naam van de tabel in om te exporteren naar CSV:"
    },
    "addforcedjoinchannelhandler": {
        "text": "Voer de gegevens in van het verplichte kanaal dat je wilt toevoegen:"
    },
    "deleteforcedjoinchannelhandler": {
        "text": "Voer de gegevens in van het verplichte kanaal dat je wilt verwijderen:"
    },
    "addchannelhandler": {
        "text": "Voer de gegevens van het toe te voegen kanaal in:"
    },
    "deletechannelhandler": {
        "text": "Voer de gegevens in van het kanaal dat je wilt verwijderen:"
    },
    "addsubscriptionhandler": {
        "text": "Voer de gegevens in van het abonnement dat je wilt toevoegen:"
    },
    "deletesubscriptionhandler": {
        "text": "Voer de gegevens in van het abonnement dat je wilt verwijderen:"
    },
    "forcejoincheckerhandler": {
        "text": "Je moet lid worden van de volgende kanalen en groepen om deze bot te gebruiken:"
    },
    "confirmdeletestate": {
        "text": "Kanaal is succesvol verwijderd."
    },
    "deleteforcedjoinchannelstate": {
        "text": "Selecteer het kanaal dat je wilt verwijderen:"
    },
    "confirmdeletechannelstate": {
        "text": "Kanaal is succesvol verwijderd."
    },
    "deletechannelstate": {
        "text": "Selecteer het kanaal dat je wilt verwijderen:"
    },
    "deletesubscriptionstate": {
        "text": "Selecteer het abonnement dat je wilt verwijderen:"
    },
    "listsubscriptionsstate": {
        "text": "Selecteer een abonnement:"
    },
    "confirmdeleteanotherstate": {
        "text": "Abonnement is verwijderd.\nWil je een ander abonnement verwijderen?"
    },
    "DeleteAnotherSubscriptionState": {
        "text": "Selecteer een abonnement:"
    },
    "showlistoftableshandler": {
        "text":
            "1. Kanalen\n"
            "2. Abonnementen\n"
            "3. Gebruikers-abonnementen\n"
            "4. Speciale gebruikers\n"
            "5. Betalingen\n"
            "6. Verplichte deelname\n"
            "7. Gebruikers"
    },
    "addchannelstate": {
        "text": "Stuur de link van het kanaal:"
    },
    "getchatidstate": {
        "text": "Kanaal succesvol toegevoegd."
    },
    "addforcedjoinchannelstate": {
        "text": "Stuur de link van het verplichte kanaal:"
    },
    "getchannellinkstate": {
        "text": "Kanaal succesvol toegevoegd."
    },
    "getchannelhandler": {
        "text": "Selecteer een kanaal om de gebruiker als speciaal toe te voegen:"
    },
    "addsubscriptionstate": {
        "text": "Selecteer een kanaal:"
    },
    "getnamestate": {
        "text": "Voer de naam van het abonnement in:"
    },
    "getpriceState": {
        "text": "Voer de prijs in (in USD):"
    },
    "getdaystate": {
        "text": "Voer het aantal dagen in voor het abonnement:"
    },
    "confirmaddanotherstate": {
        "text": "Abonnement is aangemaakt. Wil je er nog een toevoegen?"
    },
    "selectsubscriptionstate": {
        "text": "Selecteer een abonnement:"
    }
}
