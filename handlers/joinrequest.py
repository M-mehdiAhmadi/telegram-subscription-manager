from handlers import *
# from model import User, User2subscriptions, Subscriptions,Specialuser
import datetime
from api_client.user_client import UserClient
from api_client.special_user import SpecialUserClient
from api_client.user2subscriptions import User2SubscriptionsClient
from api_client.sub_client import SubscriptionClient

class JoinRequestHandler(BaseHandler):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False
    
    async def get(self):
        userclient: UserClient = UserClient()
        user = userclient.getUser_by_username(username=self.update.chat_join_request.from_user.id)
        
        chat = self.update.chat_join_request.chat

        if not user:
            await self.update.chat_join_request.decline()
            return  # کاربر ثبت‌نام نکرده است

        specialclient: SpecialUserClient = SpecialUserClient()
        specialuser =specialclient.filter_by_username(username=user.username)
        
        
        if specialuser:
            await self.update.chat_join_request.approve()
        else:
            return
    
        current_date = datetime.datetime.now()
        
        user_subscriptions_client = User2SubscriptionsClient()
        
        user_subscriptions = user_subscriptions_client.get_by_username_and_chat_id(username=user.username,chat_id=chat.id)
        
        
        
    
        subscriptionclient = SubscriptionClient()
        for user_sub in user_subscriptions:
            try:
                sub_date = datetime.datetime.strptime(user_sub.date, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                continue  # تاریخ نادرست
            
            sub_info_list = subscriptionclient.get_user_subscription(subscription_id=user_sub.subscriptions)
            if not sub_info_list:
                continue
            
            sub_info = sub_info_list[0]
            expire_date = sub_date + datetime.timedelta(days=sub_info.day)
            
            if expire_date > current_date:
                # اشتراک هنوز معتبر است، پس اجازه بده
                await self.update.chat_join_request.approve()
                return
        
        # هیچ اشتراک معتبری پیدا نشد
        await self.update.chat_join_request.decline()
