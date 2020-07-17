#!/usr/bin/env python 
"""
@author:闫学雷
@project:学习
@file: readExcel.py
@time:2020/6/16 0016
"""

import xlrd
import random
# from PythonYan.数据库.connectMysql import connect_mysql #绝对路径导入文件并使用其中的方法
from 数据库.connectMysql import connect_mysql

def read_excel():
    wb = xlrd.open_workbook("D:\python37\PythonYan\文件的操作\捷越直接放款债权明细.xlsx") #打开Excel文件
    sheet = wb.sheet_by_name("Sheet1")   #通过excel表格名称(rank)获取工作表
    print('<<<<<<<<<<<<<<<<<文件开始读取>>>>>>>>>>>>>>>>>>')
    return sheet

def write_mysql():
    db = connect_mysql()
    # 创建游标
    cur = db.cursor()
    run = 0
    sheet = read_excel()
    for a in range(sheet.nrows):  # 循环读取表格内容（每次读取一行数据）
        cells = sheet.row_values(a)  # 每行数据赋值给cells
        if '*' in cells[3]:
            cells[3] = '621483011226' + str(random.randint(1000,9999))
            insert = ("INSERT INTO `excel`(name,card_id,phone,bank_card) VALUES ('%s','%s','%s',%s)" % (
                cells[0], cells[1], cells[2], cells[3]))
            cur.execute(insert)
            db.commit()
            run = run + 1
            print('已执行{}行到数据库'.format(run))
        else:
            insert = ("INSERT INTO `excel`(name,card_id,phone,bank_card) VALUES ('%s','%s','%s',%s)" % (
            cells[0], cells[1], cells[2], cells[3]))
            cur.execute(insert)
            db.commit()
            run = run + 1
            print('已执行{}行到数据库'.format(run))
    print("<<<<<<<<<<<<执行完毕>>>>>>>>>>>>>>")
write_mysql()