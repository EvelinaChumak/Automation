from framework.pages.base_page import BasePage
from framework.elements.label import Label


class InfoForm(BasePage):

    MESS_RIVAL_LEAVE = "Противник вышел из игры"
    MESS_SERVER_ERROR = "Ошибка сервера"
    MESS_SOME_ERROR = "Неизвестная ошибка"
    MESS_YOU_LOSE = "Вы проиграли"

    lbl_place_ships_loc = "//*[@class='notification notification__init']"
    lbl_start_game_loc = "//*[@class='notification notification__game-started-move-on']"
    lbl_start_rival_loc = (
        "//*[@class='notification notification__game-started-move-off']"
    )
    lbl_wait_rival_loc = "//*[@class='notification notification__waiting-for-rival']"
    lbl_move_loc = "//*[@class='notification notification__move-on']"
    lbl_rival_move_loc = "//*[@class='notification notification__move-off']"
    lbl_rival_leave_loc = "//*[@class='notification notification__rival-leave']"
    lbl_you_win_loc = "//*[@class='notification notification__game-over-win']"
    lbl_you_lose_loc = "//*[@class='notification notification__game-over-lose']"
    lbl_server_error_loc = "//*[@class='notification notification__server-error']"
    lbl_some_error_loc = "//*[@class='notification notification__game-error']"

    def __init__(self):
        super().__init__(
            locator=InfoForm.lbl_place_ships_loc, page_name=self.__class__.__name__
        )

        self.lbl_place_ships = Label(
            locator=self.lbl_place_ships_loc, name="Place your ships"
        )

        self.lbl_start_game = Label(
            locator=self.lbl_start_game_loc, name="You start game"
        )
        self.lbl_wait_rival = Label(locator=self.lbl_wait_rival_loc, name="Wait rival")
        self.lbl_start_rival = Label(
            locator=self.lbl_start_rival_loc, name="Rival start game"
        )
        self.lbl_move = Label(locator=self.lbl_move_loc, name="You move")
        self.lbl_rival_move = Label(locator=self.lbl_rival_move_loc, name="Rival move")
        self.lbl_rival_leave = Label(
            locator=self.lbl_rival_leave_loc, name="Rival leave"
        )
        self.lbl_you_win = Label(locator=self.lbl_you_win_loc, name="You win")
        self.lbl_you_lose = Label(locator=self.lbl_you_lose_loc, name="You lose")
        self.lbl_server_error = Label(
            locator=self.lbl_server_error_loc, name="Server error"
        )
        self.lbl_some_error = Label(locator=self.lbl_some_error_loc, name="Some error")

    def wait_my_move(self):
        if (
            self.lbl_start_rival.is_displayed()
            or self.lbl_rival_move.is_displayed()
            or self.lbl_wait_rival.is_displayed()
        ):
            self.lbl_move.wait_for_visibility()

    def is_game_continue(self):
        return not (
            self.lbl_rival_leave.is_displayed()
            or self.lbl_server_error.is_displayed()
            or self.lbl_some_error.is_displayed()
            or self.lbl_you_lose.is_displayed()
            or self.lbl_you_win.is_displayed()
        )

    def why_end(self):
        win = False
        mess = ""
        if self.lbl_you_win.is_displayed():
            win = True
        elif self.lbl_rival_leave.is_displayed():
            mess = self.MESS_RIVAL_LEAVE
        elif self.lbl_server_error.is_displayed():
            mess = self.MESS_SERVER_ERROR
        elif self.lbl_some_error.is_displayed():
            mess = self.MESS_SOME_ERROR
        elif self.lbl_you_lose.is_displayed():
            mess = self.MESS_YOU_LOSE
        return win, mess
