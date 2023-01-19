import hashlib
import time
import random

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


def gen_header(app_id, app_key, security_key, content_type, request_body, request_path, method):
    split = '::'
    if content_type != content_type_json:
        content_md5 = hashlib.md5(''.encode(encoding="UTF-8")).hexdigest()
    else:
        content_md5 = hashlib.md5(request_body.encode(encoding="UTF-8")).hexdigest()
    timestamp = int(round(time.time() * 1000))
    request_id = gen_request_id()
    print('X-Zn-Open-App-Id:', app_id)
    print('X-Zn-Open-App-Key:', app_key)
    print('X-Zn-Content-MD5:', content_md5)
    print('Content-Type:', content_type)
    print('X-Zn-Open-Request-Id:', request_id)
    print('X-Zn-Open-Timestamp:', timestamp)
    temp_sign = ''
    if content_type != content_type_json:
        temp_sign = app_id \
                    + split + app_key \
                    + split + request_id \
                    + split \
                    + split + str(timestamp) \
                    + split + method \
                    + split + request_path \
                    + split + content_type \
                    + split + security_key
    else:
        temp_sign = app_id \
                    + split + app_key \
                    + split + request_id \
                    + split + content_md5 \
                    + split + str(timestamp) \
                    + split + method \
                    + split + request_path \
                    + split + content_type \
                    + split + security_key
    print(temp_sign)
    md = hashlib.md5()
    md.update(temp_sign.encode('utf-8'))
    sign = md.hexdigest()
    print('X-Zn-Open-Signature:', sign)


# 请求体，复制时不要换行
body = '{"phone":"02810957721","sequence":"92652883","code":"167916"}'
# 请求地址
request_url = '/sms/validate/beforehand'
# 请求类型 content_type_json为json格式 content_type_file为文件格式
content_type = content_type_json
gen_header('qingdao-yeda', 'AhgfP0GF2KpD9J4bV3TExRORpwVeKnuY',
           'H4xJmjwsU0ZcEEBuCvxodMMBENyovncH9spdO8VOffxPDpzK5Sigod0g6pLe6nUW', content_type, body,
           request_url, 'POST')
