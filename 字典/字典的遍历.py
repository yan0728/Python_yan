# 遍历字典中所以的keys
persion = {'username':'yan','age':29,'sex':'男'}

# for key in persion.keys():
#     print(key)

# 使用value方法遍历所以的值
# for key in persion.values():
#     print(key)

# 使用items方法遍历字典中所以的建和值
items = persion.items()
# for item in items:
#     key,value = item #元组解饱
    # print(key,value)

for key,value in items:
    print(key,value)