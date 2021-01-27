#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: test_1051.py
@time:2021/1/25 0025
"""
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

    def test_1051(self):
        exceldata = ReadExcel.ReadExcel.getExcelData1051(1)
        for i in range(0, len(exceldata)):
            params = exceldata[i]
            if params['method'] == 'post':
                # str.encode('utf-8') 转化成utf-8
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
