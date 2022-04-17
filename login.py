import requests

# 在这输入账号密码
user = ""
password = ""


url = "http://172.19.12.51/eportal/InterFace.do?method=login"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "972",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "172.19.12.51",
    "Origin": "http://172.19.12.51",
    "Referer": "http://172.19.12.51/eportal/index.jsp?wlanuserip=142de391c67f618cb5ddbb6634a7f625&wlanacname=c7ddbc656907fe2bea63172c004e0e66&ssid=&nasip=271f5e5e3a8ca7057aa6b2d761215d0a&snmpagentip=&mac=0ae5a1555fcea2846f9af616666431b4&t=wireless-v2&url=2c0328164651e2b4f13b933ddf36628bea622dedcc302b30&apmac=&nasid=c7ddbc656907fe2bea63172c004e0e66&vid=bcfe2cf728fa0228&port=9bdeca5efa34f87c&nasportid=f5eb983692924fa26e6431fe9df4835fc71979d9799e25fca13ee498c3e1e61771ec4385071ff036b3ab40b9e497a52d",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
}

data = {
    "userId": user,
    "password": password,
    "service": "%E6%9C%89%E7%BA%BF%E6%9C%8D%E5%8A%A1",
    "queryString": "wlanuserip%3D142de391c67f618cb5ddbb6634a7f625%26wlanacname%3Dc7ddbc656907fe2bea63172c004e0e66%26ssid%3D%26nasip%3D271f5e5e3a8ca7057aa6b2d761215d0a%26snmpagentip%3D%26mac%3D0ae5a1555fcea2846f9af616666431b4%26t%3Dwireless-v2%26url%3D2c0328164651e2b4f13b933ddf36628bea622dedcc302b30%26apmac%3D%26nasid%3Dc7ddbc656907fe2bea63172c004e0e66%26vid%3Dbcfe2cf728fa0228%26port%3D9bdeca5efa34f87c%26nasportid%3Df5eb983692924fa26e6431fe9df4835fc71979d9799e25fca13ee498c3e1e61771ec4385071ff036b3ab40b9e497a52d",
    "passwordEncrypt": "false",
}

response = requests.post(url=url, data=data, headers=headers)
