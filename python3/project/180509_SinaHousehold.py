'''
新浪家居装修论坛爬虫
2018/05/09
'''
from urllib import request
from urllib import parse
import urllib


req = request.Request('http://bbs.jiaju.com')
rep = request.urlopen(req)
open('debug.txt','w',encoding='utf-8').write(rep.read().decode('gbk','ignore').encode('utf-8').decode('utf-8'))

