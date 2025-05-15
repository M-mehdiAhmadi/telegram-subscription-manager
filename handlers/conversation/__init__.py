from handlers import *
from telegram.ext import ConversationHandler,CallbackQueryHandler,CommandHandler,MessageHandler,filters
# from model import Channel,Subscriptions,User2subscriptions,Payment,Joinforce,Specialuser
from handlers.handlers_permissions import *


class Invoice:
    def __init__(self, channel_id=None, subscription_id=None, cryptocurrency=None):
        self.channel_id = channel_id
        self.subscription_id = subscription_id
        self.cryptocurrency = cryptocurrency
    