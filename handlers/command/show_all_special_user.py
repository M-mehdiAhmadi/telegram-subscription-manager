from handlers import *
from handlers.handlers_permissions import permissions
# from model import User
from api_client.user_client import UserClient

class ShowAllSpecialUserHandler(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]
    def __init__(self):
        super().__init__(parent=self)

    async def get(self):
        await self.show_pannel()

    async def get_text(self):
        userclient = UserClient()
        
        special_users = userclient.get_all_special()
        text = ""
        if not special_users:
            text = "No special users found."
        else:
            special_list = "List of Special Users:\n"
            # special_list = await super().get_text()
            for user in special_users:
                user = await self.context.bot.get_chat(chat_id=user.chat_id)
                special_list += f"- Chat ID: {user.id}, Username: {user.username if user.username else 'N/A'}\n"
            admin_list += "Total Special Users: {}".format(len(special_users))
            text = admin_list
        return text
