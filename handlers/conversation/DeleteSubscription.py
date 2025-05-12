from handlers.conversation import *
from model import Channel, Subscriptions
from handlers.handlers_permissions import permissions

class ConversationStates(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]
    
    LIST_CHANNELS = 1
    LIST_SUBSCRIPTIONS = 2
    CONFIRM_DELETE_ANOTHER = 3

class DeleteSubscriptionState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)

    async def get(self):
        await self.show_pannel()
        
        return self.LIST_CHANNELS
    
    async def get_keyboard(self):
        channels = Channel.get_all()
        
        keyboard = [
            [InlineKeyboardButton(text=channel.name, callback_data=f"select_channel:{channel.id}")]
            for channel in channels
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        return reply_markup
        

class ListSubscriptionsState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)

    async def get(self):
        query = self.update.callback_query
        await query.answer()

        channel_id = int(query.data.split(":")[-1])
        self.context.user_data['channel_id'] = channel_id
        await self.show_pannel()
        return self.LIST_SUBSCRIPTIONS
    async def get_keyboard(self):
        
        subscriptions = Subscriptions.filter(channel=self.context.user_data['channel_id'])

        

        keyboard = [
            [InlineKeyboardButton(text=sub.name, callback_data=f"delete_subscription:{sub.id}")]
            for sub in subscriptions
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        return reply_markup
        

class ConfirmDeleteAnotherState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)

    async def get(self):
        query = self.update.callback_query
        await query.answer()

        subscription_id = int(query.data.split(":")[-1])
        subscription = Subscriptions.filter(id=subscription_id)
        subscription[0].delete()
        await self.show_pannel()
        
        return self.CONFIRM_DELETE_ANOTHER

class DeleteAnotherSubscriptionState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)

    async def get(self):
        response = self.update.message.text.lower()

        if response == 'yes':
            await self.show_pannel()
            return self.LIST_CHANNELS
        else:
            await Cancel()(update=self.update, context=self.context)
            return ConversationHandler.END

class Cancel(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)

    async def get(self):
        
        return ConversationHandler.END

delete_subscription_handler = ConversationHandler(
    entry_points=[CommandHandler("delete_subscription", DeleteSubscriptionState().get)],
    states={
        ConversationStates.LIST_CHANNELS: [CallbackQueryHandler(ListSubscriptionsState().get, pattern="^select_channel_\d+$")],
        ConversationStates.LIST_SUBSCRIPTIONS: [CallbackQueryHandler(ConfirmDeleteAnotherState().get, pattern="^delete_subscription_\d+$")],
        ConversationStates.CONFIRM_DELETE_ANOTHER: [MessageHandler(filters.TEXT & ~filters.COMMAND, DeleteAnotherSubscriptionState().get)],
    },
    fallbacks=[CommandHandler("cancel", Cancel().get)],
    allow_reentry=True,
    conversation_timeout=120,  # 2 minutes
)