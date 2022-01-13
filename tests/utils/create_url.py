from tests.config.urls import Urls


class CreateUrl():

    @staticmethod
    def get_url(params: dict):
        url = Urls.API_URL
        for key, val in params.items():
            url = url + key + '=' + str(val) + '&'
        url = url + 'appid=' + Urls.API_KEY
        return url
