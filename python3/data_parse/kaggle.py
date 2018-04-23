#!/usr/bin/env python3
#-*-coding:utf-8-*-

from __future__ import division#小数不约为0
import pandas as pd#矩阵操作
import numpy as np#向量操作
from scipy import stats#数学计算

'''
数据诊断的统计指标
1.均值/中位数/最大值/最小值等
2.计数类
3.缺失值/方差等
4.分位点/值的频数等
'''


#数据读取
df = pd.read_csv('train.csv')
label = df['MSSubClass']
df =df.drop(['Id','MSSubClass'],axis=1)


#基本描述统计-计数类
missSet=[np.nan,9999999999,-999999]#缺失值

print(len(df.iloc[:,0].unique()))
count_un = df.iloc[:,0:3].apply(lambda x:len(x.unique()))
print(count_un)

print(np.sum(df.iloc[:,0] ==0))
count_zero = df.iloc[:,0:3].apply(lambda x:np.sum(x==0))
print(count_zero)
