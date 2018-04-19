#!/usr/bin/env python3
#-*-coding:utf-8-*-

#python 列表的用法


#1.添加元素的三种方法
def test1():
    member = ["牡丹","月季","玫瑰","蔷薇","杜鹃","菊花"]
    print(member)

    member.append("夹竹桃")#单个元素添加到列表结尾
    print(member)
    #['牡丹', '月季', '玫瑰', '蔷薇', '杜鹃', '菊花', '夹竹桃']

    member.extend(["向日葵","荷花"])#将另一个列表扩展列表结尾
    print(member)
    #['牡丹', '月季', '玫瑰', '蔷薇', '杜鹃', '菊花', '夹竹桃', '向日葵', '荷花']

    member.insert(1,"桂花")#将单个元素添加到指定的下标位置
    print(member)
    #['牡丹', '桂花', '月季', '玫瑰', '蔷薇', '杜鹃', '菊花', '夹竹桃', '向日葵', '荷花']


#2.删除元素的三种方法
def test2():
    member = ["牡丹","月季","玫瑰","蔷薇","杜鹃","菊花"]
    print(member)
    #['牡丹', '月季', '玫瑰', '蔷薇', '杜鹃', '菊花']

    member.remove("蔷薇")#删除已知的元素
    print(member)
    #['牡丹', '月季', '玫瑰', '杜鹃', '菊花']

    mem = member.pop()#弹出最后一个元素，
    print(member,mem)
    #['牡丹', '月季', '玫瑰', '杜鹃'] 菊花

    mem = member.pop(2)#弹出指定下标的元素
    print(member,mem)
    #['牡丹', '月季', '杜鹃'] 玫瑰
    
    del member#删除整个列表，列表对象也不存在了


#3.其他常用方法
def test3():
    #计算5出现的次数
    list1 = [1,3,3,4,5,9,2,6,7,0,8,16,22,10,5]
    print(list1.count(5))
    #2

    #0第一次出现的位置
    i = list1.index(0)
    print(i)
    #9

    #排序，从大到小
    list1.sort()
    print(list1)
    #[0, 1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 10, 16, 22]

    #倒序
    list1.reverse()
    print(list1)
    #[22, 16, 10, 9, 8, 7, 6, 5, 5, 4, 3, 3, 2, 1, 0]

    #倒序排序
    list1.sort(reverse=True)
    print(list1)
    #[22, 16, 10, 9, 8, 7, 6, 5, 5, 4, 3, 3, 2, 1, 0]

    #列表拷贝
    list2 = list1[:]
    print(list2)
    #[22, 16, 10, 9, 8, 7, 6, 5, 5, 4, 3, 3, 2, 1, 0]



#test1()    
#test2()
test3()

