# 1. 需要使用模块化函数
# 2.宠物的信息包括：宠物编号，宠物种类，宠物名字，宠物特色，宠物价格
# 3.需要实现：添加，查找，删除，修改，退出程序的功能
# 4.需要使用文件来储存信息，下次打开系统，数据依然存在



print('===欢迎来到宠物寄养系统===')
print('请输入你要选择的内容1：添加，2：查找，3：删除，4：修改，5：退出程序')

def xz():
    a = input("请输入您的选:")
    if a.isdigit():
        run(int(a))
    else:
        print("输入有误，请输入数字")
        xz()


def run(select):
    if select == 1 :
        add_cw()

    elif select == 2:
        select_cw()

    elif select == 3:
        delete_cw()

    elif select == 4:
        credits()

    elif select == 5:
        exit_wc()

    else:
        print("输入有误，只能输入1，2，3，4，5")
        xz()


def add_cw():
    print('===开始添加新的宠物===')
    id = input("请输入宠物ID")
    type = input("请输入宠物类型")
    name = input("请输入宠物名字")
    ts = input("请输入宠物特色")
    jg = input("请输入宠物价格")
    add = {'id':id,'类型':type,'名字':name,'特色':ts,'价格':jg}

    with open('cwmanger.txt','a') as fp:
        fp.write(str(add))


def select_cw():
    print('===宠物列表内宠物如下===')
    with open('cwmanger.txt', 'r') as fp:
        str = fp.read()

    #     判断是否是空列表
    if str == {} or str == [] or  str == () :
        print("没有宠物,请添加")
    else:
        print(str)

def delete_cw():
    print('delete cw')

def edit_cw():
    print('edit cw')

def exit_wc():
    print('exit cw')

if __name__ == '__main__':
    xz()

