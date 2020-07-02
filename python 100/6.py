'''

题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），
又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

在数学上，费波那契数列是以递归的方法来定义

'''
def fin(n):
    list = [0,1]

    for i in range(1,n):
        f = list[i-1] + list[i]
        list.append(f)
    print(list)
fin(20)