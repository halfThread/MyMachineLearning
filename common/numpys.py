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


def func():
    # shape 一个整型数字的元组，元组中的每个元素表示相应的数组每一维的长度
    # 如dataSet 返回[4,2]
    dataSet = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    print(dataSet.shape[0])

    # tile 对矩阵进行重复，tile(inx, (m,n)) 表示对矩阵inx y方向重复m次，x方向重复n次
    inx = [0, 1]
    redata = tile(inx, (4, 2))

    print(redata)


if __name__ == '__main__':
    func()
