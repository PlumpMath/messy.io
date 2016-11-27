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
        
        # If a name is ambiguous:
#        client.rtm_send_message(client.find_channel_by_name('ambiguous'), "To ambiguous the channel")
#        client.rtm_send_message(client.find_user_by_name('ambiguous'), "To ambiguous the user")
        
        # Attachments can be sent with `client.rtm_send_message(..., attachments=attachments)`.

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

