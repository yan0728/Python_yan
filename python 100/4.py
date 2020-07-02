'''
题目：输入某年某月某日，判断这一天是这一年的第几天？

程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
特殊情况，闰年且输入月份大于2时需考虑多加一天：


'''

year = int(input("请输入年:\n"))
month = int(input("请输入月:\n"))
day = int(input("请输入日:\n"))

months = (0,31,59,90,120,151,181,212,243,273,304,334)

if 0 < month <=12 and 0 <day<= 31:
    sum = months[month -1] + day
    print(sum)

else:
    print("日期输入错误")