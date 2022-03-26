# coding=utf-8
"""
@Author: wangxd
"""
import pytest
import allure


@allure.feature('登录功能')
class TestLogin:
    @allure.story('登录成功')
    def test_login_success(self):
        print('这是登录测试用例，登录成功')
        pass

    @allure.story('登录失败')
    def test_login_fail(self):
        print('这是登录测试用例，登录失败')
        pass

    @allure.story('密码缺失')
    def test_login_nopwd(self):
        with allure.step('点击用户名'):
            print('输入用户名')
        with allure.step('点击密码'):
            print('输入密码')
        print('点击登录')
        with allure.step('点击登录后登录失败'):
            print('登录失败')
