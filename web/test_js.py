# coding=utf-8
"""
@Author: wangxd
"""
import time

from web.base import Base


class TestJs(Base):
    def test_js_scroll(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(2)
        element = self.driver.execute_script('return document.getElementById("su")')
        element.click()
        time.sleep(2)
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        time.sleep(2)
        self.driver.find_element_by_link_text('下一页 >').click()
        for code in [
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))
