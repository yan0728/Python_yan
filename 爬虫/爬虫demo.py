#!/usr/bin/env python 
import urllib.request
from bs4 import BeautifulSoup
import re
#将字符串写入文本中，这里要指定encoding格式，不然会报错。‘a’表示继续写入，不覆盖之前的内容#关于with的语法笔者会研究后再整理
def writeFile(str,file):
    if file:
        with open(file, 'a', encoding='utf-8') as f:
            f.write(str)
    else:
        with open(file, 'a', encoding='utf-8') as f:
            f.write(str)
#主函数
#输出的txt路径。笔者选择了当前目录下
outputTxtFile = '寒门崛起'
#章节目录的网址
contentUrl = 'https://www.xxbiquge.com/12_12914/'
#网址前缀
url = 'https://www.xxbiquge.com'
res = urllib.request.urlopen(contentUrl)
html = res.read().decode('utf-8')
soup = BeautifulSoup(html,'lxml')
pattern = re.compile('第.+章')
for chapter in soup.find_all('a'):
    if(pattern.match(chapter.string)):
        readRes = urllib.request.urlopen(url + chapter.get('href'))
        readHtml = readRes.read().decode('utf-8')
        readSoup = BeautifulSoup(readHtml, 'lxml')
        writeFile(chapter.string+'\n',outputTxtFile)
        for k in readSoup.find_all(id = 'content'):
            str=''
            for line in k.stripped_strings:
                str = str + line + '\n'
                writeFile(str, outputTxtFile)
                print('导入 ' + chapter.string + ' 完成')


# 这个是手册的中文地址https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
