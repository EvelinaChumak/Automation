import json
from tests.config.info_for_api import InfoForProject
from random import randint


class CityList():

    __file = None

    def read_file(self):
        with open(InfoForProject.JSON_NAME, encoding='utf-8', mode='r') as f:
            self.__file = json.loads(f.read())

    def get_random_city(self):
        city = self.__file[randint(0, len(self.__file))]
        return city

    def get_city_id(self, city: dict):
        return city.get('id')

    def get_city_name(self, city: dict):
        return city.get('name')

    def get_city_coord(self, city: dict):
        """
        Returns:
            lon, let
        """
        return city.get('coord').get('lon'), city.get('coord').get('lat')
