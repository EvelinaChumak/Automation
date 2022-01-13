from tests.utils.weather_api import WeatherApi
import allure


class TestWeatherApi(object):
    def test_xml(self):
        api = WeatherApi()
        answ = api.get_xml()
        assert False

