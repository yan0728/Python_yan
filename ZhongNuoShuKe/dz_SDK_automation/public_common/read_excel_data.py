# -*- coding: utf-8 -*-
"""
@time :    2023/1/20  0:29
@File:     read_excel_data.py
@Software: PyCharm
@Author :  yanxuelei
@Version:  python3.8
"""

import xlrd
from dz_SDK_automation.setting import config



class ReadExcel:
    def __init__(self):
        pass
    # @staticmethod  #静态方法 通过类直接调用，不需要创建对象，不会隐式传递self
    def getExcelData(self,sheet_name):
        wb = xlrd.open_workbook(config.TEST_CASE_PATH) #获取文件
        # sheet = wb.sheet_by_index(0)
        # 获取sheet
        sheet = wb.sheet_by_name(sheet_name)
        nrows , cols= sheet.nrows , sheet.ncols
        # # print('行：', nrows)
        # # print('列：',cols )
        title = sheet.row_values(0)
        newlist = []
        for i in range(1,nrows):
            get_sheet_data = sheet.row_values(i)
            newlist.append(dict(zip(title, get_sheet_data)))
        # print(newlist,nrows)
        return newlist,nrows

re = ReadExcel()
re.getExcelData("小额打款")
