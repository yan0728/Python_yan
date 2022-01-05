from Faker实战教程 import Faker
# 初始化需要指定国家，生成的数据是根据中国进行生成
f=Faker(locale='zh-CN')

def creatTestData():
    print(f.email()) #随机生成邮箱
    print(f.name())#随机生成名字
    print(f.address())#随机生成地址
    print(f.company())#随机生成公司
    print(f.job())#随机生成部门/职位
    print(f.phone_number())#随机生成手机号
    print(f.ssn())#随机生成身份证

    #一键构造人物信息
    #print(f.profile(fields='陈伟',sex=22))
    print(f.profile())#生成复杂人物信息
    print(f.simple_profile())#生成简单人物信息

    #打印对象可用的所有方法
    ##print(dir(f))

    print(f.file_name()) #随机生成文件名称
    print(f.province()) #随机生成省份
    print(f.password()) #随机生成密码
    print(f.image_url()) #随机生成图片连接
    print(f.country()) #随机生成国家名称
    print(f.city()) #随机生成城市名称
    print(f.date()) #随机生成时间
    print(f.color_name())#随机颜色名
    print(f.rgb_color())#随机RGB颜色
    print(f.hex_color())#随机HEX颜色
    print(f.md5())#随机生成md5值

testdate = creatTestData()