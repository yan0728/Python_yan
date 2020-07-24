#!/usr/bin/env python 
"""
@author:闫学雷
@project:PythonYan
@file: test.py
@time:2020/7/17 0017
"""

from connectMysql import connect_mysql

def selctPhone():
    db = connect_mysql() #调用connectMysql文件内的connect_mysql方法，并把返回值db赋值给变量db
    # 创建游标
    cur = db.cursor()
    selectphone = 'SELECT * FROM test.`phone`'
    cur.execute(selectphone)
    results = cur.fetchall()
    # print(results)
    for row in results:
        id = row[0]
        name = row[1]
        phone_num = row[2]
        card_id = row[3]
        print(id,'|',name,'|',phone_num,'|',card_id)
selctPhone()