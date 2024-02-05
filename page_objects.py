from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IMDbSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "navbar-query")
        self.search_button = (By.ID, "navbar-submit-button")

    def search_for_name(self, name):
        try:
            search_box = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.search_box)
            )
            search_box.clear()
            search_box.send_keys("Tom Hanks")

            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.search_button)
            )
            search_button.click()
        except Exception as e:
            print(f"Exception occurred: {e}")

