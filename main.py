import telebot
from telebot import types
from language import answers
import random
from colorama import  Fore
import atexit


TOKEN = '6804013273:AAGprSmqIMYQxmpQ7gMXLBEFJJq5S5w1i7E'
bot = telebot.TeleBot(TOKEN)

# /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, answers["greetings"])

# /help
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message, answers["help"])

# /kick
@bot.message_handler(commands=['kick'])
def kick_user(message):
    admins = bot.get_chat_administrators(message.chat.id)
    user_id = message.from_user.id
    print(user_id)
    for admin in admins:
        if admin.user.id == user_id:
            break
    else:
        bot.reply_to(message, "You are not an admin")
        return

    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.kick_chat_member(message.chat.id, user_id)
        bot.reply_to(message, f"User {message.reply_to_message.from_user.first_name} has been kicked from the chat.")
    else:
        bot.reply_to(message, "Use this command by replying to a user's message.")

# /mute
@bot.message_handler(commands=['mute'])
def mute_user(message):
    admins = bot.get_chat_administrators(message.chat.id)
    user_id = message.from_user.id
    print(user_id)
    for admin in admins:
        if admin.user.id == user_id:
            break
    else:
        bot.reply_to(message, "You are not an admin")
        return

    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=False)
        bot.reply_to(message, f"User {message.reply_to_message.from_user.first_name} has been muted.")
    else:
        bot.reply_to(message, "Use this command by replying to a user's message.")


# /unmute
@bot.message_handler(commands=['unmute'])
def unmute_user(message):
    admins = bot.get_chat_administrators(message.chat.id)
    user_id = message.from_user.id
    print(user_id)
    for admin in admins:
        if admin.user.id == user_id:
            break
    else:
        bot.reply_to(message, "You are not an admin")
        return

    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=True)
        bot.reply_to(message, f"User {message.reply_to_message.from_user.first_name} has been unmuted.")
    else:
        bot.reply_to(message, "Use this command by replying to a user's message.")


# /language
@bot.message_handler(commands=['language'])
def language_command(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(types.InlineKeyboardButton("English🇺🇸", callback_data='english'))
    bot.reply_to(message, "Choose the language of the bot:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'english')
def callback_handler(call):
    bot.send_message(call.message.chat.id, "You have chosen English🇺🇸 language.")
    bot.delete_message(call.message.chat.id, call.message.message_id)

# Обработчик упоминания бота в сообщении
@bot.message_handler(func=lambda message: message.text and ('бот' in message.text.lower() or '@StarlineOrgBot' in message.text or 'bot' in message.text))
def reply_to_bot_mention(message):
    bot.reply_to(message, answers["bot_mention"])

# Обработчик сообщений с вопросами
@bot.message_handler(func=lambda message: message.text and message.text.lower().startswith('starline') and '?' in message.text.lower())
def answer_question(message):
    response = random.choice(answers["questions"])
    bot.reply_to(message, response)

print(Fore.LIGHTGREEN_EX + "░██████╗████████╗░█████╗░██████╗░████████╗███████╗██████╗░░░░░░░░░░██╗░░░░░░░██╗░█████╗░██████╗░██╗░░██╗")
print(Fore.LIGHTGREEN_EX + "██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗░░░░░░░░░██║░░██╗░░██║██╔══██╗██╔══██╗██║░██╔╝")
print(Fore.LIGHTGREEN_EX + "╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░█████╗░░██║░░██║░░░░░░░░░╚██╗████╗██╔╝██║░░██║██████╔╝█████═╝░")
print(Fore.LIGHTGREEN_EX + "░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░██╔══╝░░██║░░██║░░░░░░░░░░████╔═████║░██║░░██║██╔══██╗██╔═██╗░")
print(Fore.LIGHTGREEN_EX + "██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░███████╗██████╔╝░░░░░░░░░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██║░╚██╗")
print(Fore.LIGHTGREEN_EX + "╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░░░░░░░░░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝")
def stop_work():
    print(Fore.LIGHTRED_EX + "███████╗██╗███╗░░██╗██╗░██████╗██╗░░██╗███████╗██████╗░░░░░░░░░░██╗░░░░░░░██╗░█████╗░██████╗░██╗░░██╗")
    print(Fore.LIGHTRED_EX + "██╔════╝██║████╗░██║██║██╔════╝██║░░██║██╔════╝██╔══██╗░░░░░░░░░██║░░██╗░░██║██╔══██╗██╔══██╗██║░██╔╝")
    print(Fore.LIGHTRED_EX + "█████╗░░██║██╔██╗██║██║╚█████╗░███████║█████╗░░██║░░██║░░░░░░░░░╚██╗████╗██╔╝██║░░██║██████╔╝█████═╝░")
    print(Fore.LIGHTRED_EX + "██╔══╝░░██║██║╚████║██║░╚═══██╗██╔══██║██╔══╝░░██║░░██║░░░░░░░░░░████╔═████║░██║░░██║██╔══██╗██╔═██╗░")
    print(Fore.LIGHTRED_EX + "██║░░░░░██║██║░╚███║██║██████╔╝██║░░██║███████╗██████╔╝░░░░░░░░░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██║░╚██╗")
    print(Fore.LIGHTRED_EX + "╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝╚═════╝░╚═╝░░╚═╝╚══════╝╚═════╝░░░░░░░░░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝")
atexit.register(stop_work)
bot.infinity_polling(none_stop=True)
