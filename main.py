import time
import unittest
import chromedriver_autoinstaller
from selenium import webdriver
from page import SignInPage, Urls
from decouple import config

# Pulls username and password from .env
USERNAME = config("APP_USERNAME")
PASSWORD = config("APP_PASSWORD")

# Monday -> Sunday
HOURS = [8, 8, 8, 8, 8, 0, 0]


class PayHero(unittest.TestCase):
    """A small script to automatically log PayHero hours"""

    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_log_hours(self):
        """Logs into PayHero and logs hours"""
        self.driver.get(Urls.login)
        self.assertIn("PayHero", self.driver.title)

        sign_in_page = SignInPage(self.driver)
        sign_in_page.sign_in(USERNAME, PASSWORD)

        time.sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
