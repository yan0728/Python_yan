import requests
import json
import random
import datetime
fileNo = 'FL' + str(random.randint(10000,99999))

data = "text={'addr':'yidong/20210510/180000/移动资料.zip','assets':['HBD10006'],'extension':'pdf','fileName':'再保理合同.pdf','fileNo':'%s','fileSize':20480,'fileType':'01','loanAmountTotal':30000}" % fileNo

print(data)