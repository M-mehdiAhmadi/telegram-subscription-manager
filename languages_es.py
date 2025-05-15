es = {
    "starthandler": {
        "text": "¡Bienvenido! Por favor, selecciona una opción:",
        "keyboard": [
            {"text": "Comprar suscripción de canales", "callback_data": "buychannelsubscriptions"},
            {"text": "Cambiar idioma", "callback_data": "select_language"}
        ]
    },
    "selectlanguagehandler": {
        "text": "Por favor, selecciona tu idioma:",
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
        "text": "Tu idioma ha sido cambiado a Español."
    },
    "selectchannelsubscriptionstate": {
        "text": "Selecciona tu canal:"
    },
    "selectsubscriptionsstate": {
        "text": "Selecciona la suscripción:"
    },
    "selectsubscriptionstate": {
        "text": "Selecciona la suscripción:"
    },
    "selectcryptostate": {
        "text": "Selecciona tu criptomoneda:"
    },
    "sendpaymentlinkstate": {
        "text": "Usa el siguiente enlace para realizar el pago:"
    },
    "checkpaymentstatusstate": {
        "text": "Haz clic en el botón inferior para comprobar el estado del pago.\nID de factura:",
        "keyboard": [
            {"text": "Comprobar estado del pago", "callback_data": ""}
        ]
    },
    "cancel": {
        "text": "Tu pago fue cancelado o expiró por inactividad.\nPor favor, intenta nuevamente."
    },
    "joinrequesthandler": {
        "text": "Tu solicitud de unión fue recibida. Por favor, espera la aprobación."
    },
    "addadminhandler": {
        "text": "Por favor, introduce el ID del usuario para otorgar permisos de administrador."
    },
    "addspecialuserhandler": {
        "text": "Por favor, introduce el ID del usuario para marcarlo como especial."
    },
    "banuserhandler": {
        "text": "Por favor, introduce el ID del usuario que deseas bloquear."
    },
    "checkpaymentstatushandler": {
        "text": "Verificando estado de pago. Por favor espera..."
    },
    "adminpannelhandler": {
        "text": """
Guía de comandos del administrador:

1. **Agregar canal obligatorio**: /addjoinforcechannel
2. **Eliminar canal obligatorio**: /deletejoinforcechannel
3. **Agregar canal**: /addchannel
4. **Eliminar canal**: /deletechannel
5. **Agregar suscripción**: /addsubscription
6. **Eliminar suscripción**: /deletesubscription
7. **Bloquear usuario**: /banuser
8. **Desbloquear usuario**: /unbanuser
9. **Agregar administrador**: /addadmin
10. **Eliminar administrador**: /removeadmin
11. **Mostrar todos los administradores**: /showalladmin
12. **Agregar usuario especial**: /addspecialuser
13. **Eliminar usuario especial**: /removespecialuser
14. **Exportar tabla como CSV**: /exporttabletocsv

Escribe el comando para realizar la acción correspondiente.
"""
    },
    "selectchannelsubscriptions": {
        "text": "Por favor, selecciona tu canal:"
    },
    "unbanuserhandler": {
        "text": "Por favor, introduce el ID del usuario para desbloquearlo."
    },
    "removeadminhandler": {
        "text": "Por favor, introduce el ID del usuario para eliminar permisos de administrador."
    },
    "showalladminhandler": {
        "text": "Aquí está la lista de todos los administradores:"
    },
    "removespecialuserhandler": {
        "text": "Por favor, introduce el ID del usuario para eliminarlo de los especiales."
    },
    "exporttabletocsvhandler": {
        "text": "Por favor, introduce el nombre de la tabla que deseas exportar como CSV."
    },
    "addforcedjoinchannelhandler": {
        "text": "Por favor, introduce los detalles del canal obligatorio que deseas agregar."
    },
    "deleteforcedjoinchannelhandler": {
        "text": "Por favor, introduce los detalles del canal obligatorio que deseas eliminar."
    },
    "addchannelhandler": {
        "text": "Por favor, introduce los detalles del canal que deseas agregar."
    },
    "deletechannelhandler": {
        "text": "Por favor, introduce los detalles del canal que deseas eliminar."
    },
    "addsubscriptionhandler": {
        "text": "Por favor, introduce los detalles de la suscripción que deseas agregar."
    },
    "deletesubscriptionhandler": {
        "text": "Por favor, introduce los detalles de la suscripción que deseas eliminar."
    },
    "forcejoincheckerhandler": {
        "text": "Estamos comprobando si te has unido al canal obligatorio..."
    },
    "confirmdeletestate": {
        "text": "¿Estás seguro de que deseas eliminar esto?"
    },
    "deleteforcedjoinchannelstate": {
        "text": "Selecciona el canal obligatorio que deseas eliminar:"
    },
    "confirmdeletechannelstate": {
        "text": "¿Confirmas que deseas eliminar este canal?"
    },
    "deletechannelstate": {
        "text": "Selecciona el canal que deseas eliminar:"
    },
    "deletesubscriptionstate": {
        "text": "Selecciona la suscripción que deseas eliminar:"
    },
    "listsubscriptionsstate": {
        "text": "Aquí están las suscripciones disponibles:"
    },
    "confirmdeleteanotherstate": {
        "text": "¿Deseas eliminar otra suscripción?"
    },
    "DeleteAnotherSubscriptionState": {
        "text": "¿Quieres eliminar otra suscripción?"
    },
    "showlistoftableshandler": {
        "text": "Estas son las tablas disponibles en el sistema:"
    },
    "addchannelstate": {
        "text": "Por favor, proporciona los datos del canal para agregar."
    },
    "getchatidstate": {
        "text": "Por favor, proporciona el chat ID del canal."
    },
    "addforcedjoinchannelstate": {
        "text": "Introduce el canal que deseas añadir como obligatorio."
    },
    "getchannellinkstate": {
        "text": "Por favor, proporciona el enlace del canal."
    },
    "getchannelhandler": {
        "text": "Proporciona el identificador del canal que deseas consultar."
    },
    "addsubscriptionstate": {
        "text": "Proporciona los detalles de la suscripción."
    },
    "getnamestate": {
        "text": "Introduce el nombre de la suscripción:"
    },
    "getpriceState": {
        "text": "Introduce el precio de la suscripción:"
    },
    "getdaystate": {
        "text": "Introduce la duración (en días):"
    },
    "confirmaddanotherstate": {
        "text": "¿Quieres agregar otra suscripción?"
    }
}
