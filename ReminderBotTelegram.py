import datetime
import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram.ext import CallbackContext


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

REMINDER_MESSAGE, REMINDER_DATE = range(2)

def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Hi! I am a reminder bot. What do you want me to remind you of?')
    return REMINDER_MESSAGE

def reminder_message(update: Update, context: CallbackContext) -> int:
    context.user_data['reminder_message'] = update.message.text
    update.message.reply_text('When do you want me to remind you? Please enter date and time in this format: YYYY-MM-DD HH:MM')
    return REMINDER_DATE

def reminder_date(update: Update, context: CallbackContext) -> int:
    reminder_date = datetime.datetime.strptime(update.message.text, '%Y-%m-%d %H:%M')
    context.user_data['reminder_date'] = reminder_date.strftime('%Y-%m-%d %H:%M:%S')
    context.job_queue.run_once(alarm, reminder_date.timestamp(), context=update.message.chat_id)
    update.message.reply_text(f'I will remind you of "{context.user_data["reminder_message"]}" on {context.user_data["reminder_date"]}')
    return ConversationHandler.END

def alarm(context: CallbackContext) -> None:
    job = context.job
    context.bot.send_message(job.context, text=f'Reminder: {context.user_data["reminder_message"]}')

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Reminder cancelled.')
    return ConversationHandler.END

def main() -> None:
    """Run bot."""
    # Create Updater object and attach dispatcher to it
    updater = Updater("5910821343:AAHvLoixXPdBhX6-7S2pJoDm-f0xCOBKPWI", use_context=True)
    dispatcher = updater.dispatcher

    # Add conversation handler with the states REMINDER_MESSAGE and REMINDER_DATE
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            REMINDER_MESSAGE: [MessageHandler(Filters.text & ~Filters.command, reminder_message)],
            REMINDER_DATE: [MessageHandler(Filters.regex(r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$'), reminder_date)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    
    # Add conversation handler to dispatcher
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

if __name__ == '__main__':
    main()