# -*- coding: utf-8 -*-
""" 
@date:          Sat Feb  5 14:36:10 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Algorithms/binarysearch.py
"""

from binarysearch import fixedPoint, numSmallerByFrequency, numSmallerByFrequency2
from binarysearch import findMissing, findSpecialInteger, findSpecialInteger2, findTheDistanceValue
from binarysearch import findKthPositive

def main():
    print('#### fixedPoint #########################')
    print(fixedPoint([-10,-5,0,3,7]))
    print(fixedPoint([0,2,5,8,17]))
    print(fixedPoint([-10,-5,3,4,7,9]))
    print('#### numSmallerByFrequency numSmallerByFrequency2 #########################')
    print(numSmallerByFrequency( ["cbd"], ["zaaaz"] ))
    print(numSmallerByFrequency( ["bbb","cc"], ["a","aa","aaa","aaaa"] ))
    print(numSmallerByFrequency2( ["cbd"], ["zaaaz"] ))
    print(numSmallerByFrequency2( ["bbb","cc"], ["a","aa","aaa","aaaa"] ))
    print('#### findMissing #########################')
    print(findMissing([2, 4, 8, 10, 12, 14]))
    print(findMissing([1, 6, 11, 16, 21, 31]))
    print('#### findSpecialInteger #########################')
    print(findSpecialInteger([1,2,2,6,6,6,6,7,10]))
    print(findSpecialInteger([1,1]))
    print(findSpecialInteger2([1,2,2,6,6,6,6,7,10]))
    print(findSpecialInteger2([1,1]))
    print('#### findTheDistanceValue #########################')
    print(findTheDistanceValue([4,5,8], [10,9,1,8], 2))
    print(findTheDistanceValue([1,4,2,3], [-4,-3,6,10,20,30], 3))
    print(findTheDistanceValue([2,1,100,3], [-5,-2,10,-3,7], 6))
    print('#### findKthPositive #########################')
    print(findKthPositive([2,3,4,7,11], 5))
    print(findKthPositive([1,2,3,4], 2))
    