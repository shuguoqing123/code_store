#!/usr/bin/env python3
#-*-coding:utf-8-*-

from urllib import request
from urllib import parse
import urllib
import random

#基本用法，get请求
def test1():
    with open('result.txt','w') as f:
        resp = request.urlopen("https://www.baidu.com/")
        f.write(resp.read().decode("utf-8",'ignore'))

#模拟浏览器加上请求头
def test2():
    with open('result.txt','w') as f:
        req = request.Request("https://www.baidu.com/")
        req.add_header("User-Agent","Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:56.0) Gecko/20100101 Firefox/56.0")
        resp = request.urlopen(req)
        f.write(resp.read().decode("utf-8",'ignore'))

#post请求，携带请求信息，模拟登陆豆瓣
def test3():
    with open('result.txt','w') as f:
        postdata = parse.urlencode([
                ('source','index_nav'),
                ('form_email','183xxxx4860'),
                ('form_password','lixxxxx1001'),
                ])

        req =  request.Request("https://www.douban.com/login")
        req.add_header("User-Agent","Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:56.0) Gecko/20100101 Firefox/56.0")
        req.add_header("Host","www.douban.com")
        req.add_header("Content-Type","application/x-www-form-urlencoded")
        resp = request.urlopen(req,data=postdata.encode('utf-8'))
        f.write(resp.read().decode("utf-8",'ignore'))


#关于代理的使用。免费代理服务器，可以在这些网站中查找：
#http://www.xicidaili.com/
#http://www.youdaili.net/Daili/http/36812.html
#数据库维护一个ip池
#https://blog.csdn.net/lw_power/article/details/77946852#t0
def test4():
    proxy_list = [{"http" : "124.88.67.81:80"},
                  {"http" : "180.110.191.10:808"},
                  {"http" : "222.187.232.21:1080"},
                  {"http" : "180.110.19.215:808"},
                  {"http" : "114.82.109.134:8118"}]

    with open('result.txt','w') as f:
        proxy_addr = random.choice(proxy_list)
        proxy = urllib.request.ProxyHandler(proxy_addr)
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen("https://www.douban.com").read().decode('utf-8')
        f.write(data)
                            

#test1()
#test2()
#test3()
test4()
