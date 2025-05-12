from handlers.callbackquery import *
from handlers.handlers_permissions import permissions

class SelectLanguageHandler(BaseHandler):
    permissions = [permissions.IsActiveUserPermissionHandler]
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = True
        self.fallback_to_delete = True
    async def get(self):
        await self.show_pannel()
        await self.update.callback_query.answer()
    
    