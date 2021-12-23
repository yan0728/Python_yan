li = [1,2,3,4,5,6]

def PaiXu(list):
    for j in range(0,len(li)-1):
        for i in range(0,len(li)-1):
            if li[i] > li[i+1]:
                li[i],li[i+1] = li[i+1],li[i]
    print(li)

# PaiXu(li)

def QiuHe(list):
    sum = 0
    for i in range(0,len(li)):
        sum = sum + li[i]
    # print(sum)

QiuHe(li)

a = ''
for i in li:
    a = a + str(i)
print(a)