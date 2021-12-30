from framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.elements.text_box import TextBox
from framework.elements.label import Label
from framework.elements.button import Button
from selenium.webdriver.common.keys import Keys
from framework.browser.browser import Browser
from framework.utils.logger import Logger
from framework.utils.random import Random
from time import sleep
from tests.config.sequence_of_moves import ROW, COLUMN
# from


class Play(BasePage):
    search_condition = By.XPATH
    

    _for_hit = 4

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
    style_hit = "battlefield-cell__hit"
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
    
    def is_game_continue(self):
        if (self.lbl_rival_leave.is_displayed() or self.lbl_server_error.is_displayed() or \
            self.lbl_some_error.is_displayed() or self.lbl_you_lose.is_displayed() or \
            self.lbl_you_win.is_displayed()):
            return False
        else: 
            return True
    
    def _create_cell(self, row, collummn):
        lbl_cell_loc = "//*[@class= 'battlefield battlefield__rival']//tbody/tr[{}]/td[{}]".format(row,collummn)
        for key, value in ROW.items():
            if value == row:
                row = key
        for key, value in COLUMN.items():
            if value == collummn:
                collummn = key
        lbl_cell = Label(search_condition=self.search_condition, locator=lbl_cell_loc,
                      name="Cell: {} {}".format(row, collummn))
        Logger.info("Cell: {} {}".format(row, collummn))
        return lbl_cell
    
    def my_move(self, move_list: list):
        i = ROW[move_list[0][0]]
        j = COLUMN[move_list[0][1]]
        

        lbl_cell = self._create_cell(i,j)
        
        if (self.style_miss in lbl_cell.get_attribute_class() or \
            self.style_hit in lbl_cell.get_attribute_class()):
            Logger.info('мисклик или хит: удаляю')
            move_list.pop(0)

        else:
            lbl_cell.click()
            Logger.info('кликаю и удаляю {}'.format(move_list[0]))
            move_list.pop(0)
            
            while self.style_hit in lbl_cell.get_attribute_class():
                rand = Random.get_number_1_to_4()
                Logger.info('поврежден {}'.format(lbl_cell))
                if rand == 1 and i != 1: # top row = 1
                    i = i - 1
                    lbl_cell= self._create_cell(i,j)
                    if (self.style_miss in lbl_cell.get_attribute_class() or \
                        self.style_hit in lbl_cell.get_attribute_class()):
                        i = i + 1
                    else: 
                        lbl_cell.click()
                        
                elif rand == 2 and i != 10: # bottom row = 10
                    i = i + 1
                    lbl_cell = self._create_cell(i,j)
                    if (self.style_miss in lbl_cell.get_attribute_class() or \
                        self.style_hit in lbl_cell.get_attribute_class()):
                        i = i - 1
                    else: 
                        lbl_cell.click()
                
                elif rand == 3 and j != 1: # left collumn = 1
                    j = j - 1
                    lbl_cell = self._create_cell(i,j)
                    if (self.style_miss in lbl_cell.get_attribute_class() or \
                        self.style_hit in lbl_cell.get_attribute_class()):
                        j = j + 1
                    else: 
                        lbl_cell.click()
                
                elif rand == 4 and j != 10: # right collumn = 1
                    j = j + 1
                    lbl_cell = self._create_cell(i,j)
                    if (self.style_miss in lbl_cell.get_attribute_class() or \
                        self.style_hit in lbl_cell.get_attribute_class()):
                        j = j - 1
                    else: 
                        lbl_cell.click()

                    
        return move_list
            