'''

题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'

'''

strinput = input("please input any world:")

alpha = 0
space = 0
num = 0
other = 0

if len(strinput) <=0:
    print("请输入正确的字符\n")

else:

    for i in strinput:
        if i.isalpha(): #是否有字符
            alpha = alpha + 1

        elif i.isspace(): #是否有空格
            space = space + 1

        elif i.isdigit(): #是否有数字
            num = num + 1

        else:
            other = other + 1

print("字母有{}个，空格有{}个，数字有{}个，其他字符有{}个".format(alpha,space,num,other))