import os

class Urls(object):
    API_URL = "http://api.openweathermap.org/data/{}/weather?"
    API_KEY = os.getenv('WEATHER_API_KEY')
