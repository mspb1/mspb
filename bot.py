import telebot
import openai
# import logging
import telegram

API_TOKEN = '6097689040:AAFO6YXBb1b3xR1R77a4QznBhO5GMA81-aE'
YOUR_API_KEY = "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"
bot = telebot.TeleBot(API_TOKEN)
openai.api_key = (YOUR_API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет чем могу тебе помочь?')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Use the OpenAI API to get the answer to the question
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message.text}",
        # max_tokens=4097,
        # n=1,
        # stop=None,
        # temperature=0.5,
    )
    bot.send_message(message.chat.id, response.choices[0].text)

bot.polling()
