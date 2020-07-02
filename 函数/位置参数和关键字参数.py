# 位置参数

# def add(a,b):
#     print(a+b)
#
# add(1,2) #1=a,2=b 位置是一一对应的 所以叫位置参数

#关键字参数

# def add(a,b):
#     print(a+b)
#     print(a,b)
#
# add(a=2,b=1) # 这时候 a的参数是2 ，b的参数是1

# *args: arguments (缺省的位置参数）

# def add(a,b,*args):
#     print(a,b,args)

# add(1,2) # 1 2 ()
# add(1,2,3,4,5,6) # 1 2 (3, 4, 5, 6)


# **kwargs : keywordargs  (缺省的关键字参数)
# def add(a,b,**kwargs):
#     print(a)
#     print(b)
#     print(kwargs)
# add(1,2,c=3,d=4)  #1 2 {'c': 3, 'd': 4}

# 将一个元组解包成缺省的位置参数传递出去
# # 在调用这个函数的时候，可以将一个元组前面加一个*的语法来将一个元组解包，然后将里面的值传递出去
# def add(*args):
#     print(args)
#
# a_tuple = (1,2)
# add(*a_tuple)  #(1, 2)

# 将一个字典解包成关键字参数传递出去 需要在字典前面加两个*
def add(**kwargs):
    print(kwargs)
add(**{'username':'yan','age':18})