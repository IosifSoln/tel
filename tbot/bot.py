import config, requests, telebot
import notify
bot = telebot.TeleBot(config.token)
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


'''клавиатура с командами'''
"""приветственное сообщение с информацией"""


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/start', '/rate','/listOfCurrencies')
    bot.send_message(message.chat.id, text='Hi! to find out the rate, enter the command /rate,'
                                           ' if the required currency '
                                           'is not there, just enter the name '
                                           'of the desired currency'
                                           'to see a list of available currencies '
                                           'enter /listOfCurrencies', reply_markup=keyboard)


"""создается клавиатура"""


@bot.message_handler(commands=['rate'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='BTC', callback_data='BTC'))
    markup.add(telebot.types.InlineKeyboardButton(text='ETH', callback_data='ETH'))
    markup.add(telebot.types.InlineKeyboardButton(text='LTC', callback_data='LTC'))
    markup.add(telebot.types.InlineKeyboardButton(text='USDT', callback_data='USDT'))
    markup.add(telebot.types.InlineKeyboardButton(text='ADA', callback_data='ADA'))
    markup.add(telebot.types.InlineKeyboardButton(text='DOT', callback_data='DOT'))
    markup.add(telebot.types.InlineKeyboardButton(text='XRP', callback_data='XRP'))
    markup.add(telebot.types.InlineKeyboardButton(text='EOS', callback_data='EOS'))
    markup.add(telebot.types.InlineKeyboardButton(text='DOGE', callback_data='DOGE'))

    bot.send_message(message.chat.id, text='what cryptocurrency rate do you need ?', reply_markup=markup)


"""ответ на клавиатуру с вопросами"""


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    str = 'USD-' + call.data
    answer = notify.main(str)

    bot.send_message(call.message.chat.id, answer+'$')


"""создание списка клавиатур"""


@bot.message_handler(commands=['listOfCurrencies'])
def send_spis(message):
    bot.send_message(message.chat.id, text='BTC , DOGE , ETH , USDT , ADA , SC , LTC ,'
                                           ' DGB ,XRP , HBAR , TUSD , LINK , XLM'
                                           ', CELO , TRX , USDC , ALGO , RVN , BCH ,'
                                           'DASH ,BSV , EOS , DOT  , ATOM , CRO , XTZ ,'
                                           'ETC , UNI , ENJ , ZRX , WAXP , BAT , DAI ,'
                                           'ADABULL , ZEN , COMP , PAX , OMG , IOTA ,'
                                           'MATIC , SOLVE , FIL , GRT , RSV , KMD , MANA , HIVE')


"""переводит введенный текст"""


@bot.message_handler(content_types=['text'])
def send(message):
    str = 'USD-' + message.text.upper()
    bot.send_message(message.chat.id, notify.main(str))







"""бесконечный цикл работы"""
if __name__ == '__main__':
    bot.infinity_polling()
