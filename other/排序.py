li = [56,44,67,28,68,79,3]

for j in range(0,len(li)-1):
    for i in range(0,len(li)-1):
        if li[i] > li[i+1]:
            li[i],li[i+1] = li[i+1],li[i]
print(li)