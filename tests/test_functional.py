from tests.config.info_for_api import InfoForProject
from tests.utils.weather_api import WeatherApi
from framework.constants.status import Status
import allure
import pytest


class TestWeatherApi():

    def test_xml(self, read_city_info):
        api = WeatherApi()

        pytest.city_list.get_random_city()
        lon, lat = pytest.city_list.get_city_coord()

        weather = api.get_xml_by_coord(lat, lon)
        code = api.get_status()

        assert code == Status.OK, 'Ответ получен с кодом {}'.format(code)

        assert api.is_xml(), 'Данные получены не в формате xml'

        assert weather.is_lat_lon_correct(lat, lon), 'Полученные координаты: {}, ожидаемые: {}'.format(
            weather.get_coords(), [lat, lon])

        assert weather.is_rus_leng, 'Данные получены не на русском языке'

    def test_temp(self):
        api = WeatherApi()

        pytest.city_list.get_random_city()
        id = pytest.city_list.get_city_id()

        weather = api.get_json_by_id(id)

        code = api.get_status()

        assert code == Status.OK, 'Ответ получен с кодом {}'.format(code)

        assert weather.is_temp_cels(), 'Температура не в градусах Цельсия'

    def test_fullness(self):
        api = WeatherApi()

        pytest.city_list.get_random_city()
        name = pytest.city_list.get_city_name()
        state = pytest.city_list.get_city_state()
        country = pytest.city_list.get_city_coord()

        weather = api.get_json_by_name(name, state, country)

        code = api.get_status()

        assert code == Status.OK, 'Ответ получен с кодом {}'.format(code)

        assert weather.is_args_correct(), 'Параметров {} нет среди полуенных {}'.format(
            InfoForProject.FIELDS, weather.get_main_args())
