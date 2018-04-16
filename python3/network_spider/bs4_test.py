#!/usr/bin/env python3
#-*-coding:utf-8-*-

from bs4 import BeautifulSoup


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#使用BeautifulSoup上面的代码,能够得到一个 BeautifulSoup 的对象,并能按照标准的缩进格式的结构输出
def test1():
    #html.parser--python内置解析器，执行速度适中，文档容错能力强，但是python2.7.3或3.2.2之前的版本支持不太好，容错能力差。
    soup = BeautifulSoup(html_doc,'html.parser')
    print(soup.prettify())

    #lxml HTML解析器，执行速度快，容错能力强，但需要安装C语言库
    soup = BeautifulSoup(html_doc,'lxml')
    print(soup.prettify())
    
    #lxml XML解析器，速度快唯一支持xml的解析器，需要安装C语言库
    soup = BeautifulSoup(html_doc,'lxml-xml')
    print(soup.prettify())
    
    #最好的容错性，以浏览器的方式解析文档生成html5格式，速度慢，不依赖外部扩展
    soup = BeautifulSoup(html_doc,'html5lib')
    print(soup.prettify())


#BeautifulSoup对象常用方法
def test2(): 
    soup = BeautifulSoup(html_doc,'html.parser')
    print(soup.title)#获取title标签
    print(soup.title.name)#title标签的name
    print(soup.title.string)#title标签里的内容
    print(soup.title.parent.name)#title标签的父标签的内容
    print(soup.p)#获取第一个p标签
    print(soup.p['class'])#第一个p标签的class属性的值
    print(soup.a)#第一个a标签
    print(soup.find_all('a'))


#post请求，携带请求信息，模拟登陆豆瓣
def test3():
    pass

#test1()
test2()

#test3()
