import requests

r=requests.get('http://t.weather.itboy.net/api/weather/city/101250101')
response_data=r.json()
print(response_data)

#获取日期，响应信息，状态，城市
print(response_data['date'])
print(response_data['message'])
print(response_data['status'])
print(response_data['cityInfo']['city'])

#获取当日天气具体信息
print(response_data['data']['forecast'][0]['ymd'])
print(response_data['data']['forecast'][0]['type'])
print(response_data['data']['forecast'][0]['high'])
print(response_data['data']['forecast'][0]['low'])