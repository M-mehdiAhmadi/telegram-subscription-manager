from .base import BaseAPIClient
from model import Subscriptions


class SubscriptionClient(BaseAPIClient):
    model_class = Subscriptions

    class Subscription:
        def __init__(self, id, price, name, channel, day):
            self.id = id
            self.price = price
            self.name = name
            self.channel = channel
            self.day = day

        def __repr__(self):
            return f"<Subscription {self.name}>"

    def _to_obj(self, sub: Subscriptions):
        return self.Subscription(
            id=sub.id,
            price=sub.price,
            name=sub.name,
            channel=sub.channel,
            day=sub.day
        )

    def get_subscription_by_id(self, id) -> Subscription:
        results = Subscriptions.filter(id=id)
        if results:
            return self._to_obj(results[0])
        raise LookupError(f"Subscription with id={id} not found")

    def get_subscription_by_channel_id(self, channel_id) -> list[Subscription]:
        results = Subscriptions.filter(channel=channel_id)
        return [self._to_obj(s) for s in results]

    def create_subscription(self, price, name, channel, day) -> Subscription:
        sub = Subscriptions(id=None, price=price, name=name, channel=channel, day=day)
        sub.save()
        return self._to_obj(sub)

    def delete_subscription(self, id):
        results = Subscriptions.filter(id=id)
        if results:
            results[0].delete()
        else:
            raise LookupError(f"Subscription with id={id} not found")

    def get_all(self) -> list[Subscription]:
        return [self._to_obj(s) for s in Subscriptions.get_all()]
