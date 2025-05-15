from .base import BaseAPIClient

class SubscriptionClient(BaseAPIClient):
    
    class Subscription:
        def __init__(self, id, price, name, channel, day):
            self.id=id
            self.price = price
            self.name = name
            self.channel = channel
            self.day = day
    
    def __init__(self):
        # از مسیر /v1/api/subscriptions/ استفاده می‌کند
        super().__init__("v1/api/subscriptions/")

    def get_user_subscription(self,subscription_id) -> list[Subscription] :
        subscriptions = self.filter(id=subscription_id)
        return [self.Subscription(**subscription) for subscription in subscriptions]
    
    def get_subscription_by_channel_id(self,channel_id) -> list[Subscription] :
        subscriptions = self.filter(channel=channel_id)
        return [self.Subscription(**subscription) for subscription in subscriptions]
    
    def create_subscription(self, price, name, channel, day) -> Subscription :
        data = {
            "price":price,
            "channel":channel,
            "name":name,
            "day":day
        }
        obj = self.create(data=data)
        if obj:
            return self.Subscription(**obj)
        raise LookupError("createion Error")
    def get_subscription_by_channel_id(self,channel_id) -> list[Subscription]:
        subscriptions = self.filter(channel=channel_id)
        return [self.Subscription(**subscription) for subscription in subscriptions]
    
    def get_subscription_by_id(self,id) -> Subscription :
        subscription = self.retrieve(obj_id=id)
        return self.Subscription(**subscription)