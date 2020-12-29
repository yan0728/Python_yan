#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: readWord.py
@time:2020/12/29 0029
"""


import docx

file = docx.Document("123.docx")

# 输出每一段内容
for i in file.paragraphs:
    print(i.text)
