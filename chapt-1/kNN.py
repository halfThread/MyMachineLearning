#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
k-近邻算法
@version: 
@author: lh
@license: Apache Licence 
@contact: liuhuan0672@gmail.com
@site: 
@software: PyCharm
@file: kNN.py
@time: 2017/12/27 14:14

shape[0] :为numpy自带的函数方法，返回整数型数组，数组每个数字表示该维数组的长度,[0]表示第一维

"""
from numpy import *


def classify0(inX, dataSet, labelB, k):
    dataSetSize = dataSet.shape[0]
    print(inX)
    print(tile(inX, (dataSetSize, 1)))
    # diffMat = tile(inX, (dataSetSize, 1)) - dataSet


if __name__ == '__main__':
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    classify0([0, 0], group, labels, 3)
