# -*- coding: utf-8 -*-
""" 
@date:          Wed Feb  2 20:26:40 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Algorithms/backtracking.py
"""

from backtracking import exist, letterCasePermutation, subsets, subsets2, subsetsWithDup
from backtracking import permute, permuteUnique, combine, combinationSum, combinationSum2, combinationSum3
from backtracking import generateParenthesis, letterCombinations

def main():
    print('#### exist #########################')
    board   = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 
    word    = "ABCCED"
    print(exist(board, word))
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 
    word = "SEE"
    print(exist(board, word))
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]] 
    word = "ABCB"
    print(exist(board, word))
    print('#### letterCasePermutation #########################')
    print(letterCasePermutation("a1b2"))
    print(letterCasePermutation("3z4"))
    print(letterCasePermutation("hey"))
    print('#### subsets subsets2 #########################')
    print(subsets([1,2,3]))
    print(subsets([0]))
    print(subsets2([1,2,3]))
    print(subsets2([0]))
    print('#### subsetsWithDup #########################')
    print(subsetsWithDup([1,2,2]))
    print(subsetsWithDup([0]))
    print('#### permute #########################')
    print(permute([1,2,3]))
    print(permute([0,1]))
    print(permute([1]))
    print('#### permuteUnique #########################')
    print(permuteUnique([1,1,2]))
    print(permuteUnique([1,2,3]))
    print('#### combine #########################')
    print(combine(4,2))
    print(combine(1,1))
    print('#### combinationSum #########################')
    print(combinationSum([2,3,6,7], 7))
    print(combinationSum([2,3,5], 8))
    print(combinationSum([2,], 1))
    print('#### combinationSum2 #########################')
    print(combinationSum2([10,1,2,7,6,1,5], 8))
    print(combinationSum2([2,5,2,1,2], 5))
    print('#### combinationSum3 #########################')
    print(combinationSum3(3, 7))
    print(combinationSum3(3, 9))
    print('#### generateParenthesis #########################')
    print(generateParenthesis(3))
    print(generateParenthesis(1))
    print('#### letterCombinations #########################')
    print(letterCombinations("23"))
    print(letterCombinations(""))
    print(letterCombinations("2"))
    