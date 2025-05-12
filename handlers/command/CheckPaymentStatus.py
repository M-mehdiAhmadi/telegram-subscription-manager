from handlers import *
from handlers.handlers_permissions import permissions
from model import Payment, Subscriptions,Channel,User2subscriptions

class CheckPaymentStatusHandler(BaseHandler):
    permissions = [permissions.IsActiveUserPermissionHandler]
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False
    
    async def get(self):
        self.payment_id = self.update.callback_query.data.split(":")[-1]
        payment: Payment = Payment.filter(id=self.payment_id)
        operation: plisio.Operation = client.get_operation(payment_id=payment.invoice_id)
        
        if operation.status == plisio.OperationStatus.completed:
            subscription: Subscriptions = Subscriptions.filter(payment.subscriptions)
            channel: Channel = Channel.filter(id=subscription.channel.id)
            user = User.get_by_chat_id(self.chat_id)
            self.link = channel.link
            User2subscriptions(
                user=user,
                subscriptions=subscription,
                date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                
                link=channel.link,
                chat_id=channel.chat_id
            ).save()
            await self.show_pannel()
    
    async def get_text(self):
        text = await super().get_text()
        text += f"\n{self.payment_id}"
        return text
    
        