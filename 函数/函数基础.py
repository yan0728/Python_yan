# 使用def 定义函数 define

# def fuction1(): #定义一个无参数的函数
#     print("hello world")
#
# fuction1() #执行函数


# 定义有参数的函数 这个参数叫形参
# def add(a,b):
#     c = a + b
#     print(c)
#
# add(1,2) # 1 和 2 叫实参


#练习题 使用filter函数过滤小于3的数
# 筛选函数’，filter()把传人的函数依次作用于序列的每个元素，
# 然后根据返回值是True还是false决定保留还是丢弃该元素，返回符合条件的序列

a = [1,2,3,4,5,6]

def guolu(n):
    return n > 3

n_List = filter(guolu,a)
new_list = list(n_List)
# print(new_list)

# 使用map函数 将下列数组中的数字扩大10倍
# map()：遍历序列，对序列中每个元素进行操作，最终获取新的序列
b = [1,2,3,4,5,6,7,8]

def chengshi(kd):
    return kd * 10
n_kd = map(chengshi,b)
new_kd = list(n_kd)
# print(new_kd)

# reduce()：对于序列内所有元素进行累计操作，
# 即是序列中后面的元素与前面的元素做累积计算（结果是所有元素共同作用的结果）
from functools import reduce
def xc(x,y):
    return x + y
print(reduce(xc,range(1,101)))
