# class 所有的函数第一个参数必须是self，self代表的就是当前类的对象

class Persion(object):
    # 构造函数，相当于给类直接添加了 name，age，eat的属性
    def __init__(self,name,age,eat):
        self.name = name
        self.age = age
        self.eat = eat

    def run(self,a,c):
        j = a * c
        print("总共跑了{}".format(j))


# r1 = Persion.run(4,5)
# p1 = Persion('yanxulei',18,'肉')
# print(p1.name,p1.age,p1.eat)


#受保护的属性,在参数前面添加'_'下划线。代表最好不要用，不是不可以用
# class Women(object):
#     #定义一个受保护的age属性
#     def __init__(self,age):
#         self._age = age
#
# woman = Women(19)
# print(woman._age)

# 私有属性：就是在变量前面添加两个下划线'__'，这样在外部将不能访问
class Account(object):
    def __init__(self,a_id,pw):
        self.a_id = a_id
        self.__pw = pw

    def __account_list(self):
        print("我是一个私有方法")
        return [11,-11,22]
    # 通过函数调用私有方法
    def get_account_list(self,password):
        if password == self.__pw:
            return self.__account_list()
        else:
            return None

account = Account('6214830112262497','0115123')

print(account.a_id)
print(account.get_account_list('0115123'))
# print(account.__pw) #因为是私有的，将会提示没有这个属性
