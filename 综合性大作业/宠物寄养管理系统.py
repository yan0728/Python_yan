# 1. 需要使用模块化函数
# 2.宠物的信息包括：宠物编号，宠物种类，宠物名字，宠物特色，宠物价格
# 3.需要实现：添加，查找，删除，修改，退出程序的功能
# 4.需要使用文件来储存信息，下次打开系统，数据依然存在


from 数据库.connectMysql import connect_mysql
from 数据库.connectMysql import connect_mysql_home
connect = 'home'
# connect = 'company'

print('===欢迎来到宠物寄养系统===')

def xz():
    print('============请输入你要选择的内容1：添加，2：查找，3：删除，4：修改，5：退出程序=============')
    a = input("请输入您的选择:")
    if a.isdigit():
        run(int(a))
    else:
        print("输入有误，请输入数字")
        xz()

def run(select):
    if select == 1 :
        add_cw(connect)

    elif select == 2:
        select_cw(connect)

    elif select == 3:
        delete_cw(connect)

    elif select == 4:
        edit_cw(connect)

    elif select == 5:
        exit_wc()

    else:
        print("输入有误，只能输入1，2，3，4，5")
        xz()

def add_cw(connect):
    print('===开始添加新的宠物===')
    type = input("请输入宠物类型")
    name = input("请输入宠物名字")
    ts = input("请输入宠物特色")
    jg = input("请输入宠物价格")
    # 数据库操作
    if connect == 'company':
        db = connect_mysql()
    else:
        db = connect_mysql_home()
    cur = db.cursor()
    addsql = ("INSERT INTO `ainimal` (type,name,feature,price)VALUES ('{}','{}','{}','{}')".format(type,name,ts,jg))
    # print(addsql)
    cur.execute(addsql)
    db.commit()
    db.close()
    print("恭喜您，宠物寄养成功")
    xz()

def select_cw(connect):
    print('===宠物列表内宠物如下===')
    if connect == 'company':
        db = connect_mysql()
    else:
        db = connect_mysql_home()
    cur = db.cursor()
    selectsql = ('SELECT * FROM `ainimal`')
    cur.execute(selectsql)
    results = cur.fetchall()
    if results ==():
        print("目前没有寄样任何动物")
    else:
        for row in results:
            id = row[0]
            type = row[1]
            name = row[2]
            feature = row[3]
            price = row[4]
            print(id,'|',type,'|',name,'|',feature,'|',price)
    db.close()
    xz()

def delete_cw(connect):
    id =  input("请输入你要删除数据的id")
    if connect == 'company':
        db = connect_mysql()
    else:
        db = connect_mysql_home()
    cur = db.cursor()
    delsql = ('DELETE FROM	`ainimal` WHERE id = {};'.format(id))
    cur.execute(delsql)
    db.commit()
    db.close()
    print("数据已删除成功")
    xz()

def edit_cw(connect):
    print('edit cw')

def exit_wc():
    print('退出成功')

if __name__ == '__main__':
    xz()
