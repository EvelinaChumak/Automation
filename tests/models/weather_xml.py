from lxml import etree


class Weather_XML():

    def __init__(self, root: etree.Element):
        all_child = root.iterdescendants()
        for child in all_child:
            for key in child.keys():
                setattr(self, '{}_{}'.format(child.tag, key), child.get(key))

        print(self.__dict__)

    def get_values(self, *args):
        val = []
        for arg in args:
            if self.__dict__.get(arg) is None:
                raise 'Unknown argument {}'.format(arg)
            else:
                val.append(self.__dict__.get(arg))
        if len(val) == 1:
            return val[0]
        return val
