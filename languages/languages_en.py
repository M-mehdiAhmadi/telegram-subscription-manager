en = {
    "starthandler": {
        "text": "Welcome! Please select an option:",
        "keyboard": [
            {"text": "Select Channel Subscriptions", "callback_data": "buychannelsubscriptions"},
            {"text": "Select Language", "callback_data": "select_language"}
        ]
    },
    "selectlanguagehandler": {
        "text": "Please select a language:",
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
        "text": "Your language has been changed to English."
    },
    "selectchannelsubscriptionstate": {
        "text": "Choose your channel."
    },
    "selectsubscriptionsstate": {
        "text": "Choose your subscription."
    },
    "selectcryptostate": {
        "text": "Choose your cryptocurrency."
    },
    "sendpaymentlinkstate": {
        "text": "Use the link below to pay."
    },
    "checkpaymentstatusstate": {
        "text": "Click on the button below to check your payment status.\nInvoice ID:",
        "keyboard": [
            {"text": "Check Payment Status", "callback_data": ""}
        ]
    },
    "cancel": {
        "text": "Your payment has been canceled or expired due to inactivity.\nPlease try again."
    },
    "joinrequesthandler": {
        "text": "Your join request has been received. Please wait for approval."
    },
    "addadminhandler": {
        "text": "Please provide the user ID to grant admin privileges."
    },
    "addspecialuserhandler": {
        "text": "Please provide the user ID to mark as special."
    },
    "banuserhandler": {
        "text": "Please provide the user ID to ban."
    },
    "checkpaymentstatushandler": {
        "text": "Checking payment status. Please wait..."
    },
    "adminpannelhandler": {
        "text": """
Admin Panel Commands Guide:

1. **Add Forced Join Channel**: Use `/addjoinforcechannel` to add a channel that users must join.
2. **Delete Forced Join Channel**: Use `/deletejoinforcechannel` to remove a forced join channel.
3. **Add Channel**: Use `/addchannel` to add a new channel to the system.
4. **Delete Channel**: Use `/deletechannel` to remove an existing channel.
5. **Add Subscription**: Use `/addsubscription` to create a new subscription for a channel.
6. **Delete Subscription**: Use `/deletesubscription` to remove an existing subscription.
7. **Ban User**: Use `/banuser` to ban a user from the system.
8. **Unban User**: Use `/unbanuser` to unban a previously banned user.
9. **Add Admin**: Use `/addadmin` to grant admin privileges to a user.
10. **Remove Admin**: Use `/removeadmin` to revoke admin privileges from a user.
11. **Show All Admins**: Use `/showalladmin` to list all admins in the system.
12. **Add Special User**: Use `/addspecialuser` to mark a user as special.
13. **Remove Special User**: Use `/removespecialuser` to remove the special status from a user.
14. **Export Table to CSV**: Use `/exporttabletocsv` to export a database table to a CSV file.

Please type the corresponding command to execute the desired action.
"""
    },
    "selectchannelsubscriptions": {
        "text": "Please select your channel."
    },
    "unbanuserhandler": {
        "text": "Please provide the user ID to unban."
    },
    "removeadminhandler": {
        "text": "Please provide the user ID to revoke admin privileges."
    },
    "showalladminhandler": {
        "text": "Here is the list of all admins in the system."
    },
    "removespecialuserhandler": {
        "text": "Please provide the user ID to remove from special users."
    },
    "exporttabletocsvhandler": {
        "text": "Please provide the table name to export as a CSV file."
    },
    "addforcedjoinchannelhandler": {
        "text": "Please provide the details of the channel to add as forced join."
    },
    "deleteforcedjoinchannelhandler": {
        "text": "Please provide the details of the channel to remove from forced join."
    },
    "addchannelhandler": {
        "text": "Please provide the details of the channel to add."
    },
    "deletechannelhandler": {
        "text": "Please provide the details of the channel to delete."
    },
    "addsubscriptionhandler": {
        "text": "Please provide the details of the subscription to add."
    },
    "deletesubscriptionhandler": {
        "text": "Please provide the details of the subscription to delete."
    },
    "forcejoincheckerhandler": {
        "text": "To use the bot, join the following channels and groups:"
    },
    "confirmdeletestate": {
        "text": "Channel successfully deleted."
    },
    "deleteforcedjoinchannelstate": {
        "text": "Select a channel to delete."
    },
    "confirmdeletechannelstate": {
        "text": "Channel successfully deleted."
    },
    "deletechannelstate": {
        "text": "Select a channel to delete."
    },
    "deletesubscriptionstate": {
        "text": "Select a subscription to delete."
    },
    "listsubscriptionsstate": {
        "text": "Choose your subscription."
    },
    "confirmdeleteanotherstate": {
        "text": "Subscription deleted.\nDo you want to delete another?"
    },
    "DeleteAnotherSubscriptionState": {
        "text": "Choose your subscription."
    },
    "showlistoftableshandler": {
        "text":
            "1. channels\n"
            "2. subscriptions\n"
            "3. user2subscriptions\n"
            "4. specialusers\n"
            "5. payments\n"
            "6. joinforce\n"
            "7. users"
    },
    "addchannelstate": {
        "text": "Send the link of the channel."
    },
    "getchatidstate": {
        "text": "Channel added successfully."
    },
    "addforcedjoinchannelstate": {
        "text": "Send the link of the channel."
    },
    "getchannellinkstate": {
        "text": "Channel added successfully."
    },
    "getchannelhandler": {
        "text": "Select a channel to mark the user as special."
    },
    "addsubscriptionstate": {
        "text": "Choose your channel."
    },
    "getnamestate": {
        "text": "Enter the subscription name."
    },
    "getpriceState": {
        "text": "Enter the price in dollars."
    },
    "getdaystate": {
        "text": "Enter the number of days for the subscription."
    },
    "confirmaddanotherstate": {
        "text": "Subscription created. Do you want to add another?"
    },
    "selectsubscriptionstate": {
        "text": "Choose your subscription."
    }
}

