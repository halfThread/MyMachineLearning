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
import operator
import matplotlib.pyplot as plt


def classify0(inX, dataSet, labelB, k):
    dataSetSize = dataSet.shape[0]
    # tile重复inx dataSetSize次，一次矩阵减法，算出当前点inx到训练集的所有点的距离
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet

    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)  # axis 每行相加
    distances = sqDistances ** 0.5  # 开根号

    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labelB[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1  # 计数统计标签出现的次数
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)

    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    arrayOfLines = fr.readlines()
    numberOfLines = len(arrayOfLines)
    returnMat = zeros((numberOfLines, 3))  # 生成全是0的SizeX3的矩阵
    classLabelVector = []
    index = 0
    for line in arrayOfLines:
        line = line.strip()  # 去除头尾空格
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


# 为减少数据值对结果的影响
# 使用归一法，将数值转化为0-1之间
def autoNorm(dataSet):
    minVals = dataSet.min(0)  # 0表示从矩阵的列中取最大、小值，而不是行
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


def showDataByMatplotlib(dataMat, labels):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ax.scatter(gametime, icecream, 15.0 * array(gametime), 15.0 * array(icecream))
    ax.scatter(dataMat[:, 0], dataMat[:, 1], 15.0 * array(labels), 15.0 * array(labels))
    plt.show()


def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix("datingTestSet2.txt")
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)  # 只有10%的数据用于测试
    errorCount = 0.0
    for i in range(numTestVecs):
        # 前 100 [i,:]行记录作为测试样本，后面的900 [numTestVecs:m,:] 行记录作为训练样本
        # [numTestVecs:m] 为900训练样本的标签结果， k=3
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("the classifier came back with: %d, the real answer is %d " % (classifierResult, datingLabels[i]))
        if classifierResult != datingLabels[i]:
            errorCount += 1.0
    print("the total error rate is: %f" % (errorCount / float(numTestVecs)))


if __name__ == '__main__':
    # k-近邻算法
    # group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    # labels = ['A', 'A', 'B', 'B']
    # print(classify0([0.5, 1.5], group, labels, 3))

    # 读取文件中的数据，使用散点图展示数据特点
    # datingDataMat, datingLabels = file2matrix("datingTestSet2.txt")
    # showDataByMatplotlib(datingDataMat, datingLabels)

    # dataSet = autoNorm(datingDataMat)
    # print(dataSet)

    datingClassTest()
