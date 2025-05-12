from handlers.conversation import *
from handlers.handlers_permissions import permissions
from model import User
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


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

        # Check if identifier is a chat_id or username
        if identifier.isdigit():
            user = User.filter(chat_id=int(identifier))
        else:
            user = User.filter(username=identifier)

        # Add special privileges
        if user[0].is_special == 1:
            await self.update.message.reply_text("User is already special.")
            return
        
        await self.show_pannel()
        return self.GET_CHANNEL


    async def get_keyboard(self):
        
        channels = Channel.get_all()
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
        
        user = User.get_by_chat_id(self.chat_id)
        
        channel:Channel = Channel.filter(id=channel_id)
        
        user.is_special = 1
        user.save()
        
        specialuser =Specialuser(id=None, user=user.chat_id, channel=channel_id)
        
        specialuser.save()
        
        self.context.bot.send_message(
            chat_id=self.chat_id,
            text=f"{channel.link}",
            parse_mode="html"
        )
        
        await self.show_pannel()
        
        return ConversationHandler.END
    
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