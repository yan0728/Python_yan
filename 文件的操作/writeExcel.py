import openpyxl
from openpyxl import load_workbook
from 自动化测试脚本.随机生成四要素 import fourEl
import random

# 打开excel
workbook1=load_workbook("C:\\Users\\Administrator\\Desktop\\test.xlsx")

# 定位单元格
sheet = workbook1['Sheet1']

# 操作excel的test_data表单 ,定位单元格（cell），根据行列读取测试数据
a = fourEl('男')

for i in range(2,201):
    # x = random.randint(10000,99999)
    b = a.create_idcard()
    c = a.create_name()
    dicard = sheet.cell(i,1).value = b
    name = sheet.cell(i,2).value = c
    print(str(i),'-->',dicard,name)

workbook1.save("C:\\Users\\Administrator\\Desktop\\test.xlsx")
print('保存成功')
