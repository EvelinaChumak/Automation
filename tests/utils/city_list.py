import json
from tests.config.info_for_api import InfoForProject
from random import randint


class CityList():

    __file = None
    __city = None

    def read_file(self):
        with open(InfoForProject.JSON_NAME, encoding='utf-8', mode='r') as f:
            self.__file = json.loads(f.read())

    def get_random_city(self):
        self.__city = self.__file[randint(0, len(self.__file))]
        return self.__city

    def get_city_id(self):
        return self.__city.get('id')

    def get_city_name(self):
        return self.__city.get('name')
    
    def get_city_state(self):
        return self.__city.get('state')
    
    def get_city_country(self):
        return self.__city.get('country')

    def get_city_coord(self):
        """
        Returns:
            lon, let
        """
        return self.__city.get('coord').get('lon'), self.__city.get('coord').get('lat')
