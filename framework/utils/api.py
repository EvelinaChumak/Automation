import requests
from framework.utils.logger import Logger
from framework.constants.methods import Methods

class API():

    def __init__(self, method: Methods, url, data=None):
        self.send_request(method, url, data)
    
    def send_request(self, method: Methods, url, data=None):
        Logger.info('Отправляю запрос "' + method.value + '" на ' + url)
        self.__url = url
        self.__data = data
        if method == Methods.GET:
            self.__response = requests.get(url=self.__url, data=self.__data)
        if method == Methods.POST:
            self.__response = requests.post(url=self.__url, data=self.__data)
        if method == Methods.PUT:
           self.__response = requests.put(url=self.__url, data=self.__data)
        if method == Methods.DELETE:
            self.__response = requests.put(url=self.__url, data=self.__data)
        if method == Methods.HEAD:
            self.__response = requests.head(url=self.__url, data=self.__data)
        if method == Methods.OPTIONS:
            self.__response = requests.options(url=self.__url, data=self.__data)

    def get_status(self):
        Logger.info('Получаю статус запроса')
        return self.__response.status_code

    def is_json(self):
        Logger.info('Проверка, являются ли полученные данные json')
        res = self.get_headers().get('content-type')
        return 'application/json' in res

    def get_json(self):
        Logger.info('Получаю данные в формате json')
        return self.__response.json()
    
    def get_headers(self):
        Logger.info('Получение заголовков')
        return self.__response.headers       
    