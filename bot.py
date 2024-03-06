# bot.py

import os
import psycopg2
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


updater = Updater(token=os.environ.get("BOT_TOKEN"), use_context=True)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to the bot! To access notes, please join our channel.")

def class_notes(update: Update, context: CallbackContext) -> None:
    
    if update.message.chat_id not in context.bot.get_chat_member(update.message.chat_id, update.message.from_user.id).status:
        update.message.reply_text("Please join our channel to access the notes.")
        return

  
    class_number = context.args[0]
    
    notes = fetch_notes_from_database(class_number)
    update.message.reply_text(notes)
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("class1", class_notes, pass_args=True))

updater.start_polling()
updater.idle()
