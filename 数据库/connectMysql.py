#!/usr/bin/env python 
"""
@author:闫学雷
@project:学习
@file: connectMysql.py
@time:2020/1/19 0019
"""
import pymysql
def connect_mysql():
    try:
        db = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user= 'root',
            password = '123456',
            db = 'test',
            charset = 'utf8'
        )
    except Exception as e:
        print(e)
    else:
        # print('数据库连接成功')
        return db


def selectMoble():
    db = connect_mysql()
    # 创建游标
    cur = db.cursor()
    selectMoble = 'SELECT * FROM test.test_mobile'
    cur.execute(selectMoble) #执行脚本
    results = cur.fetchall() #查询时获取结果集中的所有行，一行构成一个元组，然后再将这些元组返回（即嵌套元组）
    for row in results:
        id = row[0]
        MobileOS = row[1]
        changshang = row[2]
        type = row[3]
        xuliehao = row[4]
        fenbianlv =row[5]
        size = row[6]
        Osversion = row[7]
        colour = row[8]
        user = row[9]
        borrow_date = row[10]

        print(id,'|',MobileOS,'|',changshang,'|',type,'|',xuliehao,'|',fenbianlv,'|',size,'|',Osversion,'|',colour,'|',user,'|',borrow_date)
# selectMoble()

def select_cw():
    print('===宠物列表内宠物如下===')
    db = connect_mysql()
    cur = db.cursor()
    selectsql = ('SELECT * FROM `ainimal`')
    cur.execute(selectsql)
    results = cur.fetchall()
    print(type(results))
    # db.close()
# select_cw()

def selctPhone():
    db = connect_mysql()
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
# selctPhone()

def updatePhone():
    db = connect_mysql()
    # 创建游标
    cur = db.cursor()
    cardId = input("请输入数字:")
    update = ("UPDATE `phone` SET card_id = {} WHERE id  = '1'".format(cardId))
    cur.execute(update)
    db.commit()
# updatePhone()

def insertInto():
    db = connect_mysql() #调用连接方法，复制给db
    cur = db.cursor() # 创建游标
    name = input("输入姓名:")
    phoneNum = input("请输入手机号:")
    cardId = input("请输入身份证号")
    # insert = ("INSERT INTO `phone`(name,phone_num,card_id) VALUES ({},{},{})".format(name,int(phoneNum),cardId))
    insert = ("INSERT INTO `phone`(name,phone_num,card_id) VALUES ('%s','%d','%s')"%(name, int(phoneNum), cardId))
    cur.execute(insert)
    db.commit()
    print("添加成功")
# insertInto()