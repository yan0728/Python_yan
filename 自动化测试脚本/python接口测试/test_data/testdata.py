#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: testdata.py
@time:2021/1/15 0015
"""
header = {'Content-Type': 'application/json;charset=UTF-8','User-Agent': 'Apache-HttpClient/4.5.5 (Java/1.8.0_121)'}


api1118 = '/loan-api-link/api/appbiz/LoanEasyRest/1118/v1'
data1118 = {
    "sysSource": "4",
    "frontTransNo": "20210107221401599",
    "frontTransTime": "2019-07-18 15:15:20",
    "interfaceNo": "1118",
    "busiCode": "CSB18",
    "telephone": "13916263326",
    "appAmount": "30000",
    "appPeriod": "24",
    "custmerManger": "11037385",
    "position": "301000817",
    "telemarketing": "0"
}

api1050 = '/loan-api-link/api/appbiz/LoanEasyRest/1050/v1'
data1050 = {"curPage":"1","interfaceNo":"1050","frontTransNo":"20210105143601399","sysSource":"4","busiCode":"CSB50","cardId":"65210119860216133X","pageSize":"20","telephone":"15809959223","totalRows":"0","custName":"买买提江·肉孜","frontTransTime":"2021-01-05 14:36:01"}
