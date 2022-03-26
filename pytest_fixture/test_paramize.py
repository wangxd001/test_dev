# coding=utf-8
"""
@Author: wangxd
"""
import pytest


@pytest.mark.parametrize('test_input, expected', [('3+5', 8), ('2+5', 7), ('3*5', 16), ])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


# 参数组合
@pytest.mark.parametrize('x', [1, 2])
@pytest.mark.parametrize('y', [10, 20, 30])
def test_foo(x, y):
    # print('组合参数测试 x：{}, y:{}'.format(x, y))
    print(f'组合参数测试 x：{x}, y:{y}')


# 方法名作为参数
test_user_data = ['Tom', 'Bob']


@pytest.fixture(scope='module')
def login_u(request):
    user = request.param
    print(f'\n登录用户： {user}')
    return user


@pytest.mark.parametrize('login_u', test_user_data, indirect=True)
def test_login(login_u):
    a = login_u
    print(f'测试用例中login的返回值：{a}')
    assert a != ''
