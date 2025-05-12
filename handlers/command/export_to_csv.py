from handlers import *
from handlers.handlers_permissions import permissions

class ExportToCSVHandler(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False
    
    async def get(self):
        args =  self.context.args
        if not args:
            await self.update.message.reply_text("Usage: /export_to_csv <table_name>")
            return
        
        table_name = args[0]
        model_class = BaseModel.get_model_by_table_name(table_name)
        if not model_class:
            await self.update.message.reply_text(f"❌ No such table: {table_name}")
            return

        try:
            file_path = model_class.export_to_csv()
            await self.update.message.reply_document(document=open(file_path, "rb"))
        except Exception as e:
            await self.update.message.reply_text(f"⚠️ Error exporting CSV:\n{e}")
        