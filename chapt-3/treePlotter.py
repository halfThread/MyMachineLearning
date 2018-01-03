#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@version: 
@author: lh
@license: Apache Licence 
@contact: liuhuan0672@gmail.com
@site: 
@software: PyCharm
@file: treePlotter.py
@time: 2018/1/3 16:29
"""
import matplotlib.pyplot as plt

# 定义文本框和箭头格式
decisionNode = dict(boxStyle="sawtooth", fc="0.8")
leafNode = dict(boxStyle="round4", fc="0.8")
arrow_args = dict(arrowStyle="<-")


def plotNode(nodeTxt, centerPt, parantPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parantPt, xycoords='axes fraction',
                            xytext=centerPt, textcoords='axes fraction', va="center", ha="center", bbox=nodeType,
                            arrowprops=arrow_args)


def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotNode('decisionNode', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('leafNode', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()


# 计算树结构字典的叶节点数
def getNumLeafs(myTree):
    numLeafs = 0
    # python3改变了dict.keys,返回的是dict_keys对象,支持iterable 但不支持indexable，可以将其明确的转化成list
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs


# 计算树结构字典的深度
def getTreeDept(myTree):
    maxDept = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDept = 1 + getTreeDept(secondDict[key])
        else:
            thisDept = 1
        if thisDept > maxDept: maxDept = thisDept
    return maxDept


if __name__ == '__main__':
    # createPlot()
    listOfTrees = [{'nosurfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                   {'nosurfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}]

    numLeaf = getNumLeafs(listOfTrees[1])
    dept = getTreeDept(listOfTrees[1])
    print(numLeaf)
    print(dept)
