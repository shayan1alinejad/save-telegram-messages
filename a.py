import telebot

bot = telebot.TeleBot("توکن بات دریافت شده از باتفادر")



##اکو کردن کل مسیج ها
@bot.message_handler(func=lambda message: True)
def echo_all(message):
  bot.reply_to(message, "saved to database")
  with open('Saved.txt', 'a') as f: 
    f.write(message.from_user.first_name+" Ino Ferestad: "+message.text+"\n") 

bot.infinity_polling()
