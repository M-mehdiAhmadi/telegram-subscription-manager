from handlers.command import *










class StartHandler(BaseHanler):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False
    async def get(self):
        await self.show_pannel()

        
    