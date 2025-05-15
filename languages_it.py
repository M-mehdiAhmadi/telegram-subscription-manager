it = {
    "starthandler": {
        "text": "Benvenuto! Seleziona un'opzione:",
        "keyboard": [
            {"text": "Seleziona abbonamenti ai canali", "callback_data": "buychannelsubscriptions"},
            {"text": "Seleziona lingua", "callback_data": "select_language"}
        ]
    },
    "selectlanguagehandler": {
        "text": "Seleziona una lingua:",
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
        "text": "La tua lingua è stata cambiata in italiano."
    },
    "selectchannelsubscriptionstate": {
        "text": "Scegli il tuo canale."
    },
    "selectsubscriptionsstate": {
        "text": "Scegli il tuo abbonamento."
    },
    "selectcryptostate": {
        "text": "Scegli la tua criptovaluta."
    },
    "sendpaymentlinkstate": {
        "text": "Utilizza il link qui sotto per pagare."
    },
    "checkpaymentstatusstate": {
        "text": "Clicca sul pulsante qui sotto per controllare lo stato del pagamento.\nID della fattura:",
        "keyboard": [
            {"text": "Controlla lo stato del pagamento", "callback_data": ""}
        ]
    },
    "cancel": {
        "text": "Il pagamento è stato annullato o è scaduto per inattività.\nPer favore, riprova."
    },
    "joinrequesthandler": {
        "text": "La tua richiesta di accesso è stata ricevuta. Attendi l'approvazione."
    },
    "addadminhandler": {
        "text": "Inserisci l'ID utente a cui assegnare i privilegi di amministratore."
    },
    "addspecialuserhandler": {
        "text": "Inserisci l'ID utente da contrassegnare come speciale."
    },
    "banuserhandler": {
        "text": "Inserisci l'ID utente da bannare."
    },
    "checkpaymentstatushandler": {
        "text": "Verifica in corso dello stato del pagamento. Attendere prego..."
    },
    "adminpannelhandler": {
        "text": """
Guida ai comandi del pannello amministratore:

1. **Aggiungi canale obbligatorio**: Usa `/addjoinforcechannel` per aggiungere un canale che gli utenti devono seguire.
2. **Rimuovi canale obbligatorio**: Usa `/deletejoinforcechannel` per rimuovere un canale obbligatorio.
3. **Aggiungi canale**: Usa `/addchannel` per aggiungere un nuovo canale.
4. **Elimina canale**: Usa `/deletechannel` per eliminare un canale esistente.
5. **Aggiungi abbonamento**: Usa `/addsubscription` per creare un nuovo abbonamento.
6. **Elimina abbonamento**: Usa `/deletesubscription` per eliminare un abbonamento esistente.
7. **Blocca utente**: Usa `/banuser` per bloccare un utente.
8. **Sblocca utente**: Usa `/unbanuser` per sbloccare un utente precedentemente bloccato.
9. **Aggiungi amministratore**: Usa `/addadmin` per assegnare i privilegi di amministratore a un utente.
10. **Rimuovi amministratore**: Usa `/removeadmin` per revocare i privilegi di amministratore.
11. **Mostra tutti gli amministratori**: Usa `/showalladmin` per elencare tutti gli amministratori.
12. **Aggiungi utente speciale**: Usa `/addspecialuser` per contrassegnare un utente come speciale.
13. **Rimuovi utente speciale**: Usa `/removespecialuser` per rimuovere lo stato speciale.
14. **Esporta tabella in CSV**: Usa `/exporttabletocsv` per esportare una tabella del database in formato CSV.

Inserisci il comando desiderato per procedere.
"""
    },
    "selectchannelsubscriptions": {
        "text": "Seleziona il tuo canale."
    },
    "unbanuserhandler": {
        "text": "Inserisci l'ID dell'utente da sbloccare."
    },
    "removeadminhandler": {
        "text": "Inserisci l'ID utente a cui revocare i privilegi di amministratore."
    },
    "showalladminhandler": {
        "text": "Ecco l'elenco di tutti gli amministratori del sistema."
    },
    "removespecialuserhandler": {
        "text": "Inserisci l'ID utente da rimuovere dall'elenco speciale."
    },
    "exporttabletocsvhandler": {
        "text": "Inserisci il nome della tabella da esportare in formato CSV."
    },
    "addforcedjoinchannelhandler": {
        "text": "Inserisci i dettagli del canale da aggiungere come obbligatorio."
    },
    "deleteforcedjoinchannelhandler": {
        "text": "Inserisci i dettagli del canale da rimuovere dall'obbligo di iscrizione."
    },
    "addchannelhandler": {
        "text": "Inserisci i dettagli del canale da aggiungere."
    },
    "deletechannelhandler": {
        "text": "Inserisci i dettagli del canale da eliminare."
    },
    "addsubscriptionhandler": {
        "text": "Inserisci i dettagli dell'abbonamento da aggiungere."
    },
    "deletesubscriptionhandler": {
        "text": "Inserisci i dettagli dell'abbonamento da eliminare."
    },
    "forcejoincheckerhandler": {
        "text": "Per usare il bot, unisciti ai seguenti canali e gruppi:"
    },
    "confirmdeletestate": {
        "text": "Canale eliminato con successo."
    },
    "deleteforcedjoinchannelstate": {
        "text": "Seleziona un canale da eliminare."
    },
    "confirmdeletechannelstate": {
        "text": "Canale eliminato con successo."
    },
    "deletechannelstate": {
        "text": "Seleziona un canale da eliminare."
    },
    "deletesubscriptionstate": {
        "text": "Seleziona un abbonamento da eliminare."
    },
    "listsubscriptionsstate": {
        "text": "Scegli il tuo abbonamento."
    },
    "confirmdeleteanotherstate": {
        "text": "Abbonamento eliminato.\nVuoi eliminarne un altro?"
    },
    "DeleteAnotherSubscriptionState": {
        "text": "Scegli il tuo abbonamento."
    },
    "showlistoftableshandler": {
        "text":
            "1. canali\n"
            "2. abbonamenti\n"
            "3. utente2abbonamenti\n"
            "4. utenti speciali\n"
            "5. pagamenti\n"
            "6. joinforce\n"
            "7. utenti"
    },
    "addchannelstate": {
        "text": "Invia il link del canale."
    },
    "getchatidstate": {
        "text": "Canale aggiunto con successo."
    },
    "addforcedjoinchannelstate": {
        "text": "Invia il link del canale."
    },
    "getchannellinkstate": {
        "text": "Canale aggiunto con successo."
    },
    "getchannelhandler": {
        "text": "Seleziona un canale per contrassegnare l'utente come speciale."
    },
    "addsubscriptionstate": {
        "text": "Scegli il tuo canale."
    },
    "getnamestate": {
        "text": "Inserisci il nome dell'abbonamento."
    },
    "getpriceState": {
        "text": "Inserisci il prezzo in dollari."
    },
    "getdaystate": {
        "text": "Inserisci il numero di giorni per l'abbonamento."
    },
    "confirmaddanotherstate": {
        "text": "Abbonamento creato. Vuoi aggiungerne un altro?"
    },
    "selectsubscriptionstate": {
        "text": "Scegli il tuo abbonamento."
    }
}
