import faker

f=faker.Faker(locale='zh-CN') #需要指定国家，生成的数据是根据中国进行生成，比如电话号码等
for i in range(5):
    print(f.name() + ":" + f.address())   #随机生成中文姓名和地址,name()函数生成姓名，address()函数生成地址