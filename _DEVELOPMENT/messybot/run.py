import sys
sys.path.insert(0, '/Users/provolot/github/slackbot')
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import re, datetime
import logging
from lib.singleton import Messybot
from lib.isyclient import IsyClient
import slackbot_settings


@default_reply
def my_default_handler(message):
    message.reply("Sorry, but I didn't understand you")

def main(db_location):

    logging.basicConfig()

    #singletonclass
    messybot = Messybot()

    # TODO: Database connection
    # TODO: something like   messybot.db = sqlite3.connect(db_location, check_same_thread=False)

    # TODO: other integrations
    #    messybot.sonos = Sonos(slackbot_settings) ETC ETC

    messybot.isyclient = IsyClient(slackbot_settings)

    # TODO: The slackbot itself

    messybot.bot = Bot()
    messybot.bot.run()

if __name__ == "__main__":
    main("DBNAME")

