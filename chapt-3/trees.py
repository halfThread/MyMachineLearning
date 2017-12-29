#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@version: 
@author: lh
@license: Apache Licence 
@contact: liuhuan0672@gmail.com
@site: 
@software: PyCharm
@file: trees.py
@time: 2017/12/29 14:51
"""

from math import log


# 计算给定数据集的熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}  # 统计数据集的所有分类数
    for featVec in dataSet:
        currentLabel = featVec[-1]  # 数据的结论在数据集的最后一个特征属性
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        # 分类出现的次数/数据记录总数 = 该分类出现的概率
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


# 按照给定特征划分数据集
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


if __name__ == '__main__':
    fishDataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    # shannonEnt = calcShannonEnt(fishDataSet)
    # print(shannonEnt)

    result1 = splitDataSet(fishDataSet, 0, 1)
    result1 = splitDataSet(fishDataSet, 0, 0)
    print(result1)
