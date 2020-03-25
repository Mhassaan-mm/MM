from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionWeather(Action):
    def name(self):
        return 'action_weather'
    def run(self, dispatcher, tracker, domain):
        # from apixu.client import ApixuClient
        from weatherstack import ApixuClient
        api_key = 'ec2ebc55f3e54c4ee9b91960a2000d83'
        client = ApixuClient(api_key)

        loc = tracker.get_slot('location')
        current = client.current(q=loc)
        # print(current)
        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['weather_descriptions']
        temperature_c = current['current']['temperature']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_speed']

        response = """It is currently {} in {} at the moment. The temperature is {} degrees,the humidity is {}% and the wind speed is {} mph.""".format(condition,city,temperature_c,humidity,wind_mph)

        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]


