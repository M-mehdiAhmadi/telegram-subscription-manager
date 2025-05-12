from handlers import *
from model import User, User2subscriptions, Subscriptions,Specialuser
import datetime

class JoinRequestHandler(BaseHandler):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False
    
    async def get(self):
        user: User = User.get_by_chat_id(self.update.chat_join_request.from_user.id)
        chat = self.update.chat_join_request.chat

        if not user:
            return  # کاربر ثبت‌نام نکرده است

        specialuser=Specialuser.filter(user=user)
        if specialuser:
            await self.update.chat_join_request.approve()
        else:
            return
    
        current_date = datetime.datetime.now()
        
        user_subscriptions = User2subscriptions.filter(user=user.chat_id, chat_id=chat.id)
        
    
        
        for user_sub in user_subscriptions:
            try:
                sub_date = datetime.datetime.strptime(user_sub.date, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                continue  # تاریخ نادرست

            sub_info_list = Subscriptions.filter(id=user_sub.subscriptions)
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
