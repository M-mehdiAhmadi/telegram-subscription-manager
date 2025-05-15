from handlers import *
from handlers.handlers_permissions import permissions
# from model import Payment, Subscriptions,Channel,User2subscriptions
from api_client.payment_client import PaymentClient
from api_client.sub_client import SubscriptionClient
from api_client.channel_client import ChannelClient
from api_client.user2subscriptions import User2SubscriptionsClient



class CheckPaymentStatusHandler(BaseHandler):
    permissions = [permissions.IsActiveUserPermissionHandler]
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False
    
    async def get(self):
        self.payment_id = self.update.callback_query.data.split(":")[-1]
        paymentclient = PaymentClient()
        payment:PaymentClient.Payment = paymentclient.get_payment_by_id(id=self.payment_id)
        
        operation: plisio.Operation = client.get_operation(payment_id=payment.invoice_id)
        
        subscriptionclient = SubscriptionClient()
        channelclient = ChannelClient()
        userclient = UserClient()
        user2subscriptionsclient = User2SubscriptionsClient()
        if operation.status == plisio.OperationStatus.completed:
            payment.Completed = True
            payment.save()
            subscription: SubscriptionClient.Subscription = subscriptionclient.get_subscription_by_id(id=payment.subscriptions.id)
            channel: ChannelClient.Channel = channelclient.get_channel_by_id(id=subscription.channel.id)
            user:UserClient.User = userclient.getUser_by_username(username=self.chat_id)
            self.link = channel.link
            user2subscriptionsclient.create_subscription_user(
                user=user,
                subscriptions=subscription,
                date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                link=channel.link,
                chat_id=channel.chat_id
            )
            await self.show_pannel()
    
    async def get_text(self):
        text = await super().get_text()
        text += f"\n{self.payment_id}"
        return text
    
        