ja = {
    "starthandler": {
        "text": "ようこそ！オプションを選択してください：",
        "keyboard": [
            {"text": "チャンネル購読を選択", "callback_data": "buychannelsubscriptions"},
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
        "text": "言語が日本語に変更されました。"
    },
    "selectchannelsubscriptionstate": {
        "text": "チャンネルを選択してください。"
    },
    "selectsubscriptionsstate": {
        "text": "購読を選択してください。"
    },
    "selectcryptostate": {
        "text": "仮想通貨を選択してください。"
    },
    "sendpaymentlinkstate": {
        "text": "以下のリンクを使用してお支払いください。"
    },
    "checkpaymentstatusstate": {
        "text": "支払い状況を確認するには、下のボタンをクリックしてください。\n請求ID：",
        "keyboard": [
            {"text": "支払い状況を確認", "callback_data": ""}
        ]
    },
    "cancel": {
        "text": "支払いがキャンセルされたか、非アクティブのため期限切れになりました。\nもう一度お試しください。"
    },
    "joinrequesthandler": {
        "text": "参加リクエストが受信されました。承認をお待ちください。"
    },
    "addadminhandler": {
        "text": "管理者権限を付与するユーザーIDを入力してください。"
    },
    "addspecialuserhandler": {
        "text": "特別ユーザーとしてマークするユーザーIDを入力してください。"
    },
    "banuserhandler": {
        "text": "禁止するユーザーIDを入力してください。"
    },
    "checkpaymentstatushandler": {
        "text": "支払い状況を確認しています。しばらくお待ちください..."
    },
    "adminpannelhandler": {
        "text": """
管理パネル コマンドガイド：

1. **強制参加チャンネルを追加**：`/addjoinforcechannel` を使用して、ユーザーが参加する必要のあるチャンネルを追加します。
2. **強制参加チャンネルを削除**：`/deletejoinforcechannel` を使用して、強制チャンネルを削除します。
3. **チャンネルを追加**：`/addchannel` を使用して新しいチャンネルを追加します。
4. **チャンネルを削除**：`/deletechannel` を使用してチャンネルを削除します。
5. **購読を追加**：`/addsubscription` を使用して新しい購読を作成します。
6. **購読を削除**：`/deletesubscription` を使用して購読を削除します。
7. **ユーザーを禁止**：`/banuser` を使用してユーザーを禁止します。
8. **ユーザーの禁止を解除**：`/unbanuser` を使用して禁止を解除します。
9. **管理者を追加**：`/addadmin` を使用して管理者権限を付与します。
10. **管理者を削除**：`/removeadmin` を使用して管理者権限を削除します。
11. **全管理者を表示**：`/showalladmin` を使用して全管理者を表示します。
12. **特別ユーザーを追加**：`/addspecialuser` を使用してユーザーを特別扱いにします。
13. **特別ユーザーを削除**：`/removespecialuser` を使用して特別ユーザーから除外します。
14. **CSVへテーブルをエクスポート**：`/exporttabletocsv` を使用してデータベースのテーブルをCSVにエクスポートします。

希望の操作に対応するコマンドを入力してください。
"""
    },
    "selectchannelsubscriptions": {
        "text": "チャンネルを選択してください。"
    },
    "unbanuserhandler": {
        "text": "禁止を解除するユーザーIDを入力してください。"
    },
    "removeadminhandler": {
        "text": "管理者権限を削除するユーザーIDを入力してください。"
    },
    "showalladminhandler": {
        "text": "システム内のすべての管理者のリストです。"
    },
    "removespecialuserhandler": {
        "text": "特別ユーザーから削除するユーザーIDを入力してください。"
    },
    "exporttabletocsvhandler": {
        "text": "CSVファイルとしてエクスポートするテーブル名を入力してください。"
    },
    "addforcedjoinchannelhandler": {
        "text": "強制参加チャンネルとして追加するチャンネルの詳細を入力してください。"
    },
    "deleteforcedjoinchannelhandler": {
        "text": "強制参加チャンネルから削除するチャンネルの詳細を入力してください。"
    },
    "addchannelhandler": {
        "text": "追加するチャンネルの詳細を入力してください。"
    },
    "deletechannelhandler": {
        "text": "削除するチャンネルの詳細を入力してください。"
    },
    "addsubscriptionhandler": {
        "text": "追加する購読の詳細を入力してください。"
    },
    "deletesubscriptionhandler": {
        "text": "削除する購読の詳細を入力してください。"
    },
    "forcejoincheckerhandler": {
        "text": "このボットを使用するには、以下のチャンネルおよびグループに参加してください："
    },
    "confirmdeletestate": {
        "text": "チャンネルは正常に削除されました。"
    },
    "deleteforcedjoinchannelstate": {
        "text": "削除するチャンネルを選択してください。"
    },
    "confirmdeletechannelstate": {
        "text": "チャンネルは正常に削除されました。"
    },
    "deletechannelstate": {
        "text": "削除するチャンネルを選択してください。"
    },
    "deletesubscriptionstate": {
        "text": "削除する購読を選択してください。"
    },
    "listsubscriptionsstate": {
        "text": "購読を選択してください。"
    },
    "confirmdeleteanotherstate": {
        "text": "購読は削除されました。\n別の購読を削除しますか？"
    },
    "DeleteAnotherSubscriptionState": {
        "text": "購読を選択してください。"
    },
    "showlistoftableshandler": {
        "text":
            "1. チャンネル\n"
            "2. 購読\n"
            "3. ユーザー2購読\n"
            "4. 特別ユーザー\n"
            "5. 支払い\n"
            "6. 強制参加\n"
            "7. ユーザー"
    },
    "addchannelstate": {
        "text": "チャンネルのリンクを送信してください。"
    },
    "getchatidstate": {
        "text": "チャンネルが正常に追加されました。"
    },
    "addforcedjoinchannelstate": {
        "text": "チャンネルのリンクを送信してください。"
    },
    "getchannellinkstate": {
        "text": "チャンネルが正常に追加されました。"
    },
    "getchannelhandler": {
        "text": "ユーザーを特別としてマークするチャンネルを選択してください。"
    },
    "addsubscriptionstate": {
        "text": "チャンネルを選択してください。"
    },
    "getnamestate": {
        "text": "購読名を入力してください。"
    },
    "getpriceState": {
        "text": "価格（ドル）を入力してください。"
    },
    "getdaystate": {
        "text": "購読日数を入力してください。"
    },
    "confirmaddanotherstate": {
        "text": "購読が作成されました。別の購読を追加しますか？"
    },
    "selectsubscriptionstate": {
        "text": "購読を選択してください。"
    }
}
