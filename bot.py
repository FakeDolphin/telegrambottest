import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('stickers/stic1.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Random int")
    item2 = types.KeyboardButton("How are you?")

    markup.add(item1, item2)

    #keyboard2
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    item3 = types.InlineKeyboardMarkup("Well", callback_data='good')
    item4 = types.InlineKeyboardMarkup("Nice", callback_data='bad')

    bot.send_message(message.chat.id, "Hello cunt, {0.first_name}!\nI - <b>{1.first_name}</b>, бот созданный чтобы послать тебя нахуй".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def repeat(message):
        if message.chat.type == "private":
            if message.text == 'Random int':
                bot.send_message(message.chat.id, str(random.randint(0, 1000)))
            elif message.text == 'How are you?':
                markup2.add(item3, item4)
                bot.send_message(message.chat.id, 'Good wub?',reply_markup=markup2)
            else:
                bot.send_message(message.chat.id, 'Repeat, I dont understand')

@bot.callback_query_handler(func = lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'Well':
                bot.send_message(call.message.chat.id, 'Super')
            elif call.data == 'Nice':
                bot.send_message(call.message.chat.id, 'And?')

            #remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text_reply_markup=None)

            #show alert
            bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False,text="It's test")
    except Exception as e:
        print(repr(e))

#Отвечает так же как и ты
#@bot.message_handler(content_types=['text'])
#def repeat(message):
#    bot.send_message(message.chat.id, message.text)

#RUN
bot.polling(none_stop=True)