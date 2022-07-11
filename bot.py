import telebot
import re
from parsing import NewsParser

TOKEN = "5489489521:AAHXdvbppXhj0Stywme1rdL69WO6niPgMNU"

bot = telebot.TeleBot(TOKEN)
p = NewsParser()


@bot.message_handler(commands=['start', 'help'])
def print_help(message):
    bot.reply_to(message, 'Bot loads the news from rbc.ru.\n\nFor starters try /news')


@bot.message_handler(commands=['news'])
def print_news(message):
    p.parse()
    news = p.get_news()
    answer = ''
    num = 1
    for item in news:
        answer += '/' + str(num) + ' ' + item['heading'] + ", " + item['time'] + ": " + item['title'] + '\n'
        num += 1
    bot.reply_to(message, answer)


@bot.message_handler(regexp=r'/[\d]{1,2}')
def print_detailed(message):
    bot.reply_to(message, p.get_detailed(int(message.text.replace('/', ''))-1))


@bot.message_handler(content_types='text')
def reverse_text(message):
    bot.reply_to(message, message.text)


bot.polling()
