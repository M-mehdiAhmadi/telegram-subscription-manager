from handlers.conversation import *
from handlers.handlers_permissions import permissions
from api_client.channel_client import ChannelClient
from api_client.sub_client import SubscriptionClient

class ConversationStates(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]
    LIST_CHANNELS = 1
    GET_NAME = 2
    GET_PRICE = 3
    GET_DAY = 4
    CONFIRM_ADD_ANOTHER = 5

class AddSubscriptionState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        await self.show_pannel()
        return self.LIST_CHANNELS
    
    async def get_keyboard(self):
        channelclient = ChannelClient()
        
        channels = channelclient.get_all()
        
        if not channels:
            await self.context.bot.send_message(
                chat_id=self.chat_id,
                text="No channels found."
            )
            return ConversationHandler.END

        keyboard = [
            [InlineKeyboardButton(text=channel.name, callback_data=f"select_channel:{channel.id}")]
            for channel in channels
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        return reply_markup
        
class GetNameState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        query = self.update.callback_query
        await query.answer()

        channel_id = int(query.data.split(":")[-1])
        self.context.user_data['channel_id'] = channel_id

        await self.show_pannel()
        return self.GET_NAME

class GetPriceState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        subscription_name = self.update.message.text
        self.context.user_data['subscription_name'] = subscription_name

        await self.show_pannel()
        return self.GET_PRICE

class GetDayState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        price = self.update.message.text
        self.context.user_data['price'] = price

        await self.show_pannel()
        return self.GET_DAY

class ConfirmAddAnotherState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        day = self.update.message.text
        channel_id = self.context.user_data['channel_id']
        subscription_name = self.context.user_data['subscription_name']
        price = self.context.user_data['price']

        # Save to database
        subscriptionclient = SubscriptionClient()
        subscriptionclient.create_subscription( price=price, name=subscription_name, channel=channel_id, day=day)
        
        await self.show_pannel()
        return self.CONFIRM_ADD_ANOTHER

class AddAnotherSubscriptionState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        response = self.update.message.text.lower()

        if response == 'yes':
            self.show_pannel()
            return self.GET_NAME
        else:
            await Cancel()(update=self.update, context=self.context)

class Cancel(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        self.show_pannel()
        return ConversationHandler.END

add_subscription_handler = ConversationHandler(
    entry_points=[CommandHandler("add_subscription", AddSubscriptionState().get)],
    states={
        ConversationStates.LIST_CHANNELS: [CallbackQueryHandler(GetNameState().get, pattern="^select_channel_\d+$")],
        ConversationStates.GET_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, GetPriceState().get)],
        ConversationStates.GET_PRICE: [MessageHandler(filters.TEXT & ~filters.COMMAND, GetDayState().get)],
        ConversationStates.GET_DAY: [MessageHandler(filters.TEXT & ~filters.COMMAND, ConfirmAddAnotherState().get)],
        ConversationStates.CONFIRM_ADD_ANOTHER: [MessageHandler(filters.TEXT & ~filters.COMMAND, AddAnotherSubscriptionState().get)],
    },
    fallbacks=[CommandHandler("cancel", Cancel().get)],
    allow_reentry=True,
    conversation_timeout=120,  # 2 minutes
)