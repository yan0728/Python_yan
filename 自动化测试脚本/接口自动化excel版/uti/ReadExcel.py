#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: ReadExcel.py
@time:2021/1/22 0022
"""

import xlrd
import xlwt
from 自动化测试脚本.接口自动化excel版.setting import config

class ReadExcel():
    # @property
    def getExcelData(self):
        wb = xlrd.open_workbook(config.TEST_CASE_PATH) #获取文件
        sheet = wb.sheet_by_index(0) # sheet = wb.sheet_by_name("Sheet1") 获取sheet
        nrows , cols= sheet.nrows , sheet.ncols
        # print('行：', nrows)
        # print('列：',cols )
        title = sheet.row_values(0)
        newList = []

        for i in range(1,nrows):
            # print(sheet.row_values(i))
            newList.append(dict(zip(title,sheet.row_values(i))))
        # print(newList[0]['request'])

        return newList

    def getExcelData1118(self):
        wb = xlrd.open_workbook(config.TEST_CASE_PATH)
        # wb = xlrd.open_workbook(self)
        # sheet = wb.sheet_by_index(0)
        sheet = wb.sheet_by_name("1118")
        nrows, cols = sheet.nrows, sheet.ncols
        # print('行：', nrows)
        # print('列：',cols )
        title = sheet.row_values(0)
        newList = []

        for i in range(1, nrows):
            # print(sheet.row_values(i))
            newList.append(dict(zip(title, sheet.row_values(i))))
        return newList

    def getExcelData1026(self):
        wb = xlrd.open_workbook(config.TEST_CASE_PATH)
        # wb = xlrd.open_workbook(self)
        # sheet = wb.sheet_by_index(0)
        sheet = wb.sheet_by_name("1026")
        nrows, cols = sheet.nrows, sheet.ncols
        # print('行：', nrows)
        # print('列：',cols )
        title = sheet.row_values(0)
        newList = []

        for i in range(1, nrows):
            # print(sheet.row_values(i))
            newList.append(dict(zip(title, sheet.row_values(i))))
        # print(newList[0]['request'])

        return newList

    def getExcelData1050(self):
        wb = xlrd.open_workbook(config.TEST_CASE_PATH)
        # wb = xlrd.open_workbook(self)
        # sheet = wb.sheet_by_index(0)
        sheet = wb.sheet_by_name("1050")
        nrows, cols = sheet.nrows, sheet.ncols
        # print('行：', nrows)
        # print('列：',cols )
        title = sheet.row_values(0)
        newList = []

        for i in range(1, nrows):
            # print(sheet.row_values(i))
            newList.append(dict(zip(title, sheet.row_values(i))))
        # print(newList[0]['request'])

        return newList

    def getExcelData1051(self):
        wb = xlrd.open_workbook(config.TEST_CASE_PATH)
        # wb = xlrd.open_workbook(self)
        # sheet = wb.sheet_by_index(0)
        sheet = wb.sheet_by_name("1051")
        nrows, cols = sheet.nrows, sheet.ncols
        # print('行：', nrows)
        # print('列：',cols )
        title = sheet.row_values(0)
        newList = []

        for i in range(1, nrows):
            # print(sheet.row_values(i))
            newList.append(dict(zip(title, sheet.row_values(i))))
        # print(newList[0]['request'])

        return newList
