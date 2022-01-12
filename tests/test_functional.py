from selenium.common.exceptions import TimeoutException
from framework.browser.browser import Browser
from tests.pages.info_form import InfoForm
from tests.pages.play import Play
from tests.pages.start_game import StartGame
from tests.config.urls import Urls
from tests.config.sequence_of_moves import SEQUENCE_OF_MOVES


class TestSeaBattle(object):
    def test_move_alg(self, create_browser):
        Browser.get_browser().set_url(Urls.TEST_STAND_URL)
        game = StartGame()
        game.choose_random_rival()
        game.choose_random_location()
        game.start_game()

        play = Play()
        info = InfoForm()

        while info.is_game_continue():
            try:
                info.wait_my_move()
            except TimeoutException:
                break
            play.my_move()

        win, mess = info.why_end()

        assert win, "{}".format(mess)
