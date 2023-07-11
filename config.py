from telebot import TeleBot
from redis import Redis


TOKEN = "6390422137:AAFwCPPG-pX8lHjkQS6-mkIxrM71Y1yHDtQ"
bot = TeleBot(TOKEN)

API_exchange = 'E480C05D-954A-4131-9929-7FB85082629A'

red = Redis('localhost', 6379)

cur_dict = {'USD': 'USD', 'RUB': 'RUB', 'Bitcoin': 'BTC', 'Ethereum': 'ETH', 'Dogecoin': 'DOGE', 'Litecoin': 'LTC',
            'Tether': 'USDT', 'USD Coin': 'USDC', 'Pepe': "PEPE", 'TRON': 'TRX', 'Kava': 'KAVA', 'XRP': 'XRP',
            'Bitcoin Cash': 'BCH', 'Solana': 'SOL', 'Waves': 'WAVES', 'Polygon': 'MATIC', 'True USD': 'TUSD',
            'Cardano': 'ADA', 'eCash': 'XEC', 'Metal': 'MTL', 'Arbitrum': 'ARB'}
cur_list = list(cur_dict)

text0 = 'Добро пожаловать в наш конвертер валют!\nВыберите исходную валюту:'
text1 = 'Выберите целевую валюту:'
text2, text3 = 'Напишите, сколько ', ' необходимо сконвертировать?'
text4 = 'Неверный формат! Попробуйте еще раз'
b00 = 'Назад'
b01 = 'Еще'
