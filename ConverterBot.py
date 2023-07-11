from functions import *


@bot.message_handler(commands=['start'])
def start(message):
    mes_depot(message, text0, cur_list, new_mes=True)


@bot.callback_query_handler(func=lambda call: True)
def call_back_handler(call):
    data = call.data
    chat_id = call.message.chat.id
    text = call.message.text
    message = call.message
    if data == b00:
        bot.clear_step_handler_by_chat_id(chat_id)
        mes_depot(message, text0, cur_list)
    elif data == b01:
        mes_depot(message, text0, cur_list, new_mes=True)
        bot.edit_message_reply_markup(chat_id, message.id)
    elif text == text0:
        red.set(str(chat_id) + "cur1", data)
        cur = cur_list.copy()
        cur.remove(data)
        mes_depot(message, text1, cur, back_but=True)
    elif text == text1:
        red.set(str(chat_id) + "cur2", data)
        mes_depot(message, text2 + red.get(str(chat_id) + "cur1").decode() + text3, back_but=True)
        bot.register_next_step_handler(message, read_money)


bot.infinity_polling()
