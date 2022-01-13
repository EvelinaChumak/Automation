from framework.utils.api import API
from framework.constants.methods import Methods
from framework.utils.logger import Logger
from tests.utils.create_url import CreateUrl
from tests.utils.xml import XML
from tests.config.info_for_api import InfoForProject
from tests.models.weather_xml import Weather_XML
import string


class WeatherApi():

    def get_xml_by_coord(self, lat, lon):
        params = {
            'lat': lat,
            'lon': lon,
            'mode': 'xml',
            'lang': InfoForProject.LANG
        }
        url = CreateUrl.get_url(params=params)
        self.responce = API(method=Methods.GET, url=url)
        answ = XML.get_tree(self.responce.get_content())
        weather_xml = Weather_XML(answ)
        return weather_xml

    def is_xml(self):
        return self.responce.is_xml()

    def is_rus_leng(self, weather: Weather_XML):
        val = weather.get_values('weather_value')
        for c in val:
            if c not in string.ascii_letters:
                return False
        return True
