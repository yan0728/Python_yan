# 字典基础
# 创建字典 1,使用{}的方式,比较推荐这种方式
a_dict = {"姓名":"yanxuelei","年龄":"29"}
print(a_dict) #{'username': 'yanxuelei', 'age': '29'}


#len(d):返回字典的键值对的长度
# print(len(a_dict)) #2


# 访问字典里的值
# print(a_dic["username"]) #yanxuelei


# 给字典添加值，如何字典已经有这个key那就是修改
a_dict['heigh'] = 165
a_dict['age'] = 28
# print(a_dict) #{'username': 'yanxuelei', 'age': 28, 'heigh': 165}


# 删除字典中的一项 关键字:del
del a_dict['heigh']
# print(a_dict) #{'username': 'yanxuelei', 'age': 28}


# # 查询字典是否存在某个key
# if 'username' in a_dict:
#     print('Ture')
# else:print("Fale")


# 字典中的value可以为任意类型，key只能使不可变的类型：字符串，浮点型，整形或者元组
a = ('ai','bi')
tem = {a:'12'}
# print(tem)  #{('ai', 'bi'): '12'}
