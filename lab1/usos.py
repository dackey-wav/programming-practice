import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
    def tearDown(self):
        self.driver.close()

class InputTesting(TestCase):
    BLOG_URL = "https://login.pwr.edu.pl/auth/realms/pwr.edu.pl/protocol/cas/login?service=https%3A%2F%2Fweb.usos.pwr.edu.pl%2Fkontroler.php%3F_action%3Dlogowaniecas%2Findex%26callback%3DK7YyNrVS0s%252FOzyspys9JLdIryCiwj09MLsnMz7PNSy0v1k9JTUsszSlRsgYA6db54092aec98dbd244d8c33ddbd92b3086404df&locale=pl"
    INPUT_NAME = "username"
    CLEAR_BUTTON_ID = "clearForm"

    def setUp(self):
        self.driver = webdriver.Edge()

    def test_clear_button(self):
        self.driver.get(self.BLOG_URL)
        
        try:
            login_box = self.driver.find_element(by=By.NAME, value=self.INPUT_NAME)
            clear_button = self.driver.find_element(by=By.ID, value=self.CLEAR_BUTTON_ID)
            
            login_box.send_keys("test_student")
            self.assertEqual("test_student", login_box.get_attribute("value"))
            
            clear_button.click()
            
            self.assertEqual("", login_box.get_attribute("value"))
            
        except Exception:
            self.fail("element not found")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()