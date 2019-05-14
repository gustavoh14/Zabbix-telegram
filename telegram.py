
#!/usr/bin/env python

import telebot,sys

BOT_TOKEN='899380405:AAGn3WAe_FTe6ISuPp47DpLJk1yv2y9EsOE'
DESTINATION=sys.argv[1]
SUBJECT=sys.argv[2]
MESSAGE=sys.argv[3]

MESSAGE = MESSAGE.replace('/n','\n')
tb = telebot.TeleBot(BOT_TOKEN)
tb.send_message(DESTINATION,SUBJECT + '\n' + MESSAGE)
