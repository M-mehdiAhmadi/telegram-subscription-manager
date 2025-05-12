languages = {
    "en": {
        "starthandler": {
            "text": "Welcome! Please select an option:",
            "keyboard": [
                {"text": "select channel Subscriptions",
                    "callback_data": "buychannelsubscriptions"},
                {"text": "select Language", "callback_data": "select_language"}
            ]
        },
        "selectlanguagehandler": {
            "text": "please select language:",
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
            "text": "your language has been changed to english"
        },
        "selectchannelsubscriptionsstate": {
            "text": "choose your channel"
        },
        "selectsubscriptionsstate": {
            "text": "choose your subscription"
        },
        "selectcryptostate": {
            "text": "choose your crypto currency"
        },
        "sendpaymentlinkstate": {
            "text": "use link below to pay",
        },
        "checkpaymentstatusstate": {
            "text": "clieck on button below to check your payment status. \ninvoice id:",
            "keyboard": [
                {"text": "check payment status",
                    "callback_data": ""}
            ]
        },
        "cancel": {
            "text": "your payment has been canceled or expired due to unactivity.\nplease try again.",
        },
        "joinrequesthandler": {
            "text": "Your join request has been received. Please wait for approval."
        },
        "addadminhandler": {
            "text": "Admin has been successfully added."
        },
        "addspecialuserhandler": {
            "text": "Special user has been successfully added."
        },
        "adminpannelhandler": {
            "text": "Welcome to the admin panel. Use the commands provided to manage the system."
        },
        "banuserhandler": {
            "text": "The user has been successfully banned."
        },
        "checkpaymentstatushandler": {
            "text": "Checking payment status. Please wait..."
        },
        "adminpannel": {
            "text":
            """
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
""",

        },
        "selectchannelsubscriptions": {
            "text": "Please select your channel."
        },
        "selectsubscriptionsstate": {
            "text": "Please select your subscription."
        },
        "selectcryptostate": {
            "text": "Please select your cryptocurrency."
        },
        "sendpaymentlinkstate": {
            "text": "Use the link below to complete your payment."
        },
        "checkpaymentstatusstate": {
            "text": "Click the button below to check your payment status.\nInvoice ID:",
            "keyboard": [
                {"text": "Check Payment Status", "callback_data": ""}
            ]
        },
        "addforcedjoinchannel": {
            "text": "Please provide the details of the channel to add as a forced join."
        },
        "deleteforcedjoinchannel": {
            "text": "Please provide the details of the channel to remove from forced join."
        },
        "addchannel": {
            "text": "Please provide the details of the channel to add."
        },
        "deletechannel": {
            "text": "Please provide the details of the channel to delete."
        },
        "addsubscription": {
            "text": "Please provide the details of the subscription to add."
        },
        "deletesubscription": {
            "text": "Please provide the details of the subscription to delete."
        },
        "banuser": {
            "text": "Please provide the user ID to ban."
        },
        "unbanuser": {
            "text": "Please provide the user ID to unban."
        },
        "addadmin": {
            "text": "Please provide the user ID to grant admin privileges."
        },
        "removeadmin": {
            "text": "Please provide the user ID to revoke admin privileges."
        },
        "showalladmin": {
            "text": "Here is the list of all admins in the system."
        },
        "addspecialuser": {
            "text": "Please provide the user ID to mark as special."
        },
        "removespecialuser": {
            "text": "Please provide the user ID to remove from special users."
        },
        "exporttabletocsv": {
            "text": "Please provide the table name to export as a CSV file."
        },
    },
    "fa": {
        "starthandler": {
            "text": "سلام! لطفاً یک گزینه را انتخاب کنید:",
            "keyboard": [
                {"text": "انتخاب اشتراک کانال",
                    "callback_data": "buychannelsubscriptions"},
                {"text": "انتخاب زبان", "callback_data": "select_language"}
            ]
        },
        "selectlanguagehandler": {
            "text": "لطفاً زبان را انتخاب کنید:",
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
            "text": "زبان شما به انگلیسی تغییر یافت."
        },
        "selectchannelsubscriptionsstate": {
            "text": "کانال خود را انتخاب کنید."
        },
        "selectsubscriptionsstate": {
            "text": "اشتراک خود را انتخاب کنید."
        },
        "selectcryptostate": {
            "text": "ارز دیجیتال خود را انتخاب کنید."
        },
        "sendpaymentlinkstate": {
            "text": "از لینک زیر برای پرداخت استفاده کنید."
        },
        "checkpaymentstatusstate": {
            "text": "برای بررسی وضعیت پرداخت روی دکمه زیر کلیک کنید.\nشناسه فاکتور:",
            "keyboard": [
                {"text": "بررسی وضعیت پرداخت", "callback_data": ""}
            ]
        },
        "cancel": {
            "text": "پرداخت شما لغو شده یا به دلیل عدم فعالیت منقضی شده است.\nلطفاً دوباره تلاش کنید."
        },
        "joinrequesthandler": {
            "text": "درخواست عضویت شما دریافت شد. لطفاً منتظر تأیید باشید."
        },
        "addadminhandler": {
            "text": "مدیر با موفقیت اضافه شد."
        },
        "addspecialuserhandler": {
            "text": "کاربر ویژه با موفقیت اضافه شد."
        },
        "adminpannelhandler": {
            "text": "به پنل مدیریت خوش آمدید. از دستورات ارائه شده برای مدیریت سیستم استفاده کنید."
        },
        "banuserhandler": {
            "text": "کاربر با موفقیت مسدود شد."
        },
        "checkpaymentstatushandler": {
            "text": "در حال بررسی وضعیت پرداخت. لطفاً صبر کنید..."
        },
        "adminpannel": {
            "text": """
راهنمای دستورات پنل مدیریت:

۱. **افزودن کانال اجباری**: از دستور `/addjoinforcechannel` برای افزودن کانالی که کاربران باید عضو شوند استفاده کنید.
۲. **حذف کانال اجباری**: از دستور `/deletejoinforcechannel` برای حذف کانال اجباری استفاده کنید.
۳. **افزودن کانال**: از دستور `/addchannel` برای افزودن کانال جدید استفاده کنید.
۴. **حذف کانال**: از دستور `/deletechannel` برای حذف کانال موجود استفاده کنید.
۵. **افزودن اشتراک**: از دستور `/addsubscription` برای ایجاد اشتراک جدید استفاده کنید.
۶. **حذف اشتراک**: از دستور `/deletesubscription` برای حذف اشتراک موجود استفاده کنید.
۷. **مسدود کردن کاربر**: از دستور `/banuser` برای مسدود کردن کاربر استفاده کنید.
۸. **رفع مسدودی کاربر**: از دستور `/unbanuser` برای رفع مسدودی کاربر استفاده کنید.
۹. **افزودن مدیر**: از دستور `/addadmin` برای اعطای دسترسی مدیر به کاربر استفاده کنید.
۱۰. **حذف مدیر**: از دستور `/removeadmin` برای لغو دسترسی مدیر استفاده کنید.
۱۱. **نمایش همه مدیران**: از دستور `/showalladmin` برای نمایش لیست همه مدیران استفاده کنید.
۱۲. **افزودن کاربر ویژه**: از دستور `/addspecialuser` برای ویژه کردن کاربر استفاده کنید.
۱۳. **حذف کاربر ویژه**: از دستور `/removespecialuser` برای حذف وضعیت ویژه کاربر استفاده کنید.
۱۴. **خروجی گرفتن از جدول به CSV**: از دستور `/exporttabletocsv` برای خروجی گرفتن از جدول به فایل CSV استفاده کنید.

لطفاً دستور مورد نظر را تایپ کنید تا اجرا شود.
"""
        },
        "selectchannelsubscriptions": {
            "text": "لطفاً کانال خود را انتخاب کنید."
        },
        "addforcedjoinchannel": {
            "text": "لطفاً جزئیات کانالی که می‌خواهید به عنوان کانال اجباری اضافه کنید را وارد کنید."
        },
        "deleteforcedjoinchannel": {
            "text": "لطفاً جزئیات کانالی که می‌خواهید از کانال‌های اجباری حذف کنید را وارد کنید."
        },
        "addchannel": {
            "text": "لطفاً جزئیات کانالی که می‌خواهید اضافه کنید را وارد کنید."
        },
        "deletechannel": {
            "text": "لطفاً جزئیات کانالی که می‌خواهید حذف کنید را وارد کنید."
        },
        "addsubscription": {
            "text": "لطفاً جزئیات اشتراکی که می‌خواهید اضافه کنید را وارد کنید."
        },
        "deletesubscription": {
            "text": "لطفاً جزئیات اشتراکی که می‌خواهید حذف کنید را وارد کنید."
        },
        "banuser": {
            "text": "لطفاً شناسه کاربری که می‌خواهید مسدود کنید را وارد کنید."
        },
        "unbanuser": {
            "text": "لطفاً شناسه کاربری که می‌خواهید رفع مسدودی کنید را وارد کنید."
        },
        "addadmin": {
            "text": "لطفاً شناسه کاربری که می‌خواهید به عنوان مدیر اضافه کنید را وارد کنید."
        },
        "removeadmin": {
            "text": "لطفاً شناسه کاربری که می‌خواهید از مدیران حذف کنید را وارد کنید."
        },
        "showalladmin": {
            "text": "لیست همه مدیران سیستم به شرح زیر است:"
        },
        "addspecialuser": {
            "text": "لطفاً شناسه کاربری که می‌خواهید به عنوان کاربر ویژه اضافه کنید را وارد کنید."
        },
        "removespecialuser": {
            "text": "لطفاً شناسه کاربری که می‌خواهید از کاربران ویژه حذف کنید را وارد کنید."
        },
        "exporttabletocsv": {
            "text": "لطفاً نام جدولی که می‌خواهید به فایل CSV خروجی بگیرید را وارد کنید."
        },
    },
    "es": {  # Spanish
        "starthandler": {
            "text": "¡Bienvenido! Por favor selecciona una opción:",
            "keyboard": [
                {"text": "seleccionar suscripciones de canal",
                    "callback_data": "buychannelsubscriptions"},
                {"text": "seleccionar idioma", "callback_data": "select_language"}
            ]
        },
        "selectlanguagehandler": {
            "text": "por favor selecciona un idioma:",
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
            "text": "tu idioma ha sido cambiado a inglés."
        },
        "selectchannelsubscriptionsstate": {
            "text": "Por favor selecciona tu canal."
        },
        "selectsubscriptionsstate": {
            "text": "Por favor selecciona tu suscripción."
        },
        "selectcryptostate": {
            "text": "Por favor selecciona tu criptomoneda."
        },
        "sendpaymentlinkstate": {
            "text": "Usa el enlace de abajo para completar tu pago."
        },
        "checkpaymentstatusstate": {
            "text": "Haz clic en el botón de abajo para verificar el estado de tu pago.\nID de factura:",
            "keyboard": [
                {"text": "Verificar estado de pago", "callback_data": ""}
            ]
        },
        "cancel": {
            "text": "Tu pago ha sido cancelado o expirado debido a inactividad.\nPor favor, inténtalo de nuevo."
        },
        "joinrequesthandler": {
            "text": "Tu solicitud de unión ha sido recibida. Por favor espera la aprobación."
        },
        "addadminhandler": {
            "text": "El administrador ha sido añadido con éxito."
        },
        "addspecialuserhandler": {
            "text": "El usuario especial ha sido añadido con éxito."
        },
        "adminpannelhandler": {
            "text": "Bienvenido al panel de administración. Usa los comandos proporcionados para gestionar el sistema."
        },
        "banuserhandler": {
            "text": "El usuario ha sido bloqueado con éxito."
        },
        "checkpaymentstatushandler": {
            "text": "Verificando el estado del pago. Por favor espera..."
        },
        "adminpannel": {
            "text": """
Guía de comandos del panel de administración:

1. **Añadir canal obligatorio**: Usa `/addjoinforcechannel` para añadir un canal que los usuarios deben unirse.
2. **Eliminar canal obligatorio**: Usa `/deletejoinforcechannel` para eliminar un canal obligatorio.
3. **Añadir canal**: Usa `/addchannel` para añadir un nuevo canal al sistema.
4. **Eliminar canal**: Usa `/deletechannel` para eliminar un canal existente.
5. **Añadir suscripción**: Usa `/addsubscription` para crear una nueva suscripción para un canal.
6. **Eliminar suscripción**: Usa `/deletesubscription` para eliminar una suscripción existente.
7. **Bloquear usuario**: Usa `/banuser` para bloquear a un usuario del sistema.
8. **Desbloquear usuario**: Usa `/unbanuser` para desbloquear a un usuario previamente bloqueado.
9. **Añadir administrador**: Usa `/addadmin` para otorgar privilegios de administrador a un usuario.
10. **Eliminar administrador**: Usa `/removeadmin` para revocar los privilegios de administrador de un usuario.
11. **Mostrar todos los administradores**: Usa `/showalladmin` para listar todos los administradores en el sistema.
12. **Añadir usuario especial**: Usa `/addspecialuser` para marcar a un usuario como especial.
13. **Eliminar usuario especial**: Usa `/removespecialuser` para eliminar el estado especial de un usuario.
14. **Exportar tabla a CSV**: Usa `/exporttabletocsv` para exportar una tabla de la base de datos a un archivo CSV.

Por favor, escribe el comando correspondiente para ejecutar la acción deseada.
"""
        },
        "selectchannelsubscriptions": {
            "text": "Por favor selecciona tu canal."
        },
        "addforcedjoinchannel": {
            "text": "Por favor proporciona los detalles del canal que deseas añadir como obligatorio."
        },
        "deleteforcedjoinchannel": {
            "text": "Por favor proporciona los detalles del canal que deseas eliminar de los obligatorios."
        },
        "addchannel": {
            "text": "Por favor proporciona los detalles del canal que deseas añadir."
        },
        "deletechannel": {
            "text": "Por favor proporciona los detalles del canal que deseas eliminar."
        },
        "addsubscription": {
            "text": "Por favor proporciona los detalles de la suscripción que deseas añadir."
        },
        "deletesubscription": {
            "text": "Por favor proporciona los detalles de la suscripción que deseas eliminar."
        },
        "banuser": {
            "text": "Por favor proporciona el ID del usuario que deseas bloquear."
        },
        "unbanuser": {
            "text": "Por favor proporciona el ID del usuario que deseas desbloquear."
        },
        "addadmin": {
            "text": "Por favor proporciona el ID del usuario que deseas añadir como administrador."
        },
        "removeadmin": {
            "text": "Por favor proporciona el ID del usuario que deseas eliminar como administrador."
        },
        "showalladmin": {
            "text": "Aquí está la lista de todos los administradores en el sistema:"
        },
        "addspecialuser": {
            "text": "Por favor proporciona el ID del usuario que deseas marcar como especial."
        },
        "removespecialuser": {
            "text": "Por favor proporciona el ID del usuario que deseas eliminar de los usuarios especiales."
        },
        "exporttabletocsv": {
            "text": "Por favor proporciona el nombre de la tabla que deseas exportar a un archivo CSV."
        },
    },
    "de": {  # German
        "starthandler": {
            "text": "Willkommen! Bitte wählen Sie eine Option:",
            "keyboard": [
                {"text": "Kanalabonnements auswählen",
                    "callback_data": "buychannelsubscriptions"},
                {"text": "Sprache auswählen", "callback_data": "select_language"}
            ]
        },
        "selectlanguagehandler": {
            "text": "Bitte wählen Sie eine Sprache:",
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
            "text": "Ihre Sprache wurde auf Englisch geändert."
        },
        "selectchannelsubscriptionsstate": {
            "text": "Bitte wählen Sie Ihren Kanal aus."
        },
        "selectsubscriptionsstate": {
            "text": "Bitte wählen Sie Ihr Abonnement aus."
        },
        "selectcryptostate": {
            "text": "Bitte wählen Sie Ihre Kryptowährung aus."
        },
        "sendpaymentlinkstate": {
            "text": "Verwenden Sie den untenstehenden Link, um Ihre Zahlung abzuschließen."
        },
        "checkpaymentstatusstate": {
            "text": "Klicken Sie auf die Schaltfläche unten, um den Status Ihrer Zahlung zu überprüfen.\nRechnungs-ID:",
            "keyboard": [
                {"text": "Zahlungsstatus überprüfen", "callback_data": ""}
            ]
        },
        "cancel": {
            "text": "Ihre Zahlung wurde storniert oder ist aufgrund von Inaktivität abgelaufen.\nBitte versuchen Sie es erneut."
        },
        "joinrequesthandler": {
            "text": "Ihre Beitrittsanfrage wurde erhalten. Bitte warten Sie auf die Genehmigung."
        },
        "addadminhandler": {
            "text": "Der Administrator wurde erfolgreich hinzugefügt."
        },
        "addspecialuserhandler": {
            "text": "Der spezielle Benutzer wurde erfolgreich hinzugefügt."
        },
        "adminpannelhandler": {
            "text": "Willkommen im Admin-Panel. Verwenden Sie die bereitgestellten Befehle, um das System zu verwalten."
        },
        "banuserhandler": {
            "text": "Der Benutzer wurde erfolgreich gesperrt."
        },
        "checkpaymentstatushandler": {
            "text": "Zahlungsstatus wird überprüft. Bitte warten Sie..."
        },
        "adminpannel": {
            "text": """
Admin-Panel-Befehlsanleitung:

1. **Erzwingten Beitrittskanal hinzufügen**: Verwenden Sie `/addjoinforcechannel`, um einen Kanal hinzuzufügen, dem Benutzer beitreten müssen.
2. **Erzwingten Beitrittskanal entfernen**: Verwenden Sie `/deletejoinforcechannel`, um einen erzwingten Beitrittskanal zu entfernen.
3. **Kanal hinzufügen**: Verwenden Sie `/addchannel`, um einen neuen Kanal zum System hinzuzufügen.
4. **Kanal entfernen**: Verwenden Sie `/deletechannel`, um einen vorhandenen Kanal zu entfernen.
5. **Abonnement hinzufügen**: Verwenden Sie `/addsubscription`, um ein neues Abonnement für einen Kanal zu erstellen.
6. **Abonnement entfernen**: Verwenden Sie `/deletesubscription`, um ein vorhandenes Abonnement zu entfernen.
7. **Benutzer sperren**: Verwenden Sie `/banuser`, um einen Benutzer im System zu sperren.
8. **Benutzer entsperren**: Verwenden Sie `/unbanuser`, um einen zuvor gesperrten Benutzer zu entsperren.
9. **Administrator hinzufügen**: Verwenden Sie `/addadmin`, um einem Benutzer Administratorrechte zu gewähren.
10. **Administrator entfernen**: Verwenden Sie `/removeadmin`, um einem Benutzer Administratorrechte zu entziehen.
11. **Alle Administratoren anzeigen**: Verwenden Sie `/showalladmin`, um alle Administratoren im System aufzulisten.
12. **Speziellen Benutzer hinzufügen**: Verwenden Sie `/addspecialuser`, um einen Benutzer als speziell zu markieren.
13. **Speziellen Benutzer entfernen**: Verwenden Sie `/removespecialuser`, um den speziellen Status eines Benutzers zu entfernen.
14. **Tabelle als CSV exportieren**: Verwenden Sie `/exporttabletocsv`, um eine Datenbanktabelle als CSV-Datei zu exportieren.

Bitte geben Sie den entsprechenden Befehl ein, um die gewünschte Aktion auszuführen.
"""
        },
        "selectchannelsubscriptions": {
            "text": "Bitte wählen Sie Ihren Kanal aus."
        },
        "addforcedjoinchannel": {
            "text": "Bitte geben Sie die Details des Kanals an, den Sie als erzwingenden Beitrittskanal hinzufügen möchten."
        },
        "deleteforcedjoinchannel": {
            "text": "Bitte geben Sie die Details des Kanals an, den Sie aus den erzwingenden Beitrittskanälen entfernen möchten."
        },
        "addchannel": {
            "text": "Bitte geben Sie die Details des Kanals an, den Sie hinzufügen möchten."
        },
        "deletechannel": {
            "text": "Bitte geben Sie die Details des Kanals an, den Sie entfernen möchten."
        },
        "addsubscription": {
            "text": "Bitte geben Sie die Details des Abonnements an, das Sie hinzufügen möchten."
        },
        "deletesubscription": {
            "text": "Bitte geben Sie die Details des Abonnements an, das Sie entfernen möchten."
        },
        "banuser": {
            "text": "Bitte geben Sie die Benutzer-ID an, die Sie sperren möchten."
        },
        "unbanuser": {
            "text": "Bitte geben Sie die Benutzer-ID an, die Sie entsperren möchten."
        },
        "addadmin": {
            "text": "Bitte geben Sie die Benutzer-ID an, die Sie als Administrator hinzufügen möchten."
        },
        "removeadmin": {
            "text": "Bitte geben Sie die Benutzer-ID an, die Sie als Administrator entfernen möchten."
        },
        "showalladmin": {
            "text": "Hier ist die Liste aller Administratoren im System:"
        },
        "addspecialuser": {
            "text": "Bitte geben Sie die Benutzer-ID an, die Sie als speziell markieren möchten."
        },
        "removespecialuser": {
            "text": "Bitte geben Sie die Benutzer-ID an, die Sie aus den speziellen Benutzern entfernen möchten."
        },
        "exporttabletocsv": {
            "text": "Bitte geben Sie den Namen der Tabelle an, die Sie als CSV-Datei exportieren möchten."
        },
    },
    "ru": {  # Russian
        "starthandler": {
            "text": "Добро пожаловать! Пожалуйста, выберите опцию:",
            "keyboard": [
                {"text": "выбрать подписки на канал",
                    "callback_data": "buychannelsubscriptions"},
                {"text": "выбрать язык", "callback_data": "select_language"}
            ]
        },
        "selectlanguagehandler": {
            "text": "Пожалуйста, выберите язык:",
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
            "text": "Ваш язык был изменен на английский."
        },
        "selectchannelsubscriptionsstate": {
            "text": "Пожалуйста, выберите ваш канал."
        },
        "selectsubscriptionsstate": {
            "text": "Пожалуйста, выберите вашу подписку."
        },
        "selectcryptostate": {
            "text": "Пожалуйста, выберите вашу криптовалюту."
        },
        "sendpaymentlinkstate": {
            "text": "Используйте ссылку ниже, чтобы завершить оплату."
        },
        "checkpaymentstatusstate": {
            "text": "Нажмите кнопку ниже, чтобы проверить статус вашей оплаты.\nID счета:",
            "keyboard": [
                {"text": "Проверить статус оплаты", "callback_data": ""}
            ]
        },
        "cancel": {
            "text": "Ваша оплата была отменена или истекла из-за бездействия.\nПожалуйста, попробуйте снова."
        },
        "joinrequesthandler": {
            "text": "Ваш запрос на присоединение получен. Пожалуйста, ожидайте подтверждения."
        },
        "addadminhandler": {
            "text": "Администратор успешно добавлен."
        },
        "addspecialuserhandler": {
            "text": "Специальный пользователь успешно добавлен."
        },
        "adminpannelhandler": {
            "text": "Добро пожаловать в панель администратора. Используйте предоставленные команды для управления системой."
        },
        "banuserhandler": {
            "text": "Пользователь успешно заблокирован."
        },
        "checkpaymentstatushandler": {
            "text": "Проверка статуса оплаты. Пожалуйста, подождите..."
        },
        "adminpannel": {
            "text": """
Руководство по командам панели администратора:

1. **Добавить обязательный канал**: Используйте `/addjoinforcechannel`, чтобы добавить канал, к которому пользователи должны присоединиться.
2. **Удалить обязательный канал**: Используйте `/deletejoinforcechannel`, чтобы удалить обязательный канал.
3. **Добавить канал**: Используйте `/addchannel`, чтобы добавить новый канал в систему.
4. **Удалить канал**: Используйте `/deletechannel`, чтобы удалить существующий канал.
5. **Добавить подписку**: Используйте `/addsubscription`, чтобы создать новую подписку для канала.
6. **Удалить подписку**: Используйте `/deletesubscription`, чтобы удалить существующую подписку.
7. **Заблокировать пользователя**: Используйте `/banuser`, чтобы заблокировать пользователя в системе.
8. **Разблокировать пользователя**: Используйте `/unbanuser`, чтобы разблокировать ранее заблокированного пользователя.
9. **Добавить администратора**: Используйте `/addadmin`, чтобы предоставить пользователю права администратора.
10. **Удалить администратора**: Используйте `/removeadmin`, чтобы отозвать права администратора у пользователя.
11. **Показать всех администраторов**: Используйте `/showalladmin`, чтобы отобразить список всех администраторов в системе.
12. **Добавить специального пользователя**: Используйте `/addspecialuser`, чтобы отметить пользователя как специального.
13. **Удалить специального пользователя**: Используйте `/removespecialuser`, чтобы удалить специальный статус пользователя.
14. **Экспорт таблицы в CSV**: Используйте `/exporttabletocsv`, чтобы экспортировать таблицу базы данных в файл CSV.

Пожалуйста, введите соответствующую команду, чтобы выполнить желаемое действие.
"""
        },
        "selectchannelsubscriptions": {
            "text": "Пожалуйста, выберите ваш канал."
        },
        "addforcedjoinchannel": {
            "text": "Пожалуйста, предоставьте данные канала, который вы хотите добавить как обязательный."
        },
        "deleteforcedjoinchannel": {
            "text": "Пожалуйста, предоставьте данные канала, который вы хотите удалить из обязательных."
        },
        "addchannel": {
            "text": "Пожалуйста, предоставьте данные канала, который вы хотите добавить."
        },
        "deletechannel": {
            "text": "Пожалуйста, предоставьте данные канала, который вы хотите удалить."
        },
        "addsubscription": {
            "text": "Пожалуйста, предоставьте данные подписки, которую вы хотите добавить."
        },
        "deletesubscription": {
            "text": "Пожалуйста, предоставьте данные подписки, которую вы хотите удалить."
        },
        "banuser": {
            "text": "Пожалуйста, предоставьте ID пользователя, которого вы хотите заблокировать."
        },
        "unbanuser": {
            "text": "Пожалуйста, предоставьте ID пользователя, которого вы хотите разблокировать."
        },
        "addadmin": {
            "text": "Пожалуйста, предоставьте ID пользователя, которого вы хотите добавить как администратора."
        },
        "removeadmin": {
            "text": "Пожалуйста, предоставьте ID пользователя, которого вы хотите удалить из администраторов."
        },
        "showalladmin": {
            "text": "Вот список всех администраторов в системе:"
        },
        "addspecialuser": {
            "text": "Пожалуйста, предоставьте ID пользователя, которого вы хотите отметить как специального."
        },
        "removespecialuser": {
            "text": "Пожалуйста, предоставьте ID пользователя, которого вы хотите удалить из специальных пользователей."
        },
        "exporttabletocsv": {
            "text": "Пожалуйста, предоставьте имя таблицы, которую вы хотите экспортировать в файл CSV."
        },
    },
    "ja": {  # Japanese
        "starthandler": {
            "text": "ようこそ！オプションを選択してください：",
            "keyboard": [
                {"text": "チャンネルサブスクリプションを選択",
                    "callback_data": "buychannelsubscriptions"},
                {"text": "言語を選択", "callback_data": "select_language"}
            ]
        },
        "selectlanguagehandler": {
            "text": "言語を選択してください：",
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
            "text": "言語が英語に変更されました。"
        },
        "selectchannelsubscriptionsstate": {
            "text": "チャンネルを選択してください。"
        },
        "selectsubscriptionsstate": {
            "text": "サブスクリプションを選択してください。"
        },
        "selectcryptostate": {
            "text": "暗号通貨を選択してください。"
        },
        "sendpaymentlinkstate": {
            "text": "以下のリンクを使用して支払いを完了してください。"
        },
        "checkpaymentstatusstate": {
            "text": "支払い状況を確認するには、以下のボタンをクリックしてください。\n請求書ID：",
            "keyboard": [
                {"text": "支払い状況を確認", "callback_data": ""}
            ]
        },
        "cancel": {
            "text": "支払いがキャンセルされるか、非アクティブのため期限切れになりました。\nもう一度お試しください。"
        },
        "joinrequesthandler": {
            "text": "参加リクエストが受信されました。承認をお待ちください。"
        },
        "addadminhandler": {
            "text": "管理者が正常に追加されました。"
        },
        "addspecialuserhandler": {
            "text": "特別ユーザーが正常に追加されました。"
        },
        "adminpannelhandler": {
            "text": "管理パネルへようこそ。システムを管理するために提供されたコマンドを使用してください。"
        },
        "banuserhandler": {
            "text": "ユーザーが正常に禁止されました。"
        },
        "checkpaymentstatushandler": {
            "text": "支払い状況を確認しています。お待ちください..."
        },
        "adminpannel": {
            "text": """
管理パネルコマンドガイド：

1. **強制参加チャンネルを追加**: `/addjoinforcechannel` を使用して、ユーザーが参加する必要があるチャンネルを追加します。
2. **強制参加チャンネルを削除**: `/deletejoinforcechannel` を使用して、強制参加チャンネルを削除します。
3. **チャンネルを追加**: `/addchannel` を使用して、新しいチャンネルをシステムに追加します。
4. **チャンネルを削除**: `/deletechannel` を使用して、既存のチャンネルを削除します。
5. **サブスクリプションを追加**: `/addsubscription` を使用して、チャンネルの新しいサブスクリプションを作成します。
6. **サブスクリプションを削除**: `/deletesubscription` を使用して、既存のサブスクリプションを削除します。
7. **ユーザーを禁止**: `/banuser` を使用して、システムからユーザーを禁止します。
8. **ユーザーの禁止を解除**: `/unbanuser` を使用して、以前に禁止されたユーザーの禁止を解除します。
9. **管理者を追加**: `/addadmin` を使用して、ユーザーに管理者権限を付与します。
10. **管理者を削除**: `/removeadmin` を使用して、ユーザーの管理者権限を取り消します。
11. **すべての管理者を表示**: `/showalladmin` を使用して、システム内のすべての管理者を一覧表示します。
12. **特別ユーザーを追加**: `/addspecialuser` を使用して、ユーザーを特別としてマークします。
13. **特別ユーザーを削除**: `/removespecialuser` を使用して、ユーザーの特別ステータスを削除します。
14. **テーブルをCSVにエクスポート**: `/exporttabletocsv` を使用して、データベーステーブルをCSVファイルにエクスポートします。

実行したいアクションに対応するコマンドを入力してください。
"""
        },
        "selectchannelsubscriptions": {
            "text": "チャンネルを選択してください。"
        },
        "addforcedjoinchannel": {
            "text": "強制参加として追加するチャンネルの詳細を入力してください。"
        },
        "deleteforcedjoinchannel": {
            "text": "強制参加から削除するチャンネルの詳細を入力してください。"
        },
        "addchannel": {
            "text": "追加するチャンネルの詳細を入力してください。"
        },
        "deletechannel": {
            "text": "削除するチャンネルの詳細を入力してください。"
        },
        "addsubscription": {
            "text": "追加するサブスクリプションの詳細を入力してください。"
        },
        "deletesubscription": {
            "text": "削除するサブスクリプションの詳細を入力してください。"
        },
        "banuser": {
            "text": "禁止するユーザーIDを入力してください。"
        },
        "unbanuser": {
            "text": "禁止を解除するユーザーIDを入力してください。"
        },
        "addadmin": {
            "text": "管理者として追加するユーザーIDを入力してください。"
        },
        "removeadmin": {
            "text": "管理者から削除するユーザーIDを入力してください。"
        },
        "showalladmin": {
            "text": "システム内のすべての管理者のリストはこちらです："
        },
        "addspecialuser": {
            "text": "特別としてマークするユーザーIDを入力してください。"
        },
        "removespecialuser": {
            "text": "特別ユーザーから削除するユーザーIDを入力してください。"
        },
        "exporttabletocsv": {
            "text": "CSVファイルにエクスポートするテーブル名を入力してください。"
        },
    },
    "zh": {
        "starthandler": {
            "text": "欢迎！请选择一个选项：",
            "keyboard": [
                {"text": "选择频道订阅", "callback_data": "buychannelsubscriptions"},
                {"text": "选择语言", "callback_data": "select_language"}
            ]
        },
        "selectlanguagehandler": {
            "text": "请选择语言：",
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
            "text": "您的语言已更改为英语"
        },
        "selectchannelsubscriptionsstate": {
            "text": "请选择您的频道"
        },
        "selectsubscriptionsstate": {
            "text": "请选择您的订阅"
        },
        "selectcryptostate": {
            "text": "请选择您的加密货币"
        },
        "sendpaymentlinkstate": {
            "text": "请使用以下链接付款"
        },
        "checkpaymentstatusstate": {
            "text": "点击下面的按钮检查您的付款状态。\n发票编号：",
            "keyboard": [
                {"text": "检查付款状态", "callback_data": ""}
            ]
        },
        "cancel": {
            "text": "由于长时间未操作，您的付款已被取消或过期。\n请重试。"
        },
        "joinrequesthandler": {
            "text": "您的加入请求已收到，请等待审核。"
        },
        "addadminhandler": {
            "text": "管理员已成功添加。"
        },
        "addspecialuserhandler": {
            "text": "特殊用户已成功添加。"
        },
        "adminpannelhandler": {
            "text": "欢迎来到管理面板。请使用提供的命令来管理系统。"
        },
        "banuserhandler": {
            "text": "用户已成功被封禁。"
        },
        "checkpaymentstatushandler": {
            "text": "正在检查付款状态，请稍候..."
        },
        "adminpannel": {
            "text":
            """
管理面板命令指南：

1. **添加强制加入频道**：使用 `/addjoinforcechannel` 添加用户必须加入的频道。
2. **删除强制加入频道**：使用 `/deletejoinforcechannel` 删除强制加入频道。
3. **添加频道**：使用 `/addchannel` 添加新频道。
4. **删除频道**：使用 `/deletechannel` 删除现有频道。
5. **添加订阅**：使用 `/addsubscription` 为频道创建新订阅。
6. **删除订阅**：使用 `/deletesubscription` 删除现有订阅。
7. **封禁用户**：使用 `/banuser` 封禁用户。
8. **取消封禁用户**：使用 `/unbanuser` 解除用户封禁。
9. **添加管理员**：使用 `/addadmin` 赋予用户管理员权限。
10. **移除管理员**：使用 `/removeadmin` 撤销用户的管理员权限。
11. **显示所有管理员**：使用 `/showalladmin` 列出所有管理员。
12. **添加特殊用户**：使用 `/addspecialuser` 将用户标记为特殊。
13. **移除特殊用户**：使用 `/removespecialuser` 取消用户的特殊身份。
14. **导出表格为 CSV**：使用 `/exporttabletocsv` 将数据库表导出为 CSV 文件。

请输入相应命令来执行所需操作。
"""
        },
        "selectchannelsubscriptions": {
            "text": "请选择您的频道。"
        },
        "selectsubscriptionsstate": {
            "text": "请选择您的订阅。"
        },
        "selectcryptostate": {
            "text": "请选择您的加密货币。"
        },
        "sendpaymentlinkstate": {
            "text": "请使用以下链接完成付款。"
        },
        "checkpaymentstatusstate": {
            "text": "点击下面的按钮检查您的付款状态。\n发票编号：",
            "keyboard": [
                {"text": "检查付款状态", "callback_data": ""}
            ]
        },
        "addforcedjoinchannel": {
            "text": "请输入要添加为强制加入的频道信息。"
        },
        "deleteforcedjoinchannel": {
            "text": "请输入要从强制加入中删除的频道信息。"
        },
        "addchannel": {
            "text": "请输入要添加的频道信息。"
        },
        "deletechannel": {
            "text": "请输入要删除的频道信息。"
        },
        "addsubscription": {
            "text": "请输入要添加的订阅信息。"
        },
        "deletesubscription": {
            "text": "请输入要删除的订阅信息。"
        },
        "banuser": {
            "text": "请输入要封禁的用户 ID。"
        },
        "unbanuser": {
            "text": "请输入要解除封禁的用户 ID。"
        },
        "addadmin": {
            "text": "请输入要赋予管理员权限的用户 ID。"
        },
        "removeadmin": {
            "text": "请输入要撤销管理员权限的用户 ID。"
        },
        "showalladmin": {
            "text": "以下是系统中所有管理员的列表。"
        },
        "addspecialuser": {
            "text": "请输入要标记为特殊用户的用户 ID。"
        },
        "removespecialuser": {
            "text": "请输入要移除特殊身份的用户 ID。"
        },
        "exporttabletocsv": {
            "text": "请输入要导出为 CSV 文件的表格名称。"
        },
    },
    "fr": {
        "starthandler": {
            "text": "Bienvenue ! Veuillez choisir une option :",
            "keyboard": [
                {"text": "Choisir un abonnement à une chaîne",
                 "callback_data": "buychannelsubscriptions"},
                {"text": "Choisir la langue", "callback_data": "select_language"}
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
        "setlanguagehandler": {
            "text": "Votre langue a été changée en français"
        },
        "selectchannelsubscriptionsstate": {
            "text": "Veuillez choisir votre chaîne."
        },
        "selectsubscriptionsstate": {
            "text": "Veuillez choisir votre abonnement."
        },
        "selectcryptostate": {
            "text": "Veuillez choisir votre cryptomonnaie."
        },
        "sendpaymentlinkstate": {
            "text": "Veuillez effectuer le paiement via le lien ci-dessous."
        },
        "checkpaymentstatusstate": {
            "text": "Cliquez sur le bouton ci-dessous pour vérifier l'état du paiement.\nNuméro de facture :",
            "keyboard": [
                {"text": "Vérifier le paiement", "callback_data": ""}
            ]
        },
        "cancel": {
            "text": "Votre paiement a été annulé ou expiré en raison d'une inactivité prolongée.\nVeuillez réessayer."
        },
        "joinrequesthandler": {
            "text": "Votre demande d'adhésion a été reçue. Veuillez patienter pour l'examen."
        },
        "addadminhandler": {
            "text": "Administrateur ajouté avec succès."
        },
        "addspecialuserhandler": {
            "text": "Utilisateur spécial ajouté avec succès."
        },
        "adminpannelhandler": {
            "text": "Bienvenue dans le panneau d'administration. Veuillez utiliser les commandes fournies pour gérer le système."
        },
        "banuserhandler": {
            "text": "Utilisateur banni avec succès."
        },
        "checkpaymentstatushandler": {
            "text": "Vérification du paiement en cours, veuillez patienter..."
        },
        "adminpannel": {
            "text":
            """
Guide des commandes du panneau d'administration :

1. **Ajouter une chaîne obligatoire** : utilisez `/addjoinforcechannel` pour ajouter une chaîne que les utilisateurs doivent rejoindre.
2. **Supprimer une chaîne obligatoire** : utilisez `/deletejoinforcechannel` pour supprimer une chaîne obligatoire.
3. **Ajouter une chaîne** : utilisez `/addchannel` pour ajouter une nouvelle chaîne.
4. **Supprimer une chaîne** : utilisez `/deletechannel` pour supprimer une chaîne existante.
5. **Ajouter un abonnement** : utilisez `/addsubscription` pour créer un nouvel abonnement pour une chaîne.
6. **Supprimer un abonnement** : utilisez `/deletesubscription` pour supprimer un abonnement existant.
7. **Bannir un utilisateur** : utilisez `/banuser` pour bannir un utilisateur.
8. **Débannir un utilisateur** : utilisez `/unbanuser` pour débannir un utilisateur.
9. **Ajouter un administrateur** : utilisez `/addadmin` pour accorder des privilèges d'administration à un utilisateur.
10. **Retirer un administrateur** : utilisez `/removeadmin` pour retirer les privilèges d'administration d'un utilisateur.
11. **Afficher tous les administrateurs** : utilisez `/showalladmin` pour afficher la liste de tous les administrateurs.
12. **Ajouter un utilisateur spécial** : utilisez `/addspecialuser` pour marquer un utilisateur comme spécial.
13. **Retirer un utilisateur spécial** : utilisez `/removespecialuser` pour retirer le statut spécial d'un utilisateur.
14. **Exporter une table en CSV** : utilisez `/exporttabletocsv` pour exporter une table de la base de données au format CSV.

Entrez la commande souhaitée pour effectuer l'action correspondante.
"""
        },
        "selectchannelsubscriptions": {
            "text": "Veuillez sélectionner votre chaîne."
        },
        "addforcedjoinchannel": {
            "text": "Veuillez entrer les informations de la chaîne à ajouter comme obligatoire."
        },
        "deleteforcedjoinchannel": {
            "text": "Veuillez entrer les informations de la chaîne à supprimer de l'obligation."
        },
        "addchannel": {
            "text": "Veuillez entrer les informations de la chaîne à ajouter."
        },
        "deletechannel": {
            "text": "Veuillez entrer les informations de la chaîne à supprimer."
        },
        "addsubscription": {
            "text": "Veuillez entrer les informations de l'abonnement à ajouter."
        },
        "deletesubscription": {
            "text": "Veuillez entrer les informations de l'abonnement à supprimer."
        },
        "banuser": {
            "text": "Veuillez entrer l'ID de l'utilisateur à bannir."
        },
        "unbanuser": {
            "text": "Veuillez entrer l'ID de l'utilisateur à débannir."
        },
        "addadmin": {
            "text": "Veuillez entrer l'ID de l'utilisateur à nommer administrateur."
        },
        "removeadmin": {
            "text": "Veuillez entrer l'ID de l'utilisateur à retirer des administrateurs."
        },
        "showalladmin": {
            "text": "Voici la liste de tous les administrateurs."
        },
        "addspecialuser": {
            "text": "Veuillez entrer l'ID de l'utilisateur à marquer comme spécial."
        },
        "removespecialuser": {
            "text": "Veuillez entrer l'ID de l'utilisateur à retirer du statut spécial."
        },
        "exporttabletocsv": {
            "text": "Veuillez entrer le nom de la table à exporter au format CSV."
        },
    },
    "tr": {
        "starthandler": {
            "text": "Hoş geldiniz! Lütfen bir seçenek seçin:",
            "keyboard": [
                {"text": "Bir kanal aboneliği satın al",
                 "callback_data": "buychannelsubscriptions"},
                {"text": "Dili değiştir", "callback_data": "select_language"}
            ]
        },
        "selectlanguagehandler": {
            "text": "Lütfen dilinizi seçin:",
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
            "text": "Diliniz Türkçe olarak ayarlandı."
        },
        "selectchannelsubscriptionsstate": {
            "text": "Lütfen bir kanal seçin."
        },
        "selectsubscriptionsstate": {
            "text": "Lütfen bir abonelik seçin."
        },
        "selectcryptostate": {
            "text": "Lütfen bir kripto para birimi seçin."
        },
        "sendpaymentlinkstate": {
            "text": "Lütfen aşağıdaki bağlantı üzerinden ödemenizi gerçekleştirin."
        },
        "checkpaymentstatusstate": {
            "text": "Ödeme durumunu kontrol etmek için aşağıdaki butona tıklayın.\nFatura numarası:",
            "keyboard": [
                {"text": "Ödemeyi Kontrol Et", "callback_data": ""}
            ]
        },
        "cancel": {
            "text": "Ödemeniz iptal edildi veya uzun süreli hareketsizlik nedeniyle zaman aşımına uğradı.\nLütfen tekrar deneyin."
        },
        "joinrequesthandler": {
            "text": "Katılım isteğiniz alındı. Lütfen onay için bekleyin."
        },
        "addadminhandler": {
            "text": "Yönetici başarıyla eklendi."
        },
        "addspecialuserhandler": {
            "text": "Özel kullanıcı başarıyla eklendi."
        },
        "adminpannelhandler": {
            "text": "Yönetici paneline hoş geldiniz. Sistemi yönetmek için komutları kullanın."
        },
        "banuserhandler": {
            "text": "Kullanıcı başarıyla yasaklandı."
        },
        "checkpaymentstatushandler": {
            "text": "Ödeme durumu kontrol ediliyor, lütfen bekleyin..."
        },
        "adminpannel": {
            "text":
            """
Yönetici Paneli Komut Rehberi:

1. **Zorunlu kanal ekle**: `/addjoinforcechannel` komutuyla kullanıcıların katılması gereken bir kanal ekleyin.
2. **Zorunlu kanal sil**: `/deletejoinforcechannel` komutuyla zorunlu bir kanalı silin.
3. **Kanal ekle**: `/addchannel` komutuyla yeni bir kanal ekleyin.
4. **Kanal sil**: `/deletechannel` komutuyla mevcut bir kanalı silin.
5. **Abonelik ekle**: `/addsubscription` komutuyla yeni bir kanal aboneliği oluşturun.
6. **Abonelik sil**: `/deletesubscription` komutuyla mevcut bir aboneliği silin.
7. **Kullanıcı yasakla**: `/banuser` komutuyla bir kullanıcıyı yasaklayın.
8. **Kullanıcı yasağını kaldır**: `/unbanuser` komutuyla bir kullanıcının yasağını kaldırın.
9. **Yönetici ekle**: `/addadmin` komutuyla bir kullanıcıya yönetici yetkisi verin.
10. **Yönetici kaldır**: `/removeadmin` komutuyla bir kullanıcının yönetici yetkisini kaldırın.
11. **Tüm yöneticileri göster**: `/showalladmin` komutuyla tüm yöneticileri görüntüleyin.
12. **Özel kullanıcı ekle**: `/addspecialuser` komutuyla özel kullanıcı olarak işaretleyin.
13. **Özel kullanıcı sil**: `/removespecialuser` komutuyla özel kullanıcıyı kaldırın.
14. **CSV dışa aktar**: `/exporttabletocsv` komutuyla bir veritabanı tablosunu CSV formatında dışa aktarın.

İlgili işlemi yapmak için istediğiniz komutu girin.
"""
        },
        "selectchannelsubscriptions": {
            "text": "Lütfen bir kanal seçin."
        },
        "addforcedjoinchannel": {
            "text": "Lütfen zorunlu olarak eklenecek kanal bilgilerini girin."
        },
        "deleteforcedjoinchannel": {
            "text": "Lütfen zorunluluktan kaldırılacak kanal bilgilerini girin."
        },
        "addchannel": {
            "text": "Lütfen eklenecek kanal bilgilerini girin."
        },
        "deletechannel": {
            "text": "Lütfen silinecek kanal bilgilerini girin."
        },
        "addsubscription": {
            "text": "Lütfen eklenecek abonelik bilgilerini girin."
        },
        "deletesubscription": {
            "text": "Lütfen silinecek abonelik bilgilerini girin."
        },
        "banuser": {
            "text": "Lütfen yasaklanacak kullanıcının ID'sini girin."
        },
        "unbanuser": {
            "text": "Lütfen yasağı kaldırılacak kullanıcının ID'sini girin."
        },
        "addadmin": {
            "text": "Lütfen yönetici olarak atanacak kullanıcının ID'sini girin."
        },
        "removeadmin": {
            "text": "Lütfen yöneticilikten çıkarılacak kullanıcının ID'sini girin."
        },
        "showalladmin": {
            "text": "Tüm yöneticilerin listesi aşağıdadır."
        },
        "addspecialuser": {
            "text": "Lütfen özel kullanıcı olarak eklenecek kullanıcının ID'sini girin."
        },
        "removespecialuser": {
            "text": "Lütfen özel kullanıcı statüsü kaldırılacak kullanıcının ID'sini girin."
        },
        "exporttabletocsv": {
            "text": "Lütfen CSV olarak dışa aktarılacak tablo adını girin."
        },
    },
    "it": {
        "starthandler": {
            "text": "Benvenuto! Seleziona un'opzione:",
            "keyboard": [
                {"text": "Acquista un abbonamento al canale",
                 "callback_data": "buychannelsubscriptions"},
                {"text": "Cambia lingua", "callback_data": "select_language"}
            ]
        },
        "selectlanguagehandler": {
            "text": "Seleziona la tua lingua:",
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
            "text": "La tua lingua è stata impostata su Italiano."
        },
        "selectchannelsubscriptionsstate": {
            "text": "Seleziona un canale."
        },
        "selectsubscriptionsstate": {
            "text": "Seleziona un abbonamento."
        },
        "selectcryptostate": {
            "text": "Seleziona una criptovaluta."
        },
        "sendpaymentlinkstate": {
            "text": "Effettua il pagamento utilizzando il link qui sotto."
        },
        "checkpaymentstatusstate": {
            "text": "Fai clic sul pulsante qui sotto per controllare lo stato del pagamento.\nNumero della fattura:",
            "keyboard": [
                {"text": "Controlla pagamento", "callback_data": ""}
            ]
        },
        "cancel": {
            "text": "Il pagamento è stato annullato o è scaduto per inattività prolungata.\nPer favore, riprova."
        },
        "joinrequesthandler": {
            "text": "La tua richiesta di adesione è stata ricevuta. Attendi l'approvazione."
        },
        "addadminhandler": {
            "text": "Amministratore aggiunto con successo."
        },
        "addspecialuserhandler": {
            "text": "Utente speciale aggiunto con successo."
        },
        "adminpannelhandler": {
            "text": "Benvenuto nel pannello di amministrazione. Usa i comandi per gestire il sistema."
        },
        "banuserhandler": {
            "text": "Utente bloccato con successo."
        },
        "checkpaymentstatushandler": {
            "text": "Controllo dello stato del pagamento in corso, attendere..."
        },
        "adminpannel": {
            "text":
            """
Guida ai comandi del pannello di amministrazione:

1. **Aggiungi canale obbligatorio**: usa `/addjoinforcechannel` per aggiungere un canale obbligatorio.
2. **Rimuovi canale obbligatorio**: usa `/deletejoinforcechannel` per rimuovere un canale obbligatorio.
3. **Aggiungi canale**: usa `/addchannel` per aggiungere un nuovo canale.
4. **Rimuovi canale**: usa `/deletechannel` per rimuovere un canale.
5. **Aggiungi abbonamento**: usa `/addsubscription` per creare un nuovo abbonamento.
6. **Rimuovi abbonamento**: usa `/deletesubscription` per rimuovere un abbonamento esistente.
7. **Blocca utente**: usa `/banuser` per bloccare un utente.
8. **Sblocca utente**: usa `/unbanuser` per sbloccare un utente.
9. **Aggiungi amministratore**: usa `/addadmin` per nominare un utente come amministratore.
10. **Rimuovi amministratore**: usa `/removeadmin` per revocare l'accesso da amministratore.
11. **Mostra tutti gli amministratori**: usa `/showalladmin` per vedere tutti gli amministratori.
12. **Aggiungi utente speciale**: usa `/addspecialuser` per contrassegnare un utente come speciale.
13. **Rimuovi utente speciale**: usa `/removespecialuser` per rimuovere il contrassegno speciale.
14. **Esporta CSV**: usa `/exporttabletocsv` per esportare una tabella in formato CSV.

Inserisci il comando corrispondente per eseguire un'operazione.
"""
        },
        "selectchannelsubscriptions": {
            "text": "Seleziona un canale."
        },
        "addforcedjoinchannel": {
            "text": "Inserisci le informazioni del canale da aggiungere come obbligatorio."
        },
        "deleteforcedjoinchannel": {
            "text": "Inserisci le informazioni del canale da rimuovere dai canali obbligatori."
        },
        "addchannel": {
            "text": "Inserisci le informazioni del canale da aggiungere."
        },
        "deletechannel": {
            "text": "Inserisci le informazioni del canale da eliminare."
        },
        "addsubscription": {
            "text": "Inserisci le informazioni dell'abbonamento da aggiungere."
        },
        "deletesubscription": {
            "text": "Inserisci le informazioni dell'abbonamento da eliminare."
        },
        "banuser": {
            "text": "Inserisci l'ID dell'utente da bloccare."
        },
        "unbanuser": {
            "text": "Inserisci l'ID dell'utente da sbloccare."
        },
        "addadmin": {
            "text": "Inserisci l'ID dell'utente da nominare amministratore."
        },
        "removeadmin": {
            "text": "Inserisci l'ID dell'amministratore da rimuovere."
        },
        "showalladmin": {
            "text": "Ecco l'elenco di tutti gli amministratori."
        },
        "addspecialuser": {
            "text": "Inserisci l'ID dell'utente da aggiungere come speciale."
        },
        "removespecialuser": {
            "text": "Inserisci l'ID dell'utente da rimuovere dallo stato speciale."
        },
        "exporttabletocsv": {
            "text": "Inserisci il nome della tabella da esportare in formato CSV."
        },
    },
    "pt": {
        "starthandler": {
            "text": "Bem-vindo! Por favor, selecione uma opção:",
            "keyboard": [
                {"text": "Comprar assinatura de canal",
                 "callback_data": "buychannelsubscriptions"},
                {"text": "Alterar idioma", "callback_data": "select_language"}
            ]
        },
        "selectlanguagehandler": {
            "text": "Selecione seu idioma:",
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
            "text": "Seu idioma foi alterado para Português."
        },
        "selectchannelsubscriptionsstate": {
            "text": "Selecione um canal."
        },
        "selectsubscriptionsstate": {
            "text": "Selecione uma assinatura."
        },
        "selectcryptostate": {
            "text": "Selecione uma criptomoeda."
        },
        "sendpaymentlinkstate": {
            "text": "Faça o pagamento usando o link abaixo."
        },
        "checkpaymentstatusstate": {
            "text": "Clique no botão abaixo para verificar o status do pagamento.\nNúmero da fatura:",
            "keyboard": [
                {"text": "Verificar pagamento", "callback_data": ""}
            ]
        },
        "cancel": {
            "text": "O pagamento foi cancelado ou expirou por inatividade prolongada.\nPor favor, tente novamente."
        },
        "joinrequesthandler": {
            "text": "Sua solicitação de ingresso foi recebida. Por favor, aguarde aprovação."
        },
        "addadminhandler": {
            "text": "Administrador adicionado com sucesso."
        },
        "addspecialuserhandler": {
            "text": "Usuário especial adicionado com sucesso."
        },
        "adminpannelhandler": {
            "text": "Bem-vindo ao painel de administração. Use os comandos para gerenciar o sistema."
        },
        "banuserhandler": {
            "text": "Usuário bloqueado com sucesso."
        },
        "checkpaymentstatushandler": {
            "text": "Verificando o status do pagamento, por favor aguarde..."
        },
        "adminpannel": {
            "text":
            """
Guia de comandos do painel de administração:

1. **Adicionar canal obrigatório**: use `/addjoinforcechannel` para adicionar um canal obrigatório.
2. **Remover canal obrigatório**: use `/deletejoinforcechannel` para remover um canal obrigatório.
3. **Adicionar canal**: use `/addchannel` para adicionar um novo canal.
4. **Remover canal**: use `/deletechannel` para remover um canal.
5. **Adicionar assinatura**: use `/addsubscription` para criar uma nova assinatura.
6. **Remover assinatura**: use `/deletesubscription` para remover uma assinatura existente.
7. **Bloquear usuário**: use `/banuser` para bloquear um usuário.
8. **Desbloquear usuário**: use `/unbanuser` para desbloquear um usuário.
9. **Adicionar administrador**: use `/addadmin` para promover um usuário a administrador.
10. **Remover administrador**: use `/removeadmin` para revogar o acesso de administrador.
11. **Mostrar todos os administradores**: use `/showalladmin` para ver todos os administradores.
12. **Adicionar usuário especial**: use `/addspecialuser` para marcar um usuário como especial.
13. **Remover usuário especial**: use `/removespecialuser` para remover o status especial de um usuário.
14. **Exportar CSV**: use `/exporttabletocsv` para exportar uma tabela em formato CSV.

Digite o comando correspondente para executar a operação.
"""
        },
        "selectchannelsubscriptions": {
            "text": "Selecione um canal."
        },
        "addforcedjoinchannel": {
            "text": "Insira as informações do canal a ser adicionado como obrigatório."
        },
        "deleteforcedjoinchannel": {
            "text": "Insira as informações do canal a ser removido da obrigatoriedade."
        },
        "addchannel": {
            "text": "Insira as informações do canal a ser adicionado."
        },
        "deletechannel": {
            "text": "Insira as informações do canal a ser removido."
        },
        "addsubscription": {
            "text": "Insira as informações da assinatura a ser adicionada."
        },
        "deletesubscription": {
            "text": "Insira as informações da assinatura a ser removida."
        },
        "banuser": {
            "text": "Insira o ID do usuário a ser bloqueado."
        },
        "unbanuser": {
            "text": "Insira o ID do usuário a ser desbloqueado."
        },
        "addadmin": {
            "text": "Insira o ID do usuário a ser promovido a administrador."
        },
        "removeadmin": {
            "text": "Insira o ID do administrador a ser removido."
        },
        "showalladmin": {
            "text": "Aqui está a lista de todos os administradores."
        },
        "addspecialuser": {
            "text": "Insira o ID do usuário a ser marcado como especial."
        },
        "removespecialuser": {
            "text": "Insira o ID do usuário a ser removido da condição de especial."
        },
        "exporttabletocsv": {
            "text": "Insira o nome da tabela a ser exportada para CSV."
        },
    },
    "nl": {
        "starthandler": {
            "text": "Welkom! Selecteer alstublieft een optie:",
            "keyboard": [
                {"text": "Kanaalabonnement kopen",
                 "callback_data": "buychannelsubscriptions"},
                {"text": "Taal wijzigen", "callback_data": "select_language"}
            ]
        },
        "selectlanguagehandler": {
            "text": "Selecteer uw taal:",
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
            "text": "Uw taal is gewijzigd naar Nederlands."
        },
        "selectchannelsubscriptionsstate": {
            "text": "Selecteer een kanaal."
        },
        "selectsubscriptionsstate": {
            "text": "Selecteer een abonnement."
        },
        "selectcryptostate": {
            "text": "Selecteer een cryptocurrency."
        },
        "sendpaymentlinkstate": {
            "text": "Voer de betaling uit via de onderstaande link."
        },
        "checkpaymentstatusstate": {
            "text": "Klik op de knop hieronder om de betalingsstatus te controleren.\nFactuurnummer:",
            "keyboard": [
                {"text": "Controleer betaling", "callback_data": ""}
            ]
        },
        "cancel": {
            "text": "De betaling is geannuleerd of verlopen vanwege langdurige inactiviteit.\nProbeer het opnieuw."
        },
        "joinrequesthandler": {
            "text": "Uw verzoek om deel te nemen is ontvangen. Wacht alstublieft op goedkeuring."
        },
        "addadminhandler": {
            "text": "Beheerder succesvol toegevoegd."
        },
        "addspecialuserhandler": {
            "text": "Speciale gebruiker succesvol toegevoegd."
        },
        "adminpannelhandler": {
            "text": "Welkom bij het beheerderspaneel. Gebruik de commando's om het systeem te beheren."
        },
        "banuserhandler": {
            "text": "Gebruiker succesvol verbannen."
        },
        "checkpaymentstatushandler": {
            "text": "Bezig met controleren van de betalingsstatus, een moment geduld..."
        },
        "adminpannel": {
            "text":
            """
Beheerder Commandogids:

1. **Verplicht kanaal toevoegen**: gebruik `/addjoinforcechannel` om een verplicht kanaal toe te voegen.
2. **Verplicht kanaal verwijderen**: gebruik `/deletejoinforcechannel` om een verplicht kanaal te verwijderen.
3. **Kanaal toevoegen**: gebruik `/addchannel` om een nieuw kanaal toe te voegen.
4. **Kanaal verwijderen**: gebruik `/deletechannel` om een kanaal te verwijderen.
5. **Abonnement toevoegen**: gebruik `/addsubscription` om een nieuw abonnement aan te maken.
6. **Abonnement verwijderen**: gebruik `/deletesubscription` om een bestaand abonnement te verwijderen.
7. **Gebruiker verbannen**: gebruik `/banuser` om een gebruiker te blokkeren.
8. **Gebruiker deblokkeren**: gebruik `/unbanuser` om een gebruiker te deblokkeren.
9. **Beheerder toevoegen**: gebruik `/addadmin` om een gebruiker beheerder te maken.
10. **Beheerder verwijderen**: gebruik `/removeadmin` om beheerdersrechten te verwijderen.
11. **Alle beheerders tonen**: gebruik `/showalladmin` om alle beheerders te bekijken.
12. **Speciale gebruiker toevoegen**: gebruik `/addspecialuser` om een gebruiker speciaal te markeren.
13. **Speciale gebruiker verwijderen**: gebruik `/removespecialuser` om de speciale status te verwijderen.
14. **CSV exporteren**: gebruik `/exporttabletocsv` om een tabel naar CSV te exporteren.

Typ het overeenkomstige commando om de actie uit te voeren.
"""
        },
        "selectchannelsubscriptions": {
            "text": "Selecteer een kanaal."
        },
        "addforcedjoinchannel": {
            "text": "Voer de informatie van het toe te voegen verplichte kanaal in."
        },
        "deleteforcedjoinchannel": {
            "text": "Voer de informatie van het te verwijderen verplichte kanaal in."
        },
        "addchannel": {
            "text": "Voer de informatie van het toe te voegen kanaal in."
        },
        "deletechannel": {
            "text": "Voer de informatie van het te verwijderen kanaal in."
        },
        "addsubscription": {
            "text": "Voer de informatie van het toe te voegen abonnement in."
        },
        "deletesubscription": {
            "text": "Voer de informatie van het te verwijderen abonnement in."
        },
        "banuser": {
            "text": "Voer de ID in van de gebruiker die u wilt blokkeren."
        },
        "unbanuser": {
            "text": "Voer de ID in van de gebruiker die u wilt deblokkeren."
        },
        "addadmin": {
            "text": "Voer de ID in van de gebruiker die u tot beheerder wilt maken."
        },
        "removeadmin": {
            "text": "Voer de ID in van de beheerder die u wilt verwijderen."
        },
        "showalladmin": {
            "text": "Hier is de lijst met alle beheerders."
        },
        "addspecialuser": {
            "text": "Voer de ID in van de gebruiker die u als speciaal wilt markeren."
        },
        "removespecialuser": {
            "text": "Voer de ID in van de gebruiker van wie u de speciale status wilt verwijderen."
        },
        "exporttabletocsv": {
            "text": "Voer de naam in van de tabel die u naar CSV wilt exporteren."
        },
    },
}
