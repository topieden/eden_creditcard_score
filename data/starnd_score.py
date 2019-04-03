#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 28/03/2019 19:18
# @Author  : Eden
# @File    : starnd_score.py
# @Software: PyCharm

import math
import pandas as pd

def AB(score_value,pdo,odds,d):
    '''
    :param score_value:  odds比率时，希望得分为score_value  给某个特定的比率设定特定的预期分值
    :param pdo:  当增加pdo分数时，odd比率会缩小一半（确定比率翻倍的分数）
    :param odds: 好坏比率odds=p（1-p）
    :         d  截距-0.6858382480252301	7

    :return:
    '''
    B=pdo/math.log(2)
    A=score_value-B*math.log(odds)

    # 基础分
    base = round(A + B * d , 0)
    print('基础分',base)

    return A,B
def strand_score(A,B,Score):
    '''
    :param A: 补偿分数
    :param B: 刻度
    :param Score: 区间分数
    :return: 该区间  1 没有风险的概率
    '''

    odds=math.exp((Score - A)/B)

    p=(odds/(1+odds))
    return p,odds


def score_bound(start,end,step):

    p_bound = []
    odds_bound = []
    score_i_bound=[]
    for score_i in range(start, end, step):


        p,odds = strand_score(A, B, score_i)
        p_bound.append(p)
        odds_bound.append(odds)
        score_i_bound.append(score_i)


    return p_bound,odds_bound,score_i_bound




#
# # 授信额度
# def credit_money(p1,start,end,step):
#     for score_i in range(start, end, step):
#         p, odds = strand_score(A, B, score_i)
#         p_bound.append(p)
#
#
#     for i in p_bound:
#
#         pmin=p_bound[i]
#
#         pmax=p_bound[i+1]
#         p0=(pmax+pmin)/2
#
#         if p1>p0:





if __name__ == '__main__':


    # score_value=100
    # pdo=25
    # odds=50
    #
    # A,B=AB(score_value,pdo,odds)
    # p_bound,odds_bound,score_i_bound=score_bound(-100,110,10)
    # print(p_bound,odds_bound,score_i_bound)
    #
    # p_bound=pd.DataFrame({'安全概率':p_bound})
    # odds_bound=pd.DataFrame({'odds':odds_bound})
    # score_i_bound=pd.DataFrame({'得分区间':score_i_bound})
    # df=[odds_bound,p_bound,score_i_bound]
    # data=pd.concat(df,axis=1)
    # print(data)
    #
    #
    # df=pd.DataFrame(data)
    # df.to_excel(r'F:\work\yongyou\建模分析\建模过程分析\stand_score2.xlsx')

    score_value=100
    pdo=-20
    odds=0.02
    d=-0.6858382480252301

    A,B=AB(score_value,pdo,odds,d)
    p_bound,odds_bound,score_i_bound=score_bound(-60,110,20)
    print(p_bound,odds_bound,score_i_bound)

    p_bound=pd.DataFrame({'违约概率':p_bound})
    odds_bound=pd.DataFrame({'odds':odds_bound})
    score_i_bound=pd.DataFrame({'得分':score_i_bound})
    df=[odds_bound,p_bound,score_i_bound]
    data=pd.concat(df,axis=1)
    print(data)


    df=pd.DataFrame(data)
    df.to_excel(r'F:\work\yongyou\建模分析\建模过程分析\stand_score3.xlsx')













