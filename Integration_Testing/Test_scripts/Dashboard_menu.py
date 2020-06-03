import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube


class Dash_menu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()

    def test_menu(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        head = self.driver.find_element_by_xpath(Data.dash_name).text
        self.assertEqual("cQube - Dashboard",head,"Not matching words in Page")
    def tearDown(self):
            time.sleep(5)
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()