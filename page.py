from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(object):
    """Base class to initialize other pages"""

    def __init__(self, driver: WebDriver):
        self.driver = driver


class Urls:
    """Contains all the needed URLs for PayHero"""

    login = "https://login.payhero.app/"
    timesheet = "https://portal.payhero.app/#!/time/employee"


class SignInPage(BasePage):
    """The initial sign-in page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = self.driver.find_element(By.ID, "username")
        self.password_input = self.driver.find_element(By.ID, "password")
        self.sign_in_button = self.driver.find_element(By.TAG_NAME, "button")

    def sign_in(self, username: str, password: str) -> None:
        """Signs in to the application"""

        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.sign_in_button.click()


class TimesheetPage(BasePage):
    """The weekly calendar UI showing the current week's hours"""

    def __init__(self, driver):
        super().__init__(driver)
        self.daily_inputs = self.driver.find_elements(
            By.XPATH, "//input[contains(@class,'form-control table-taskRowDay')]"
        )

    def set_hours_for_week(self, hours_in_week: dict[str:int]) -> None:
        """Sets each daily hours, Monday to Sunday, to the corresponding hours"""

        assert len(hours_in_week) == 7

        for day_input, daily_hours in zip(self.daily_inputs, hours_in_week.values()):
            day_input.click()
            day_input.send_keys(daily_hours, Keys.ENTER)
