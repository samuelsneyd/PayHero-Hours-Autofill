import unittest
import chromedriver_autoinstaller
from selenium import webdriver
from page import SignInPage, Urls, TimesheetPage
from decouple import config

# Pulls username and password from .env
USERNAME = config("APP_USERNAME")
PASSWORD = config("APP_PASSWORD")

HOURS = {
    "Mon": 8,
    "Tue": 8,
    "Wed": 8,
    "Thu": 8,
    "Fri": 8,
    "Sat": 0,
    "Sun": 0,
}


class PayHero(unittest.TestCase):
    """A small script to automatically log PayHero hours"""

    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_set_hours(self):
        """Logs into PayHero and sets the hours for the current week"""
        self.driver.get(Urls.login)
        self.assertIn("PayHero", self.driver.title)

        sign_in_page = SignInPage(self.driver)
        sign_in_page.sign_in(USERNAME, PASSWORD)

        timesheet = TimesheetPage(self.driver)
        timesheet.set_hours_for_week(HOURS)

        print("Hours set successfully!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
