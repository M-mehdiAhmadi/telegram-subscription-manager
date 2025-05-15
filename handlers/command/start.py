from handlers.command import *
from handlers.handlers_permissions import permissions
from telegram.error import BadRequest
from api_client.joinforce_client import JoinforceClient

class StartHandler(BaseHandler):
    permissions = [permissions.IsActiveUserPermissionHandler]
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False
    async def get(self):
        checker = await ForceJoinCheckerHandler()(update=self.update,context=self.context)
        if not checker:
            await self.show_pannel()
        # forcejoincheckerhandler
    
class ForceJoinCheckerHandler(BaseHandler):
    permissions = [permissions.IsActiveUserPermissionHandler]
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        client = JoinforceClient()
        force_channels = client.get_all()
        
        joined = await self.check_and_prompt(force_channels)
        
        if not joined:
            return  False

        await self.show_pannel()
        return True
    
    async def get_not_joined_channels(self, force_channels:list[JoinforceClient.Joinforce]) -> list[JoinforceClient.Joinforce] :
        not_joined = []
        for channel in force_channels:
            try:
                member = await self.context.bot.get_chat_member(chat_id=channel.link, user_id=self.chat_id)
                if member.status in ['left', 'kicked']:
                    not_joined.append(channel)
            except BadRequest:
                not_joined.append(channel)
        return not_joined

    async def check_and_prompt(self, force_channels:list[JoinforceClient.Joinforce]):
        self.not_joined : list[JoinforceClient.Joinforce] = await self.get_not_joined_channels(force_channels)

        if self.not_joined:
            await self.show_pannel()
            return True  # یعنی اجازه بده کار ادامه پیدا کنه
        else:
            return False

    async def get_keyboard(self):
        replay_markup = None
        
        keyboard = [
            [InlineKeyboardButton(text=f"{ch.name}", url=f"{ch.link}")]
            for ch in self.not_joined
        ]
        
        replay_markup = InlineKeyboardMarkup(keyboard)
            
        return replay_markup
