import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from TS.reuse_func import cqube
from get_dir import pwd


class test_crc_District(unittest.TestCase):
    def setUp(self):
        driver_path = pwd()
        self.driver = webdriver.Chrome(executable_path=driver_path.get_driver_path())
        driver = cqube(self.driver)
        driver.open_cqube_appln()
        driver = cqube(self.driver)
        driver.login_cqube()

    def test_url(self):
        driver =cqube(self.driver)

        driver.navigate_to_crc_report()

        # time.sleep(45)
        # driver.CRC_dist_Clicks()

    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()