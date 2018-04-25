#!/usr/bin/env python3
#-*-coding:utf-8-*-
'''
不同操作系统底层实现不同，文件系统不同
os模块可以帮助我们屏蔽操作系统的差异
'''
import os

print(os.getcwd())#返回当前目录，脚本所在目录
os.chdir('/home/shuguoqing')#改变工作目录，相当于cd命令
print(os.getcwd())#工作目录被改变

print(os.listdir('.'))#列出目录下所有文件和目录
os.mkdir('new')#在工作目录下新建一个目录
os.makedirs('new/a/b')#在工作目录下新建多层目录

os.chdir('new/a/b')
f = open('test.txt','w')#在工作目录下新建txt文件

os.rename('test.txt','test1.txt')#重命名文件
os.remove('test1.txt')#删除文件
os.chdir('../')
os.rmdir('b')#删除非空目录，里面有子目录和文件都会抛出异常
os.chdir('../../')
os.removedirs('new/a')#从子目录开始，往回递归逐层删除多层目录，有子目录和文件抛出异常

os.system('ls -l /home/shuguoqing/workspace/code_store/python3/base')#执行shell命令

print(os.curdir)#常量，当前目录符
print(os.pardir)#常量，上级目录符
print(os.sep)#常量，路径分隔符，windows下为'\\',linux下为'/'
print(os.linesep)#常量，当前系统的换行符
print(os.name)#常量，系统名,linux为'posix',windows为'nt'


print(os.path.basename('/home/shuguoqing/workspace/code_store/python3/base/os.py'))#去掉路径，保留文件名
print(os.path.dirname('/home/shuguoqing/workspace/code_store/python3/base/os.py'))#去掉文件名，保留路径

print(os.path.join('/home/shuguoqing','workspace/code_store','python3/base'))#拼接路径


print(os.path.split('/home/shuguoqing/workspace/code_store/python3/base/os.py'))#分割文件路径的路径和文件名，返回元组
print(os.path.splitext('/home/shuguoqing/workspace/code_store/python3/base/os.py'))#分割文件的文件名和后缀，返回元组

print(os.path.getsize('/home/shuguoqing/workspace/code_store/python3/base/os.py'))#获取文件大小，单位字节
import time
print(time.localtime(os.path.getctime('/home/shuguoqing/workspace/code_store/python3/base/os.py')))#获取文件创建时间
print(time.localtime(os.path.getatime('/home/shuguoqing/workspace/code_store/python3/base/os.py')))#获取文件访问时间
print(time.localtime(os.path.getmtime('/home/shuguoqing/workspace/code_store/python3/base/os.py')))#获取文件修改时间


print(os.path.exists('/home/shuguoqing/workspace/code_store/python3/base/os.py'))#判断是否存在文件
print(os.path.isabs('/home/shuguoqing/workspace/code_store/python3/base/os.py'))#判断是否是绝对路径
print(os.path.isdir('/home/shuguoqing/workspace/code_store/python3/base/os.py'))#判断是否是目录
print(os.path.isfile('/home/shuguoqing/workspace/code_store/python3/base/os.py'))#判断是否是文件








