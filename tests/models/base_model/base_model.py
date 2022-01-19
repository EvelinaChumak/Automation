from framework.utils.api import API
from framework.constants.methods import Methods
from framework.utils.logger import Logger
from tests.utils.create_url import CreateUrl


class BaseModel():
    SELF_FIELDS = None
    response = None

    @classmethod
    def get_by_api(cls, info):
        new_info = {}
        for key, value in info.items():
            if isinstance(value, dict):
                new_info[key] = cls.SELF_FIELDS[key].get_by_api(value)
            else:
                new_info[key] = value
        return cls(**new_info)
    
    @classmethod
    def get_by_attr(cls, **info):
        url = CreateUrl.get_url(info)
        cls.response = API(method=Methods.GET, url=url)
        return cls.get_by_api(cls.response.get_json())