# -*- coding = utf-8 -*-
"""
作者：WandererX

时间：2021年02月24日  11:03:02
"""

import urllib.request

#获取y一个get请求
# response=urllib.request.urlopen('https://www.baidu.com')
# print(response.read().decode('utf-8'))  #用utf-8解析二进制文本文件

#获取一个post请求
# import urllib.parse #解析
# list=bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
# #bytes:转换为二进制形式     字典用数组封装
# response=urllib.request.urlopen('http://httpbin.org/post',data=list)
# print(response.read().decode('utf-8'))


#超时处理 一般3-5s
# try:
#     response=urllib.request.urlopen('http://httpbin.org/get',timeout=1)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print('time out!')


#伪装
# url='http://httpbin.org/get'
# headers={
# 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4168.3 Mobile Safari/537.36'
# }
# list=bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
# req=urllib.request.Request(data=list,url=url,headers=headers,method='POST')
# response=urllib.request.urlopen(req)    #将一个对象封装好进行参数的传递
# print(response.read().decode('utf-8'))
# #报错了。。urllib.error.HTTPError: HTTP Error 405: METHOD NOT ALLOWED


#尝试一下访问豆瓣
url='https://www.douban.com'
headers={
'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4168.3 Mobile Safari/537.36'
}
req=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(req)
print(response.read().decode('utf-8'))









