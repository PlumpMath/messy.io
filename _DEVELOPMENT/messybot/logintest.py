import sys
sys.path.insert(0, '/Users/provolot/github/PyISY')
sys.path.insert(0, '/home/provolot/_GITHUB/PyISY')
import PyISY
import slackbot_settings
print(slackbot_settings.PYISY_ADDR, slackbot_settings.PYISY_PORT, slackbot_settings.PYISY_USER, slackbot_settings.PYISY_PASS)
client = PyISY.ISY(slackbot_settings.PYISY_ADDR, slackbot_settings.PYISY_PORT, slackbot_settings.PYISY_USER, slackbot_settings.PYISY_PASS)
print(client.connected)
