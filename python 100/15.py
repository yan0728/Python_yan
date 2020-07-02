'''

题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。

'''

a = int(input("please input a number"))

if a >= 90:
    print("A")
elif a <= 89 and a >= 60:
    print("B")
else:
    print("C")
    