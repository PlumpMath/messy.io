import slackbot_settings
import PyISY
print(slackbot_settings.PYISY_ADDR, slackbot_settings.PYISY_PORT, slackbot_settings.PYISY_USER, slackbot_settings.PYISY_PASS)
client = PyISY.ISY(slackbot_settings.PYISY_ADDR, slackbot_settings.PYISY_PORT, slackbot_settings.PYISY_USER, slackbot_settings.PYISY_PASS)
print(client.connected)
