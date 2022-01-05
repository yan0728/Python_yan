from faker import Faker
import datetime

'''
01 什么是Faker?
Faker是python方向的一个第三方库，主要用来创造伪数据，使用Faker，
人们不再需要手动或者手写随机数来生成数据，只需要调用Faker提供的相关api即可完成数据的生成
'''

# 02初始化，设置locale为中文；默认是英文
fake = Faker('zh_CN')

# 03日期类随机数据
print('**'*10 + '03日期类随机数据' +'**'*10)
print('年月日：', fake.date(pattern = '%Y-%m-%d'))
print('随机年份：', fake.year())
print('随机年份：', fake.year())
print('随机月份：',fake.month())
print('随机几号：', fake.day_of_month())
print('随机星期数：', fake.day_of_week())
print('时间：', fake.time(pattern = '%H:%M:%S'))
# -30y是过去30年前为开始日期，end_date表示结束到今天
print('过去某一天：',fake.date_between(start_date="-30y", end_date="today"))
print('今天：',fake.date_between_dates()) #今天
print('日期和时间：',fake.date_time()) #2021-05-14 19:36:00
print('当前日期时间：',fake.date_time_between_dates())
print('未来的日期：',fake.future_date(end_date="+30d"))
print('未来的日期时间：',fake.future_datetime(end_date="+30d")) # 未来日期和时间)
print('过去的日期：',fake.past_date(start_date="-30m")) # 过去日期
print('过去的日期时间：',fake.past_datetime(start_date="-30d")) # 过去日期和时间
print('时间戳：',fake.unix_time())

# 04随机字符串/数字/加密
print('**'*10 + '04随机字符串/数字/加密' +'**'*10)
print('随机字符串:',fake.pystr())
print('随机小写字母:',fake.random_element())
print('随机大写字母:',fake.random_letter())
print('随机一个段落:',fake.paragraph())
print('随机一句话:',fake.sentence())
print('随机一篇文章:',fake.text())
print('随机一个词语:',fake.word())
print('随机Ture和False:',fake.boolean())
print('随机md5：',fake.md5())
print('随机密码:',fake.password())
print('随机SHA1:',fake.sha1())
print('随机sha256:',fake.sha256())
print('随机uuid:',fake.uuid4())
print('三位随机数字:',fake.numerify())
print('0-9随机数：',fake.random_digit())
print('1-9随机数:',fake.random_digit_not_null())
print('0-9999随机数：',fake.random_int())
print('指定位数的随机数：',fake.random_number(digits=5))
print('随机小数:',fake.pyfloat())
print('随机int数：',fake.pyint())

# 05 随机人物相关信息
print('**'*10 + '05 随机人物相关信息' +'**'*10)
print('人物名字:',fake.first_name()) # 名字
print('女性名字:',fake.first_name_female())
print('男性名字:',fake.first_name_male())
print('姓:',fake.last_name())
print('男性的姓:',fake.last_name_male())
print('女性的姓:',fake.last_name_female())
print('人物全名:',fake.name())
print('女性全名:',fake.name_female())
print('男性全名:',fake.name_male())
print('生成身份证号:',fake.ssn())
print('生成手机号:',fake.phone_number())
print("邮箱:", fake.email())

# 06 随机地址信息数据
print('**'*10 + '06 随机地址信息数据' +'**'*10)
print('完整地址：', fake.address()) #上海市慧县沈河魏路j座 436993
print('街道+地址：', fake.street_address()) #关岭街O座
print('街道名：', fake.street_name()) #李路
# print('城市名：', fake.city_name()) #澳门
print('城市：', fake.city()) #林市
print('区：',fake.district()) #华龙
print('省份名：', fake.province()) #山西省
print('邮编：', fake.postcode()) #361494
print('国家：', fake.country()) #尼泊尔
print('国家编码：', fake.country_code()) #ST
print('地理坐标(纬度):',fake.latitude()) #28.936546
print('地理坐标(经度):',fake.longitude()) #-152.654212

# 07 随机公司信息数据
print('**'*10 + '07 随机公司信息数据' +'**'*10)
print('公司名：', fake.company())
print('公司名后缀：', fake.company_suffix())
print('企业邮箱:', fake.company_email())

# 08 随机网络信息数据
print('**'*10 + '08 随机网络信息数据' +'**'*10)
print('生成域名：',fake.domain_name())
print('生成ipv4:',fake.ipv4())
print('生成ipv6:',fake.ipv6())
print('生成MAC地址:',fake.mac_address())
print('生成uri地址:',fake.uri())
print('生成url地址:',fake.url())
print('随机用户名:',fake.user_name())

# 09 随机用户代理信息
print('**'*10 + '09 随机用户代理信' +'**'*10)
print('随机安卓代理信息：',fake.ios_platform_token())
print('随机ios代理信息：',fake.android_platform_token())
print('随机chrome代理信息：',fake.chrome())
print('随机firefox代理信息：',fake.chrome())
print('随机ie代理信息：',fake.internet_explorer())
print('随机opera代理信息：',fake.opera())
print('随机safari代理信息：',fake.safari())
print('随机代理信息：',fake.user_agent())
print('随机windows代理信息：',fake.windows_platform_token())
print('随机mac代理信息：',fake.mac_platform_token())