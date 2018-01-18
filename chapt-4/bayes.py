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


# 词袋模型，分词每在词汇表中出现一个，词汇表对应的词向量值加1，而不是设置为1
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec


def trainNB0(trainMatrix, trainCategory):
    numTrainDocxs = len(trainMatrix)  # 总共有6个训练文档
    # 6个文档的训练词汇总数是32个
    # （trainMatrix是词汇表中的分词是否出现在文档中的向量矩阵）
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocxs)  # 计算属于侮辱性文档的概率 (3/6)

    p0Num = ones(numWords)  # 非侮辱文档中该分词出现的次数
    p1Num = ones(numWords)  # 侮辱文档中某分词出现的次数
    p0Denom = 2.0  # 非侮辱文档中词汇总数
    p1Denom = 2.0  # 侮辱文档中的词汇总数
    for i in range(numTrainDocxs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p0Vect = log(p0Num / p0Denom)  # 词汇表中单词出现在非侮辱文档中的概率
    p1Vect = log(p1Num / p1Denom)  # 词汇表中单词出现在侮辱性文档中的概率
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2classify * p1Vec) + log(pClass1)
    p0 = sum(vec2classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def textParse(bigString):
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]


def spamTest():
    docList = []
    classList = []
    fullText = []
    for i in range(1, 26):
        wordList = textParse(open('email/spam/%d.txt' % i, encoding='UTF-8').read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('email/ham/%d.txt' % i, encoding='UTF-8').read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)  # 根据所有邮件的词汇内容，创建词汇列表
    trainingSet = list(range(50))
    testSet = []
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del (trainingSet[randIndex])

    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))

    errorCount = 0
    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    return float(errorCount) / len(testSet)


if __name__ == '__main__':
    errorCount = 0.0
    for i in range(10):
        errorCount += spamTest()
    print("平均错误率：", errorCount / 10)

    # listOPosts, listClasses = loadDataSet()
    # myVocabList = createVocabList(listOPosts)
    # # print(myVocabList)
    # trainMat = []
    # for postinDoc in listOPosts:
    #     # 词汇表中的分词，是否出现在该文档中的向量矩阵，用来后续计算该词的概率
    #     trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    # p0V, p1V, pAb = trainNB0(trainMat, listClasses)
    #
    # testEntry = ['love', 'my', 'dalmation']
    # thisDoc = array(setOfWords2Vec(myVocabList, testEntry))  # 将文档与词汇库进行对比，生成对应的词汇向量
    # print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
    #
    # testEntry = ['stupid', 'garbage']
    # thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    # print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))




    # 判断一篇文章的分词是否存在于分词库中
    # returnVec = setOfWords2Vec(myVocabList, listOPosts[0])
    # print(returnVec)
    # returnVec1 = setOfWords2Vec(myVocabList, listOPosts[3])
    # print(returnVec1)
