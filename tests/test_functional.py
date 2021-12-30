from selenium.common.exceptions import TimeoutException
from framework.browser.browser import Browser
from tests.pages.play import Play
from tests.pages.start_game import StartGame
from tests.config.urls import Urls
from tests.config.sequence_of_moves import SEQUENCE_OF_MOVES
from time import sleep

class TestFunctional(object):
    def test_framework(self, create_browser):
        Browser.get_browser().set_url(Urls.TEST_STAND_URL)
        game = StartGame()
        game.choose_random_rival()
        game.choose_random_location()
        game.start_game()

        play = Play()
        
        move_list = list(SEQUENCE_OF_MOVES)
        
        while play.is_game_continue():
            try:
                play.wait_my_move()
            except TimeoutException:
                break
            move_list = play.my_move(move_list)
            sleep(1)
            
        assert False