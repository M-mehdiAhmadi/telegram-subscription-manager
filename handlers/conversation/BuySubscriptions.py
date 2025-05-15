from handlers.conversation import (client,Invoice,
                                   InlineKeyboardButton,InlineKeyboardMarkup,
                                   BaseHandler,plisio,datetime,
                                   ConversationHandler,CallbackQueryHandler,
                                   CommandHandler,languages,MessageHandler,
                                   filters
                                   )
from handlers.handlers_permissions import permissions
from api_client.channel_client import ChannelClient
from api_client.sub_client import SubscriptionClient
from api_client.payment_client import PaymentClient


# Define states for the conversation
class ConversationStates(BaseHandler):
    permissions = [permissions.IsActiveUserPermissionHandler]
    
    SELECT_SUBSCRIPTION = 1
    SELECT_CRYPTO = 3
    SEND_PAYMENT_LINK = 4
    CANCEL = 5

class SelectChannelSubscriptionState(ConversationStates):
    
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = True
    
    async def get(self):           
        self.context.user_data["invoice"] = Invoice()
        await self.show_pannel()
        return self.SELECT_SUBSCRIPTION

    async def get_keyboard(self):
        channelclient = ChannelClient()
        
        channels = channelclient.get_all()
        replay_markup = None

        keyboard = []
        for channel in channels:
            keyboard.append(
                    [InlineKeyboardButton(
                        text=channel.name,callback_data = f"channel_id:{channel.id}"
                )])
        replay_markup = InlineKeyboardMarkup(keyboard)

        return replay_markup
  
class SelectSubscriptionState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = True 
    
    async def get(self):
        channel_id = self.update.callback_query.data.split(":")[-1]
        
        self.invoice:Invoice = self.context.user_data["invoice"]
        self.invoice.channel_id = channel_id
        self.context.user_data["invoice"] = self.invoice
        
        await self.show_pannel()
        return self.SELECT_SUBSCRIPTION
    
    async def get_keyboard(self):
        subscriptionclient = SubscriptionClient()
        subscriptions = subscriptionclient.get_subscription_by_channel_id(channel_id=self.invoice.channel_id)
        replay_markup = None

        keyboard = []
        for subscription in subscriptions:
            keyboard.append(
                    [InlineKeyboardButton(
                        text=subscription.price,callback_data = f"subscription_id:{subscription.id}"
                )])
        replay_markup = InlineKeyboardMarkup(keyboard)

        return replay_markup

class SelectCryptoState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = True 
    
    async def get(self):
        subscription_id = self.update.callback_query.data.split(":")[-1]
        self.invoice:Invoice = self.context.user_data["invoice"]
        self.invoice.subscription_id = subscription_id
        self.context.user_data["invoice"] = self.invoice
        await self.show_pannel()
        return self.SEND_PAYMENT_LINK
    
    async def get_keyboard(self):
        currencies = {}
        for currency_symbol,currency_name in plisio.CryptoCurrency.__dict__.items():
            if currency_symbol.isupper() and not currency_symbol.startswith("__"):
                currencies[currency_symbol] = currency_name
        
        keyboard = [
            [InlineKeyboardButton(text=currency, callback_data=f"select_currency:{currency}")]
            for currency in list(currencies.keys())
        ]
        
        replay_markup = InlineKeyboardMarkup(keyboard) if keyboard else None
        
        return replay_markup

class SendPaymentLinkState(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = True 
    
    def create_invoice(self) -> PaymentClient.Payment:
        subscriptionclient = SubscriptionClient()
        subscription = subscriptionclient.get_subscription_by_id(id=self.invoice.subscription_id)
        amount = subscription.price
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        paymentclient = PaymentClient()
        payment:PaymentClient.Payment = paymentclient.create_payment(user=self.chat_id,
                          subscriptions=self.invoice.subscription_id,
                          invoice_id=None,
                          invoice_link=None,
                          date=date)
        
        
        
        invoice = client.invoice(
            currency=self.invoice.cryptocurrency,
            description=f"date: {date}\nsubscription_id: {self.invoice.subscription_id}\nchannel_id: {self.invoice.channel_id}\nuser_id: {self.chat_id}",
            source_currency=plisio.FiatCurrency.USD,
            source_amount=amount,
            order_id=payment.id,
            order_name=str(payment.id),
            allowed_currencies=[self.invoice.cryptocurrency]
        )
        payment.invoice_id = invoice["txn_id"]
        payment.invoice_link = invoice["invoice_url"]
        payment.save()
        return payment

    async def get(self):
        currency = self.update.callback_query.data.split(":")[-1]
        self.invoice:Invoice = self.context.user_data["invoice"]
        self.invoice.cryptocurrency = currency
        self.context.user_data["invoice"] = self.invoice
        self.payment = self.create_invoice()
        await self.show_pannel()
        del self.context.user_data["invoice"]
        return ConversationHandler.END
    
    async def get_text(self):
        text = await super().get_text()
        text += f"\n\n{self.payment.invoice_link}"
        return text

    async def get_keyboard(self):
        user = self.get_or_create_user()
        state = self.parent.__class__.__name__.lower()
        
        replay_markup = None    
    
        keyboard = []
        for button in languages[user.language][state]["keyboard"]:
            keyboard.append(
                [InlineKeyboardButton(text=button["text"], callback_data=f"payment_id:{self.payment.id}")]
            )
        replay_markup = InlineKeyboardMarkup(keyboard)
        
        return replay_markup

class Cancel(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = True 
    
    async def get(self):
        await self.show_pannel()
        del self.context.user_data["invoice"]
        return ConversationHandler.END

# Define the conversation handler
buy_subscriptions_conversation = ConversationHandler(
    entry_points=[CallbackQueryHandler(SelectChannelSubscriptionState(), pattern=r"buychannelsubscriptions")],
    states={
        ConversationStates.SELECT_SUBSCRIPTION: [CallbackQueryHandler(SelectSubscriptionState(),pattern=r"^channel_id:\d+$")],
        ConversationStates.SELECT_CRYPTO: [CallbackQueryHandler(SelectCryptoState(),pattern=r"^subscription_id:\d+$")],
        ConversationStates.SEND_PAYMENT_LINK: [CallbackQueryHandler(SendPaymentLinkState(),pattern=r"^select_currency:\w+$")],
    },
    fallbacks=[CommandHandler('cancel', Cancel()),
               MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, Cancel())
               ],
    allow_reentry=True,
    conversation_timeout=120,  # 2 minutes
)

