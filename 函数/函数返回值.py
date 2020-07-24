# 函数返回一个值
def add(a,b):
    c = a + b
    return c

def add1():
    d = add(1,2)
    print(d)

# add1()


# 函数一般使用元组来包装多个值进行返回，使用元组是因为元组不能修改
def greet():
    name = 'yanxuelei'
    age = 18
    return name,age

result = greet()
print(result)

#获取返回的值（获取元组的值）
a,b = result
print(a,b)