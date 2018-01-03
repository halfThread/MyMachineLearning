#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@version: 
@author: lh
@license: Apache Licence 
@contact: liuhuan0672@gmail.com
@site: 
@software: PyCharm
@file: numpys.py
@time: 2017/12/27 16:25
"""
from numpy import *
import operator


def func():
    # shape 一个整型数字的元组，元组中的每个元素表示相应的数组每一维的长度
    # 如dataSet 返回[4,2]
    dataSet = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    print(dataSet.shape[0])

    # tile 对矩阵进行重复，tile(inx, (m,n)) 表示对矩阵inx y方向重复m次，x方向重复n次
    inx = [0, 1]
    redata = tile(inx, (4, 2))
    print(redata)

    # sum 没有axis参数表示全部相加，axis＝0 表示按列相加，axis＝1 表示按照行的方向
    a = sum([[0, 1, 2], [2, 1, 3]], axis=1)
    print(a)

    # argsort() 返回数组从小到大排序的索引值
    # 获取字典里的值的时候，一个是通过键值对，即dict['key'], 另一个就是dict.get()方法
    # items方法是可以将字典中的所有项，以列表方式返回。
    # iteritems方法与items方法相比作用大致相同，只是它的返回值不是列表，而是一个迭代器。


def testFunc():
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    # numFeatures = len(dataSet[0]) - 1
    # print(numFeatures)
    # featList = [example[2] for example in dataSet]
    # print(featList)

    # sorted(iterable, cmp=None, key=None, reverse=False)
    # iterable：是可迭代类型;
    # cmp：用于比较的函数，比较什么由key决定, 有默认值，迭代集合中的一项;
    # key：用列表元素的某个属性和函数进行作为关键字，有默认值，迭代集合中的一项;
    # reverse：排序规则.reverse = True 或者 reverse = False，有默认值。
    # 返回值：是一个经过排序的可迭代类型，与iterable一样。
    # operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号
    # operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值
    sortedData = sorted(dataSet, key=operator.itemgetter(1), reverse=True)
    print(sortedData)


if __name__ == '__main__':
    testFunc()
    # func()
