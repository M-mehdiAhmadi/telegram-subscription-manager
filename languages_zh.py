zh = {
    "starthandler": {
        "text": "欢迎！请选择一个选项：",
        "keyboard": [
            {"text": "选择频道订阅", "callback_data": "buychannelsubscriptions"},
            {"text": "选择语言", "callback_data": "select_language"}
        ]
    },
    "selectlanguagehandler": {
        "text": "请选择一种语言：",
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
        "text": "您的语言已更改为中文。"
    },
    "selectchannelsubscriptionstate": {
        "text": "请选择您的频道。"
    },
    "selectsubscriptionsstate": {
        "text": "请选择您的订阅。"
    },
    "selectcryptostate": {
        "text": "请选择您的加密货币。"
    },
    "sendpaymentlinkstate": {
        "text": "请使用以下链接付款。"
    },
    "checkpaymentstatusstate": {
        "text": "点击下方按钮查看付款状态。\n发票编号：",
        "keyboard": [
            {"text": "检查付款状态", "callback_data": ""}
        ]
    },
    "cancel": {
        "text": "由于长时间未操作，您的付款已被取消或已过期。\n请重试。"
    },
    "joinrequesthandler": {
        "text": "您的加入请求已收到，请等待批准。"
    },
    "addadminhandler": {
        "text": "请输入要授予管理员权限的用户ID。"
    },
    "addspecialuserhandler": {
        "text": "请输入要设为特殊用户的用户ID。"
    },
    "banuserhandler": {
        "text": "请输入要封禁的用户ID。"
    },
    "checkpaymentstatushandler": {
        "text": "正在检查付款状态，请稍候..."
    },
    "adminpannelhandler": {
        "text": """
管理员面板命令指南：

1. **添加强制加入频道**：使用 `/addjoinforcechannel` 添加用户必须加入的频道。
2. **删除强制加入频道**：使用 `/deletejoinforcechannel` 删除强制加入频道。
3. **添加频道**：使用 `/addchannel` 添加新频道。
4. **删除频道**：使用 `/deletechannel` 删除现有频道。
5. **添加订阅**：使用 `/addsubscription` 为频道创建新订阅。
6. **删除订阅**：使用 `/deletesubscription` 删除现有订阅。
7. **封禁用户**：使用 `/banuser` 封禁用户。
8. **解除封禁**：使用 `/unbanuser` 解除封禁。
9. **添加管理员**：使用 `/addadmin` 给予用户管理员权限。
10. **移除管理员**：使用 `/removeadmin` 撤销用户的管理员权限。
11. **查看所有管理员**：使用 `/showalladmin` 查看所有管理员列表。
12. **添加特殊用户**：使用 `/addspecialuser` 将用户设为特殊用户。
13. **移除特殊用户**：使用 `/removespecialuser` 移除用户的特殊状态。
14. **导出表为CSV**：使用 `/exporttabletocsv` 将数据库表导出为CSV文件。

请输入相应命令以执行操作。
"""
    },
    "selectchannelsubscriptions": {
        "text": "请选择您的频道。"
    },
    "unbanuserhandler": {
        "text": "请输入要解除封禁的用户ID。"
    },
    "removeadminhandler": {
        "text": "请输入要撤销管理员权限的用户ID。"
    },
    "showalladminhandler": {
        "text": "以下是系统中的管理员列表。"
    },
    "removespecialuserhandler": {
        "text": "请输入要移除特殊身份的用户ID。"
    },
    "exporttabletocsvhandler": {
        "text": "请输入要导出为CSV的表名。"
    },
    "addforcedjoinchannelhandler": {
        "text": "请输入要添加为强制加入的频道信息。"
    },
    "deleteforcedjoinchannelhandler": {
        "text": "请输入要从强制加入中移除的频道信息。"
    },
    "addchannelhandler": {
        "text": "请输入要添加的频道信息。"
    },
    "deletechannelhandler": {
        "text": "请输入要删除的频道信息。"
    },
    "addsubscriptionhandler": {
        "text": "请输入要添加的订阅信息。"
    },
    "deletesubscriptionhandler": {
        "text": "请输入要删除的订阅信息。"
    },
    "forcejoincheckerhandler": {
        "text": "要使用机器人，请先加入以下频道和群组："
    },
    "confirmdeletestate": {
        "text": "频道已成功删除。"
    },
    "deleteforcedjoinchannelstate": {
        "text": "请选择要删除的频道。"
    },
    "confirmdeletechannelstate": {
        "text": "频道已成功删除。"
    },
    "deletechannelstate": {
        "text": "请选择要删除的频道。"
    },
    "deletesubscriptionstate": {
        "text": "请选择要删除的订阅。"
    },
    "listsubscriptionsstate": {
        "text": "请选择您的订阅。"
    },
    "confirmdeleteanotherstate": {
        "text": "订阅已删除。\n您想删除另一个吗？"
    },
    "DeleteAnotherSubscriptionState": {
        "text": "请选择您的订阅。"
    },
    "showlistoftableshandler": {
        "text":
            "1. 频道\n"
            "2. 订阅\n"
            "3. 用户与订阅关系\n"
            "4. 特殊用户\n"
            "5. 付款记录\n"
            "6. 强制加入\n"
            "7. 用户"
    },
    "addchannelstate": {
        "text": "请发送频道链接。"
    },
    "getchatidstate": {
        "text": "频道添加成功。"
    },
    "addforcedjoinchannelstate": {
        "text": "请发送频道链接。"
    },
    "getchannellinkstate": {
        "text": "频道添加成功。"
    },
    "getchannelhandler": {
        "text": "请选择一个频道以设定特殊用户。"
    },
    "addsubscriptionstate": {
        "text": "请选择您的频道。"
    },
    "getnamestate": {
        "text": "请输入订阅名称。"
    },
    "getpriceState": {
        "text": "请输入价格（美元）。"
    },
    "getdaystate": {
        "text": "请输入订阅天数。"
    },
    "confirmaddanotherstate": {
        "text": "订阅已创建。是否添加另一个？"
    },
    "selectsubscriptionstate": {
        "text": "请选择您的订阅。"
    }
}
