from re import search
from requests import get
from json import loads

from telebot import types

from config import *


def mes_depot(message, text, cur=None, new_mes=False, back_but=False, again_but=False, number_mes=0):
    markup = types.InlineKeyboardMarkup(row_width=3)
    if cur:
        cur_amount = len(cur)
        for i in range(0, cur_amount, 3):
            b1 = types.InlineKeyboardButton(cur[i], callback_data=cur[i])
            if cur_amount - i > 2:
                b2 = types.InlineKeyboardButton(cur[i + 1], callback_data=cur[i + 1])
                b3 = types.InlineKeyboardButton(cur[i + 2], callback_data=cur[i + 2])
                markup.add(b1, b2, b3)
            elif cur_amount - i > 1:
                b2 = types.InlineKeyboardButton(cur[i + 1], callback_data=cur[i + 1])
                markup.add(b1, b2)
            else:
                markup.add(b1)
    if back_but:
        b = types.InlineKeyboardButton(b00, callback_data=b00)
        markup.add(b)
    if again_but:
        b = types.InlineKeyboardButton(b01, callback_data=b01)
        markup.add(b)
    if new_mes:
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        bot.edit_message_text(text, message.chat.id, message.id + number_mes, reply_markup=markup)


def read_money(message):
    try:
        money = search(r'\d+(?:[.,]\d+)?', message.text)[0]
    except TypeError:
        mes_depot(message, text4, new_mes=True, back_but=True)
        mes_depot(message, text2 + red.get(str(message.chat.id) + "cur1").decode() + text3, number_mes=-1)
        bot.register_next_step_handler(message, read_money)
    else:
        if ',' in money:
            money = money.replace(',', '.')
        get_price(money, message)


def get_price(money, message):
    cur_1 = red.get(str(message.chat.id) + "cur1").decode()
    cur_1 = cur_dict[cur_1]
    cur_2 = red.get(str(message.chat.id) + "cur2").decode()
    cur_2 = cur_dict[cur_2]
    url = f'https://rest.coinapi.io/v1/exchangerate/{cur_1}/{cur_2}'
    headers = {'X-CoinAPI-Key': API_exchange}
    res = loads(get(url, headers=headers).content)
    rate = res['rate']
    cost = float(money) * rate
    cost = rounder(cost)
    rate = rounder(rate)
    text = f'{cur_1} | {money}  >>>  {cost} | {cur_2}\nКурс: {rate}'
    mes_depot(message, text, new_mes=True, again_but=True)
    bot.delete_message(message.chat.id, message.id - 1)


def rounder(digit):
    digit = float(digit)
    if digit >= 10:
        digit = round(digit, 2)
    elif digit >= 1:
        digit = round(digit, 3)
    else:
        d = digit
        counter = 0
        for i in range(30):
            d *= 10
            counter += 1
            if d >= 1:
                break
        num = counter + 3
        digit = round(digit, num)
        digit = '{:.{n}f}'.format(digit, n=num)
    return digit
