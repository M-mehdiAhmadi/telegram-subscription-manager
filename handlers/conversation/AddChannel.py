from handlers.conversation import *
# from model import Channel
from handlers.handlers_permissions import permissions
from api_client.channel_client import ChannelClient


class ConversationStates(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]
    GET_CHAT_ID = 1
    

class AddChannelState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        await self.show_pannel()
        return self.GET_CHAT_ID

class GetChatIDState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        chat_id = self.update.message.text
        channel = self.context.bot.get_chat(chat_id=chat_id)
        if not channel:
            self.update.message.reply_text("Channel not found. Please enter a valid chat ID.")
            return ConversationHandler.END
        link = self.context.bot.create_chat_invite_link(chat_id=chat_id)
        channelclient = ChannelClient()
        channelclient.create_channel(
            
            name=channel.title,
            chat_id=chat_id,
            link=link
        )
        
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

add_channel_handler = ConversationHandler(
    entry_points=[CommandHandler("add_channel", AddChannelState().get)],
    states={
        ConversationStates.GET_CHAT_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, GetChatIDState().get)],
    },
    fallbacks=[CommandHandler("cancel", Cancel().get)],
    allow_reentry=True,
    conversation_timeout=120,  # 2 minutes
)