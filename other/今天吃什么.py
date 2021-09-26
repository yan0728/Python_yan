import random
# print(random.random())  # 用于生成一个0到1之间的随机浮点数
# print(random.uniform(1, 3))  # 用于生成一个指定范围内的随机浮点数
# print(random.uniform(3, 1))  # 两个参数一个是上限，一个是下限。
# print(random.randint(1, 3))  # 用于生成一个指定范围内的整数。
# # random.randrange([start],stop[,step]) #从指定范围内，按指定的基数递增的集合中获取一个随机数
# print(random.randrange(0, 100, 2))  # 取 0到100之间的随机偶数
#
# # random.choice 从序列中获取一个随机元素。其函数原型为random.choice(sequence)，参数sequence表示
# # 一个有序类型。
# print(random.choice('改变世界'))
# print(random.choice(['sunshine', 'is', 'lower']))  # lower
# print(random.choice(('sunshine', 'always', '18')))  # 18
#
#  # random.shuffle(x[,random]) 用于将一个列表中的元素打乱。
#
# s = ['改', '变', '世', '界']
# random.shuffle(s)
# print(s)
#
#  # random.sample(sequence,k) 从指令序列中随机获取指定长度的片段。sample函数不会修改原有的序列。
l = [1, 2, 3, 4, 5, 6, 7, 8]

print(random.sample(l, 3))

# for i in range(0,10):
#     a = ['5楼','羊汤','刀削面','庆丰','外卖','川东情','KFC','二居']
#
#     food = random.choice(a)
#     print(food)


# i = random.randint(0,4)
# print(a[i])
