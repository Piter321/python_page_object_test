import sys

sys.path.append(sys.path[0] + "/...")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

import unittest
from time import sleep
from MyWebDriver import WebDriverSetup
from page import Home


class Google_Search(WebDriverSetup):
    def test_GoogleSearch(self):
        driver = self.driver
        self.driver.get("https://www.google.com/")
        self.driver.set_page_load_timeout(30)

        # Create an instance of the class so that you we can make use of the methods
        # in the class
        home = Home(driver)
        home.search_text.send_keys("LambdaTest")
        sleep(5)
        home.search_text.submit()
        sleep(10)


if __name__ == '__main__':
    unittest.main()