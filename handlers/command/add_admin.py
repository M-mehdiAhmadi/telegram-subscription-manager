from handlers import *
from handlers.handlers_permissions import permissions
from model import User

class AddAdminHandler(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]
    def __init__(self):
        super().__init__(parent=self)
    
    async def get(self):
        args = self.context.args
        if not args:
            await self.update.message.reply_text("Usage: /add_admin <chat_id>|<username>")
            return

        identifier = args[0]

        # Check if identifier is a chat_id or username
        if identifier.isdigit():
            user = User.filter(chat_id=int(identifier))
        else:
            user = User.filter(username=identifier)

        # Add admin privileges
        user[0].is_admin = 1
        user[0].save()
        await self.show_pannel()