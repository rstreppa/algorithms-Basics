# -*- coding: utf-8 -*-
""" 
@date:          Sat Jan 15 18:10:51 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Algorithms/miscellanea.py
"""

from miscellanea import search_id, longestIncreasingSubsequence_divideConquer, longestIncreasingSubsequence_dynProg
from miscellanea import maxProfit, numDecodings
from miscellanea import numberOfPaths_recursive, numberOfPaths_math, binomialCoeff, binomialCoef_dp, numberOfPaths_dp
from miscellanea import uniquePathsWithObstacles
from miscellanea import maxProfitIII, maxProfitI
from miscellanea import majorityElement, canCompleteCircuit


def main():
    print('#### search_id #########################')
    A = [2,3,7,11,13]
    idx = search_id( A, len(A), 8 ) 
    print(idx, A[idx])
    print('#### longestIncreasingSubsequence_divideConquer #########################')
    A =  [ 2, 5, 3, 7, 11, 8, 10, 13, 6 ]
    print(A)
    longestIncreasingSubsequence_divideConquer(A, len(A))
    print('#### longestIncreasingSubsequence_dynProg #########################')
    longestIncreasingSubsequence_dynProg(A, len(A))
    print('#### maxProfit #########################')
    prices = [7,2,5,8,6,3,1,4,5,4,7]
    m = maxProfit(prices)
    print(m)
    print('#### numDecodings #########################')
    A = '123'
    k = numDecodings(A)
    print(k)
    print('#### binomialCoeff #########################')
    print(binomialCoeff(7,4))
    print(binomialCoef_dp(7,4))   
    print('#### numberOfPaths_recursive #########################')
    m = 5
    n = 4
    k = numberOfPaths_recursive(m, n)
    print(k)
    print('#### numberOfPaths_math #########################')
    m = 5
    n = 4
    k = numberOfPaths_math(m, n)
    print(k)
    print('#### numberOfPaths_dp #########################')
    m = 5
    n = 4
    k = numberOfPaths_dp(m, n)
    print(k)
    print('#### uniquePathsWithObstacles #########################')
    A = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    k = uniquePathsWithObstacles(A)
    print(k)
    print('#### maxProfitIII #########################')
    prices = [1,2,4,2,5,7,2,4,9]
    k = maxProfitIII(prices)
    print(k)
    print('#### maxProfitI #########################')
    prices = [1,2,4,2,5,7,2,4,9]
    k = maxProfitI(prices)
    print(k)
    print('#### majorityElement #########################')
    A = [2, 1, 2]
    k = majorityElement(A)
    print(k)
    print('#### canCompleteCircuit #########################')
    gas  = [1,2,3,4,5]
    cost = [3,4,5,1,2]    
    k    = canCompleteCircuit(  gas, cost )
    print(k)