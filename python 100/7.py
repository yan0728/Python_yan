'''

题目：将一个列表的数据复制到另一个列表中。


'''

def fin(n):
    list = [0,1]

    for i in range(1,n):
        f = list[i-1] + list[i]
        list.append(f)
    return list

def copy_list():
    list_c = fin(10).copy()
    print(list_c)
copy_list()

