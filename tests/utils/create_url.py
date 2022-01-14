from tests.config.info_for_api import InfoForProject
from tests.config.urls import Urls


class CreateUrl():

    @staticmethod
    def get_url(params: dict):
        url = Urls.API_URL
        for key, val in params.items():
            url = url + key + '=' + str(val) + '&'
        url = url + 'lang=' + InfoForProject.LANG + '&units=' + InfoForProject.TEMPERATURE
        url = url + '&appid=' + Urls.API_KEY
        return url
