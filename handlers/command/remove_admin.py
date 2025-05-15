from handlers import *
from handlers.handlers_permissions import permissions
# from model import User
from api_client.user_client import UserClient

class RemoveAdminHandler(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]

    def __init__(self):
        super().__init__(parent=self)
    
    async def get(self):
        args = self.context.args
        if not args:
            await self.update.message.reply_text("Usage: /remove_admin <chat_id>|<username>")
            return

        identifier = args[0]

        userclient = UserClient()
        # Check if identifier is a chat_id or username
        if identifier.isdigit():
            chat_id = identifier
        else:
            chat = await self.context.bot.get_chat(chat_id=identifier)
            chat_id = chat.id

            
            
        user = userclient.getUser_by_username(username=chat_id)
        # Remove admin privileges
        user.is_admin = False
        user.save()
        await self.show_pannel()