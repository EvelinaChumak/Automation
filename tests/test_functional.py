from framework.browser.browser import Browser
from tests.pages.start_game import StartGame
from tests.config.urls import Urls

class TestFunctional(object):
    def test_framework(self, create_browser):
        Browser.get_browser().set_url(Urls.TEST_STAND_URL)
        game = StartGame()
        game.choose_random_rival()
        game.choose_random_location()
        game.start_game()
