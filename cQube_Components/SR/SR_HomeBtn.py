

import csv
import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class Dist_validation(unittest.TestCase):
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Firefox(executable_path=dri.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver.login_cqube()
        driver.navigate_to_semester_report()

    def test_validate_District(self):
        time.sleep(3)
        self.driver.find_element_by_xpath(Data.SRD12).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(Data.Download).click()
        driver = cqube(self.driver)
        time.sleep(3)
        driver.Details_text()
        driver.Click_HomeButton()
    def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
        unittest.main()