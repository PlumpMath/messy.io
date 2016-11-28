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

@respond_to("who?", re.IGNORECASE)
def who(message):
    message.reply('I am friendly bot.')
    details = ""
    details += "text = '{}'\n".format(message.body["text"])
    details += "ts = '{}'\n".format(message.body["ts"])
    details += "user id = '{}'\n".format(message.body["user"])
    details += "user name = '{}'\n".format(message._client.users.get(message.body["user"])["name"])
    details += "team id = '{}'\n".format(message.body["team"])
    details += "type = '{}'\n".format(message.body["type"])
    details += "channel = '{}'\n".format(message.body["channel"])
    message.reply('```{}```'.format(details))
