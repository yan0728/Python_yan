for m in range(1,10):
    for n in range(1,10):
        if n <= m:
            # print("%s * %s = %s  "%(n,m,m*n),end='')
            pass
    # print()


lie =1
while lie <=9:
    hang = 1
    while hang <= lie:
        # print("%s * %s = %s   "%(hang,lie,hang*lie),end="")
        hang =hang + 1
    lie = lie +1
    # print()

import random
ran = '621483011226' + str(random.randint(1000,9999))
print(ran)