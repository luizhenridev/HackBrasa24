import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from services.gpt import gen, intention, createdashboard, createPredictions, createFinancialOverview, createRecomendations, aboutBusiness
from services.goog import input



logger = logging.getLogger(__name__)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

API_KEY = os.environ.get('TOKEN_BOT') 
BOT_USERNAME = os.environ.get('BOT_USERNAME')

#Commands
async def start_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá, obrigado por falar comigo eu sou a Aurora!")

async def help_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm Who! Please Type someting so I can respond")

async def custom_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")

chatConversation = []

max_messages = 2

#Responses
def handle_response(text: str, userId:str) -> str:
    processed: str = text.lower()
    users = userId


    inte = intention(processed, id_model= "gpt-4", max_tokens= 1000)


    match inte:
        case "1":
            chatConversation.append(processed)

            if len(chatConversation) >= max_messages:
                chatConversation.pop(0)
                

            string= ' '.join([str(element) for element in chatConversation])
            string = string.strip()

            answer = createdashboard(string, id_model = "gpt-4", max_tokens= 1000)
            answer = answer.strip()

            chatConversation.append(answer)
            print(chatConversation)
            return answer
        case "2":
            chatConversation.append(processed)

            if len(chatConversation) >= max_messages:
                chatConversation.pop(0)
                

            string= ' '.join([str(element) for element in chatConversation])
            string = string.strip()

            answer = createPredictions(string, id_model = "gpt-4", max_tokens= 1000)
            answer = answer.strip()

            chatConversation.append(answer)
            print(chatConversation)
            return answer
        case "3":
            chatConversation.append(processed)

            if len(chatConversation) >= max_messages:
                chatConversation.pop(0)
                

            string= ' '.join([str(element) for element in chatConversation])
            string = string.strip()

            answer = createFinancialOverview(string, id_model = "gpt-4", max_tokens= 1000)
            answer = answer.strip()

            chatConversation.append(answer)
            print(chatConversation)
            return answer
        case "4":
            chatConversation.append(processed)

            if len(chatConversation) >= max_messages:
                chatConversation.pop(0)
                

            string= ' '.join([str(element) for element in chatConversation])
            string = string.strip()

            answer = createRecomendations(string, id_model = "gpt-4", max_tokens= 1000)
            answer = answer.strip()

            chatConversation.append(answer)
            print(chatConversation)
            return answer
        case _:
            chatConversation.append(processed)

            if len(chatConversation) >= max_messages:
                chatConversation.pop(0)
                

            string= ' '.join([str(element) for element in chatConversation])
            string = string.strip()

            answer = aboutBusiness(string, id_model = "gpt-4", max_tokens= 1000)
            answer = answer.strip()

            chatConversation.append(answer)
            print(chatConversation)
            return answer


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    userId: int = update.message.chat.id
    userFirstName: str = update.message.from_user.first_name
    userLastName: str= update.message.from_user.last_name
    fullUserName: str = f"{userFirstName} {userLastName}" 
    cellphoneNumber: str = "85"
    chat_id: int = update.message.chat_id
    message_id: int = update.message.message_id

    print(f'User({userId}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text:str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text, userId)
        else:
            return
    else:
        response: str = handle_response(text, userId)
    
    print('Bot:', response)
    await update.message.reply_text(response, connect_timeout=10)

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
    app.run_polling(poll_interval=10)