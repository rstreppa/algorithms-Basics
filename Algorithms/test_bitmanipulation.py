# -*- coding: utf-8 -*-
""" 
@date:          Sat Jan 22 10:37:10 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Algorithms/bitmanipulation.py
"""

from bitmanipulation import singleNumber, isPowerof2, log2, myswap, power2, rightmostOne
from bitmanipulation import countBits, binaryArray, countBits2

def main():
    print('#### singleNumber #########################')
    nums = [2,2,1]
    print(singleNumber(nums))
    nums = [4,1,2,1,2]
    print(singleNumber(nums))
    nums = [1]
    print(singleNumber(nums))
    print('#### isPowerof2 #########################')
    print(16, isPowerof2(16))
    print(15, isPowerof2(15))
    print(0, isPowerof2(0))
    print('#### log2 #########################')
    print(16, log2(16))
    print(4096, log2(4096))
    print(15, log2(15))
    print('#### myswap #########################')
    print(myswap(1,2))
    print('#### power2 #########################')
    print(5, power2(5))
    print('#### rightmostOne #########################')
    for i in range(10):
        print(bin(rightmostOne(i)))
    print('#### binaryArray #########################')
    print(binaryArray(2))
    print(binaryArray(5))
    print('#### countBits #########################')
    print(countBits(2))
    print(countBits(5))
    print('#### countBits2 #########################')
    print(countBits2(2))
    print(countBits2(5))
