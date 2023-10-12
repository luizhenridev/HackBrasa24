import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from services.gpt import gen


logger = logging.getLogger(__name__)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

API_KEY = os.environ.get('TOKEN_BOT') 
BOT_USERNAME = os.environ.get('BOT_USERNAME')

#Commands
async def start_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me! I am Who")

async def help_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm Who! Please Type someting so I can respond")

async def custom_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")

chatConversation = []

max_messages = 4

#Responses
def handle_response(text: str, userId:int) -> str:
    processed: str = text.lower()
    users = (userId)

    chatConversation.append(processed)

    if len(chatConversation) > max_messages:
        chatConversation.pop(0)

    string= ' '.join([str(element) for element in chatConversation])
    string = string.strip()

    answer = gen(string, users ,id_model = "gpt-3.5-turbo", max_tokens= 100)
    answer = answer.strip()

    chatConversation.append(answer)
    print(chatConversation)
    return answer




async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    userId: int = update.message.chat.id

    print(f'User({userId}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text:str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text, userId)
    
    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting Bot')
    app = Application.builder().token(API_KEY).build()

    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    app.add_error_handler(error)

    #Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)