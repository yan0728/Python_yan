'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列

123 124 132 134 142 143
'''

sum = 0
for b in range(1,5):
    for s in range(1,5):
        for g in range(1,5):
            if b != s and b != g and s != g:
                print(b*100 + s*10 + g)
                sum = sum + 1
print('总共有{}个这样的数'.format(sum))
