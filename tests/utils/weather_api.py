from framework.utils.api import API
from framework.constants.methods import Methods
from framework.utils.logger import Logger
from tests.utils.create_url import CreateUrl
from tests.utils.xml import XML

class WeatherApi():
    
    def get_xml(self):
        params = {
            'q' : 'London',
            'mode' : 'xml',
        }
        url = CreateUrl.get_url(params=params)
        self.responce = API(method=Methods.GET, url=url)
        answ = XML.get_tree(self.responce.get_content())
        return answ