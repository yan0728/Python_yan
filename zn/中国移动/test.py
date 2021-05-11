from faker import Faker
import requests
import json
import random
import time
import datetime

now_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

time1 = datetime.date.today().strftime('%Y%m%d')

faker = Faker(locale='zh_CN')

addr =  "yidong/"+ "20210512"+"/180000/"+"FL16551_20210512_64846"+".rar"

No = 'NO' + now_str
address1 = faker.name()
print(now_str,No,time1,addr)
