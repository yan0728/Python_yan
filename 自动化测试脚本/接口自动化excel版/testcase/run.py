#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: run.py
@time:2021/1/25 0025
"""

import pytest
import time
now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
pytest.main(["--html=..\\report\\{}_report.html".format(now)])