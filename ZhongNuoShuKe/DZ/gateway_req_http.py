import hashlib
import json
import time
import random
import requests

ascii_number_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                      "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                      "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4",
                      "5", "6", "7", "8", "9", "0"]
content_type_json = 'application/json;charset=UTF-8'
content_type_file = 'multipart/form-data;boundary=1000'


def gen_request_id():
    random_list = []
    for i in range(32):
        random_list.append(random.choice(ascii_number_chars))
    return ''.join(random_list)


def req_http(app_id, app_key, security_key, req_content_type, request_body, request_path, method):
    split = '::'
    if req_content_type != content_type_json:
        content_md5 = hashlib.md5(''.encode("UTF-8")).hexdigest()
    else:
        content_md5 = hashlib.md5(request_body.encode("UTF-8")).hexdigest()
    timestamp = int(round(time.time() * 1000))
    request_id = gen_request_id()
    print('X-Zn-Open-App-Id:', app_id)
    print('X-Zn-Open-App-Key:', app_key)
    print('X-Zn-Content-MD5:', content_md5)
    print('Content-Type:', req_content_type)
    print('X-Zn-Open-Request-Id:', request_id)
    print('X-Zn-Open-Timestamp:', timestamp)
    if req_content_type != content_type_json:
        temp_sign = app_id + split + app_key + split + request_id + split + split + str(
            timestamp) + split + method + split + request_path + split + req_content_type + split + security_key
    else:
        temp_sign = app_id + split + app_key + split + request_id + split + content_md5 + split + str(
            timestamp) + split + method + split + request_path + split + req_content_type + split + security_key
    md = hashlib.md5()
    md.update(temp_sign.encode('utf-8'))
    sign = md.hexdigest()
    print('X-Zn-Open-Signature:', sign)
    headers = {
        'X-Zn-Open-App-Id': app_id,
        'X-Zn-Open-App-Key': app_key,
        'X-Zn-Content-MD5': content_md5,
        'Content-Type': req_content_type,
        'X-Zn-Open-Request-Id': request_id,
        'X-Zn-Open-Timestamp': str(timestamp),
        'X-Zn-Open-Signature': sign,
    }
    # 网关的基础地址
    base_url = 'http://123.57.27.89'
    response = requests.post(url=base_url + request_url, data=request_body.encode(), headers=headers)
    print(json.dumps(response.json(), sort_keys=True, indent=2, ensure_ascii=False))


# 请求体，复制时不要换行
body = '{"minutes":2,"content":"尊敬的用户您好，您正在进行修改个人账号，验证码为【变量】，有效时间15分钟，验证通过即可修改，请勿向他人泄露","phone":"13260283502"}'
# 请求地址
request_url = '/sms/send-code'
# 请求类型 content_type_json为json格式 content_type_file为文件格式
content_type = content_type_json
req_http('qingdao-yeda', 'AhgfP0GF2KpD9J4bV3TExRORpwVeKnuY',
         'H4xJmjwsU0ZcEEBuCvxodMMBENyovncH9spdO8VOffxPDpzK5Sigod0g6pLe6nUW', content_type, body,
         request_url, 'POST')
