class Persian:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print('人类在吃饭')


class Student(Persian):
    # 子类重写父类方法
    def eat(self):
        print('学生在吃饭')

s = Student('yanxuelei','18')
s.eat()