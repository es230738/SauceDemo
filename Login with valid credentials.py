from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class Test(unittest.TestCase):

    def testvalidcredentials(self):
        driver = webdriver.Chrome(executable_path=r"C:\Users\SARAN\PycharmProjects\Drivers\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.saucedemo.com/")
        driver.set_page_load_timeout(1)

        user_input = driver.find_element_by_id('user-name')
        user_input.send_keys("standard_user")
        user_input = driver.find_element_by_id("password")
        user_input.send_keys("secret_sauce")

        driver.find_element_by_id("login-button").click()
        driver.find_element_by_xpath('//select[@class="product_sort_container"]/option[@value="lohi"]').click()

        # Selecting first item
        item_1_label = driver. \
            find_element_by_xpath('//div[@class="inventory_item_name"][contains(text(), "Sauce Labs Fleece Jacket")]')
        item_1 = item_1_label.find_element_by_xpath('../../..')
        price_1 = item_1.find_element_by_xpath('.//div[@class="pricebar"]/div[@class="inventory_item_price"]').text
        # self.assertEqual(price_1, "$49")
        item_1.find_element_by_xpath('.//div[@class="pricebar"]/button[contains(text(), "Add to cart")]').click()

        # Selecting second item
        item_2_label = driver. \
            find_element_by_xpath('//div[@class="inventory_item_name"][contains(text(), "Sauce Labs Backpack")]')
        item_2 = item_2_label.find_element_by_xpath('../../..')
        price_2 = item_2.find_element_by_xpath('.//div[@class="pricebar"]/div[@class="inventory_item_price"]').text
        # self.assertEqual(price_2, "$29")
        item_2.find_element_by_xpath('.//div[@class="pricebar"]/button[contains(text(), "Add to cart")]').click()
        # go to checkout
        driver.find_element_by_xpath('//a[@class="shopping_cart_link"]').click()
        cart_element_1 = driver. \
            find_elements_by_xpath('//div[@class="inventory_item_name"][contains(text(), "Sauce Labs Fleece Jacket")]')
        self.assertGreater(len(cart_element_1), 0)
        cart_element_2 = driver. \
            find_elements_by_xpath('//div[@class="inventory_item_name"][contains(text(), "Sauce Labs Backpack")]')
        self.assertGreater(len(cart_element_2), 0)

        driver.find_element_by_id("checkout").click()
        first_name = driver.find_element_by_id("first-name")
        first_name.send_keys("Eshita")
        first_name = driver.find_element_by_id("last-name")
        first_name.send_keys("Gurung")
        first_name = driver.find_element_by_id("postal-code")
        first_name.send_keys("12345")
        driver.find_element_by_id("continue").click()

        # Get payment information
        payment_info = driver.find_element_by_xpath('//div[@class ="summary_value_label"][1]').text
        self.assertEqual(payment_info, "SauceCard #31337")

        # Get shipping information
        shipping_info = driver.find_element_by_xpath('//div[@class ="summary_value_label"][2]').text
        self.assertEqual(shipping_info, "FREE PONY EXPRESS DELIVERY!")

        # Get total value
        total_value = driver.find_element_by_xpath('//div[@class="summary_total_label"]').text.split(':')[1]
        self.assertEqual(total_value.strip(), "$86.38")

        driver.find_element_by_id("finish").click()
        driver.close()


if __name__ == "__main__":
    unittest.main()
