from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import idle
import re
import time

@respond_to('stat$', re.IGNORECASE)
@respond_to('stat (.*) (.*)', re.IGNORECASE)
def stats(message, start_date=None, end_date=None):
    print("stats!")
    message.reply("okay stats")
    message.reply(start_date)
    message.reply(end_date)


@respond_to('respondtime', re.IGNORECASE)
def respondtime(message):
    message.reply("respond: current time =" + str(datetime.datetime.now()))

@listen_to('listentime', re.IGNORECASE)
def listentime(message):
    message.reply("listen: current time =" + str(datetime.datetime.now()))

