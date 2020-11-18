#!/usr/bin/env python
"""
@author:闫学雷
@project:PythonYan
@file: test.py
@time:2020/7/17 0017
"""
import  pymysql

def connect_mysql():
    try:
        db = pymysql.connect(
            host = '10.50.181.34',
            port = 3306,
            user= 'galaxy_edu',
            password = 'galaxy_edu',
            db = 'galaxy_edu',
            charset = 'utf8'
        )
    except Exception as e:
        print(e)
    else:
        print('数据库连接成功')
        return db

# connect_mysql()

def updateJY():
    db = connect_mysql()
    # 创建游标
    cur = db.cursor()
    studentnum = 2
    for i in range(113,302):
        update = ("UPDATE `base_student_study_info` SET student_num = {} WHERE student_id = {}".format(str(studentnum),i))
        cur.execute(update)
        db.commit()
        # studentnum = studentnum + 1
    print("提交成功")
updateJY()
