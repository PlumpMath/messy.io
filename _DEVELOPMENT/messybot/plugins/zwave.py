from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
from lib.singleton import Messybot
import time

messybot = Messybot()

@listen_to('zwavestatus', re.IGNORECASE)
def zwavestatus(message):
    message.reply("Zwave status: " + str(messybot.isyclient.getStatus()))

@listen_to('runteston', re.IGNORECASE)
def runteston(message):
    messybot.isyclient.isy.programs['0003'].runThen()
    message.reply("ranThen program 0003!")

@listen_to('runtestoff', re.IGNORECASE)
def runtestoff(message):
    messybot.isyclient.isy.programs['0003'].runElse()
    message.reply("ranElse program 0003!")

@respond_to('unlock.*door', re.IGNORECASE)
def unlockdoor(message):
    # Message is replied to the sender (prefixed with @user)
    timedelay = 5
    message.reply("Okay! I'll unlock the door for the next " + str(timedelay) + " seconds.")
    messybot.isyclient.isy.nodes['ZW017_1'].on()
    time.sleep(timedelay)
    messybot.isyclient.isy.nodes['ZW017_1'].off()



