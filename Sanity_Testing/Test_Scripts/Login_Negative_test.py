import time
import unittest

from selenium import webdriver

from Data.parameters import Data
from get_dir import pwd


class login_test(unittest.TestCase):
    def setUp(self):
        dri = pwd()
        self.driver = webdriver.Chrome(dri.get_driver_path())
        self.driver.implicitly_wait(15)

    def test_url(self):
        self.driver.maximize_window()
        self.driver.get(Data.url)
        self.driver.find_element_by_xpath(Data.email).send_keys("tibil@cqe.com")
        self.driver.find_element_by_xpath(Data.pwd).send_keys("tibl")

        self.driver.find_element_by_xpath(Data.login).click()
        time.sleep(4)
        errormsg = self.driver.find_element_by_xpath("//p").text
        print(errormsg)
        self.assertEqual(errormsg,"User not found" , msg="Failed")

    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()