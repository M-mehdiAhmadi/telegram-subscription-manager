from handlers.conversation import *
from handlers.handlers_permissions import permissions
# from model import User
from api_client.user_client import UserClient


# class ShowAllAdminHandler(BaseHandler):
#     permissions = [permissions.IsAdminPermissionHandler]
#     def __init__(self):
#         super().__init__(parent=self)

#     async def get(self):
#         await self.show_pannel()

#     async def get_text(self):
#         userclient = UserClient()
#         admins = userclient.get_all_admin()
#         text = ""
#         if not admins:
#             text = "No admins found."
#         else:
#             admin_list = "List of Admins:\n"
#             # admin_list = await super().get_text()
#             for user in admins:
#                 admin = await self.context.bot.get_chat(chat_id=user.username)
#                 admin_list += f"- Chat ID: {admin.id}, Username: {admin.username if admin.username else 'N/A'}\n"
#             admin_list += "Total Admins: {}".format(len(admins))
#             text = admin_list
#         return text


class ConversationStates(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]
    

class ShowAllAdminState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = True
        self.fallback_to_delete = False
    
    async def get(self):
        await self.show_pannel()
        return ConversationHandler.END
    
    async def get_text(self):
        userclient = UserClient()
        admins = userclient.get_all_admin()
        text = ""
        if not admins:
            text = "No admins found."
        else:
            admin_list = "List of Admins:\n"
            # admin_list = await super().get_text()
            for user in admins:
                admin = await self.context.bot.get_chat(chat_id=user.username)
                admin_list += f"- Chat ID: {admin.id}, Username: {admin.username if admin.username else 'N/A'}\n"
            admin_list += "Total Admins: {}".format(len(admins))
            text = admin_list
        return text


class Cancel(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        await self.show_pannel()
        return ConversationHandler.END 


show_all_admin_conversation = ConversationHandler(
    entry_points=[CallbackQueryHandler(pattern=r"show_all_admin", callback=ShowAllAdminState())],
    states={
        0: [CommandHandler("cancel", Cancel())],
    },
    fallbacks=[CommandHandler("cancel", Cancel())],
    allow_reentry=True,
    conversation_timeout=120,  # 2 minutes
)
