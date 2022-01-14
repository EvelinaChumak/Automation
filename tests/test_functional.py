from tests.utils.weather_api import WeatherApi
from tests.utils.city_list import CityList
from framework.constants.status import Status
import allure
import pytest


class TestWeatherApi(object):

    def test_xml(self, read_city_info):
        api = WeatherApi()

        city = pytest.city_list.get_random_city()
        lon, lat = pytest.city_list.get_city_coord(city)

        weather = api.get_xml_by_coord(lat, lon)
        code = api.get_status()

        assert code == Status.OK, 'Ответ получен с кодом {}'.format(code)

        assert api.is_xml(), 'Данные получены не в формате xml'

        assert weather.is_lat_lon_correct(lat, lon), 'Полученные координаты: {}, ожидаемые: {}'.format(
            weather.get_coords(), [lat, lon])

        assert weather.is_rus_leng, 'Данные получены не на русском языке'

    def test_temp(self):
        api = WeatherApi()

        city = pytest.city_list.get_random_city()
        id = pytest.city_list.get_city_id(city)

        weather = api.get_json_by_id(id)

        code = api.get_status()

        assert code == Status.OK, 'Ответ получен с кодом {}'.format(code)

        assert weather.is_temp_cels(), 'Температура не в градусах Цельсия'
