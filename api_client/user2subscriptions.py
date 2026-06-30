from .base import BaseAPIClient
from model import User2subscriptions
import datetime


class User2SubscriptionsClient(BaseAPIClient):
    model_class = User2subscriptions

    class User2Subscriptions:
        def __init__(self, id, user, subscriptions, date, link, chat_id):
            self.id = id
            self.user = user
            self.subscriptions = subscriptions
            self.date = date
            self.link = link
            self.chat_id = chat_id

        def __repr__(self):
            return f"<User2Subscriptions user={self.user}>"

    def _to_obj(self, u2s: User2subscriptions):
        return self.User2Subscriptions(
            id=u2s.id,
            user=u2s.user,
            subscriptions=u2s.subscriptions,
            date=u2s.date,
            link=u2s.link,
            chat_id=u2s.chat_id
        )

    def get_by_username_and_chat_id(self, username, chat_id) -> list[User2Subscriptions] | None:
        results = User2subscriptions.filter(user=username, chat_id=chat_id)
        if not results:
            return None
        return [self._to_obj(u) for u in results]

    def get_users_by_chat_id(self, chat_id) -> list[User2Subscriptions]:
        results = User2subscriptions.filter(chat_id=chat_id)
        return [self._to_obj(u) for u in results]

    def create_subscription_user(self, user, subscriptions, date, link, chat_id) -> User2Subscriptions:
        if date is None:
            date = str(datetime.datetime.now())
        u2s = User2subscriptions(
            user=user,
            subscriptions=subscriptions,
            date=date,
            id=None,
            link=link,
            chat_id=chat_id
        )
        u2s.save()
        return self._to_obj(u2s)
