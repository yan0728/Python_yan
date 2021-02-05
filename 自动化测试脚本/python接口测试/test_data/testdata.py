#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: testdata.py
@time:2021/1/15 0015
"""

from ..tools import uti
from ..test_case import test_case


api1118 = '/loan-api-link/api/appbiz/LoanEasyRest/1118/v1'
data1118 = {
    "sysSource": "4",
    "frontTransNo": str(uti.frontTransNo),
    "frontTransTime": uti.ti,
    "interfaceNo": "1118",
    "busiCode": "CSB18",
    "telephone": uti.phone,
    "appAmount": "30000",
    "appPeriod": "24",
    "custmerManger": "11037385",
    "position": "301000817",
    "telemarketing": "0"
}


api1037 = '/loan-api-link/api/appbiz/LoanEasyRest/1037/v1'
data1037 = {
    "position": "301002007",
    "cardId": uti.idCare,
    "birthday": "1990-07-28",
    "sex": "M",
    "cardUrlB": "group1/M00/0A/02/rBJkp13zNp2APEikAADZJJumDD4067.jpg",
    "interfaceNo": "1037",
    "consultId": test_case.test_1118(),
    "cardUrlA": "group1/M00/0A/02/rBJkp13zNp2ATXBGAADfWiHhKAY873.jpg",
    "frontTransNo": str(uti.frontTransNo),
    "custmerManger": "11037385",
    "cardEndT": "2021-12-21",
    "busiCode": "CSB37",
    "nation": "汉",
    "areaName": "北京市大兴区采育镇沙窝营村金光街东六条9号",
    "telemarketing": "0",
    "cardStartT": "2011-12-21",
    "sysSource": "1",
    "custName": uti.name,
    "telephone": uti.phone,
    "frontTransTime": uti.ti
}

api1084 = '/loan-api-link/api/appbiz/LoanEasyRest/1084/v1'
data1084 = {
	"cardId": uti.idCare,
	"interfaceNo": "1084",
	"consultId": test_case.test_1118(),
	"frontTransNo": uti.frontTransNo,
	"opType": "02",
	"custName": uti.name,
	"sysSource": "1",
	"busiCode": "CSB84",
	"telephone": uti.phone,
	"frontTransTime": uti.ti
}

api1038 = '/loan-api-link/api/appbiz/LoanEasyRest/1038/v1'
data1038 = {
    "consultId":test_case.test_1118(),
    "interfaceNo":"1038",
    "frontTransNo":uti.frontTransNo,
    "sysSource":"1",
    "busiCode":"CSB38",
    "cardId":uti.idCare,
    "telephone":uti.phone,
    "urlImg":"group1/M00/06/06/rBJkp11l89OAHNdyAABuiCLq2Z4435.jpg",
    "custName":uti.name,
    "frontTransTime":uti.ti
}

api1049 = '/loan-api-link/api/appbiz/LoanEasyRest/1049/v1'
data1049 = {
	"cardId": uti.idCare ,
	"position": "301002007",
	"interfaceNo": "1049",
	"consultId": test_case.test_1118(),
	"frontTransNo": uti.frontTransNo,
	"custmerManger": "11037385",
	"busiCode": "CSB49",
	"lbTIntoInfoCustomer": [{
		"currentAddr": uti.address,
		"currentAreacode": "110101",
		"hDegree": "1",
		"homeType": "1",
		"loanPrePurpose": "101",
		"loanPurpose": "11",
		"email":uti.email
	}],
	"sysSource": "1",
	"custName": uti.name,
	"telephone": uti.phone,
	"intoDetailType": "lbTIntoInfoCustomer",
	"frontTransTime": uti.ti
}

