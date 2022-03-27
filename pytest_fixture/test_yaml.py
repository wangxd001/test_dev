# coding=utf-8
"""
@Author: wangxd
"""
import pytest
import yaml


class TestData:
    @pytest.mark.parametrize('a, b', yaml.safe_load(open('../data/data.yaml')))
    def test_data(self, a, b):
        print(a + b)

    def test_demo(self):
        with open('../data/demo.yaml') as file:
            print(yaml.safe_load(file))