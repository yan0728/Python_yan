#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: 测试报告.py
@time:2021/1/4 0004
"""
import unittest
import HTMLTestRunnerCN
import time
from UI自动化selenium import testCase

if __name__ == '__main__':
        suite = unittest.TestSuite()
        # Test3是要测试的类名，test_one是要执行的测试方法
        suite.addTest(testCase.Test3("test_one"))
        suite.addTest(testCase.Test3("test_two"))

        # 实践中发现执行时的当前路径，不一定是此文件所在的文件夹，所以使用绝对路径
        now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        filename = now + "testReport.html"
        fp = open(filename , 'wb')
        runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title="自动化测试报告", description="详细测试用例结果")
        runner.run(suite)
        print("生产报告成功")
        fp.close()
