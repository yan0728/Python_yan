import  pip
import time
import datetime
import jwt

encoded = jwt.encode({"account": "13146152021","overdue_time":"1655827200"}, "secret", algorithm="HS256")
print(encoded)

res=jwt.decode(encoded, "secret", algorithms=["HS256"])

print(res)

class Assist_Get_Data():
    '''生成、检验本地token、辅佐获取系统数据'''

    def judge_login(self, account, own_token):
        '''判断是否登录有效'''
        ###检验own_token是否有效
        judge_own_token = self.verify_token(own_token, account)

        ###如果无效返回False
        if not judge_own_token:
            return False

        ###如果有效则获取token
        correlation_account = models.User_Account.objects.filter(account=account).first()
        token = models.Login_Record.objects.filter(account=correlation_account).first().token
        return token

    def time_str_int(self, date_str):
        '''将时间字符串转为时间戳'''
        ##将时间字符串转为时间数组
        timeArray = time.strptime(date_str, "%Y-%m-%d")
        ##将时间数组转为时间戳
        timeStamp = int(time.mktime(timeArray))
        return timeStamp

    def create_token(self, account):
        '''生成本地token'''
        ##获取一天后的时间戳，token过期时间为一天后
        overdue_time = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        overdue_timeStamp = self.time_str_int(overdue_time)
        ###生成token
        own_token = jwt.encode({"account": account, "overdue_time": overdue_timeStamp}, SECRET_KEY, algorithm="HS256")
        return own_token

    def verify_token(self, own_token, account):
        '''检验token'''
        ##解密token
        decode_token = jwt.decode(own_token, SECRET_KEY, algorithms=["HS256"])
        ##获取token中的account
        token_account = decode_token['account']
        ##获取token中的过期时间
        token_overdue_time = decode_token['overdue_time']
        ##获取当前时间的时间
        now_time = datetime.datetime.now().strftime("%Y-%m-%d")
        ##转为时间戳
        now_timeStamp = self.time_str_int(now_time)
        ###进行判断token,如果账号对的上以及当前访问时间没有超过token过期时间则返回True
        if token_account == account and now_timeStamp < token_overdue_time:
            return True
        else:
            return False
