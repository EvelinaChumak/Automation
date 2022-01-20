import os
from dotenv import load_dotenv


class Urls(object):
    API_URL = "http://api.openweathermap.org/data/{}/weather?"
    load_dotenv()
    API_KEY = str(os.environ.get('WEATHER_API_KEY'))
