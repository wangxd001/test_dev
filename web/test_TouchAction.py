# coding=utf-8
"""
@Author: wangxd
"""
from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_touchaction_scroll(self):
        self.driver.get('https://www.baidu.com')
        input_ele = self.driver.find_element_by_id('kw')
        input_ele.send_keys('selenium')
        search_ele = self.driver.find_element_by_id('su')
        action = TouchActions(self.driver)
        action.tap(search_ele).perform()
        action.scroll_from_element(input_ele, 0, 4000).perform()
        pass