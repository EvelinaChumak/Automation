from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.text_box import TextBox
from framework.elements.label import Label
from framework.elements.button import Button
from selenium.webdriver.common.keys import Keys
from framework.browser.browser import Browser
from framework.utils.random import Random
# from


class StartGame(BasePage):
    search_condition = By.XPATH

    lbl_random_rival_loc = "//*[@class='battlefield-start-choose_rival-variant-link']"
    lbl_random_rival = Label(search_condition=search_condition, locator=lbl_random_rival_loc,
                      name="Random rival")
    
    lbl_random_location_loc = "//*[@class='placeships-variant placeships-variant__randomly']/span"
    lbl_random_location = Label(search_condition=search_condition, locator=lbl_random_location_loc,
                      name="Random location")
    
    lbl_start_loc = "//*[@class='battlefield-start-button']"
    lbl_start = Label(search_condition=search_condition, locator=lbl_start_loc,
                      name="Start game")

    def __init__(self):
        super().__init__(search_condition=StartGame.search_condition, locator=StartGame.lbl_random_rival_loc,
                         page_name=self.__class__.__name__)
        super().wait_for_page_opened()

        self.lbl_random_rival = Label(search_condition=StartGame.search_condition, locator=StartGame.lbl_random_rival_loc,
                               name="Random rival")

    def choose_random_rival(self):
        self.lbl_random_rival.click()
        
    def choose_random_location(self):
        num = Random.get_number_1_to_15()
        for i in range (0, num):
            self.lbl_random_location.click()
    
    def start_game(self):
        self.lbl_start.click()
