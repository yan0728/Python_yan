#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: demo.py
@time:2020/8/15 0015
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    print('hello world')
    return "hello world"

if __name__ == 'main':
    app.run()