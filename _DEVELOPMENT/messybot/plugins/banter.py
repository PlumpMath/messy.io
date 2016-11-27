from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

@listen_to('repeat', re.IGNORECASE)
def repeat(message):
    print(message)
    message.reply('repeatrepeat')

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


@listen_to('omg')
def omg(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply("omg, what what what?")

