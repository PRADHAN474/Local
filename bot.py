# bot.py

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from config import config

# Initialize the bot
updater = Updater(token=config['BOT_TOKEN'], use_context=True)
dispatcher = updater.dispatcher

# Define command handlers
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to the bot! To access notes, please join our channel.")

def class_notes(update: Update, context: CallbackContext) -> None:
    # Check if user is a member of the channel
    if update.message.chat_id not in context.bot.get_chat_member(update.message.chat_id, update.message.from_user.id).status:
        update.message.reply_text("Please join our channel to access the notes.")
        return

    # Fetch and send the notes based on the button clicked
    class_number = context.args[0]
    # Retrieve notes from the database based on class_number
    notes = fetch_notes_from_database(class_number)
    update.message.reply_text(notes)

# Add command handlers to dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("class1", class_notes, pass_args=True))

# Start the bot
updater.start_polling()
updater.idle()
