from handlers import *
from handlers.handlers_permissions import permissions
from model import User


class ShowAllAdminHandler(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]
    def __init__(self):
        super().__init__(parent=self)

    async def get(self):
        await self.show_pannel()

    async def get_text(self):
        admins = User.filter(is_admin=1)
        text = ""
        if not admins:
            text = "No admins found."
        else:
            admin_list = "List of Admins:\n"
            for admin in admins:
                admin_list += f"- Chat ID: {admin.chat_id}, Username: {admin.username if admin.username else 'N/A'}\n"
            admin_list += "Total Admins: {}".format(len(admins))
            text = admin_list
        return text
