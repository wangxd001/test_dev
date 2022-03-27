# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestSearch():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_search(self):
        self.driver.get("https://www.baidu.com/")
        # time.sleep(2)
        # self.driver.set_window_size(1206, 814)
        # time.sleep(2)
        self.driver.find_element(By.ID, "kw").send_keys("github")
        # time.sleep(2)
        self.driver.find_element(By.ID, "su").click()
        time.sleep(4)
