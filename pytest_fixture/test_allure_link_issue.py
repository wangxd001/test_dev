# coding=utf-8
"""
@Author: wangxd
"""
import allure


@allure.link('https://www.baidu.com', name='链接')
def test_link():
    print('这是一个加了链接的测试用例')


TEST_CASE_LINK = 'https://github.com'


@allure.testcase(TEST_CASE_LINK, '登录用例')
def test_with_case_link():
    print('这是一条测试用例的链接，链接到用例里面')
