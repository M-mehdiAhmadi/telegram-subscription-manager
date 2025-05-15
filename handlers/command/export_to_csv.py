from handlers import *
from handlers.handlers_permissions import permissions
from api_client.export_csv_client import ExportClient


class ExportToCSVHandler(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]

    def __init__(self):
        super().__init__(parent=self)
        self.api = ExportClient()

    async def get(self):
        args = self.context.args
        if not args:
            await self.update.message.reply_text("Usage: /export_to_csv <table_name>")
            return

        table_name = args[0].lower()
        try:
            data = self.api.fetch_data(table_name)
            file_path = self.api.save_csv(data, f"exports/{table_name}.csv")
            await self.update.message.reply_document(document=open(file_path, "rb"))
        except Exception as e:
            await self.update.message.reply_text(f"❌ Error exporting table `{table_name}`:\n{e}")
