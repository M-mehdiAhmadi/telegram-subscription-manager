fa = {
    "starthandler": {
        "text": "خوش آمدید! لطفاً یک گزینه را انتخاب کنید:",
        "keyboard": [
            {"text": "انتخاب اشتراک کانال", "callback_data": "buychannelsubscriptions"},
            {"text": "انتخاب زبان", "callback_data": "select_language"}
        ]
    },
    "selectlanguagehandler": {
        "text": "لطفاً یک زبان انتخاب کنید:",
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
        "text": "زبان شما به فارسی تغییر یافت."
    },
    "selectchannelsubscriptionstate": {
        "text": "کانال مورد نظر را انتخاب کنید."
    },
    "selectsubscriptionsstate": {
        "text": "اشتراک مورد نظر را انتخاب کنید."
    },
    "selectcryptostate": {
        "text": "رمزارز مورد نظر را انتخاب کنید."
    },
    "sendpaymentlinkstate": {
        "text": "از لینک زیر برای پرداخت استفاده کنید."
    },
    "checkpaymentstatusstate": {
        "text": "روی دکمه زیر کلیک کنید تا وضعیت پرداخت بررسی شود.\nشناسه فاکتور:",
        "keyboard": [
            {"text": "بررسی وضعیت پرداخت", "callback_data": ""}
        ]
    },
    "cancel": {
        "text": "پرداخت شما لغو شده یا به دلیل عدم فعالیت منقضی شده است.\nلطفاً دوباره تلاش کنید."
    },
    "joinrequesthandler": {
        "text": "درخواست عضویت شما دریافت شد. لطفاً منتظر تأیید بمانید."
    },
    "addadminhandler": {
        "text": "لطفاً شناسه کاربر را برای اعطای دسترسی ادمین ارسال کنید."
    },
    "addspecialuserhandler": {
        "text": "لطفاً شناسه کاربر را برای افزودن به کاربران ویژه ارسال کنید."
    },
    "banuserhandler": {
        "text": "لطفاً شناسه کاربر را برای مسدود کردن وارد کنید."
    },
    "checkpaymentstatushandler": {
        "text": "در حال بررسی وضعیت پرداخت... لطفاً صبر کنید."
    },
    "adminpannelhandler": {
        "text": """
راهنمای دستورات پنل مدیریت:

1. **افزودن کانال اجبار به عضویت**: استفاده از دستور `/addjoinforcechannel`.
2. **حذف کانال اجبار به عضویت**: استفاده از دستور `/deletejoinforcechannel`.
3. **افزودن کانال**: استفاده از دستور `/addchannel`.
4. **حذف کانال**: استفاده از دستور `/deletechannel`.
5. **افزودن اشتراک**: استفاده از دستور `/addsubscription`.
6. **حذف اشتراک**: استفاده از دستور `/deletesubscription`.
7. **مسدود کردن کاربر**: استفاده از دستور `/banuser`.
8. **رفع مسدودی کاربر**: استفاده از دستور `/unbanuser`.
9. **افزودن ادمین**: استفاده از دستور `/addadmin`.
10. **حذف ادمین**: استفاده از دستور `/removeadmin`.
11. **نمایش همه ادمین‌ها**: استفاده از دستور `/showalladmin`.
12. **افزودن کاربر ویژه**: استفاده از دستور `/addspecialuser`.
13. **حذف کاربر ویژه**: استفاده از دستور `/removespecialuser`.
14. **خروجی گرفتن از جدول به CSV**: استفاده از دستور `/exporttabletocsv`.

لطفاً دستور مورد نظر را وارد کنید.
"""
    },
    "selectchannelsubscriptions": {
        "text": "لطفاً کانال خود را انتخاب کنید."
    },
    "unbanuserhandler": {
        "text": "لطفاً شناسه کاربر را برای رفع مسدودی ارسال کنید."
    },
    "removeadminhandler": {
        "text": "لطفاً شناسه کاربر را برای حذف دسترسی ادمین وارد کنید."
    },
    "showalladminhandler": {
        "text": "فهرست همه ادمین‌های سیستم:"
    },
    "removespecialuserhandler": {
        "text": "لطفاً شناسه کاربر را برای حذف از کاربران ویژه وارد کنید."
    },
    "exporttabletocsvhandler": {
        "text": "لطفاً نام جدول مورد نظر برای خروجی CSV را وارد کنید."
    },
    "addforcedjoinchannelhandler": {
        "text": "لطفاً مشخصات کانال مورد نظر برای افزودن به عضویت اجباری را وارد کنید."
    },
    "deleteforcedjoinchannelhandler": {
        "text": "لطفاً مشخصات کانال مورد نظر برای حذف از عضویت اجباری را وارد کنید."
    },
    "addchannelhandler": {
        "text": "لطفاً مشخصات کانال مورد نظر برای افزودن را ارسال کنید."
    },
    "deletechannelhandler": {
        "text": "لطفاً مشخصات کانال مورد نظر برای حذف را ارسال کنید."
    },
    "addsubscriptionhandler": {
        "text": "لطفاً مشخصات اشتراک مورد نظر برای افزودن را ارسال کنید."
    },
    "deletesubscriptionhandler": {
        "text": "لطفاً مشخصات اشتراک مورد نظر برای حذف را ارسال کنید."
    },
    "forcejoincheckerhandler": {
        "text": "برای استفاده از ربات، در کانال‌ها و گروه‌های زیر عضو شوید:"
    },
    "confirmdeletestate": {
        "text": "کانال با موفقیت حذف شد."
    },
    "deleteforcedjoinchannelstate": {
        "text": "یک کانال برای حذف انتخاب کنید."
    },
    "confirmdeletechannelstate": {
        "text": "کانال با موفقیت حذف شد."
    },
    "deletechannelstate": {
        "text": "کانال مورد نظر برای حذف را انتخاب کنید."
    },
    "deletesubscriptionstate": {
        "text": "اشتراک مورد نظر برای حذف را انتخاب کنید."
    },
    "listsubscriptionsstate": {
        "text": "اشتراک مورد نظر را انتخاب کنید."
    },
    "confirmdeleteanotherstate": {
        "text": "اشتراک حذف شد.\nآیا می‌خواهید اشتراک دیگری را حذف کنید؟"
    },
    "DeleteAnotherSubscriptionState": {
        "text": "اشتراک مورد نظر را انتخاب کنید."
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
        "text": "لینک کانال را ارسال کنید."
    },
    "getchatidstate": {
        "text": "کانال با موفقیت اضافه شد."
    },
    "addforcedjoinchannelstate": {
        "text": "لینک کانال را ارسال کنید."
    },
    "getchannellinkstate": {
        "text": "کانال با موفقیت اضافه شد."
    },
    "getchannelhandler": {
        "text": "برای علامت‌گذاری کاربر به عنوان ویژه، یک کانال انتخاب کنید."
    },
    "addsubscriptionstate": {
        "text": "کانال مورد نظر را انتخاب کنید."
    },
    "getnamestate": {
        "text": "نام اشتراک را وارد کنید."
    },
    "getpriceState": {
        "text": "قیمت را به دلار وارد کنید."
    },
    "getdaystate": {
        "text": "مدت زمان اشتراک را بر حسب روز وارد کنید."
    },
    "confirmaddanotherstate": {
        "text": "اشتراک ایجاد شد. آیا می‌خواهید اشتراک دیگری اضافه کنید؟"
    },
    "selectsubscriptionstate": {
        "text": "اشتراک مورد نظر را انتخاب کنید."
    }
}
