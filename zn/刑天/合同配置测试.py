import requests
import json
import time

header_base = {'Content-Type': 'application/json;multipart/form-data;charset=UTF-8','User-Agent': 'Apache-HttpClient/4.5.5 (Java/1.8.0_121)'}
# 查询missionuuid脚本
'''
SELECT 
  UUID
FROM
  `test-contract`.`XtSignMission` 
WHERE productNo = 
  (SELECT 
    NO 
  FROM
    `test-finance`.`CoreProduct` 
  WHERE shortName = '全流程-1220-1')
'''
# 签署任务的uuid
missionuuid = '5af98968-0acd-4b11-99af-c8428a586ca5'
getdata2 = None
getdata3 = None
getdata4 = None
getdata5 = None
getdata6 = None
getdata7 = None
getdata8 = None
getdata9 = None
getdata11 = None
getdata12 = None
getdata13 = None
getdata14 = None
getdata15 = None


def logIn():
    url = 'https://test-api-xingtian.lianjieabs.com/entry/login'
    parameter = {"account":"13810957727","pwd":"3E10ADC3949BA59ABBE56E057F20F883E"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header_base)
    if r.json()["code"] == 'SUCCESS':
        ksid = r.json()["data"]["ksid"]
        print("登录成功 获取k-sid:" + ksid)
        return ksid
    else:
        print("刑天登录失败，失败原因：")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))

header = {'Content-Type': 'application/json;multipart/form-parameter;charset=UTF-8','User-Agent': 'Apache-HttpClient/4.5.5 (Java/1.8.0_121)','k-sid':logIn()}

# 查询合同模板
def getContractMode():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template/'+ missionuuid
    r = requests.get(url=url,data=None, headers=header)
    if r.json()["code"] == 'SUCCESS':
        getuuid = r.json()["data"][0]["uuid"]
        return getuuid
    else:
        print("获取合同模板失败，失败原因：")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
