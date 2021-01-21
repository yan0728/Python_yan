# 多态 = 鸭子类型 是一种编程方法
class Chengyj():

    def dazhao(self):
        print('程咬金启动回血大招!!!')

    def yjn(self):
        print("程咬金1技能位移加减速")

class Ake():

    def dazhao(self):
        print('阿珂启动隐身大招!!!')

    def yjn(self):
        print("阿珂使用一技能:刺两下")

while True: #通过让while True 死循环可以一直选择英雄，通过break退出循环
    # hero = None

    hero = input('请输入你选择的英雄:')
    # 多态的写法，h根据用户输入，可以是任何的英雄
    if hero == 'cyj':
        h = Chengyj()
        jn = input("输入要使用的技能")
        if jn == '1':
            h.yjn()
        else:
            h.dazhao()
        break

    elif hero == 'ake':
        h = Ake()
        jn = input("输入要使用的技能")
        if jn == '1':
            h.yjn()
        else:
            h.dazhao()
        break

    else:
        print('***输入有误请重新输入***')
        print('=' * 13)
