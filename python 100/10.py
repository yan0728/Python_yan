'''

题目：暂停一秒输出，并格式化当前时间。

我们可以使用 time 模块的 strftime 方法来格式化日期，：


'''

import time
# 日历
import calendar

t = time.strftime('%Y-%m-%d %H:%M:%S')
time.sleep(1)
print(t+'\n')


cal = calendar.month(2020,1)

print(cal)