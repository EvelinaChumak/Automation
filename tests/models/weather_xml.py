from lxml import etree
import string


class WeatherXML():

    def __init__(self, root: etree.Element):
        all_child = root.iterdescendants()
        for child in all_child:
            for key in child.keys():
                setattr(self, '{}_{}'.format(child.tag, key), child.get(key))

    def get_values(self, *args):
        val = []
        for arg in args:
            if self.__dict__.get(arg) is None:
                raise 'Unknown argument {}'.format(arg)
            else:
                val.append(self.__dict__.get(arg))
        return val[0] if len(val) == 1 else val

    def is_rus_leng(self):
        val = self.get_values('weather_value')
        for c in val:
            if c not in string.ascii_letters:
                return False
        return True

    def is_lat_lon_correct(self, lat, lon):
        """
        Maybe api has bug in coords, therefore use round()
        """
        val = self.get_values('coord_lat', 'coord_lon')
        val_lat = round(float(val[0]), 4)
        val_lon = round(float(val[1]), 4)
        return val_lat == round(lat, 4) and val_lon == round(lon, 4)

    def get_coords(self):
        return self.get_values('coord_lat', 'coord_lon')
