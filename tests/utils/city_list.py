import json
from tests.config.info_for_api import InfoForProject
from random import choice


class CityList():
    ID = 'id'
    NAME = 'name'
    STATE = 'state'
    COUNTRY = 'country'
    COORD = 'COORD'

    with open(InfoForProject.JSON_NAME, encoding='utf-8', mode='r') as f:
        __file = json.loads(f.read())

    @staticmethod
    def get_random_city():
        return choice(CityList.__file)

    @staticmethod
    def get_attr(city, attribute):
        """
        Args:
            city ([dict]): city from get_random_city()
            attribute ([str]) or (CityList.attribute): key in city

        Returns:
            [str] or [number]: if choose CityList.COORD return 2 values
        """
        if attribute == CityList.COORD:
            return city.get('coord').get('lon'), city.get('coord').get('lat')
        else:
            return city.get(attribute)
