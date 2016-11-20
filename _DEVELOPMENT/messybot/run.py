from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
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

@default_reply
def my_default_hanlder(messsage):
    message.reply("Sorry, but I didn't understand you")


def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()

