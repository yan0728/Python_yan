import urllib, urllib2, time, json, cookielib

url3 = 'https://www.wanglibao.com/yunying/rpc'
url4 = 'https://www.wanglibao.com/passport/service.php?c=account'

#url3 = 'https://php1.wanglibao.com/yunying/rpc'
#url4 = 'https://php1.wanglibao.com/passport/service.php?c=account'

loginparm = {
    "jsonrpc": "2.0",
    "method": "signin",
    "params": [
        {
            "username": "13810957727",
            "password": "123456"
        }
    ],
    "id":1
}


rockparms = {
    "id":1,
    "jsonrpc":"2.0",
    "method":"signInSystemDraw",
    "params":[]
}

def Login(url, parm):
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    h = urllib2.urlopen(url)

    body_value = json.JSONEncoder().encode(parm)
    request = urllib2.Request(url, body_value)
    result = urllib2.urlopen(request).read()
    return result

Login(url4, loginparm)

def Rock(url, parm):
    body_value = json.JSONEncoder().encode(parm)
    request = urllib2.Request(url, body_value)
    # request.add_header('set-cookie', 'WANGLIBAO_TOKEN=7ms8fmsh62jmv0n6iap0f62r73')
    result = urllib2.urlopen(request).read()
    return result

a = 1
while a < 300:
    #print Rock(url3, rockparms)
    Rock(url3,rockparms)
    time.sleep(3.2)
    a += 1
    # print a

