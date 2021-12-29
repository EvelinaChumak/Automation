from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.text_box import TextBox
from framework.elements.label import Label
from framework.elements.button import Button
from selenium.webdriver.common.keys import Keys
from framework.browser.browser import Browser
from framework.utils.random import Random
from time import sleep
# from


class Play(BasePage):
    search_condition = By.XPATH

    lbl_wait_rival_loc = "//*[@class='notification notification__waiting-for-rival']"
    lbl_wait_rival = Label(search_condition=search_condition, locator=lbl_wait_rival_loc,
                      name="Wait rival")
    
    lbl_chat_loc = "//*[@class='chat-gap']"
    lbl_chat = Label(search_condition=search_condition, locator=lbl_chat_loc,
                      name="Chat")
    
    lbl_start_game_loc = "//*[@class='notification notification__game-started-move-on']"
    lbl_start_game = Label(search_condition=search_condition, locator=lbl_start_game_loc,
                      name="You start game")
    
    lbl_start_rival_loc = "//*[@class='notification notification__game-started-move-off']"
    lbl_start_rival = Label(search_condition=search_condition, locator=lbl_start_rival_loc,
                      name="Rival start game")

    lbl_move_loc = "//*[@class='notification notification__move-on']"
    lbl_move = Label(search_condition=search_condition, locator=lbl_move_loc,
                      name="You move")
    
    lbl_rival_move_loc = "//*[@class='notification notification__move-off']"
    lbl_rival_move = Label(search_condition=search_condition, locator=lbl_rival_move_loc,
                      name="Rival move")
    
    lbl_rival_leave_loc = "//*[@class='notification notification__rival-leave']"
    lbl_rival_leave = Label(search_condition=search_condition, locator=lbl_rival_leave_loc,
                      name="Rival leave")
    
    lbl_you_win_loc = "//*[@class='notification notification__game-over-win']"
    lbl_you_win = Label(search_condition=search_condition, locator=lbl_you_win_loc,
                      name="You win")
    
    lbl_you_lose_loc = "//*[@class='notification notification__game-over-lose']"
    lbl_you_lose = Label(search_condition=search_condition, locator=lbl_you_lose_loc,
                      name="You lose")
    
    lbl_server_error_loc = "//*[@class='notification notification__server-error']"
    lbl_server_error = Label(search_condition=search_condition, locator=lbl_server_error_loc,
                      name="Server error")
    
    lbl_some_error_loc = "//*[@class='notification notification__game-error']"
    lbl_some_error = Label(search_condition=search_condition, locator=lbl_some_error_loc,
                      name="Some error")
    
    lbl_cell_loc = "//*[@class= 'battlefield battlefield__rival']//tbody/tr[{}]/td[{}]"
    lbl_cell = Label(search_condition=search_condition, locator=lbl_cell_loc,
                      name="Cell")
    
    style_miss_auto = "battlefield-cell__miss__auto"
    style_miss = "battlefield-cell__miss"
    style_done = "battlefield-cell__done"
    
    def __init__(self):
        super().__init__(search_condition=Play.search_condition, locator=Play.lbl_chat_loc,
                         page_name=self.__class__.__name__)
        super().wait_for_page_opened()

        self.lbl_chat = Label(search_condition=Play.search_condition, locator=Play.lbl_chat_loc,
                               name="Chat")

    def wait_my_move(self):
        if (self.lbl_start_rival.is_displayed() or  \
            self.lbl_rival_move.is_displayed() or self.lbl_wait_rival.is_displayed()):
            self.lbl_move.wait_for_visibility()
        return True
            