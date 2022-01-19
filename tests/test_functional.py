from tests.config.info_for_api import InfoForProject
from tests.config.urls import Urls
from tests.models.weather_api import WeatherAPI
from tests.config.info_for_api import InfoForProject
from framework.utils.api import API
from tests.utils.city_list import CityList
import allure
import pytest


class TestWeatherApi():

    def test_xml(self):
        city = CityList.get_random_city()
        id = CityList.get_attr(city, CityList.ID)

        weather = WeatherAPI.get_by_attr(id=id)
        code = weather.get_status()

        assert code == API.OK, 'Ответ получен с кодом {}'.format(code)
        
        temp = weather.main.temp 

        assert InfoForProject.TEMP_MIN < temp < InfoForProject.TEMP_MAX, 'Температура не в градусах Цельсия'

