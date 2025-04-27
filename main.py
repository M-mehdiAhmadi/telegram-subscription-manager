import os
from telegram import Update
from telegram.ext import ContextTypes,ApplicationBuilder,CommandHandler,CallbackQueryHandler
from handlers.command.start import StartHandler
from handlers.callbackquery.SelectLanguage import SelectLanguageHandler
from handlers.callbackquery.SetLanguage import SetLanguageHandler
TOKEN = "7552347461:AAGuZrGFK07qvKT18vabBxxxSsXbFShXcgY"
application = ApplicationBuilder().token(TOKEN).build()

application.add_handler(CommandHandler("start",StartHandler() ))
application.add_handler(CallbackQueryHandler(SelectLanguageHandler(),"select_language"))
application.add_handler(CallbackQueryHandler(SetLanguageHandler(),r"\b[a-z]{2}\b"))







application.run_polling()