'''

题目：判断101-200之间有多少个素数，并输出所有素数。

程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数

'''
import math

leap = 1
sum = 0

for i in  range(101,201):
    k = math.sqrt(i)
    for j in range(2,int(k+1)):
        if i % j == 0:
            leap = 0
            break

    if leap == 1:
        print(i)
        sum = sum+1
    leap = 1

print("总共有{}个素数".format(sum))