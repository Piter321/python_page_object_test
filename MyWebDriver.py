from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import urllib3
import unittest


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        if (self.driver != None):
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()