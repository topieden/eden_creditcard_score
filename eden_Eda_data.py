#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 01/04/2019 15:18
# @Author  : Eden
# @File    : eden_Eda_data.py
# @Software: PyCharm

import pandas as pd

from scipy import stats

data=pd.read_csv('F:/work/yongyou/data/bigdata_finance.pai_nightkeysclass_test.csv')
print(data.describe())

# 求众数

# num=data['d1classifier']
num1=stats.mode(data['d1classifier'])[0][0]
print(num1)

data_sort=data['d1classifier'].sort_index
print(data_sort)

data2=data=pd.read_csv('F:/work/yongyou/data/bigdata_finance.pai_nightkeysclass_test2.csv')

num2=stats.mode(data2['d1classifier'])[0][0]
print(num2)


data3=pd.read_csv(r'F:\work\yongyou\data\bigdata_finance.eden_prediction_score.csv')

num3=stats.mode(data3['prediction_score'])[0][0]
print(num3)


