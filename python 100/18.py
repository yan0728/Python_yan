'''

题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

程序分析：关键是计算出每一项的值。

'''
a = int(input("a"))
n = int(input("n"))

js = ''
k = []
sum = 0

for i in range(n):
    js = js + '1'
    Ta = a * int(js)
    k.append(Ta)
    sum = sum + k[i]

print(sum)