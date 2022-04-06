# -*- coding: utf-8 -*-
""" 
@date:          Tue Feb  1 21:07:51 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Data_Structures/Hash/myhash.py
"""

from myhash import largestUniqueNumber, countCharacters, calculateTime, uniqueOccurrences
from myhash import canFormArray, countKDifference, kthDistinct, mostFrequent
from myhash import smallestCommonElement, longestWPI, countPairs, maxOperations, countNicePairs

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
    print('#### canFormArray #########################')
    print( canFormArray( [15,88], [[88],[15]] ) )
    print( canFormArray( [49,18,16], [[16,18,49]] ) )
    print( canFormArray( [91,4,64,78], [[78],[4,64],[91]] ) )
    print('#### countKDifference #########################')
    print( countKDifference( [1,2,2,1], 1 ) )
    print( countKDifference( [1,3], 3 ) )
    print( countKDifference( [3,2,1,5,4], 2 ) )
    print('#### kthDistinct #########################')
    print( kthDistinct( ["d","b","c","b","c","a"], 2 ) )
    print( kthDistinct( ["aaa","aa","a"], 1 ) )
    print( kthDistinct( ["a","b","a"], 3 ) )    
    print('#### mostFrequent #########################')
    print( mostFrequent( [1,100,200,1,100], 1 ) )
    print( mostFrequent( [2,2,2,2,3], 2 ) )
    print('#### smallestCommonElement #########################')
    print( smallestCommonElement( [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]] ) )
    print('#### longestWPI #########################')
    print( longestWPI([9,9,6,0,6,6,9]) )
    print( longestWPI([6,6,6]) )
    print('#### countPairs #########################')
    print( countPairs( [1,3,5,7,9] ) )
    print( countPairs( [1,1,1,3,3,3,7] ) )
    print('#### maxOperations #########################')
    print( maxOperations( [1,2,3,4], 5 ) )
    print( maxOperations( [3,1,3,4,3], 6 ) )
    print('#### countNicePairs #########################')
    print( countNicePairs( [42,11,1,97] ) )
    print( countNicePairs( [13,10,35,24,76] ) )
    