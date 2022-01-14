from framework.utils.api import API
from framework.constants.methods import Methods
from tests.utils.create_url import CreateUrl
from tests.utils.xml import XML
from tests.config.info_for_api import InfoForProject
from tests.models.weather_xml import WeatherXML
from tests.models.weather_json import WeatherJSON


class WeatherApi():

    def get_xml_by_coord(self, lat, lon):
        params = {
            'lat': lat,
            'lon': lon,
            'mode': InfoForProject.MODE_XML,
        }
        url = CreateUrl.get_url(params=params)
        self.responce = API(method=Methods.GET, url=url)
        answ = XML.get_tree(self.responce.get_content())
        weather_xml = WeatherXML(answ)
        return weather_xml

    def is_xml(self):
        return self.responce.is_xml()

    def get_status(self):
        return self.responce.get_status()

    def get_json_by_id(self, id):
        params = {
            'id': id
        }
        url = CreateUrl.get_url(params=params)
        self.responce = API(method=Methods.GET, url=url)
        weather_json = WeatherJSON(self.responce.get_json())
        return weather_json

    def get_json_by_name(self, name, state='', country=''):
        params = {
            'q': '{},{},{}'.format(name, state, country)
        }
        url = CreateUrl.get_url(params=params)
        self.responce = API(method=Methods.GET, url=url)
        weather_json = WeatherJSON(self.responce.get_json())
        return weather_json
