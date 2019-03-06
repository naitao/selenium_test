from selenium import webdriver
import unittest
from values import strings
class TestQABoy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(strings.base_url)


    def test_home_screen_components(self):
        pass

    def tearDown(self):
        self.driver.instance.quit()

if __name__ == '__main__':
    unittest.main()

def test_home_screen_components(self):
    home_screen = HomeScreen(self.driver)
    home_screen.validate_title_is_present()
    home_screen.validate_icon_is_present()
    home_screen.validate_menu_options_are_present()
    home_screen.validate_posts_are_visible()
    home_screen.validate_social_media_links()
