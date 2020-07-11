# 多态 = 鸭子类型 是一种编程方法

class Hero(object):

    def __init__(self):
         pass


class Chengyj(Hero):

    def dazhao(self):
        print('程咬金启动回血大招!!!')

class Ake(Hero):

    def dazhao(self):
        print('阿珂启动隐身大招!!!')

while True: #通过让while True 死循环可以一直选择英雄，通过break退出循环
    hero = None

    hero = input('请输入你选择的英雄:')
    # 多态的写法，h根据用户输入，可以是任何的英雄
    if hero == 'cyj':
        h = Chengyj()
        break

    elif hero == 'ake':
        h = Ake()
        break

    else:
        print('***输入有误请重新输入***')
        print('=' * 13)

h.dazhao()