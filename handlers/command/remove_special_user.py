from handlers import *
from handlers.handlers_permissions import permissions
from model import User

class RemoveSpecialUserHandler(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]
    def __init__(self):
        super().__init__(parent=self)
    
    async def get(self):
        args = self.context.args
        if not args:
            await self.update.message.reply_text("Usage: /remove_special <chat_id>|<username>")
            return

        identifier = args[0]

        # Check if identifier is a chat_id or username
        if identifier.isdigit():
            user = User.filter(chat_id=int(identifier))
        else:
            user = User.filter(username=identifier)

        # Remove special privileges
        user[0].is_special = 0
        user[0].save()
        await self.show_pannel()