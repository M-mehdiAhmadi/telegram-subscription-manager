languages = {
    "en": {
        "starthandler": {
            "text": "Welcome! Please select an option:",
            "keyboard": [
                {"text": "Subscriptions", "callback_data": "subscriptions"},
                {"text": "Manage Channels", "callback_data": "manage_channels"},
                {"text": "select Language", "callback_data": "select_language"}
            ]
        },"selectlanguagehandler":{
            "text":"please select language:",
            "keyboard": [
                {"text": "english", "callback_data": "en"},
                {"text": "فارسی", "callback_data": "fa"},
                
                ]
            
            
        },
            "setlanguagehandler":
                {
                    "text" :"your language has been changed to english"
                }
    },
    "fa": {
        "starthandler": {
            "text": "سلام! لطفاً یک گزینه را انتخاب کنید:",
            "keyboard": [
                {"text": "اشتراک‌ها", "callback_data": "subscriptions"},
                {"text": "مدیریت کانال‌ها", "callback_data": "manage_channels"},
                {"text": "انتخاب زبان", "callback_data": "select_language"}
            ]
        },
        "selectlanguagehandler":
            {
            "text":"زبان را انتخاب کنید:",
            "keyboard": [
                {"text": "english", "callback_data": "en"},
                {"text": "فارسی", "callback_data": "fa"},
                
                ]
            
            
        },
            "setlanguagehandler":
                {
                    "text" :"زبان شما به فارسی تغییر یافت"
                }
    }
}
