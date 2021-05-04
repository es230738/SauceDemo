from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class Test(unittest.TestCase):

    def testLogin(self):
        driver = webdriver.Chrome(executable_path=r"C:\Users\SARAN\PycharmProjects\Drivers\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.saucedemo.com/")
        driver.set_page_load_timeout(1)

        user_input = driver.find_element_by_id('user-name')
        user_input.send_keys("locked_out_user")

        user_input = driver.find_element_by_id("password")
        user_input.send_keys("secret_sauce")
        user_input = driver.find_element_by_id("login-button").click()
        error_element = driver.find_element_by_xpath('//h3[@data-test="error"]')
        self.assertEqual(error_element.text, "Epic sadface: Sorry, this user has been locked out.")
        driver.close()


if __name__ == "__main__":
    unittest.main()








