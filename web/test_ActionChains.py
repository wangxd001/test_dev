# coding=utf-8
"""
@Author: wangxd
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_case_click(self):
        self.driver.get('https://sahitest.com/demo/clicks.htm')
        element_click = self.driver.find_element_by_css_selector('input[value="click me"]')
        element_dbclick = self.driver.find_element(By.CSS_SELECTOR, 'input[value="dbl click me"]')
        element_rightclick = self.driver.find_element(By.XPATH, '//input[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(element_click)
        time.sleep(3)
        action.double_click(element_dbclick)
        time.sleep(3)
        action.context_click(element_rightclick)
        time.sleep(3)
        action.perform()

    def test_moveto(self):
        self.driver.get('https://www.baidu.com')
        element = self.driver.find_element_by_id('s-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
        time.sleep(2)
        pass

    def test_dragdrop(self):
        self.driver.get('https://sahitest.com/demo/dragDropMooTools.htm')
        drag_ele = self.driver.find_element_by_id('dragger')
        drop_ele = self.driver.find_element_by_class_name('item')
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_ele, drop_ele).perform()
        action.click_and_hold(drag_ele).release(drop_ele).perform()
        pass

    def test_keys(self):
        self.driver.get('https://sahitest.com/demo/label.htm')
        ele = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys('username').pause(3)
        action.send_keys(Keys.SPACE).pause(2)
        action.send_keys('Tom').pause(2)
        action.send_keys(Keys.CONTROL).pause(2)
        action.send_keys(Keys.BACK_SPACE).pause(2).perform()
        pass
