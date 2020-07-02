'''

题目：输出指定格式的日期。

程序分析：使用 datetime 模块。

datetime模块定义了5个类，分别是

1.datetime.date：表示日期的类

2.datetime.datetime：表示日期时间的类

3.datetime.time：表示时间的类

4.datetime.timedelta：表示时间间隔，即两个时间点的间隔

5.datetime.tzinfo：时区的相关信息

'''

import datetime
import time

# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
print(datetime.date.today().strftime('%d/%m/%y'))

# 创建日期对象
miketime = datetime.date(2019,1,1)
print(miketime.strftime('%y/%m/%d'))

# 日期算术运算  timedelta 表示时间间隔
s = miketime + datetime.timedelta(1)
print(s.strftime('%d-%m-%y'))

# 日期替换 datetime.date.replace(year,month,day)：替换给定日期，但不改变原日期
dateth = s.replace(month= s.month+1)
print(dateth.strftime('%y-%m-%d'))