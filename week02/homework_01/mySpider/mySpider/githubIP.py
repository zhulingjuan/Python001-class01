
import requests
import json, random

def getIP():
    # 获取请求到的ip内容，一共有11页
    url = 'http://ip.jiangxianli.com/api/proxy_ips?page=' + str(random.randint(1,11))
    # 该获取ip接口 分页 为 1 到 11
    res = requests.get(url)
    # 每页有15条，随机取值
    ip = json.loads(res.content)['data']['data'][random.randint(0,14)].get('ip')
    print('代理ip-----------------------------------')
    print(ip) 
    print('-----------------------------------')
    return ip
    

   