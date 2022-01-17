from lxml import etree


class XML():

    @staticmethod
    def get_tree(resp_xml_content):
        s = etree.XML(resp_xml_content)
        return s
