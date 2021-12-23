
import json
import time
import datetime
import random
import hashlib

seqNo = str(int(time.time()))
time = datetime.date.today().strftime('%Y-%m-%d')
invoiceNo = str(random.randint(10000000,99999999))
invoiceCode = str(random.randint(100000,999999))

apiType = 'ABS_ASSET_INFO'
appId = 'dev_newhope'
dataStr = str(
{
                "seqNo":"seqNo"+seqNo,
                "merchCode": "",
                "assetList": [
                    {
                        "fundNo": "NO"+ seqNo,
                        "requestNo": "RQ"+ seqNo,
                        "fundType": "销售费用",
                        "companyName": "深圳市金兰湾贸易有限公司",
                        "companyVatNum": "91440300342921125A",
                        "companyArea": "",
                        "vendorName": "中山市风行广告有限公司",
                        "vendorVatNum": "914420007857977335",
                        "vendorArea": "",
                        "bankName": "供应商的收款银行开户行",
                        "acctName": "供应商的银行账户名",
                        "acctNo": "供应商的银行账号",
                        "factorAmount": 100.00,
                        "limtedAmount":1.00,
                        "transferAmount": 10.00,
                        "discountRate": 10.00,
                        "baseContName": "基础交易合同名称",
                        "baseContNo": "基础交易合同名称编号",
                        "baseContDate": time,
                        "baseContAmount": "",
                        "companyContracts": "闫学雷",
                        "companyPhone": "13810957727",
                        "companyEmail": "",
                        "vendorContracts": "闫学雷",
                        "vendorPhone": "13810957727",
                        "vendorEmail": "",
                        "extendJson": "",
                        "invoiceList": [
                            {
                                "invoiceNo": invoiceNo,
                                "invoiceAmount": 100.12,
                                "invoiceDate": time,
                                "noTaxAmount": 1,
                                "invoiceCode":invoiceCode,
                                "verifyCode": "",
                                "invoiceDistAmount": 1.11
                            }
                        ]
                    }
                ]}
)

def MD5():
    m = hashlib.md5()
    # Tips
    # 此处必须encode
    # 若写法为m.update(str)  报错为： Unicode-objects must be encoded before hashing
    # 因为python3里默认的str是unicode
    # 或者 b = bytes(str, encoding='utf-8')，作用相同，都是encode为bytes
    b = str.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()

    print('MD5加密前为 ：' + str)
    print('MD5加密后为小写 ：' + str_md5)

    # 另一种写法：b‘’前缀代表的就是bytes
    # str_md5 = hashlib.md5(b str).hexdigest()
    print('MD5加密后为大写 ：' + str_md5.upper())

def creatData():
    rc ={
        "apiType": apiType,
        "appId": appId,
        "dataStr":
            dataStr,
        "sign": "",
        "timestamp": seqNo
    }
    rcw = json.dumps(rc)
    print(rcw)
    return rcw

creatData()