from framework.pages.base_page import BasePage
from framework.elements.label import Label
from framework.utils.random import Random
from tests.config.sequence_of_moves import ROW, COLUMN
# from


class Play(BasePage):

    _for_hit = 4
    hit_cell = None
    _row = 0
    _col = 0

    lbl_wait_rival_loc = "//*[@class='notification notification__waiting-for-rival']" 
    lbl_chat_loc = "//*[@class='chat-gap']"
    lbl_start_game_loc = "//*[@class='notification notification__game-started-move-on']"
    lbl_start_rival_loc = "//*[@class='notification notification__game-started-move-off']"
    lbl_move_loc = "//*[@class='notification notification__move-on']"
    lbl_rival_move_loc = "//*[@class='notification notification__move-off']" 
    
    lbl_rival_leave_loc = "//*[@class='notification notification__rival-leave']" 
    lbl_you_win_loc = "//*[@class='notification notification__game-over-win']"
    lbl_you_lose_loc = "//*[@class='notification notification__game-over-lose']"
    lbl_server_error_loc = "//*[@class='notification notification__server-error']"
    lbl_some_error_loc = "//*[@class='notification notification__game-error']"
    
    lbl_cell_loc = "//*[@class= 'battlefield battlefield__rival']//tbody/tr[{}]/td[{}]"
    lbl_cell = Label(locator=lbl_cell_loc,
                      name="Cell")
    
    style_miss_auto = "battlefield-cell__miss__auto"
    style_miss = "battlefield-cell__miss"
    style_hit = "battlefield-cell__hit"
    style_done = "battlefield-cell__done"
    
    def __init__(self):
        super().__init__(locator=Play.lbl_chat_loc,
                         page_name=self.__class__.__name__)
        
        self.lbl_wait_rival = Label(locator=self.lbl_wait_rival_loc,
                      name="Wait rival")

        self.lbl_chat = Label(locator=Play.lbl_chat_loc,
                               name="Chat")
        self.lbl_chat = Label(locator=self.lbl_chat_loc,
                      name="Chat")
        self.lbl_start_game = Label(locator=self.lbl_start_game_loc,
                      name="You start game")
        self.lbl_start_rival = Label(locator=self.lbl_start_rival_loc,
                      name="Rival start game")
        self.lbl_move = Label(locator=self.lbl_move_loc,
                      name="You move")
        self.lbl_rival_move = Label(locator=self.lbl_rival_move_loc,
                      name="Rival move")
        self.lbl_rival_leave = Label(locator=self.lbl_rival_leave_loc,
                      name="Rival leave")
        self.lbl_you_win = Label(locator=self.lbl_you_win_loc,
                      name="You win")
        self.lbl_you_lose = Label(locator=self.lbl_you_lose_loc,
                      name="You lose")
        self.lbl_server_error = Label(locator=self.lbl_server_error_loc,
                      name="Server error")
        self.lbl_some_error = Label(locator=self.lbl_some_error_loc,
                      name="Some error")

    def wait_my_move(self):
        if (self.lbl_start_rival.is_displayed() or  \
            self.lbl_rival_move.is_displayed() or self.lbl_wait_rival.is_displayed()):
            self.lbl_move.wait_for_visibility()
    
    def is_game_continue(self):
        return not (self.lbl_rival_leave.is_displayed() or self.lbl_server_error.is_displayed() or \
            self.lbl_some_error.is_displayed() or self.lbl_you_lose.is_displayed() or \
            self.lbl_you_win.is_displayed())
        
    def why_end(self):
        win = False
        mess = ''     
        if self.lbl_you_win.is_displayed(): 
            win = True
        if self.lbl_rival_leave.is_displayed():
            mess = 'Противник вышел из игры'
        if self.lbl_server_error.is_displayed():
            mess = 'Ошибка сервера'
        if self.lbl_some_error.is_displayed():
            mess = 'Неизвестная ошибка'
        if self.lbl_you_lose.is_displayed():
            mess = 'Вы проиграли'
        return win, mess
    
    def _create_cell(self, row, collummn):
        lbl_cell_loc = "//*[@class= 'battlefield battlefield__rival']//tbody/tr[{}]/td[{}]".format(row,collummn)
        for key, value in ROW.items():
            if value == row:
                row = key
        for key, value in COLUMN.items():
            if value == collummn:
                collummn = key
        lbl_cell = Label(locator=lbl_cell_loc,
                      name="Cell: {} {}".format(row, collummn))
        return lbl_cell
    
    def my_move(self, move_list: list):
        
        if self.hit_cell == None: 
            
            i = ROW[move_list[0][0]]
            j = COLUMN[move_list[0][1]]
            
            lbl_cell = self._create_cell(i,j)
            
            if (self.style_miss in lbl_cell.get_attribute_class() or \
                self.style_hit in lbl_cell.get_attribute_class()):
                move_list.pop(0)

            else:
                lbl_cell.click()
                move_list.pop(0)
                
                if self.style_hit in lbl_cell.get_attribute_class():
                    self.hit_cell = lbl_cell
                    self._for_hit = 4
                    self._row = i
                    self._col = j
        
        else:
            
            while self.style_hit in self.hit_cell.get_attribute_class():
                lbl_cell = self.hit_cell
                i = self._row
                j = self._col            
                rand = Random.get_number_1_to_4()
                if rand == 1 and i != 1: # top row = 1
                    i = i - 1
                    self._for_hit = self._for_hit - 1
                    lbl_cell = self._create_cell(i,j)
                    if (self.style_miss in lbl_cell.get_attribute_class() or \
                        self.style_hit in lbl_cell.get_attribute_class()):
                        i = i + 1
                    else: 
                        lbl_cell.click()
                        
                elif rand == 2 and i != 10: # bottom row = 10
                    i = i + 1
                    lbl_cell = self._create_cell(i,j)
                    self._for_hit = self._for_hit - 1
                    if (self.style_miss in lbl_cell.get_attribute_class() or \
                        self.style_hit in lbl_cell.get_attribute_class()):
                        i = i - 1
                    else: 
                        lbl_cell.click()
                
                elif rand == 3 and j != 1: # left collumn = 1
                    j = j - 1
                    lbl_cell = self._create_cell(i,j)
                    self._for_hit = self._for_hit - 1
                    if (self.style_miss in lbl_cell.get_attribute_class() or \
                        self.style_hit in lbl_cell.get_attribute_class()):
                        j = j + 1
                    else: 
                        lbl_cell.click()
                
                elif rand == 4 and j != 10: # right collumn = 1
                    j = j + 1
                    lbl_cell = self._create_cell(i,j)
                    self._for_hit = self._for_hit - 1
                    if (self.style_miss in lbl_cell.get_attribute_class() or \
                        self.style_hit in lbl_cell.get_attribute_class()):
                        j = j - 1
                    else: 
                        lbl_cell.click()                     
                if self.style_hit in lbl_cell.get_attribute_class() and \
                    self.style_done not in lbl_cell.get_attribute_class() and \
                    self._for_hit != 0:
                    self.hit_cell = lbl_cell
                    self._for_hit = 4
                    self._col = j
                    self._row = i
                elif self._for_hit == 0 or \
                    self.style_done in lbl_cell.get_attribute_class():
                    self.hit_cell = None
                    break
                    
        return move_list
