import telebot
import config
import datetime

now = datetime.datetime.now()
today = now.weekday()
hour = now.hour

chat_id = config.chat_id

bot = telebot.TeleBot(config.API)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Welcome CSE-3A \n" +
                          "I'll send you your timetable for the day\n"+
                          "Every morning at 8 AM \n" + 
                          "Made with love by Anmol Goel."
            )

if today == 0:
    bot.send_message(chat_id=chat_id,
                text = "Monday - Time Table\n"+
		       str(now.day) + "-" +str(now.month) + "-" + str(now.year) + "\n" +
                       "08:30 - CGMM\n"+
                       "09:20 - DS\n" + 
                       "10:10 - FCS\n" +
                       "11:00 - CNS\n" +
                       "12:20 - STLD\n" +
                       "1:10 - AM\n" +
                       "2:20 - CGMM Lab-I & CNS Lab-II"
            )
elif today == 1:
    bot.send_message(chat_id=chat_id,
                text = "Tuesday - Time Table\n"+
		       str(now.day) + "-" +str(now.month) + "-" + str(now.year) + "\n" +
                       "08:30 - AM\n"+
                       "09:20 - STLD\n" + 
                       "10:10 - DS\n" +
                       "11:00 - CNS\n" +
                       "12:20 - DS Lab-I & STLD Lab-II\n" +
                       "2:20 - CGMM\n" +
                       "3:10 - FCS"
            )
elif today == 2:
    bot.send_message(chat_id=chat_id,
                text = "Wednesday - Time Table\n"+
		       str(now.day) + "-" +str(now.month) + "-" + str(now.year) + "\n" +
                       "08:30 - CNS\n"+
                       "09:20 - STLD\n" + 
                       "10:10 - FCS\n" +
                       "11:00 - DS\n" +
                       "12:20 - AM\n" +
                       "1:10 - CGMM\n" +
                       "2:20 - Activity"
            )
elif today == 3:
    bot.send_message(chat_id=chat_id,
                text = "Thursday - Time Table\n"+
		       str(now.day) + "-" +str(now.month) + "-" + str(now.year) + "\n" +
                       "08:30 - AM\n"+
                       "09:20 - CGMM\n" + 
                       "10:10 - FCS\n" +
                       "11:00 - CNS\n" +
                       "12:20 - STLD Lab-I & CGMM Lab-II\n" +
                       "2:20 - STLD\n" +
                       "2:20 - DS"
            )
elif today == 4:
    bot.send_message(chat_id=chat_id,
                text = "Friday - Time Table\n"+
		       str(now.day) + "-" +str(now.month) + "-" + str(now.year) + "\n" +
                       "08:30 - DS\n"+
                       "09:20 - CGMM\n" + 
                       "10:10 - CNS\n" +
                       "11:00 - Library\n" +
                       "12:20 - STLD\n" +
                       "1:10 - AM\n" +
                       "2:20 - CNS Lab-I & DS Lab-II"
            )
  
    
