# -*- coding: utf-8 -*-
""" 
@date:          Tue Feb  1 21:07:51 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Data_Structures/Hash/myhash.py
"""

from myhash import largestUniqueNumber, countCharacters, calculateTime, uniqueOccurrences

def main():
    print('#### largestUniqueNumber #########################')
    print(largestUniqueNumber([5,7,3,9,4,9,8,3,1]))
    print(largestUniqueNumber([9,9,8,8]))
    print('#### countCharacters #########################')
    words = ["cat","bt","hat","tree"] 
    chars = "atach"
    print(countCharacters(words, chars))
    words = ["hello","world","leetcode"] 
    chars = "welldonehoneyr"
    print(countCharacters(words, chars))
    print('#### calculateTime #########################')
    keyboard    = "abcdefghijklmnopqrstuvwxyz" 
    word        = "cba"
    print(calculateTime(keyboard, word))
    keyboard    = "pqrstuvwxyzabcdefghijklmno" 
    word        = "hello"
    print(calculateTime(keyboard, word))
    print('#### uniqueOccurrences #########################')
    print(uniqueOccurrences([1,2,2,1,1,3]))
    print(uniqueOccurrences([1,2]))
    print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
    