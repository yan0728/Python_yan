import random
# 饺子,刀削面，大盘鸡，烤鱼，小碗菜，自助，鸭血粉丝，麻辣烫，煲仔饭，鱼滑，米线
# print(random.random())  # 用于生成一个0到1之间的随机浮点数
# print(random.uniform(1, 3))  # 用于生成一个指定范围内的随机浮点数
# print(random.uniform(3, 1))  # 两个参数一个是上限，一个是下限。
# print(random.randint(1, 3))  # 用于生成一个指定范围内的整数。
# # random.randrange([start],stop[,step]) 从指定范围内，按指定的基数递增的集合中获取一个随机数
# print(random.randrange(0, 100, 2))  # 取 0到100之间的随机偶数

# random.choice 从序列中获取一个随机元素。其函数原型为random.choice(sequence)，参数sequence表示
# 一个有序类型。
# print(random.choice('改变世界'))  # 世
# print(random.choice(['sunshine', 'is', 'lower']))  # lower
# print(random.choice(('sunshine', 'always', '18')))  # 18
#
#  random.shuffle(x[,random]) 用于将一个列表中的元素打乱。
#
# s = ['改', '变', '世', '界']
# random.shuffle(s)
# print(s)  # ['变', '世', '改', '界']
#
#  random.sample(sequence,k) 从指令序列中随机获取指定长度的片段。sample函数不会修改原有的序列。
# l = [1, 2, 3, 4, 5, 6, 7, 8]
# print(random.sample(l, 3))  # [7, 3, 5]

# a = ['饺子','刀削面','大盘鸡','烤鱼','小碗菜','自助','鸭血粉丝','麻辣烫','煲仔饭','鱼滑','米线']
# i = random.randint(0,10)
# print(a[i])

food = random.choice(['饺子','刀削面','大盘鸡','烤鱼','小碗菜','自助','鸭血粉丝','麻辣烫','煲仔饭','鱼滑','米线','出去吃','炸酱面'])
print(food)