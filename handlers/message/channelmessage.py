from handlers.message import *
import asyncio
from api_client.user2subscriptions import User2SubscriptionsClient


class ChannelMessageHandler(BaseHandler):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False
        
    async def get(self):
                
        await self.remove_extra_users()
    
    async def remove_extra_users(self):
        """
        Remove extra users from the channel.
        """
        # Get the list of users in the channel
        current_date = datetime.datetime.now()
        
        client = User2SubscriptionsClient()
        
        users: list[User2SubscriptionsClient.User2Subscriptions] = client.get_users_by_chat_id(chat_id=self.chat_id)
        
        sleep_member_after_kick = 10
        
        counter = 0
        # Remove users whose date is less than the current date
        for user in users:
            user_date = datetime.datetime.strptime(user.date, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(days=user.subscriptions.day)
            is_member = await self.is_member(chat_id=user.chat_id, user_id=user.user.chat_id)
            if user_date > current_date and is_member:
                if counter < sleep_member_after_kick:
                    await self.remove_user(channel_chat_id=user.chat_id,user_chat_id=user.user.chat_id)
                    counter += 1
                else:
                    await asyncio.sleep(2)
                    counter = 0

    async def is_member(self, chat_id, user_id):
        try:
            member = await self.context.bot.get_chat_member(chat_id=chat_id, user_id=user_id)
            # فقط کسانی که هنوز عضو هستند و معمولی‌اند حذف شوند
            return member.status in ['member']
        except Exception as e:
            print(f"Error checking membership for {user_id}: {e}")
            return False
       
    async def remove_user(self, channel_chat_id,user_chat_id):
        """
        Remove a user from the channel.
        """
        try:
            await self.context.bot.ban_chat_member(chat_id=channel_chat_id, user_id=user_chat_id)
            await self.context.bot.unban_chat_member(chat_id=channel_chat_id, user_id=user_chat_id)
            
        except Exception as e:
            print(f"Error removing user {user_chat_id}: {e}")