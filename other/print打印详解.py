
# 占位符 字符串类型%s
name = 'yanxulei'
print('my name is %s'%(name))

# 占位符 整形%d
age = 18
print('my age is %d'%(age))

# 占位符 浮点类型%f
apple = 19.5
print('apple 价钱是 %f'%(apple))

# folat 类型四舍五入 就是在 % 和 f之间输入"."
print('apple 价钱是 %.f'%(apple))

# 如果小数后面仅需要1位数字，就在 % 和 f之间输入".1" 两位即".2"
print('%.1f'%(apple))

# 字符串拼接 元祖方法
print('my name is %s and my age is %d'%(name,age))