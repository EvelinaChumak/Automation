# coding=utf-8
from framework.elements.base.base_element import BaseElement
from selenium.webdriver.common.by import By

class Label(BaseElement):

    def __init__(self, locator, name, search_condition=By.XPATH):
        super(Label, self).__init__(search_condition_of=search_condition, loc=locator, name_of=name)

    def __getitem__(self, key):
        new_element = super(Label, self).__getitem__(key=key)
        return Label(new_element.get_search_condition(), new_element.get_locator(), new_element.get_name())

    def __call__(self, sublocator, new_name_of=None):
        new_element = super(Label, self).__call__(sublocator=sublocator, new_name_of=new_name_of)
        return Label(new_element.get_search_condition(), new_element.get_locator(), new_element.get_name())

    def get_element_type(self):
        return "Label"
