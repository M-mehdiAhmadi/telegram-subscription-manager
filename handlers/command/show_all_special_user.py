from handlers import *
from handlers.handlers_permissions import permissions
from model import User


class ShowAllSpecialUserHandler(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]
    def __init__(self):
        super().__init__(parent=self)

    async def get(self):
        await self.show_pannel()

    async def get_text(self):
        special_users = User.filter(is_special=1)
        text = ""
        if not special_users:
            text = "No special users found."
        else:
            admin_list = "List of Special Users:\n"
            for user in special_users:
                admin_list += f"- Chat ID: {user.chat_id}, Username: {user.username if user.username else 'N/A'}\n"
            admin_list += "Total Special Users: {}".format(len(special_users))
            text = admin_list
        return text
