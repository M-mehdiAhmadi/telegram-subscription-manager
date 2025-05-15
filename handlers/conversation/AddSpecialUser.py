from handlers.conversation import *
from handlers.handlers_permissions import permissions
# from model import User
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from api_client.channel_client import ChannelClient
from api_client.user_client import UserClient
from api_client.special_user import SpecialUserClient

class ConversationStates(BaseHandler):
    permissions = [permissions.IsAdminPermissionHandler]
    GET_CHAT_ID = 1
    GET_CHANNEL = 2
    

class AddSpecialUserHandler(ConversationStates):
    
    def __init__(self):
        super().__init__(parent=self)
    
    async def get(self):
        args = self.context.args
        if not args:
            await self.update.message.reply_text("Usage: /add_special <chat_id>|<username>")
            return

        identifier = args[0]
        userclient = UserClient()
        # Check if identifier is a chat_id or username
        if identifier.isdigit():
            chat_id = int(identifier)
            
        else:
            chat = await self.context.bot.get_chat(chat_id=identifier)
            chat_id = chat.id
        
        user = userclient.getUser_by_username(username=chat_id)

        # Add special privileges
        if user.is_special == True:
            await self.update.message.reply_text("User is already special.")
            return
        self.context.user_data["user"] = user
        
        await self.show_pannel()
        return self.GET_CHANNEL


    async def get_keyboard(self):
        
        channelclient = ChannelClient()
        
        channels = channelclient.get_all()
        if not channels:
            await self.update.message.reply_text("No channels available.")
            return
                
        replay_markup = None

        keyboard = []
        for channel in channels:
            keyboard.append(
                [InlineKeyboardButton(text=channel.name, callback_data=f"channel_id:{channel.id}")]
            )
        replay_markup = InlineKeyboardMarkup(keyboard)
        
        return replay_markup
        
class GetChannelHandler(ConversationStates):
    
    def __init__(self):
        super().__init__(parent=self)
    
    async def get(self):
        query = self.update.callback_query
        channel_id = int(query.data.split(":")[1])
        
        user:UserClient.User = self.context.user_data["user"]
        
        channelclient = ChannelClient()
        specialuserclient = SpecialUserClient()
                
        channel:ChannelClient.Channel = channelclient.retrieve(obj_id=channel_id)
        
        specialuserclient.create_special_user(user=user,channel=channel)
        
        user.is_special =True
        user.save()
        
        self.link = channel.link
        
        await self.show_pannel()
        
        return ConversationHandler.END
    
    async def get_text(self):
        text = await super().get_text()
        text += f"\n{self.link}"
        return text
        
class Cancel(ConversationStates):
    def __init__(self):
        super().__init__(parent=self)
        self.edit_enabled = False
        self.fallback_to_delete = False

    async def get(self):
        self.show_pannel()
        return ConversationHandler.END

add_special_user_handler = ConversationHandler(
    entry_points=[CommandHandler("add_special", AddSpecialUserHandler())],
    states={
        ConversationStates.GET_CHANNEL: [
            CallbackQueryHandler(GetChannelHandler(), pattern=r"channel_id:\d+"),
        ],
    },
    fallbacks=[CommandHandler("cancel", Cancel())],
    allow_reentry=True,
    conversation_timeout=120
)