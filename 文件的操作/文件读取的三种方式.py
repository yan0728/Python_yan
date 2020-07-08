# read函数
# fp = open('xxx.txt','r',encoding='utf-8')
# print(fp.read())
# fp.close()

# readline 函数 --- 调用一次执行读取一行内容
# fp = open('xxx.txt','r',encoding='utf-8')
# line1 = fp.readline()
# line2 = fp.readline()
# print(line1)
# print(line2)
# fp.close()

# readlings 函数
# fp = open('xxx.txt','r',encoding='utf-8')
# lines = fp.readlines()
# # print(type(lines))
# for i in lines:
#     print(i)
# fp.close()

# 遍历文件指针对象：可以读取大文件
fp = open('xxx.txt','r')
for line in fp:
    print(line)