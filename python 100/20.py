'''

题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

'''

h = 100
times = 1
ft_list = []


for i in range(0,10):
    ft = h / (2 * times)
    ft_list.append(ft)
    times = times + 1

sum = sum(ft_list)
print(sum)