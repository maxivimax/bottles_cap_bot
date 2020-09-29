import telebot
import time
import random
import os
from telebot import types

# http://qrcoder.ru/
# https://decodeit.ru/binary/

all_shop = ['buy1', 'buy2', 'buy3', 'buy4']

print("GGG")

bot = telebot.TeleBot('1351828918:AAGZw4c9oiPng4NkVK2X6eyzaTYny7hU36U')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Ввести код для баллов')
keyboard1.row('Что такое баллы?', 'Рандомный товар', 'Мой баланс')
keyboard1.row('Мой код для покупок')


@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1) 

@bot.message_handler(content_types=['photo'])
def sss(message):
        user_id = message.from_user.id
        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        file_path = 'F:/ПРОЕКТЫ/BotTele/photos/'+str(user_id)+".jpg"

        src='F:/ПРОЕКТЫ/BotTele/photos/'+str(user_id)+".jpg";
        with open(src, 'wb') as new_file:
           new_file.write(downloaded_file)
        time.sleep(1) #ТЕСТ!
        os.remove(file_path)

@bot.message_handler(content_types=['text'])
def send_text(message):
    user_id = message.from_user.id
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')

    elif message.text.lower() == 'ввести код для баллов':
    	print("d")
        # user_id = message.from_user.id
        # print("+")
        # global fr
        # keyboard1.row('Отмена')

        # bot.register_next_step_handler(message, number_add)
    elif message.text.lower() == 'что такое баллы?':
        user_id = message.from_user.id
        bot.send_message(message.chat.id, 'Баллы нужны для покупки товаров. Их можно получить сдавая крышки от бутылок в наших аппаратах')
    elif message.text.lower() == 'отмена':
        user_id = message.from_user.id
        bot.send_message(message.chat.id, 'Баллы нужны для покупки товаров. Их можно получить сдавая крышки от бутылок в наших аппаратах')

    elif message.text.lower() == 'рандомный товар':

        user_id = message.from_user.id
        lol="rand"

        rand = random.choices(all_shop, k=1)
        if(lol == rand):
        	rand = random.choices(all_shop, k=1)
        else:
        	lol = rand
	        print(rand)
	        
	        if(str(rand) == "['buy1']"):
	            keyboard = types.InlineKeyboardMarkup()
	            callback_button2 = types.InlineKeyboardButton(text="Купить", url="https://maxivimax.github.io/buy/1.html")
	            keyboard.add(callback_button2)
	            bot.send_message(message.chat.id, 'https://maxivimax.github.io/buy/1.html', reply_markup=keyboard)
	            img = open('img/1.PNG', 'rb')
	            bot.send_photo(message.chat.id, img)
	        elif(str(rand) == "['buy2']"):
	            keyboard = types.InlineKeyboardMarkup()
	            callback_button2 = types.InlineKeyboardButton(text="Купить", url="https://maxivimax.github.io/buy/2.html")
	            keyboard.add(callback_button2)
	            bot.send_message(message.chat.id, 'https://maxivimax.github.io/buy/2.html', reply_markup=keyboard)
	            img = open('img/2.PNG', 'rb')
	            bot.send_photo(message.chat.id, img)
	        elif(str(rand) == "['buy3']"):
	            keyboard = types.InlineKeyboardMarkup()
	            callback_button2 = types.InlineKeyboardButton(text="Купить", url="https://maxivimax.github.io/buy/3.html")
	            keyboard.add(callback_button2)
	            bot.send_message(message.chat.id, 'https://maxivimax.github.io/buy/3.html', reply_markup=keyboard)
	            img = open('img/3.PNG', 'rb')
	            bot.send_photo(message.chat.id, img)
	        elif(str(rand) == "['buy4']"):
	            keyboard = types.InlineKeyboardMarkup()
	            callback_button2 = types.InlineKeyboardButton(text="Купить", url="https://maxivimax.github.io/buy/4.html")
	            keyboard.add(callback_button2)
	            bot.send_message(message.chat.id, 'https://maxivimax.github.io/buy/4.html', reply_markup=keyboard)
	            img = open('img/4.PNG', 'rb')
	            bot.send_photo(message.chat.id, img)
	        else:
	        	bot.send_message(message.chat.id, 'Эммм')


    elif message.text.lower() == 'мой баланс':
        user_id = message.from_user.id
        fr = "Повторите запрос"
        try:
            kr = open(str(user_id) + ".txt", "r")
            fr = kr.read()
        except IOError:
            print ("No file")

            open(str(uSser_id) + '.txt', 'tw', encoding='utf-8')

            f1 = open(str(user_id) + ".txt", 'w')
            f1.write("0")

        bot.send_message(message.chat.id, 'Ваш баланс: ' + str(fr) + ' крышек')

def number_add(msg):
    user_id = msg.from_user.id
    msga = msg.text

    print(msg)

    try:
        kr = open(str(user_id) + ".txt", "r")
        fr = kr.read()
        baka = "1"
        if(fr == ""):
            print ("No file")

            open(str(user_id) + '.txt', 'tw', encoding='utf-8')

            f1 = open(str(user_id) + ".txt", 'w')
            f1.write("0")

        idNumber = int(fr) + int(msga) 
        # "НЕРЕШИМАЯ ЗАДАЧА"

        f1 = open(str(user_id) + ".txt", 'w')
        # Что надо было
        f1.write(str(idNumber))
    except IOError:
        print ("No file")

        open(str(user_id) + '.txt', 'tw', encoding='utf-8')

        f1 = open(str(user_id) + ".txt", 'w')
        f1.write("0")

bot.polling()