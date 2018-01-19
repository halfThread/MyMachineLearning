#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@file: logRegres.py
@time: 2018/1/19 8:46
"""

from numpy import *


def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))  # exp 返回x的指数,e(x)


# 批处理梯度上升算法，只能处理少量数据
def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)  # mat方法将py的list转为numpy的矩阵数据类型
    labelMat = mat(classLabels).transpose()  # 将矩阵进行转置，将矩阵的行变为列
    m, n = shape(dataMatrix)  # shape 返回矩阵为几维几列
    alpha = 0.001
    maxCycles = 500
    weights = ones((n, 1))  # shape的第一个参数为矩阵的shape
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)
        error = (labelMat - h)
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights


# 随机梯度上升算法
# 增加参数numIter，增加随机次数，使得梯度递减系数收敛
def stocGradAscent0(dataMatrix, classLabels, numIter=150):
    m, n = shape(dataMatrix)
    # alpha = 0.01
    weights = ones(n)
    for j in range(numIter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4 / (1.0 + j + i) + 0.01
            randIndex = int(random.uniform(0, len(dataIndex)))
            # h = sigmoid(sum(dataMatrix[i] * weights))
            h = sigmoid(sum(dataMatrix[randIndex] * weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * dataMatrix[randIndex] * error
            del (dataIndex[randIndex])
    return weights


def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y.T)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


def classifyVector(inX, weights):
    prob = sigmoid(sum(inX * weights))
    if prob > 0.5:
        return 1.0
    else:
        return 0.0


def colicTest():
    frTrain = open('horseColicTraining.txt')
    frTest = open('horseColicTest.txt')
    trainingSet = []
    trainingLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    # 根据训练样本，获得各个特征值的回归系数。
    trainWeights = stocGradAscent0(array(trainingSet), trainingLabels, 500)
    # print(trainWeights)
    # 用回归系数，对测试样本进行预测
    errorCount = 0
    numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        # 如果预测失败，错误计数加1
        if int(classifyVector(array(lineArr), trainWeights)) != int(currLine[21]):
            errorCount += 1

    errorRate = (float(errorCount) / numTestVec)
    print("the error rate of this test is: %f" % errorRate)
    return errorRate


def multiTest():
    numTest = 10
    errorSum = 0.0
    for k in range(numTest):
        errorSum += colicTest()
    print("after %d iterations the average error rate is %f " % (numTest, errorSum / float(numTest)))


if __name__ == '__main__':
    # dataMatIn, classLabels = loadDataSet()
    # weights = gradAscent(dataMatIn, classLabels)
    # weights = stocGradAscent0(array(dataMatIn), classLabels)
    # plotBestFit(weights)

    # colicTest()
    multiTest()
