from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
from lib.singleton import Messybot
import time

messybot = Messybot()

@listen_to('zwavestatus', re.IGNORECASE)
def zwavestatus(message):
    message.reply("Zwave status: " + str(messybot.isyclient.getStatus()))

@listen_to('all.*on', re.IGNORECASE)
def runteston(message):
    message.reply("lights all on - ranThen program 0003!")
    messybot.isyclient.isy.programs['0003'].runThen()

@listen_to('all.*off', re.IGNORECASE)
def runtestoff(message):
    message.reply("lights all off - ranElse program 0003!")
    messybot.isyclient.isy.programs['0003'].runElse()

@listen_to('unlock.*door', re.IGNORECASE)
def unlockdoor(message):
    # Message is replied to the sender (prefixed with @user)
    timedelay = 5
    message.reply("Okay! I'll unlock the door for the next " + str(timedelay) + " seconds.")
    messybot.isyclient.isy.nodes['ZW017_1'].on()
    time.sleep(timedelay)
    messybot.isyclient.isy.nodes['ZW017_1'].off()
    message.reply("Door locked again!")



