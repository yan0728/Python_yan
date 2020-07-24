# 多继承
class Ma(object):
    def __init__(self):
        pass

    def run(self):
        print('马再跑')

class Lv(object):
     def __init__(self):
         pass

     def lamo(self):
         print('驴在拉磨')
# Luozi同时继承了马类和驴类
class Luozi(Ma,Lv):
        pass

# luozi = Luozi()
# luozi.run()
# luozi.lamo()

# 子类不能继承父类的私有属性（变量和方法）

class Persion(object):
    def __init__(self,name,age):
        self.__name = name
        self._age = age

    def __eat(self): # 私有方法
        print('人类在吃饭')

    def run(self):
        print('人类在奔跑')

class Student(Persion):

    def greet(self):
        # print('my name is ',self.__name) # 父类的私有方法不能被继承，因此会报错
        print('my age is',self._age) #父类受保护的变量可以被使用

    def test(self):
        # self.__eat() #父类私有的的方法不能被继承，因此会报错
        self.run()

s = Student('yan',12)
s.greet()
s.test()