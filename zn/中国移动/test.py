from faker import Faker
import time
import random

fileNo = 'FL' + str(random.randint(10000,99999))
faker = Faker(locale='zh_CN')



time = time.strftime("%Y%m%d%H%M%S", time.localtime())
No = 'NO' + time
address1 = faker.name()
print(time,No,fileNo)
