# -*- coding: utf-8 -*-
""" 
@date:          Sat Jan 22 12:22:38 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Algorithms/dynamicprogramming.py
"""

from dynamicprogramming import climbStairs, maxProfit, maxProfitI, maxSubArray
from dynamicprogramming import sumRange, minWindow, findTargetSumWays, rob

def main():
    print('#### climbStairs #########################')
    print(climbStairs(2))
    print(climbStairs(3))
    print(climbStairs(45))
    print('#### maxProfit #########################')
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))
    prices = [7,6,4,3,1]
    print(maxProfit(prices))
    print('#### maxProfitI #########################')
    prices = [7,1,5,3,6,4]
    print(maxProfitI(prices))
    prices = [7,6,4,3,1]
    print(maxProfitI(prices))
    print('#### maxSubArray #########################')
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))
    nums = [1]
    print(maxSubArray(nums))
    print('#### sumRange #########################')
    print(sumRange([-2, 0, 3, -5, 2, -1], 0, 2 ))
    print(sumRange([-2, 0, 3, -5, 2, -1], 2, 5 ))
    print(sumRange([-2, 0, 3, -5, 2, -1], 0, 5 ))
    print('#### minWindow #########################')
    print(minWindow("abcdebdde", "bde"))
    print('#### findTargetSumWays #########################')
    print(findTargetSumWays([1,1,1,1,1], 3))
    print(findTargetSumWays([1], 1))
    print('#### rob #########################')
    print(rob([1,2,3,1]))
    print(rob([2,7,9,3,1]))