def uploadContractFile1():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/command/upload'
    parameter = {"uuid":"{}".format(getContractMode()),"fileOssPath":"TestContract/1-《保理业务合同》适用于原始债权人和原始权益人签署.docx"}

    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
      print("1-《保理业务合同》适用于原始债权人和原始权益人签署 上传完成")
    else:
        print("1-《保理业务合同》适用于原始债权人和原始权益人签署 上传失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))

#添加第2个合同
def getData2():
    global getdata2
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template'
    parameter = {"xtSignRoles":[],"missionUuid":"{}".format(missionuuid),"protocolType":"Sign","contractType":None,"contractName":"《应收账款转让登记协议》适用于原始债权人和原始权益人签署","no":"02"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        getdata2 = r.json()["data"]
        # return getdata
    else:
        print("获取data失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 配置第2个合同
def setContract2():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template/{}'.format(getdata2)
    parameter = {
        "xtSignRoles": [{"roleId": "Creditor", "roleType": "signer"}, {"roleId": "Original", "roleType": "signer"}],
        "missionUuid": "{}".format(missionuuid), "uuid": "{}".format(getdata2), "contractType": "business",
        "contractName": "《应收账款转让登记协议》适用于原始债权人和原始权益人签署", "no": "02"}

    r = requests.put(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        pass
    else:
        print("2-《应收账款转让登记协议》适用于原始债权人和原始权益人签署 配置失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 上传合同文件
def uploadContractFile2():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/command/upload'
    parameter = {"uuid":"{}".format(getdata2),
                 "fileOssPath":"TestContract/2-《应收账款转让登记协议》适用于原始债权人和原始权益人签署.docx"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        print("2-《应收账款转让登记协议》适用于原始债权人和原始权益人签署 配置并上传完成")

    else:
        print("2-《应收账款转让登记协议》适用于原始债权人和原始权益人签署 上传失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))

# 添加合同3
def getData3():
    global getdata3
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template'
    parameter = {"xtSignRoles":[],"missionUuid":"{}".format(missionuuid),"protocolType":"Sign","contractType":None,"contractName":"《应收账款转让通知书》适用于原始债权人向直接债务人出具","no":"03"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        getdata3 = r.json()["data"]
    else:
        print("获取data失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 配置第3个合同
def setContract3():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template/{}'.format(getdata3)
    parameter = {
        "xtSignRoles":[{"roleId":"Creditor","roleType":"notifier"},{"roleId":"DirectObligor","roleType":"receiver"}],
        "missionUuid":"{}".format(missionuuid),"uuid":"{}".format(getdata3),
        "contractType":"notification","contractName":"《应收账款转让通知书》适用于原始债权人向直接债务人出具","no":"03"}

    r = requests.put(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        pass
    else:
        print("3-《应收账款转让通知书》适用于原始债权人向直接债务人出具 配置失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 上传合同文件
def uploadContractFile3():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/command/upload'
    parameter = {"uuid":"{}".format(getdata3),
                 "fileOssPath":"TestContract/3-《应收账款转让通知书》适用于原始债权人向直接债务人出具.docx"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        print("3-《应收账款转让通知书》适用于原始债权人向直接债务人出具 配置并上传完成")

    else:
        print("3-《应收账款转让通知书》适用于原始债权人向直接债务人出具 上传失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))

# 添加合同4
def getData4():
    global getdata4
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template'
    parameter = {"xtSignRoles":[],"missionUuid":"{}".format(missionuuid),"protocolType":"Sign","contractType":None,"contractName":"《应收账款转让通知书回执》适用于直接债务人向原始债权人出具","no":"04"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        getdata4 = r.json()["data"]
    else:
        print("获取data失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 配置第4个合同
def setContract4():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template/{}'.format(getdata4)
    parameter = {"xtSignRoles": [{"roleId": "DirectObligor", "roleType": "notifier"},
                     {"roleId": "Creditor", "roleType": "receiver"}],
     "missionUuid": "{}".format(missionuuid), "uuid": "{}".format(getdata4),
     "contractType": "notification-receipt", "contractName": "《应收账款转让通知书回执》适用于直接债务人向原始债权人出具", "no": "04"}

    r = requests.put(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        pass
    else:
        print("4-《应收账款转让通知书回执》适用于直接债务人向原始债权人出具 配置失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 上传合同文件
def uploadContractFile4():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/command/upload'
    parameter = {"uuid":"{}".format(getdata4),
                 "fileOssPath":"TestContract/4-《应收账款转让通知书回执》适用于直接债务人向原始债权人出具.docx"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        print("4-《应收账款转让通知书回执》适用于直接债务人向原始债权人出具 配置并上传完成")

    else:
        print("4-《应收账款转让通知书回执》适用于直接债务人向原始债权人出具 上传失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))

# 添加合同5
def getData5():
    global getdata5
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template'
    parameter = {"xtSignRoles":[],"missionUuid":"{}".format(missionuuid),"protocolType":"Sign","contractType":None,"contractName":"《付款确认文件》适用于直接债务人向原始债权人出具","no":"05"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        getdata5 = r.json()["data"]
    else:
        print("获取data失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 配置第5个合同
def setContract5():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template/{}'.format(getdata5)
    parameter ={"xtSignRoles": [{"roleId": "DirectObligor", "roleType": "notifier"},
                     {"roleId": "Creditor", "roleType": "receiver"}],
     "missionUuid": "{}".format(missionuuid), "uuid": "{}".format(getdata5),
     "contractType": "notification", "contractName": "《付款确认文件》适用于直接债务人向原始债权人出具", "no": "05"}

    r = requests.put(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        pass
    else:
        print("5-《付款确认文件》适用于直接债务人向原始债权人出具 配置失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 上传合同文件
def uploadContractFile5():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/command/upload'
    parameter = {"uuid":"{}".format(getdata5),
                 "fileOssPath":"TestContract/5-《付款确认文件》适用于直接债务人向原始债权人出具.docx"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        print("5-《付款确认文件》适用于直接债务人向原始债权人出具 配置并上传完成")

    else:
        print("5-《付款确认文件》适用于直接债务人向原始债权人出具 上传失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))

# 添加合同6
def getData6():
    global getdata6
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template'
    parameter = {"xtSignRoles":[],"missionUuid":"{}".format(missionuuid),"protocolType":"Sign","contractType":None,"contractName":"《应收账款转让通知书》适用于原始债权人向共同债务人出具","no":"06"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        getdata6 = r.json()["data"]
    else:
        print("获取data失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 配置第6个合同
def setContract6():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template/{}'.format(getdata6)
    parameter ={"xtSignRoles": [{"roleId": "Creditor", "roleType": "notifier"},
                     {"roleId": "JointObligor", "roleType": "receiver"}],
     "missionUuid": "{}".format(missionuuid), "uuid": "{}".format(getdata6),
     "contractType": "notification", "contractName": "《应收账款转让通知书》适用于原始债权人向共同债务人出具", "no": "06"}

    r = requests.put(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        pass
    else:
        print("6-《应收账款转让通知书》适用于原始债权人向共同债务人出具 配置失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 上传合同文件
def uploadContractFile6():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/command/upload'
    parameter = {"uuid":"{}".format(getdata6),
                 "fileOssPath":"TestContract/6-《应收账款转让通知书》适用于原始债权人向共同债务人出具.docx"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        print("6-《应收账款转让通知书》适用于原始债权人向共同债务人出具 配置并上传完成")

    else:
        print("6-《应收账款转让通知书》适用于原始债权人向共同债务人出具 上传失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))

# 添加合同7
def getData7():
    global getdata7
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template'
    parameter = {"xtSignRoles":[],"missionUuid":"{}".format(missionuuid),"protocolType":"Sign","contractType":None,"contractName":"《应收账款转让通知书回执》适用于共同债务人向原始债权人出具","no":"07"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        getdata7 = r.json()["data"]
    else:
        print("获取data失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 配置第7个合同
def setContract7():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template/{}'.format(getdata7)

    parameter ={"xtSignRoles": [{"roleId": "JointObligor", "roleType": "notifier"},
                     {"roleId": "Creditor", "roleType": "receiver"}],
     "missionUuid": "{}".format(missionuuid), "uuid": "{}".format(getdata7),
     "contractType": "notification-receipt", "contractName": "《应收账款转让通知书回执》适用于共同债务人向原始债权人出具", "no": "07"}

    r = requests.put(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        pass
    else:
        print("7-《应收账款转让通知书回执》适用于共同债务人向原始债权人出具 配置失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 上传合同文件
def uploadContractFile7():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/command/upload'
    parameter = {"uuid":"{}".format(getdata7),
                 "fileOssPath":"TestContract/7-《应收账款转让通知书回执》适用于共同债务人向原始债权人出具.docx"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        print("7-《应收账款转让通知书回执》适用于共同债务人向原始债权人出具 配置并上传完成")

    else:
        print("7-《应收账款转让通知书回执》适用于共同债务人向原始债权人出具 上传失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))

# 添加合同8
def getData8():
    global getdata8
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template'
    parameter = {"xtSignRoles":[],"missionUuid":"{}".format(missionuuid),"protocolType":"Sign","contractType":None,
                 "contractName":"《付款确认文件》适用于共同债务人向原始债权人出具","no":"08"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        getdata8 = r.json()["data"]
    else:
        print("获取data失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 配置第8个合同
def setContract8():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template/{}'.format(getdata8)

    parameter ={"xtSignRoles": [{"roleId": "JointObligor", "roleType": "notifier"},
                     {"roleId": "Creditor", "roleType": "receiver"}],
     "missionUuid": "{}".format(missionuuid), "uuid": "{}".format(getdata8),
     "contractType": "notification", "contractName": "《付款确认文件》适用于共同债务人向原始债权人出具", "no": "08"}

    r = requests.put(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        pass
    else:
        print("8-《付款确认文件》适用于共同债务人向原始债权人出具 配置失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 上传合同文件
def uploadContractFile8():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/command/upload'
    parameter = {"uuid":"{}".format(getdata8),
                 "fileOssPath":"TestContract/8-《付款确认文件》适用于共同债务人向原始债权人出具.docx"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        print("8-《付款确认文件》适用于共同债务人向原始债权人出具 配置并上传完成")

    else:
        print("8-《付款确认文件》适用于共同债务人向原始债权人出具 上传失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))

# 添加合同9
def getData9():
    global getdata9
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template'
    parameter = {"xtSignRoles":[],"missionUuid":"{}".format(missionuuid),"protocolType":"Sign","contractType":None,
                 "contractName":"《应收账款转让通知书》适用于原始权益人向直接债务人出具","no":"09"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        getdata9 = r.json()["data"]
    else:
        print("获取data失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 配置第9个合同
def setContract9():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template/{}'.format(getdata9)

    parameter ={"xtSignRoles": [{"roleId": "Original", "roleType": "notifier"},
                     {"roleId": "DirectObligor", "roleType": "receiver"}],
     "missionUuid": "{}".format(missionuuid), "uuid": "{}".format(getdata9),
     "contractType": "notification", "contractName": "《应收账款转让通知书》适用于原始权益人向直接债务人出具", "no": "09"}

    r = requests.put(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        pass
    else:
        print("9-《应收账款转让通知书》适用于原始权益人向直接债务人出具 配置失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 上传合同文件
def uploadContractFile9():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/command/upload'
    parameter = {"uuid":"{}".format(getdata9),
                 "fileOssPath":"TestContract/9-《应收账款转让通知书》适用于原始权益人向直接债务人出具.docx"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        print("9-《应收账款转让通知书》适用于原始权益人向直接债务人出具 配置并上传完成")

    else:
        print("9-《应收账款转让通知书》适用于原始权益人向直接债务人出具 上传失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))

# 添加合同11
def getData11():
    global getdata11
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template'
    parameter = {"xtSignRoles":[],"missionUuid":"{}".format(missionuuid),"protocolType":"Sign","contractType":None,
                 "contractName":"《付款确认文件》适用于直接债务人向原始权益人出具","no":"11"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        getdata11 = r.json()["data"]
    else:
        print("获取data失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 配置第11个合同
def setContract11():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template/{}'.format(getdata11)

    parameter ={"xtSignRoles": [{"roleId": "DirectObligor", "roleType": "notifier"},
                     {"roleId": "Original", "roleType": "receiver"}],
     "missionUuid": "{}".format(missionuuid), "uuid": "{}".format(getdata11),
     "contractType": "notification", "contractName": "《付款确认文件》适用于直接债务人向原始权益人出具", "no": "11"}

    r = requests.put(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        pass
    else:
        print("11-《付款确认文件》适用于直接债务人向原始权益人出具 配置失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 上传合同文件
def uploadContractFile11():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/command/upload'
    parameter = {"uuid":"{}".format(getdata11),
                 "fileOssPath":"TestContract/11-《付款确认文件》适用于直接债务人向原始权益人出具.docx"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        print("11-《付款确认文件》适用于直接债务人向原始权益人出具 配置并上传完成")

    else:
        print("11-《付款确认文件》适用于直接债务人向原始权益人出具 上传失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))

# 添加合同12
def getData12():
    global getdata12
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template'
    parameter = {"xtSignRoles":[],"missionUuid":"{}".format(missionuuid),"protocolType":"Sign","contractType":None,
                 "contractName":"《应收账款转让通知书》适用于原始权益人向共同债务人出具","no":"12"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        getdata12 = r.json()["data"]
    else:
        print("获取data失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 配置第12个合同
def setContract12():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template/{}'.format(getdata12)

    parameter = {"xtSignRoles": [{"roleId": "Original", "roleType": "notifier"},
                     {"roleId": "JointObligor", "roleType": "receiver"}],
     "missionUuid": "{}".format(missionuuid), "uuid": "{}".format(getdata12),
     "contractType": "notification", "contractName": "《应收账款转让通知书》适用于原始权益人向共同债务人出具", "no": "12"}

    r = requests.put(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        pass
    else:
        print("12-《应收账款转让通知书》适用于原始权益人向共同债务人出具 配置失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 上传合同文件
def uploadContractFile12():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/command/upload'
    parameter = {"uuid":"{}".format(getdata12),
                 "fileOssPath":"TestContract/12-《应收账款转让通知书》适用于原始权益人向共同债务人出具.docx"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        print("12-《应收账款转让通知书》适用于原始权益人向共同债务人出具 配置并上传完成")

    else:
        print("12-《应收账款转让通知书》适用于原始权益人向共同债务人出具 上传失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))

# 添加合同13
def getData13():
    global getdata13
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template'
    parameter = {"xtSignRoles":[],"missionUuid":"{}".format(missionuuid),"protocolType":"Sign","contractType":None,
                 "contractName":"《应收账款转让通知书回执》适用于共同债务人向原始权益人出具","no":"13"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        getdata13 = r.json()["data"]
    else:
        print("获取data失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 配置第13个合同
def setContract13():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template/{}'.format(getdata13)

    parameter ={"xtSignRoles": [{"roleId": "JointObligor", "roleType": "notifier"},
                     {"roleId": "Original", "roleType": "receiver"}],
     "missionUuid": "{}".format(missionuuid), "uuid": "{}".format(getdata13),
     "contractType": "notification-receipt", "contractName": "《应收账款转让通知书回执》适用于共同债务人向原始权益人出具", "no": "13"}
    r = requests.put(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        pass
    else:
        print("13-《应收账款转让通知书回执》适用于共同债务人向原始权益人出具 配置失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 上传合同文件
def uploadContractFile13():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/command/upload'
    parameter = {"uuid":"{}".format(getdata13),
                 "fileOssPath":"TestContract/13-《应收账款转让通知书回执》适用于共同债务人向原始权益人出具.docx"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        print("13-《应收账款转让通知书回执》适用于共同债务人向原始权益人出具 配置并上传完成")

    else:
        print("13-《应收账款转让通知书回执》适用于共同债务人向原始权益人出具 上传失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))

# 添加合同14
def getData14():
    global getdata14
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template'
    parameter = {"xtSignRoles":[],"missionUuid":"{}".format(missionuuid),"protocolType":"Sign","contractType":None,
                 "contractName":"《付款确认文件》适用于共同债务人向原始权益人出具","no":"14"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        getdata14 = r.json()["data"]
    else:
        print("获取data失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 配置第14个合同
def setContract14():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template/{}'.format(getdata14)

    parameter ={"xtSignRoles": [{"roleId": "JointObligor", "roleType": "notifier"},
                     {"roleId": "Original", "roleType": "receiver"}],
     "missionUuid": "{}".format(missionuuid), "uuid": "{}".format(getdata14),
     "contractType": "notification", "contractName": "《付款确认文件》适用于共同债务人向原始权益人出具", "no": "14"}

    r = requests.put(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        pass
    else:
        print("14-《付款确认文件》适用于共同债务人向原始权益人出具 配置失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 上传合同文件
def uploadContractFile14():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/command/upload'
    parameter = {"uuid":"{}".format(getdata14),
                 "fileOssPath":"TestContract/14-《付款确认文件》适用于共同债务人向原始权益人出具.docx"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        print("14-《付款确认文件》适用于共同债务人向原始权益人出具 配置并上传完成")

    else:
        print("14-《付款确认文件》适用于共同债务人向原始权益人出具 上传失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))

# 添加合同15
def getData15():
    global getdata15
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template'
    parameter = {"xtSignRoles":[],"missionUuid":"{}".format(missionuuid),"protocolType":"Cancel","contractType":None,
                 "contractName":"《解除合同协议》适用于原始债权人和原始权益人签署","no":"15"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        getdata15 = r.json()["data"]
    else:
        print("获取data失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 配置第15个合同
def setContract15():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/entity/template/{}'.format(getdata15)

    parameter ={"xtSignRoles": [{"roleId": "Creditor", "roleType": "notifier"}, {"roleId": "Original", "roleType": "receiver"}],
     "missionUuid": "{}".format(missionuuid), "uuid": "{}".format(getdata15),
     "contractType": "notification", "contractName": "《解除合同协议》适用于原始债权人和原始权益人签署", "no": "15"}

    r = requests.put(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        pass
    else:
        print("15-《解除合同协议》适用于原始债权人和原始权益人签署 配置失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
# 上传合同文件
def uploadContractFile15():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/command/upload'
    parameter = {"uuid":"{}".format(getdata15),
                 "fileOssPath":"TestContract/15-《解除合同协议》适用于原始债权人和原始权益人签署.docx"}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        print("15-《解除合同协议》适用于原始债权人和原始权益人签署 配置并上传完成")

    else:
        print("15-《解除合同协议》适用于原始债权人和原始权益人签署 上传失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))

def checkMission():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/command/check/mission'
    parameter = {"signMissionUuid":"{}".format(missionuuid)}
    r = requests.post(url=url, data=json.dumps(parameter), headers=header)
    if r.json()["code"] == "SUCCESS":
        print("验证成功,请进入页面继续完成后续操作")
        print("https://test-api-xingtian.lianjieabs.com/entry/login")
    else:
        print("提交失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))

def checkPassMission():
    url = 'https://test-api-xingtian.lianjieabs.com/xingtian/contract/preview/command/check-pass/mission/{}'.format(missionuuid)
    r = requests.get(url=url, data=None, headers=header)
    if r.json()["code"] == "SUCCESS":
        print("提交中，请进入页面继续完成后续操作")
        print("https://test-api-xingtian.lianjieabs.com/entry/login")
    else:
        print("提交失败")
        print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))


#上传1-《保理业务合同》适用于原始债权人和原始权益人签署
uploadContractFile1()
time.sleep(1)
#配置2-《应收账款转让登记协议》适用于原始债权人和原始权益人签署
getData2()
setContract2()
uploadContractFile2()
time.sleep(1)
# 配置3-《应收账款转让通知书》适用于原始债权人向直接债务人出具
getData3()
setContract3()
uploadContractFile3()
time.sleep(1)
# 配置4-《应收账款转让通知书回执》适用于直接债务人向原始债权人出具
getData4()
setContract4()
uploadContractFile4()
time.sleep(1)
# 配置5-《付款确认文件》适用于直接债务人向原始债权人出具
getData5()
setContract5()
uploadContractFile5()
time.sleep(1)
# 配置6-《应收账款转让通知书》适用于原始债权人向共同债务人出具
getData6()
setContract6()
uploadContractFile6()
time.sleep(1)
# 配置7-《应收账款转让通知书回执》适用于共同债务人向原始债权人出具
getData7()
setContract7()
uploadContractFile7()
time.sleep(1)
# 配置8-《付款确认文件》适用于共同债务人向原始债权人出具
getData8()
setContract8()
uploadContractFile8()
time.sleep(1)
# 配置9-《应收账款转让通知书》适用于原始权益人向直接债务人出具
getData9()
setContract9()
uploadContractFile9()
time.sleep(1)
# 配置11-《付款确认文件》适用于直接债务人向原始权益人出具
getData11()
setContract11()
uploadContractFile11()
time.sleep(1)
# 配置12-《付款确认文件》适用于直接债务人向原始权益人出具
getData12()
setContract12()
uploadContractFile12()
time.sleep(1)
# 配置13-《应收账款转让通知书回执》适用于共同债务人向原始权益人出具
# getData13()
# setContract13()
# uploadContractFile13()
#
# # 配置14-《付款确认文件》适用于共同债务人向原始权益人出具
# getData14()
# setContract14()
# uploadContractFile14()

# 配置15-《解除合同协议》适用于原始债权人和原始权益人签署
getData15()
setContract15()
uploadContractFile15()

# 验证
# checkMission()
#
#提交
# checkPassMission()


