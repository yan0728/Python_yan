'''

题目：暂停一秒输出。

程序分析：使用 time 模块的 sleep() 函数

'''

import time

for i in range(1,10):
    for j in range(1,10):
        if j <= i:
            time.sleep(1)
            print('{1} * {0} = {2}  '.format(i,j,i*j),end="")
    print()