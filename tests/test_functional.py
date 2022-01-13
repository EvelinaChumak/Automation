from tests.utils.weather_api import WeatherApi
from tests.utils.city_list import CityList
from framework.constants.status import Status
import allure


class TestWeatherApi(object):
    def test_xml(self):
        api = WeatherApi()

        city_list = CityList()
        city_list.read_file()
        city = city_list.get_random_city()
        lon, lat = city_list.get_city_coord(city)

        weather = api.get_xml_by_coord(lat, lon)
        code = api.get_status()

        assert code == Status.OK, 'Ответ получен с кодом {}'.format(code)

        assert api.is_xml(), 'Данные получены не в формате xml'

        assert weather.is_lat_lon_correct(lat, lon), 'Полученные координаты: {}, ожидаемые: {}'.format(
            weather.get_coords(), [lat, lon])

        assert weather.is_rus_leng, 'Данные получены не на русском языке'
