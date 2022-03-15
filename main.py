import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller


# Monday -> Sunday
HOURS = [8, 8, 8, 8, 8, 0, 0]
USERNAME = "test"
PASSWORD = "test"


def main():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get(Urls.login)
    assert "PayHero" in driver.title

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    sign_in_button = driver.find_element(By.TAG_NAME, "button")

    username_input.clear()
    username_input.send_keys(USERNAME)
    password_input.clear()
    password_input.send_keys(PASSWORD)
    sign_in_button.click()

    driver.close()


class Urls:
    login = "https://login.payhero.app/"


if __name__ == "__main__":
    main()
