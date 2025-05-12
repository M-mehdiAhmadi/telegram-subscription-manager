import os
from settings import BOT_TOKEN
from telegram import Update
from telegram.ext import (ContextTypes,ApplicationBuilder,CommandHandler,
                          CallbackQueryHandler,ConversationHandler,MessageHandler,filters)

from handlers.command.start import StartHandler
from handlers.command.CheckPaymentStatus import CheckPaymentStatusHandler
from handlers.command.adminpannel import AdminPannelHandler
from handlers.command.ban_user import BanUserHandler
from handlers.command.unban_user import UnbanUserHandler
from handlers.command.add_admin import AddAdminHandler
from handlers.command.remove_admin import RemoveAdminHandler
from handlers.command.show_all_admin import ShowAllAdminHandler
from handlers.command.remove_special_user import RemoveSpecialUserHandler
from handlers.command.show_all_special_user import ShowAllSpecialUserHandler
from handlers.command.show_list_of_tables import ShowListOfTablesHandler
from handlers.command.export_to_csv import ExportToCSVHandler

from handlers.callbackquery.SelectLanguage import SelectLanguageHandler
from handlers.callbackquery.SetLanguage import SetLanguageHandler

from handlers.conversation.BuySubscriptions import buy_subscriptions_conversation
from handlers.conversation.AddForcedJoinChannel import add_forced_join_channel_handler
from handlers.conversation.DeleteForcedJoinChannel import delete_forced_join_channel_handler
from handlers.conversation.AddChannel import add_channel_handler
from handlers.conversation.DeleteChannel import delete_channel_handler
from handlers.conversation.AddSubscription import add_subscription_handler
from handlers.conversation.DeleteSubscription import delete_subscription_handler
from handlers.conversation.AddSpecialUser import add_special_user_handler

from handlers.customfilters import AllowedChannelFilter
from handlers.message.channelmessage import ChannelMessageHandler

application = ApplicationBuilder().token(BOT_TOKEN).build()

application.add_handler(CommandHandler("start",StartHandler() ))
application.add_handler(CommandHandler("admin",AdminPannelHandler() ))
application.add_handler(CommandHandler("ban_user", BanUserHandler()))
application.add_handler(CommandHandler("unban_user", UnbanUserHandler()))
application.add_handler(CommandHandler("add_admin", AddAdminHandler()))
application.add_handler(CommandHandler("remove_admin", RemoveAdminHandler()))
application.add_handler(CommandHandler("show_all_admin", ShowAllAdminHandler()))
application.add_handler(CommandHandler("remove_special_user", RemoveSpecialUserHandler()))
application.add_handler(CommandHandler("show_all_special_user", ShowAllSpecialUserHandler()))
application.add_handler(CommandHandler("show_list_of_tables", ShowListOfTablesHandler()))
application.add_handler(CommandHandler("export_to_csv", ExportToCSVHandler()))

application.add_handler(CallbackQueryHandler(SelectLanguageHandler(),r"select_language"))
application.add_handler(CallbackQueryHandler(SetLanguageHandler(),r"\b[a-z]{2}\b"))
application.add_handler(CallbackQueryHandler(CheckPaymentStatusHandler(),r"payment_id:\d+"))

application.add_handler(buy_subscriptions_conversation)
application.add_handler(add_forced_join_channel_handler)
application.add_handler(delete_forced_join_channel_handler)
application.add_handler(add_channel_handler)
application.add_handler(delete_channel_handler)
application.add_handler(add_subscription_handler)
application.add_handler(delete_subscription_handler)
application.add_handler(add_special_user_handler)

application.add_handler(MessageHandler(filters.ChatType.CHANNEL & AllowedChannelFilter() , ChannelMessageHandler()))

application.run_polling()