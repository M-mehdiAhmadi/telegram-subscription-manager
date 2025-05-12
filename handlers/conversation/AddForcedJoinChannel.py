from handlers.conversation import *
from handlers.handlers_permissions import permissions

class ConversationStates(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]
    
    GET_CHANNEL_LINK = 1
    GET_CHANNEL_NAME = 2
    
class AddForcedJoinChannelState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        await self.show_pannel()
        return self.GET_CHANNEL_LINK

class GetChannelLinkState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        channel_link = self.update.message.text
        self.context.user_data["channel_link"] = channel_link
        await self.show_pannel()
        return self.GET_CHANNEL_NAME

class GetChannelNameState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        channel_name = self.update.message.text
        channel_link = self.context.user_data["channel_link"]
        joinforce = Joinforce(id=None,
                              channel_name=channel_name,
                              channel_link=channel_link)
        joinforce.save()
        del self.context.user_data["channel_link"]
        await self.show_pannel()
        return ConversationHandler.END

class Cancel(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        del self.context.user_data["channel_link"]
        await self.show_pannel()
        return ConversationHandler.END

add_forced_join_channel_handler = ConversationHandler(
    entry_points=[CommandHandler("add_forced_join_channel", AddForcedJoinChannelState().get)],
    states={
        ConversationStates.GET_CHANNEL_LINK: [MessageHandler(filters.TEXT & ~filters.COMMAND, GetChannelLinkState().get)],
        ConversationStates.GET_CHANNEL_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, GetChannelNameState().get)],
    },
    fallbacks=[CommandHandler("cancel", Cancel().get)],
    allow_reentry=True,
    conversation_timeout=120,  # 2 minutes
)