from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.label import Label
from framework.utils.random import Random


class StartGame(BasePage):
    
    lbl_random_rival_loc = "//*[@class='battlefield-start-choose_rival-variant-link']"
    
    lbl_random_location_loc = "//*[@class='placeships-variant placeships-variant__randomly']/span"
    
    lbl_start_loc = "//*[@class='battlefield-start-button']"

    def __init__(self):
        super().__init__(locator=StartGame.lbl_random_rival_loc,
                         page_name=self.__class__.__name__)

        self.lbl_random_rival = Label(locator=StartGame.lbl_random_rival_loc,
                               name="Random rival")
        self.lbl_random_rival = Label( locator=self.lbl_random_rival_loc,
                      name="Random rival")
        self.lbl_random_location = Label(locator=self.lbl_random_location_loc,
                      name="Random location")
        self.lbl_start = Label(locator=self.lbl_start_loc,
                      name="Start game")

    def choose_random_rival(self):
        self.lbl_random_rival.click()
        
    def choose_random_location(self):
        num = Random.get_number_1_to_15()
        for i in range (0, num):
            self.lbl_random_location.click()
    
    def start_game(self):
        self.lbl_start.click()
