#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: ReqApi.py
@time:2021/1/22 0022
"""

import requests
from 自动化测试脚本.接口自动化excel版.uti import ReadExcel,WriteResult
from 自动化测试脚本.接口自动化excel版.setting import config

class Test_Request():

    def test_case(self):
        exceldata = ReadExcel.ReadExcel.getExcelData(1)
        for i in range(0, len(exceldata)):
            params = exceldata[i]
            if params['method'] == 'post':
                # str.encode('utf-8') 转化成utf-8
                # eval方法:自动去掉字符串两侧的引号，将字符串转为python语句，即字符串转命令，然后执行转化后的语句
                r = requests.post(url=params['base_url']+params['api'],data= params['requestBody'].encode('utf-8'),headers = eval(params['header']))
                # print('接口:',params['base_url']+params['api'])
                try:
                    assert r.status_code == 200
                    # return r.status_code
                    WriteResult.writeResult(i+2,r.text,'PASS',config.report_time)
                    print("接口:",params["api_name"],"请求写入完成")
                except:
                    # return r.text
                    WriteResult.writeResult(i+2, r.text, 'FAILED',config.report_time)
                    print("接口:", params["api_name"],r.text, "请求写入完成,接口请求失败")
            else:

                r = requests.get(url=params['base_url']+params['api'],data=params['requestBody'],headers = params['header'])
                try:
                    assert r.status_code == 200
                    # return r.status_code
                    print( r.status_code)
                except:
                    print(r.text)

'''
： 一个excel表格文件包含一个工作簿（workbook），一个wb可以包含多个工作表（worksheets）

用户正在查看的表定义为激活的工作表（active sheet）。每个工作表都有行和列。行以数字1开始，列以字母A开始，

一个工作表由单元格（cell）组成，cell只存储两种数据类型，数字和字符串（除了纯数字，其它均为字符串类型）

2： 在excel中设计测试用例的时候，当代码里的值为None的时候，对应cell中不需要输入任何值，空读取出来就是None
'''