import json

from tests.config.info_for_api import InfoForProject


class WeatherJSON():

    def __init__(self, info):
        for key, val in info.items():
            if type(val) is dict:
                for v_key, v_val in val.items():
                    setattr(self, '{}_{}'.format(key, v_key), v_val)
            elif type(val) is list:
                for v in val:
                    for v_key, v_val in v.items():
                        setattr(self, '{}_{}'.format(key, v_key), v_val)
            else:
                setattr(self, '{}'.format(key), val)

    def is_temp_cels(self):
        temp = self.__dict__.get('main_temp')
        return temp > InfoForProject.TEMP_MIN and temp < InfoForProject.TEMP_MAX
