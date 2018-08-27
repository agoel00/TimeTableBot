import telebot
import config
import test
import datetime


now = datetime.datetime.now()
today = now.weekday
hour = now.hour

bot = telebot.TeleBot(config.API)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome!\n"+
                          "To view time table for any day just send me a message\n" +
                          "Like this: '\mon'(to view Monday's timetable) \n or 'tue'(to view Tuesday's time table) \n" +
                          "Made with love by Anmol Goel"
            )

@bot.message_handler(commands=['mon'])
def monday(message):
    bot.send_message(message.chat.id,
            'Monday - Time Table\n' +
            '08:30 - CGMM\n' +
            '09:20 - DS \n' +
            '10:10 - FCS \n' +
            '11:00 - CNS \n' +
            '12:20 - STLD \n' +
            '1:10 - AM \n' + 
            '2:20 - CGMM Lab-I & CNS Lab-II'
            )

@bot.message_handler(commands=['tue'])
def tuesday(message):
    bot.send_message(message.chat.id,
            'Tuesday - Time Table\n' +
            '08:30 - AM\n' +
            '09:20 - STLD \n' +
            '10:10 - DS \n' +
            '11:00 - CNS \n' +
            '12:20 - DS Lab-I & STLD Lab-II \n' +
            '2:20 - CGMM \n' + 
            '3:10 - FCS'
            )

@bot.message_handler(commands=['wed'])
def wednesday(message):
    bot.send_message(message.chat.id,
            'Wednesday - Time Table\n' +
            '08:30 - CNS\n' +
            '09:20 - STLD \n' +
            '10:10 - FCS \n' +
            '11:00 - DS \n' +
            '12:20 - AM \n' +
            '1:10 - CGMM \n' + 
            '2:20 - Activity'
            )

@bot.message_handler(commands=['thu'])
def thursday(message):
    bot.send_message(message.chat.id,
            'Thursday - Time Table\n' +
            '08:30 - AM\n' +
            '09:20 - CGMM \n' +
            '10:10 - FCS \n' +
            '11:00 - CNS \n' +
            '12:20 - STLD Lab-I & CGMM Lab-II \n' +
            '2:20 - STLD \n' + 
            '3:10 - DS'
            )

@bot.message_handler(commands=['fri'])
def friday(message):
    bot.send_message(message.chat.id,
            'Friday - Time Table\n' +
            '08:30 - DS\n' +
            '09:20 - CGMM \n' +
            '10:10 - CNS \n' +
            '11:00 - Library \n' +
            '12:20 - STLD \n' +
            '1:10 - AM \n' + 
            '2:20 - CNS Lab-I & DS Lab-II'
            )



bot.polling()
