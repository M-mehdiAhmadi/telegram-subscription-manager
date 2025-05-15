from handlers.conversation import *
# from model import Channel
from handlers.handlers_permissions import permissions
from api_client.channel_client import ChannelClient

class ConversationStates(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]
    
    
    LIST_CHANNELS = 1

class DeleteChannelState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        
        await self.show_pannel()
        return self.LIST_CHANNELS
    
    async def get_keyboard(self):
        channelclient=ChannelClient()
        
        channels = channelclient.get_all()
        
        keyboard = [
            [InlineKeyboardButton(text=channel.name, callback_data=f"delete_channel:{channel.id}")]
            for channel in channels
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        return reply_markup

class ConfirmDeleteChannelState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        query = self.update.callback_query
        await query.answer()

        channel_id = int(query.data.split(":")[-1])
        channelclient=ChannelClient()
        channel = channelclient.get_channel_by_id(id=channel_id)

        if not channel:
            await self.context.bot.send_message(
                chat_id=self.chat_id,
                text="Channel not found."
            )
            return ConversationHandler.END

        channelclient.delete(obj_id=channel.id)
        
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

delete_channel_handler = ConversationHandler(
    entry_points=[CommandHandler("delete_channel", DeleteChannelState().get)],
    states={
        ConversationStates.LIST_CHANNELS: [CallbackQueryHandler(ConfirmDeleteChannelState().get, pattern="^delete_channel:\d+$")],
    },
    fallbacks=[CommandHandler("cancel", Cancel().get)],
    allow_reentry=True,
    conversation_timeout=120,  # 2 minutes
)