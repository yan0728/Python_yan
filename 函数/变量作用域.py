# 全局变量,定义全局变量的时候一般用全大写
PHONE = 1381095772

def greet():
    # 使用global 关键字修改变量为全局变量，glabal关键在需要放在函数开头
    global PHONE
    # 局部变量
    username = 'yan'
    age = '18'
    print(username)
    print('i phone number is %s' %PHONE)
    # 修改全局变量
    PHONE = 13810957383

greet()

print(PHONE)


