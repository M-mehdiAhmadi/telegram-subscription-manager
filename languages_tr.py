tr = {
    "starthandler": {
        "text": "Hoş geldiniz! Lütfen bir seçenek seçin:",
        "keyboard": [
            {"text": "Kanal Aboneliklerini Seç", "callback_data": "buychannelsubscriptions"},
            {"text": "Dili Seç", "callback_data": "select_language"}
        ]
    },
    "selectlanguagehandler": {
        "text": "Lütfen bir dil seçin:",
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
        "text": "Diliniz Türkçe olarak değiştirildi."
    },
    "selectchannelsubscriptionstate": {
        "text": "Kanalınızı seçin."
    },
    "selectsubscriptionsstate": {
        "text": "Aboneliğinizi seçin."
    },
    "selectcryptostate": {
        "text": "Kripto paranızı seçin."
    },
    "sendpaymentlinkstate": {
        "text": "Ödeme yapmak için aşağıdaki bağlantıyı kullanın."
    },
    "checkpaymentstatusstate": {
        "text": "Ödeme durumunu kontrol etmek için aşağıdaki düğmeye tıklayın.\nFatura ID'si:",
        "keyboard": [
            {"text": "Ödeme Durumunu Kontrol Et", "callback_data": ""}
        ]
    },
    "cancel": {
        "text": "Ödemeniz iptal edildi veya hareketsizlik nedeniyle süresi doldu.\nLütfen tekrar deneyin."
    },
    "joinrequesthandler": {
        "text": "Katılma isteğiniz alındı. Lütfen onay bekleyin."
    },
    "addadminhandler": {
        "text": "Yönetici yetkisi vermek için kullanıcı ID'sini girin."
    },
    "addspecialuserhandler": {
        "text": "Özel olarak işaretlemek için kullanıcı ID'sini girin."
    },
    "banuserhandler": {
        "text": "Yasaklamak için kullanıcı ID'sini girin."
    },
    "checkpaymentstatushandler": {
        "text": "Ödeme durumu kontrol ediliyor. Lütfen bekleyin..."
    },
    "adminpannelhandler": {
        "text": """
Yönetici Paneli Komut Kılavuzu:

1. **Zorunlu Katılım Kanalı Ekle**: `/addjoinforcechannel` komutunu kullanarak bir zorunlu kanal ekleyin.
2. **Zorunlu Kanalı Sil**: `/deletejoinforcechannel` komutu ile zorunlu kanal silinir.
3. **Kanal Ekle**: `/addchannel` ile yeni bir kanal ekleyin.
4. **Kanal Sil**: `/deletechannel` ile mevcut kanalı silin.
5. **Abonelik Ekle**: `/addsubscription` komutu ile bir kanal için yeni bir abonelik oluşturun.
6. **Abonelik Sil**: `/deletesubscription` komutu ile bir aboneliği silin.
7. **Kullanıcıyı Yasakla**: `/banuser` komutu ile bir kullanıcıyı yasaklayın.
8. **Yasağı Kaldır**: `/unbanuser` komutu ile yasaklı kullanıcıyı serbest bırakın.
9. **Yönetici Ekle**: `/addadmin` komutu ile kullanıcıya yönetici yetkisi verin.
10. **Yönetici Kaldır**: `/removeadmin` komutu ile yönetici yetkisini kaldırın.
11. **Tüm Yöneticileri Göster**: `/showalladmin` komutu ile sistemdeki tüm yöneticileri görüntüleyin.
12. **Özel Kullanıcı Ekle**: `/addspecialuser` komutu ile kullanıcıyı özel yapın.
13. **Özel Kullanıcı Kaldır**: `/removespecialuser` komutu ile özel durumu kaldırın.
14. **Tabloyu CSV'ye Aktar**: `/exporttabletocsv` komutu ile tabloyu CSV dosyasına aktarın.

İşlemi gerçekleştirmek için ilgili komutu yazın.
"""
    },
    "selectchannelsubscriptions": {
        "text": "Lütfen kanalınızı seçin."
    },
    "unbanuserhandler": {
        "text": "Yasağı kaldırmak için kullanıcı ID'sini girin."
    },
    "removeadminhandler": {
        "text": "Yönetici yetkisini kaldırmak için kullanıcı ID'sini girin."
    },
    "showalladminhandler": {
        "text": "Sistemdeki tüm yöneticilerin listesi:"
    },
    "removespecialuserhandler": {
        "text": "Özel kullanıcıdan kaldırmak için kullanıcı ID'sini girin."
    },
    "exporttabletocsvhandler": {
        "text": "CSV olarak dışa aktarmak için tablo adını girin."
    },
    "addforcedjoinchannelhandler": {
        "text": "Zorunlu olarak eklenecek kanalın bilgilerini girin."
    },
    "deleteforcedjoinchannelhandler": {
        "text": "Zorunlu kanaldan silinecek kanalın bilgilerini girin."
    },
    "addchannelhandler": {
        "text": "Eklenecek kanalın bilgilerini girin."
    },
    "deletechannelhandler": {
        "text": "Silinecek kanalın bilgilerini girin."
    },
    "addsubscriptionhandler": {
        "text": "Eklenecek aboneliğin bilgilerini girin."
    },
    "deletesubscriptionhandler": {
        "text": "Silinecek aboneliğin bilgilerini girin."
    },
    "forcejoincheckerhandler": {
        "text": "Botu kullanabilmek için aşağıdaki kanal ve gruplara katılın:"
    },
    "confirmdeletestate": {
        "text": "Kanal başarıyla silindi."
    },
    "deleteforcedjoinchannelstate": {
        "text": "Silmek için bir kanal seçin."
    },
    "confirmdeletechannelstate": {
        "text": "Kanal başarıyla silindi."
    },
    "deletechannelstate": {
        "text": "Silmek için bir kanal seçin."
    },
    "deletesubscriptionstate": {
        "text": "Silmek için bir abonelik seçin."
    },
    "listsubscriptionsstate": {
        "text": "Aboneliğinizi seçin."
    },
    "confirmdeleteanotherstate": {
        "text": "Abonelik silindi.\nBaşka bir tane silmek ister misiniz?"
    },
    "DeleteAnotherSubscriptionState": {
        "text": "Aboneliğinizi seçin."
    },
    "showlistoftableshandler": {
        "text":
            "1. kanallar\n"
            "2. abonelikler\n"
            "3. user2subscriptions\n"
            "4. özel_kullanıcılar\n"
            "5. ödemeler\n"
            "6. zorunlu_kanallar\n"
            "7. kullanıcılar"
    },
    "addchannelstate": {
        "text": "Kanal bağlantısını gönderin."
    },
    "getchatidstate": {
        "text": "Kanal başarıyla eklendi."
    },
    "addforcedjoinchannelstate": {
        "text": "Kanal bağlantısını gönderin."
    },
    "getchannellinkstate": {
        "text": "Kanal başarıyla eklendi."
    },
    "getchannelhandler": {
        "text": "Kullanıcıyı özel yapmak için bir kanal seçin."
    },
    "addsubscriptionstate": {
        "text": "Kanalınızı seçin."
    },
    "getnamestate": {
        "text": "Abonelik adını girin."
    },
    "getpriceState": {
        "text": "Fiyatı dolar cinsinden girin."
    },
    "getdaystate": {
        "text": "Abonelik süresi (gün) girin."
    },
    "confirmaddanotherstate": {
        "text": "Abonelik oluşturuldu. Başka bir tane eklemek ister misiniz?"
    },
    "selectsubscriptionstate": {
        "text": "Aboneliğinizi seçin."
    }
}
