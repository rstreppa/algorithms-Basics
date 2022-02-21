# -*- coding: utf-8 -*-
""" 
@date:          Mon Jan 31 22:13:28 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Data_Structures/String/mystring.py
"""

from mystring import confusingNumber, countLetters

def main():
    print('#### confusingNumber #########################')
    print(confusingNumber(6))
    print(confusingNumber(89))
    print(confusingNumber(11))
    print(confusingNumber(25))
    print('#### countLetters #########################')
    print(countLetters("aaaba"))
    print(countLetters("aaaaaaaaaa"))
    