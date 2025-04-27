from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes,ApplicationBuilder,CommandHandler
import json
from model import User
import datetime
from languages import languages
import plisio


client = plisio.PlisioClient(api_key='your_secret_key')






class BaseHanler:
    def __init__(self,parent):
        self.parent = parent
        self.edit_enabled = True
        self.fallback_to_delete = True
        
    async def __call__(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self.context = context
        self.update = update
        self.chat_id = update.effective_chat.id
        
        return await self.get()
    async def get(self):
        """
        This method is called when the handler is invoked.
        It retrieves the chat ID and context from the update object.
        """
        raise NotImplementedError("Subclasses should implement this method.")
    
    def get_or_create_user(self):
        """
        Retrieve or create a user in the database based on the chat ID.
        If the user does not exist, create a new user with default values.
        """
        user = User.get_by_chat_id(self.chat_id)
        if user == None:
            user = User(
                chat_id=self.chat_id,
                time_created=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                is_active=0,
                phone=None,
                is_admin=1,
                language="en"
            )
            user.save()
        return user
    
    async def get_text(self):
        """
        Get the text message based on the user's language.
        This function retrieves the text message from the language data JSON file.
        """
        user = self.get_or_create_user()
        state = self.parent.__class__.__name__.lower()
        text = languages[user.language][state]["text"]
    
        return text
    async def get_keyboard(self):
        """
        Generate a keyboard based on the user's language.
        This function creates an inline keyboard with buttons based on the language data.
        """
        user = self.get_or_create_user()
        state = self.parent.__class__.__name__.lower()
        
        replay_markup = None
        
        if "keyboard" in languages[user.language][state].keys():
            keyboard = []
            for button in languages[user.language][state]["keyboard"]:
                keyboard.append(
                    [InlineKeyboardButton(text=button["text"],callback_data=button["callback_data"])]
                )
            replay_markup = InlineKeyboardMarkup(keyboard)
            
        return replay_markup
    async def show_pannel(self):
        
        if self.edit_enabled and self.get_previous_message_id() is not None:
            success = await self.edit_message()
            if not success:
                    # If editing fails, fallback to sending a new message
                await self.send_message()
        elif self.fallback_to_delete and self.get_previous_message_id() is not None:
            await self.delete_message()
            await self.send_message()
        else:
            await self.send_message()
        
            
        
        
        
        
        
    async def edit_message(self):  
        text = await self.get_text()  
        keyboard = await self.get_keyboard()
        try:
            await self.context.bot.edit_message_text(
                chat_id=self.chat_id,
                text=text,
                reply_markup=keyboard,
                message_id=self.get_previous_message_id()
                )
            return True
        except Exception as error:
            print(error)
            return False
            
            
    async def delete_message(self):
        try:
            await self.context.bot.delete_message(
                chat_id=self.chat_id
                ,message_id=self.get_previous_message_id())
            
        except Exception as error:
            print(error)
        
    async def send_message(self):
        text = await self.get_text()  
        keyboard = await self.get_keyboard()
        msg = await self.context.bot.send_message(chat_id=self.chat_id,text=text,reply_markup=keyboard)
        self.set_previous_message_id(msg.message_id)

        
        
    def get_previous_message_id(self):
        return self.context.user_data.get("previous_message_id") or None

    def set_previous_message_id(self, message_id):
        self.context.user_data["previous_message_id"] = message_id
        
        
        
        
        
        
            
    
    

        
        
        
    
            
             