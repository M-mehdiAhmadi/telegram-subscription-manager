from handlers import *
from handlers.handlers_permissions import permissions
from model import User

class UnbanUserHandler(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]

    def __init__(self):
        super().__init__(parent=self)
    
    async def get(self):
    
        # Extract chat_id or username from the command
        args = self.context.args
        if not args:
            await self.update.message.reply_text("Usage: /unban_user <chat_id>|<username>")
            return

        identifier = args[0]

        # Check if identifier is a chat_id or username
        if identifier.isdigit():
            user = User.filter(chat_id=int(identifier))
        else:
            user = User.filter(username=identifier)
        # Unban the user
        user[0].is_active = 1
        user[0].save()
        await self.show_pannel()
    
    