from handlers.conversation import *
from handlers.handlers_permissions import permissions
# from model import Joinforce
from api_client.joinforce_client import JoinforceClient

class ConversationStates(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]
    LIST_CHANNELS = 1
    CONFIRM_DELETE = 2

class DeleteForcedJoinChannelState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        await self.show_pannel()
        return self.LIST_CHANNELS

    async def get_keyboard(self):
        joinforceclient = JoinforceClient()
        
        channels: list[JoinforceClient.Joinforce] = joinforceclient.get_all()

        if not channels:
            await self.context.bot.send_message(
                chat_id=self.chat_id,
                text="No forced join channels found."
            )
            return ConversationHandler.END

        keyboard = [
            [InlineKeyboardButton(text=channel.name, callback_data=f"delete_channel:{channel.id}")]
            for channel in channels
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        
        return reply_markup
    
class ConfirmDeleteState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        query = self.update.callback_query
        await query.answer()

        channel_id = int(query.data.split(":")[-1])
        
        joinforceclient = JoinforceClient()
        
        channel: JoinforceClient.Joinforce = joinforceclient.get_channel_by_id(id=channel_id)
        

        if not channel:
            await self.context.bot.send_message(
                chat_id=self.chat_id,
                text="Channel not found."
            )
            return ConversationHandler.END
        
        joinforceclient.delete(obj_id=channel.id)
        
        await self.show_pannel()
        
        return ConversationHandler.END

class Cancel(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        await self.show_pannel()
        return ConversationHandler.END

delete_forced_join_channel_handler = ConversationHandler(
    entry_points=[CommandHandler("delete_forced_join_channel", DeleteForcedJoinChannelState().get)],
    states={
        ConversationStates.LIST_CHANNELS: [CallbackQueryHandler(ConfirmDeleteState().get, pattern="^delete_channel_\d+$")],
    },
    fallbacks=[CommandHandler("cancel", Cancel().get)],
    allow_reentry=True,
    conversation_timeout=120,  # 2 minutes
)