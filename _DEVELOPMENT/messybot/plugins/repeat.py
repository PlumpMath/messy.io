from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

@listen_to('repeat', re.IGNORECASE)
def repeat(message):
    print message
    message.reply('repeatrepeat')

