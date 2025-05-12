from handlers import *
from handlers.handlers_permissions import permissions

class ShowListOfTablesHandler(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False
    
    async def get(self):
        await self.show_pannel()
