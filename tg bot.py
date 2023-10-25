Python 3.9.13 (v3.9.13:6de2ca5339, May 17 2022, 11:37:23) 
[Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Replace 'YOUR_BOT_TOKEN' with the actual API token you obtained from BotFather
TOKEN = 'YOUR_BOT_TOKEN'

# Define a function to send "hi" messages
def send_hi(update: Update, context: CallbackContext):
    update.message.reply_text("Hi!")

def main():
    # Create an Updater instance to interact with the Telegram API
    updater = Updater(token=TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register a command handler for the /hi command
    dispatcher.add_handler(CommandHandler("hi", send_hi))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

SyntaxError: multiple statements found while compiling a single statement
>>> 