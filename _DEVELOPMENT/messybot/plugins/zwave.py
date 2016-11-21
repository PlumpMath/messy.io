from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
from lib.singleton import Messybot

messybot = Messybot()

@listen_to('zwavestatus', re.IGNORECASE)
def zwavestatus(message):
    message.reply("Zwave status: " + str(messybot.isyclient.getStatus()))

@listen_to('runteston', re.IGNORECASE)
def runteston(message):
    messybot.isyclient.session.programs['0003'].runThen()
    message.reply("ranThen program 0003!")

@listen_to('runtestoff', re.IGNORECASE)
def runtestoff(message):
    messybot.isyclient.session.programs['0003'].runElse()
    message.reply("ranElse program 0003!")


@respond_to('unlock', re.IGNORECASE)
def unlockdoor(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply("Okay! I'll unlock the door for the next 10 seconds.")



