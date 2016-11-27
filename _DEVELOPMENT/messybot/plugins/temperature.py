from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import idle
import re
import time

last_bored = time.time()
@idle
def bored(client):
    global last_bored
    if time.time() - last_bored >= 5:
        last_bored = time.time()
        
        # Messages can be sent to a channel
        client.rtm_send_message(slackbot_settings.MAIN_CHANNEL, "I'm bored!")

@listen_to('hot', re.IGNORECASE)
def hottest(message):
    message.react(':snowman:')
    message.react('fire')


