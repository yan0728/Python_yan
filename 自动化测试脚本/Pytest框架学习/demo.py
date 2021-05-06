import requests

def test_demo(base_url):
    resp = requests.get(base_url)
    status_code = resp.status_code
    if status_code == 200 :
        print(resp.text)
    else:
        print("<<<失败>>>")
