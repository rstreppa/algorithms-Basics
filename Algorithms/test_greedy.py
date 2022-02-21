# -*- coding: utf-8 -*-
""" 
@date:          Sat Feb  5 20:22:54 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Algorithms/greedy.py
"""

from greedy import largestSumAfterKNegations, twoCitySchedCost, shortestWay, shortestWay2
from greedy import canJump

def main():
    print('#### largestSumAfterKNegations #########################')
    print(largestSumAfterKNegations([4,2,3], 1))
    print(largestSumAfterKNegations([3,-1,0,2], 3))
    print(largestSumAfterKNegations([2,-3,-1,5,-4], 2))
    print('#### twoCitySchedCost #########################')
    print(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
    print(twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))
    print(twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]))
    print('#### shortestWay #########################')
    print(shortestWay("abc", "abcbc"))
    print(shortestWay("abc", "acdbc"))
    print(shortestWay("xyz", "xzyxz"))
    print(shortestWay2("abc", "abcbc"))
    print(shortestWay2("abc", "acdbc"))
    print(shortestWay2("xyz", "xzyxz"))
    print('#### canJump #########################')
    print(canJump([2,3,1,1,4]))
    print(canJump([3,2,1,0,4]))