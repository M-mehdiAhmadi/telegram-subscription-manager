from .base import BaseAPIClient


class User2SubscriptionsClient(BaseAPIClient):

    class User2Subscriptions:
        def __init__(self,
                     id,
                     user,
                     subscriptions,
                     date,
                     link,
                     chat_id,
                     ):
            self.id = id
            self.user = user
            self.subscriptions = subscriptions
            self.date = date
            self.link = link
            self.chat_id = chat_id
            

        def __repr__(self):
            return f"<User {self.user}>"

    def __init__(self):
        # این کلاینت از مسیر /core/user/users/ استفاده می‌کند
        super().__init__("v1/api/user2subscriptions/")

    def get_by_username_and_chat_id(self,username,chat_id):
        lst = self.filter(user__username=username,chat_id=chat_id)
        if not lst:
            return None
        user_subscriptions = [self.User2Subscriptions(**user2subscriptions) for user2subscriptions in lst ]
        return user_subscriptions
    
    def get_users_by_chat_id(self,chat_id) -> User2Subscriptions :
        lst = self.filter(chat_id=chat_id)
        return [self.User2Subscriptions(**data) for data in lst]
    
    def create_subscription_user(self,user,subscriptions,date,link,chat_id) -> User2Subscriptions:
        data = {
            "user":user,
            "subscriptions":subscriptions,
            "date":date,
            "link":link,
            "chat_id":chat_id
        }
        obj = self.create(data=data)
        if obj:
            return self.User2Subscriptions(**obj)
        raise LookupError("craeteion Error")