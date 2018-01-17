#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@author: lh
@file: bayes.py
@time: 2018/1/9 15:06
"""
from numpy import *


def loadDataSet():
    # 训练文档集合
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 文档是否为侮辱性=1
    return postingList, classVec


# 通过训练文档，生成保存文档中出现所有词汇的词汇表
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


# 计算输入文档inputSet中的分词，是否出现在词汇表vocabList中
# 形成与词汇表等长对应的0-1向量。
def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec


def trainNB0(trainMatrix, trainCategory):
    numTrainDocxs = len(trainMatrix)  # 总共有6个训练文档
    # 6个文档的训练词汇总数是32个
    # （trainMatrix是词汇表中的分词是否出现在文档中的向量矩阵）
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocxs)  # 计算属于侮辱性文档的概率 (3/6)

    p0Num = zeros(numWords)
    p1Num = zeros(numWords)
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(numTrainDocxs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num / p1Denom    #词汇表中单词出现在侮辱性文档中的概率
    p0Vect = p0Num / p0Denom    #词汇表中单词出现在非侮辱文档中的概率
    return p0Vect, p1Vect, pAbusive


if __name__ == '__main__':
    listOPosts, listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    # print(myVocabList)

    trainMat = []
    for postinDoc in listOPosts:
        # 词汇表中的分词，是否出现在该文档中的向量矩阵，用来后续计算该词的概率
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))

    p0V, p1V, pAb = trainNB0(trainMat, listClasses)
    print(p0V)
    print(p1V)
    print(pAb)

    # 判断一篇文章的分词是否存在于分词库中
    # returnVec = setOfWords2Vec(myVocabList, listOPosts[0])
    # print(returnVec)
    # returnVec1 = setOfWords2Vec(myVocabList, listOPosts[3])
    # print(returnVec1)
