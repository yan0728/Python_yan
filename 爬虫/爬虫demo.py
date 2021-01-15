#!/usr/bin/env python
#coding:utf-8

import requests
from bs4 import BeautifulSoup
import os

#图片保存路径:
path = "D://爬虫专用//"

URL = 'http://tieba.baidu.com/p/1753935195'
html_page = requests.get(URL)

#创建BeautifulSoup对象
soup = BeautifulSoup(html_page.text,'html.parser')

#通过class="BDE_Image"获取所有的img 标签
class_image = soup.findAll(attrs={"class":"BDE_Image"})
print(class_image)

#判断目录是否存在
if not os.path.exists(path):
    os.mkdir(path)
try:
    x = 0
    # 循环class_image列表，找到所有img标签的链接
    for i in class_image:
        #取出src对应的url地址
        src_url = i.get('src')
        #请求src_url链接地址
        imge_list = requests.get(src_url)
        #构造url名称
        #down = path + src_url.split('/')[-1]
        down = path + '%s.jpg' %x
        print(down)
        #以二进制保存图片
        with open(down,'wb') as f:
            f.write(imge_list.content)
        x += 1

except Exception as e:
    print("pass")