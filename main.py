from gtts import gTTS
import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, send me a text and I'll convert it into speech!")

def text_to_speech(update, context):
    text = ' '.join(context.args)
    language = 'en'
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save("text.mp3")
    context.bot.send_voice(chat_id=update.effective_chat.id, voice=open('text.mp3', 'rb'))

def main():
    updater = Updater(token='YOURTOKEN', use_context=True)
    dp = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dp.add_handler(start_handler)
    dp.add_handler(CommandHandler('say', text_to_speech))
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), text_to_speech))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()