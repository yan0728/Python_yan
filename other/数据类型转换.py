# a = 1
# print(type(a))
#
# b = str(a)
# print(type(b))
#
# c = float(a)
# print(type(c))

# python3 没有long 类型
import random

L=[1,2,3,4,5,6]
s=''
for i in L:
    s = s + str(i)
# print(s)


abc = {8,4,2,1,23,344,12}
count = 0

for i in abc:
    count = count + i
# print(count)

eee = random.randint(1,3)
print(eee)
if eee in abc:
    print("ture")
else:
    print("False")


print(sorted(abc))
