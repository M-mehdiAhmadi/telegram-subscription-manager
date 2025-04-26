import os
from telegram import Update
from telegram.ext import ContextTypes,ApplicationBuilder,CommandHandler
from handlers.command.start import StartHandler

TOKEN = "7552347461:AAGuZrGFK07qvKT18vabBxxxSsXbFShXcgY"
application = ApplicationBuilder().token(TOKEN).build()

application.add_handler(CommandHandler("start",StartHandler() ))


application.run_polling()