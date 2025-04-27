from handlers.callbackquery import *


class SetLanguageHandler(BaseHandler):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = True
        self.fallback_to_delete = True
    async def get(self):
        
        data = self.update.callback_query.data
        print(data)
        user = self.get_or_create_user()
        user.language = data
        user.save()
        
        await self.show_pannel()       
        await self.update.callback_query.answer()