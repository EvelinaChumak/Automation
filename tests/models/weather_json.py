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

    def is_args_correct(self):
        keys_list = []
        for key in self.__dict__.keys():
            keys_list.append(key.split('_')[0])
        for val in InfoForProject.FIELDS:
            if val not in set(keys_list):
                return False
        return True

    def get_main_args(self):
        keys_list = []
        for key in self.__dict__.keys():
            keys_list.append(key.split('_')[0])
        return set(keys_list)
