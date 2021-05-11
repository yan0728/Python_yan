# -*- coding:utf-8 -*-
import os
from xlrd import open_workbook
# import cx_Oracle
# from xlutils.copy import copy
import requests
import json
import random
from datetime import date
import string
from xml.etree import ElementTree as ElementTree

#获取身份证号
def get_idcard(maxage=60, minage=20):
	#获取生日
	now = date.today()
	birth = now.year - int(minage)
	mon = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10', '11', '12']
	mon_days = ['31', '28', '31', '30', '31', '30', '31', '31','30', '31', '30', '31']
	age = int(maxage) - int(minage)
	y = str(birth - random.randint(1, age))
	index1 = random.randint(0, 11)
	m = str(mon[index1])
	m = m.zfill(2)
	maxDay = int(mon_days[index1])
	d = str(random.randint(1, maxDay))
	d = d.zfill(2)
	s = y + m + d
	area = ["11", "12", "13", "14", "15", "21", "22", "23", "31", "32", "33", "34", "35", "36", "37", "41", "42", "43", "44","45", "46", "50", "51", "52", "53", "54", "61", "62", "63", "64", "65", "71", "81", "82", "91"]
	id = random.choice(area)+''.join(random.choice(string.digits) for i in range(4))+s+''.join(random.choice(string.digits) for i in range(3))
	id = id[0:17]
	lid = list(id)
	temp = 0
	for nn in range(2, 19):
		a = int(lid[18 - nn])     # 17到1的数
		w = (2 ** (nn - 1)) % 11  # 17到1的系数
		temp += a * w             # temp = temp+a*w 17位数字和系数相乘的结果相加
	temp = (12 - temp % 11) % 11
	if temp >= 0 and temp <= 9:
		id += str(temp)
	elif temp == 10:
		id += 'X'
	return id
#print(get_idcard())
#获取汉字
def get_name(number):
	str1 = ""
	for i in range(number):
		head = random.randint(0xb0, 0xf7)
		body = random.randint(0xa1, 0xf9)
		val = f'{head:x}{body:x}'
		str = bytes.fromhex(val).decode('gb2312')
		str1 += str
	return str1
#print(get_name(3))
#获取手机号
def get_phone():
	prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",  "150", "151", "152", "153", "155", "156", "157", "158", "159", "186", "187", "188"]
	return random.choice(prelist)+''.join(random.choice(string.digits) for i in range(8))
#print(get_phone())
#生成随机数字
def get_number(number):
	s = ''.join(random.choice(string.digits) for i in range(number))
	return s
#print(get_number(1))
#生成银行卡号以及卡bin
def cardNum_generator():
	cardNum = ('622848003988779','621336023822255','622848116619772','622841043303913','622848015822079',
               '621226120200927','621226120200930','621226120200942','621226120200951','621226120200973',
               '621483759152','621483972193','621483972030','621483759166','621483388006','621483972375','621483714380','621483027573')
	cardBin = random.choice(cardNum)
	accountNo = cardBin + "".join(random.choice("0123456789") for i in range(4))
	correctCodes = ('622848003988779','621336023822255','622848116619772','622841043303913','622848015822079')
	correctCodes2 = ('621483759152','621483972193','621483972030','621483759166','621483388006','621483972375','621483714380','621483027573')
	correctCodes3 = ('621226120200927','621226120200930','621226120200942','621226120200951','621226120200973')
	if cardBin in correctCodes:
		carBin = 103
		return accountNo , carBin
	elif cardBin in correctCodes2:
		carBin = 308
		return accountNo , carBin
	elif cardBin in correctCodes3:
		carBin = 102
		return accountNo, carBin
	else :
		carBin = 100
		return accountNo , carBin
#生成银行卡号
def cardNo_generator():
	cardNo = ('622848003988779','621336023822255','622848116619772','622841043303913','622848015822079',
               '621226120200927','621226120200930','621226120200942','621226120200951','621226120200973',
               '621483759152','621483972193','621483972030','621483759166','621483388006','621483972375','621483714380','621483027573')
	cardBin = random.choice(cardNo)
	accountNo = cardBin + "".join(random.choice("0123456789") for i in range(4))
	return accountNo
#print(cardNo_generator())

def switch_window(self, win_no):
	base_win = self.driver.current_window_handle
	self.driver.switch_to.window(self.driver.window_handles[win_no])
	self.switched_windows.append(base_win)

def switch_back_windows(self, close=False):
	if close:
		self.driver.close()
	if ([] != self.switched_windows):
		self.driver.switch_to.window(self.switched_windows.pop())


def active_user():
	userList = ('13206790745','15159488457','14706987318','18660947873','15685575211',
				'13640964659','13927377746','13106553033','15895799757','','13669717216'
				  ,'18739682670','13963367851','18785458150','13510305706','13853803151','15845012807'
				,'13849750153','13404821366')
	name = ('蒙植黥','弊枭嚯','髑笾惩','吃订亟','扰挑芜','佰晒桊','邕箪举','蒙植黥','锣鸬熙','颜忿嘈',
				'摈累钉','苣巍捶','茕篡劢','酿熘援','谫辰敷','谒诓衩','筵麴作','幽咄楦','虮赝髹','淠崖匆')

