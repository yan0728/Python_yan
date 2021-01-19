#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 111.py
@time:2021/1/19 0019
"""


import pytest
import os


# BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
@pytest.fixture()
def test_01():
    a = 5
    return a

def test_02(test_01):
    assert test_01 == 5
    print("断言成功")
