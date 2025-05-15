ru = {
    "starthandler": {
        "text": "Добро пожаловать! Пожалуйста, выберите опцию:",
        "keyboard": [
            {"text": "Выбрать подписку на канал", "callback_data": "buychannelsubscriptions"},
            {"text": "Выбрать язык", "callback_data": "select_language"}
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
        "text": "Ваш язык был изменён на русский."
    },
    "selectchannelsubscriptionstate": {
        "text": "Выберите ваш канал."
    },
    "selectsubscriptionsstate": {
        "text": "Выберите подписку."
    },
    "selectcryptostate": {
        "text": "Выберите криптовалюту."
    },
    "sendpaymentlinkstate": {
        "text": "Используйте ссылку ниже для оплаты."
    },
    "checkpaymentstatusstate": {
        "text": "Нажмите кнопку ниже, чтобы проверить статус платежа.\nID счета:",
        "keyboard": [
            {"text": "Проверить статус платежа", "callback_data": ""}
        ]
    },
    "cancel": {
        "text": "Ваш платёж был отменён или истёк по бездействию.\nПожалуйста, попробуйте снова."
    },
    "joinrequesthandler": {
        "text": "Ваш запрос на вступление получен. Пожалуйста, подождите одобрения."
    },
    "addadminhandler": {
        "text": "Пожалуйста, укажите ID пользователя, чтобы назначить его администратором."
    },
    "addspecialuserhandler": {
        "text": "Пожалуйста, укажите ID пользователя, чтобы отметить его как особого."
    },
    "banuserhandler": {
        "text": "Пожалуйста, укажите ID пользователя, чтобы заблокировать его."
    },
    "checkpaymentstatushandler": {
        "text": "Проверка статуса платежа. Пожалуйста, подождите..."
    },
    "adminpannelhandler": {
        "text": """
Инструкция по командам панели администратора:

1. **Добавить обязательный канал**: используйте `/addjoinforcechannel`, чтобы добавить обязательный канал.
2. **Удалить обязательный канал**: используйте `/deletejoinforcechannel`, чтобы удалить обязательный канал.
3. **Добавить канал**: используйте `/addchannel`, чтобы добавить новый канал.
4. **Удалить канал**: используйте `/deletechannel`, чтобы удалить существующий канал.
5. **Добавить подписку**: используйте `/addsubscription`, чтобы создать новую подписку.
6. **Удалить подписку**: используйте `/deletesubscription`, чтобы удалить подписку.
7. **Заблокировать пользователя**: используйте `/banuser`, чтобы заблокировать пользователя.
8. **Разблокировать пользователя**: используйте `/unbanuser`, чтобы разблокировать пользователя.
9. **Добавить администратора**: используйте `/addadmin`, чтобы назначить администратора.
10. **Удалить администратора**: используйте `/removeadmin`, чтобы снять администратора.
11. **Показать всех администраторов**: используйте `/showalladmin`, чтобы вывести список всех администраторов.
12. **Добавить особого пользователя**: используйте `/addspecialuser`, чтобы отметить пользователя как особого.
13. **Удалить особого пользователя**: используйте `/removespecialuser`, чтобы убрать особый статус.
14. **Экспорт таблицы в CSV**: используйте `/exporttabletocsv`, чтобы экспортировать таблицу в CSV.

Введите соответствующую команду для выполнения действия.
"""
    },
    "selectchannelsubscriptions": {
        "text": "Пожалуйста, выберите ваш канал."
    },
    "unbanuserhandler": {
        "text": "Пожалуйста, укажите ID пользователя для разблокировки."
    },
    "removeadminhandler": {
        "text": "Пожалуйста, укажите ID пользователя для удаления прав администратора."
    },
    "showalladminhandler": {
        "text": "Вот список всех администраторов системы."
    },
    "removespecialuserhandler": {
        "text": "Пожалуйста, укажите ID пользователя для удаления из списка особых."
    },
    "exporttabletocsvhandler": {
        "text": "Пожалуйста, укажите имя таблицы для экспорта в CSV."
    },
    "addforcedjoinchannelhandler": {
        "text": "Пожалуйста, укажите данные канала для добавления в обязательные."
    },
    "deleteforcedjoinchannelhandler": {
        "text": "Пожалуйста, укажите данные канала для удаления из обязательных."
    },
    "addchannelhandler": {
        "text": "Пожалуйста, укажите данные канала для добавления."
    },
    "deletechannelhandler": {
        "text": "Пожалуйста, укажите данные канала для удаления."
    },
    "addsubscriptionhandler": {
        "text": "Пожалуйста, укажите данные подписки для добавления."
    },
    "deletesubscriptionhandler": {
        "text": "Пожалуйста, укажите данные подписки для удаления."
    },
    "forcejoincheckerhandler": {
        "text": "Чтобы использовать бота, вступите в следующие каналы и группы:"
    },
    "confirmdeletestate": {
        "text": "Канал успешно удалён."
    },
    "deleteforcedjoinchannelstate": {
        "text": "Выберите канал для удаления."
    },
    "confirmdeletechannelstate": {
        "text": "Канал успешно удалён."
    },
    "deletechannelstate": {
        "text": "Выберите канал для удаления."
    },
    "deletesubscriptionstate": {
        "text": "Выберите подписку для удаления."
    },
    "listsubscriptionsstate": {
        "text": "Выберите подписку."
    },
    "confirmdeleteanotherstate": {
        "text": "Подписка удалена.\nХотите удалить другую?"
    },
    "DeleteAnotherSubscriptionState": {
        "text": "Выберите подписку."
    },
    "showlistoftableshandler": {
        "text":
            "1. каналы\n"
            "2. подписки\n"
            "3. user2subscriptions\n"
            "4. особые_пользователи\n"
            "5. платежи\n"
            "6. обязательные_каналы\n"
            "7. пользователи"
    },
    "addchannelstate": {
        "text": "Отправьте ссылку на канал."
    },
    "getchatidstate": {
        "text": "Канал успешно добавлен."
    },
    "addforcedjoinchannelstate": {
        "text": "Отправьте ссылку на канал."
    },
    "getchannellinkstate": {
        "text": "Канал успешно добавлен."
    },
    "getchannelhandler": {
        "text": "Выберите канал, чтобы отметить пользователя как особого."
    },
    "addsubscriptionstate": {
        "text": "Выберите ваш канал."
    },
    "getnamestate": {
        "text": "Введите название подписки."
    },
    "getpriceState": {
        "text": "Введите цену в долларах."
    },
    "getdaystate": {
        "text": "Введите количество дней для подписки."
    },
    "confirmaddanotherstate": {
        "text": "Подписка создана. Хотите добавить ещё одну?"
    },
    "selectsubscriptionstate": {
        "text": "Выберите подписку."
    }
}
