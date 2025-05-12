from handlers import *
from handlers.handlers_permissions import permissions

class AdminPannelHandler(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        user = self.get_or_create_user()
        if user.is_admin == 1:
            await self.show_pannel()


