languages = {
    "en": {
        "starthandler": {
            "text": "Welcome! Please select an option:",
            "keyboard": [
                {"text": "select channel Subscriptions", "callback_data": "selectchannelsubscriptions"},
                {"text": "select Language", "callback_data": "select_language"}
            ]
        }, "selectlanguagehandler": {
            "text": "please select language:",
            "keyboard": [
                {"text": "english", "callback_data": "en"},
                {"text": "فارسی", "callback_data": "fa"},

            ]


        },
        "setlanguagehandler":
        {
            "text": "your language has been changed to english"
        },
        "selectchannelsubscriptions":
        {

            "text": "choose your channel"


        }
    },
    "fa": {
        "starthandler": {
            "text": "سلام! لطفاً یک گزینه را انتخاب کنید:",
            "keyboard": [
                {"text": "انتخاب اشتراک کانال", "callback_data": "selectchannelsubscriptions"},
                {"text": "انتخاب زبان", "callback_data": "select_language"}
            ]
        },
        "selectlanguagehandler":
            {
            "text": "زبان را انتخاب کنید:",
            "keyboard": [
                {"text": "english", "callback_data": "en"},
                {"text": "فارسی", "callback_data": "fa"},

            ]


        },
            "setlanguagehandler":
                {
                    "text": "زبان شما به فارسی تغییر یافت"
        },
                "selectchannelsubscriptions":
                    {

                        "text": "کانال خود را انتخاب کنید"


        }
    }
}
