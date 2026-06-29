from handlers.conversation import *
from handlers.handlers_permissions import permissions
# from model import User
from api_client.user_client import UserClient

# class RemoveAdminHandler(BaseHandler):
#     permissions = [permissions.IsAdminPermissionHandler]

#     def __init__(self):
#         super().__init__(parent=self)
    
#     async def get(self):
#         args = self.context.args
#         if not args:
#             await self.update.message.reply_text("Usage: /remove_admin <chat_id>|<username>")
#             return

#         identifier = args[0]

#         userclient = UserClient()
#         # Check if identifier is a chat_id or username
#         if identifier.isdigit():
#             chat_id = identifier
#         else:
#             chat = await self.context.bot.get_chat(chat_id=identifier)
#             chat_id = chat.id

            
            
#         user = userclient.getUser_by_username(username=chat_id)
#         # Remove admin privileges
#         user.is_admin = False
#         user.save()
#         await self.show_pannel()


class ConversationStates(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]
    GET_ADMIN = 1
    

class RemoveAminState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = True
        self.fallback_to_delete = False

    async def get(self):
        await self.show_pannel()
        return self.GET_ADMIN

class GetUserState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False
    
    async def get(self):
        identifier = self.update.message.text
        userclient = UserClient()
        if identifier.isdigit():
            chat_id = identifier
        else:
            chat = await self.context.bot.get_chat(chat_id=identifier)
            chat_id=chat.id

        user = userclient.getUser_by_username(username=chat_id)

        # Add admin privileges
        user.is_admin = False
        user.save()
        await self.show_pannel()


class Cancel(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        await self.show_pannel()
        return ConversationHandler.END 
    
ban_admin_conversation = ConversationHandler(
    entry_points=[CallbackQueryHandler(pattern=r"remove_admin", callback=RemoveAminState())],
    states={
        ConversationStates.GET_ADMIN: [MessageHandler(filters.TEXT & ~filters.COMMAND, GetUserState())],
    },
    fallbacks=[CommandHandler("cancel", Cancel())],
    allow_reentry=True,
    conversation_timeout=120,  # 2 minutes
)
