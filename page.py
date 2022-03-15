from selenium.webdriver.common.by import By


class BasePage(object):
    """Base class to initialize other pages"""

    def __init__(self, driver):
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
