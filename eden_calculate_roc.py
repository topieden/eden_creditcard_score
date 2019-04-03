#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 01/04/2019 09:59
# @Author  : Eden
# @File    : eden_calculate_roc.py
# @Software: PyCharm




# -*- coding: utf-8 -*-
import numpy as np

############计算ROC需要的库函数#############
from sklearn.model_selection import cross_validate
from sklearn import metrics
from sklearn import svm
import matplotlib.pyplot as plt

#############计算fpr,tpr##################
##y是一个一维数组（样本的真实分类），数组值表示类别（一共有两类，1和2），人工标注，属于测试集的真实分类
##score即各个样本属于正例的概率；是网络的输出；首先用训练集训练网络，然后利用测试集的数据产生的
##fpr, tpr是ROC的横纵坐标
##thresholds是截断阈值
y = np.array([1, 1, 2, 2])
scores = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, thresholds = metrics.roc_curve(y, scores, pos_label=2)


# 截断的解释，是我们认为的选定，一个阈值，如果大于这个阈值就属于正例，如果小于这个阈值就属于负例，
# 这里auc 可以判断哪一我们的模型是否具有区分能力，

# 而ks 既可以给我们区分能力，也可以给我们到底阈值的thresholds的区分能力最大，使得TPR  FPR
print(thresholds)

#############画图##################
plt.title('ROC')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.plot(fpr, tpr, '--*b', label="tuli")
plt.legend()
plt.show()

import numpy as np
from sklearn.metrics import roc_curve

y = np.array([1,1,2,2])
pred = np.array([0.1,0.4,0.35,0.8])
fpr, tpr, thresholds = roc_curve(y, pred, pos_label=2)
print(fpr)
print(tpr)
print(thresholds)

from sklearn.metrics import auc
print(auc(fpr, tpr))
