from slackbot.bot import respond_to
from slackbot.bot import listen_to
import lib.phrases as phrases
import re


@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    message.react('+1')

@respond_to('I love you')
def love(message):
    message.reply("I love you too! "+ phrases.compliment() + "!")

@listen_to('listen')
def listen(message):
    message.reply("... I'm always listening ... ")

@listen_to('omg')
def omg(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply("omg, what what what?")

@listen_to('guys')
def guys(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply("oh heyy, did you mean " + phrases.guys_alts() + "?")

