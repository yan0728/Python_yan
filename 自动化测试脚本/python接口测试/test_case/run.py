#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: run.py
@time:2021/1/20 0020
"""
'''
完整的pytest文档
https://docs.pytest.org/en/latest/contents.html
通过python代码执行 pytest.main()
1.直接执行pytest.main() 【自动查找当前目录下，以test_开头的文件或者以_test结尾的py文件】
2.设置pytest的执行参数 pytest.main(['--html=./report.html','test_login.py'])【执行test_login.py文件，并生成html格式的报告】
main()括号内可传入执行参数和插件参数，通过[]进行分割，[]内的多个参数通过‘逗号,’进行分割
运行目录及子包下的所有用例  pytest.main(['目录名'])
运行指定模块所有用例  pytest.main(['test_reg.py'])
运行指定模块指定类指定用例  pytest.main(['test_reg.py::TestClass::test_method'])  冒号分割
 
      
-m=xxx: 运行打标签的用例
-reruns=xxx，失败重新运行
-q: 安静模式, 不输出环境信息
-v: 丰富信息模式, 输出更详细的用例执行信息
-s: 显示程序中的print/logging输出
--resultlog=./log.txt 生成log
--junitxml=./log.xml 生成xml报告
'''

import pytest
import time
now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
pytest.main(["-s","--html=..\\report\\{}_report.html".format(now),"--alluredir=..\\allure"])

