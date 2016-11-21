from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    message.react('+1')

@respond_to('I love you')
def love(message):
    message.reply('I love you too!')

@listen_to('listen')
def listen(message):
    message.reply("... I'm always listening ... ")

@listen_to('Can someone help me?')
def help(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply('Yes, I can!')

    # Message is sent on the channel
    # message.send('I can help everybody!')

@respond_to('omg')
def omg(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply('oh my god, what?')

    # Message is sent on the channel
    # message.send('I can help everybody!')

@respond_to('unlock', re.IGNORECASE)
def unlockdoor(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply("Okay! I'll unlock the door for the next 10 seconds.")

    # Message is sent on the channel
    # message.send('I can help everybody!')

@respond_to('respondtime', re.IGNORECASE)
def respondtime(message):
    message.reply("respond: current time =" + str(datetime.datetime.now()))

@listen_to('listentime', re.IGNORECASE)
def listentime(message):
    message.reply("listen: current time =" + str(datetime.datetime.now()))

