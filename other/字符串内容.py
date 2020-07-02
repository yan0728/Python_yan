# 字符串下标
username = 'yan xuelei'
# print(username[0]) #打印第一个字符
# print(username[-1]) #打印最好后一个字母

# 字符串切片
# str[开始位置:结束位置+1:步长]
# number = '123456789'
# tmp = number[0:6]
# print(tmp)

#find 找到字符串打印字符串位置  找不到返回-1
# index = username.find('xue')
# print(index)

# len() 获取字符串函数
# print(len(username))

# format 格式化 不需要考虑参数类型
# age = 18
# Danile = 'my name is {},my age is {}'.format(username,age)
# print(Danile)

# format 位置参数 {0}代表第一个参数，{1}代表第二个参数
# age = 18
# Danile = 'my name is {0}, my username is {0}, my age is {1}'.format(username,age)
# print(Danile)

#打印字符串函数的使用 dir 参数为想查看的方法名 如 str，int，list
# all_methods = dir(str)
# for a in all_methods:
#     print(a)

# 原生字符串r raw
tem = r'你 \n 好'
print(tem)
