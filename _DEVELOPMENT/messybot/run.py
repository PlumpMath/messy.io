from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import re, datetime
import logging
from lib.singleton import Messybot



@default_reply
def my_default_handler(messsage):
    message.reply("Sorry, but I didn't understand you")


def main(db_location):

    logging.basicConfig()

    #singletonclass
    messybot = Messybot()

	
    # TODO: Database connection
    # TODO: start zwave
    # TODO: The slackbot itself


    messybot.bot = Bot()
    messybot.bot.run()

if __name__ == "__main__":
    main("DBNAME")

