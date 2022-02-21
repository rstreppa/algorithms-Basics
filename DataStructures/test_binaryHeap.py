# -*- coding: utf-8 -*-
""" 
@date:          Wed Feb 16 20:13:37 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Data_Structures/BinaryHeap/binaryHeap.py 
"""

from binaryHeap import BinHeap, lastStoneWeight, minStoneSum


def main():
    print('###################')
    bh = BinHeap()
    bh.buildHeap([9, 6, 5, 2, 3])
    print('###### lastStoneWeight #############')
    print(lastStoneWeight([2,7,4,1,8,1]))
    print(lastStoneWeight([1]))
    print('###### minStoneSum #############')
    print(minStoneSum([5,4,9], 2))
    print(minStoneSum([4,3,6,7], 3))