# a = {'y':1,'e':2,'s':3,'si':4,'w':5}
# # 遍历key
# for i in a.keys():
#     print(i)
#
# print('*'*10)
#
# # 遍历value
# for m in a.values():
#     print(m)


def gcd(x, y):
    while y:
        t = x % y
        x = y
        y = t
    return x
print(gcd(4, 6))