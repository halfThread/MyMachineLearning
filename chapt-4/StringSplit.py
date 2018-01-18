#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
@file: StringSplit.py
@time: 2018/1/18 13:58
"""
import re


def txtSplitTest():
    regEx = re.compile('\\W*')
    mySent = 'This book is the best book on Python or ' \
             'M.L. I have ever laid my eyes upon.'
    listOfTokens = regEx.split(mySent)
    listOfTokens = [tok.lower() for tok in listOfTokens if len(tok) > 1]
    print(listOfTokens)


def handleEmailText():
    regEx = re.compile('\\W*')
    emailText = open('email/ham/6.txt').read()
    emailTokens = regEx.split(emailText)
    print(emailTokens)


if __name__ == '__main__':
    # txtSplitTest()
    handleEmailText()
