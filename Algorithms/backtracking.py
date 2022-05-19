# -*- coding: utf-8 -*-
""" 
@date:          Wed Feb  2 20:25:46 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   simple problerms involving backtracking
"""


def exist(board, word):
    ''' Given an m x n grid of characters board and a string word, return true if word exists in the grid.
        The word can be constructed from letters of sequentially adjacent cells, 
        where adjacent cells are horizontally or vertically neighboring. 
        The same letter cell may not be used more than once.
    '''
    if not board:
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word):
                return True
    return False

    
def dfs(board, i, j, word):
    ''' check whether can find word, start at (i,j) position '''
    if len(word) == 0: # all the characters are checked
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit again, we say in this way, that this cell was visited and changing it back after.
    # check whether can find "word" along one direction
    res = dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:]) \
    or dfs(board, i, j+1, word[1:]) or dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res   
  
def letterCasePermutation(S):
    ''' Given a string s, you can transform every letter individually 
        to be lowercase or uppercase to create another string.
        Return a list of all possible strings we could create. Return the output in any order.
    '''
    def backtrack(sub="", i=0):
        if len(sub) == len(S):
            res.append(sub)
        else:
            if S[i].isalpha():
                backtrack(sub + S[i].swapcase(), i + 1)
            backtrack(sub + S[i], i + 1)
            
    res = []
    backtrack()
    return res    

def subsets(nums):
    ''' Given an integer array nums of unique elements, return all possible subsets (the power set).
        The solution set must not contain duplicate subsets. Return the solution in any order.
    '''
    def backtrack( nums, path, res ):
        res.append(path[::])
        for i in range(len(nums)):
            backtrack( nums[i+1:], path+[nums[i]], res)
    
    res = []
    backtrack( nums, [], res )
    return res
 
def subsets2(nums):
    ''' Iteratively '''
    res = [[]]
    for n in nums:
        res += [ r + [n] for r in res ]
    return res

def subsetsWithDup(nums):
    ''' Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
        The solution set must not contain duplicate subsets. Return the solution in any order.
    '''
    def backtrack( nums, path, res ):
        res.append(path[::])
        for i in range(len(nums)):
            if (i > 0) and (nums[i] == nums[i-1]):
                continue
            newNums =   nums[i+1:]
            path    +=  [nums[i]]
            backtrack( newNums, path, res )
            path.pop()
    
    res = []
    backtrack( nums, [], res )
    return res

def permute(nums):
    ''' Given an array nums of distinct integers, return all the possible permutations. 
        You can return the answer in any order.
    '''
	# helper
    def backtrack(nums, path, res):
        if not nums: # -- NOTE [1] 
            res.append(path[::]) #  -- NOTE [2] - append a copy of the path at the leaf before we start popping/backtracking

        for i in range(len(nums)): # [1,2,3]
            newNums = nums[:i] + nums[i+1:] 
            path += [nums[i]] 
            backtrack(newNums, path, res) # - recursive call will make sure I reach the leaf 
            path.pop() # -- NOTE [3]

    res = []
    backtrack( nums, [], res )
    return res


# NOTE [1]:
# --------
# nums is empty at the leaf of the recursive tree

# NOTE [2]:
# --------
# at the leaf -> we know we have exaushted one path/permutation (each path is a permutation in a recursive tree)
# reason why we are copying here is because at lists are passed by reference and since we are maintaining only one path/perm variable throughput, we are gonna be modifiying that path variable (popping it to be precise) in order to revert the path to a previous state (aka parent node) in preperation to make a lateral/horizontal move to a sibling node. See explanation below for further understanding.

# NOTE [3]:
# ---------
# See below    res = []
# NOTE [3] Explained further : Why do we need to backtrack?
# Notice how in the code above, 
# there is only one variable path (or perm) throughout the problem. 
# This variable is passed to one recursive call after another recursive call as we move from the input 
# (the root of the tree) to the leaf (the permutation) and obvioulsy it gets modified 
# multiple times along the way. As we keep building the path (or perm). 
# It goes from [ ] -> [1,2] -> [1,2,3] as you can see in the left-most branch. 
# However, what actually happens is that everytime we append a number to the path, 
# we are actively changing the path from previous recursive states as well, 
# since all of these point to the same path list and are not independent states/copies. 
# Since effectively all these aliases are pointing to the same memory location, 
# any change to the variable are echoed to all of its aliases. 
# This can be problematic because it alters the the previous states. 
# See below for visual illustration of the problem.  

def permuteUnique(nums):
    ''' Given a collection of numbers, nums, that might contain duplicates, 
        return all possible unique permutations in any order.
    '''
	# helper
    def backtrack(nums, path, res):
        if not nums:
            res.append(path[::])

        for i in range(len(nums)): # [1,2,3]
            if (i > 0) and (nums[i] == nums[i-1]):
                continue
            newNums = nums[:i] + nums[i+1:] 
            path += [nums[i]] 
            backtrack(newNums, path, res) # - recursive call will make sure I reach the leaf 
            path.pop()

    res = []
    backtrack( nums, [], res )
    return res

def combine(n, k):
    ''' Given two integers n and k, return all possible combinations 
        of k numbers out of the range [1, n].
        You may return the answer in any order.
    '''
	# helper
    def backtrack(nums, path, res, k):
        if len(path) == k: 
            res.append(path[::])

        for i in range(len(nums)):
            newNums =   nums[i+1:]
            path += [nums[i]] 
            backtrack(newNums, path, res, k) # - recursive call will make sure I reach the leaf 
            path.pop() # -- NOTE [3]

    nums    = [ i for i in range(1, n+1) ] 
    res     = []
    backtrack( nums, [], res, k )
    return res

def combinationSum(candidates, target):
    ''' Given an array of distinct integers candidates and a target integer target, 
        return a list of all unique combinations of candidates where the chosen numbers sum to target. 
        You may return the combinations in any order.
        The same number may be chosen from candidates an unlimited number of times. 
        Two combinations are unique if the frequency of at least one of the chosen numbers is different.
        It is guaranteed that the number of unique combinations that sum up to target is less 
        than 150 combinations for the given input.
    '''
	# helper
    def backtrack(candidates, path, res, target):
        if target < 0:
            return
        if target == 0:
            res.append(path[::])

        for i in range(len(candidates)):
            backtrack(candidates[i:], path+[candidates[i]] , res, target - candidates[i])
            

    res = []
    backtrack( candidates, [], res, target )
    return res

def combinationSum2(candidates, target):
    ''' Given a collection of candidate numbers (candidates) and a target number (target), 
        find all unique combinations in candidates where the candidate numbers sum to target.
        Each number in candidates may only be used once in the combination.
        Note: The solution set must not contain duplicate combinations.
    '''
    res = []
    candidates.sort()
    def backtrack(idx, path, cur):
        if cur > target: 
            return
        if cur == target:
            res.append(path)
            return
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            backtrack(i+1, path+[candidates[i]], cur+candidates[i])
    
    backtrack(0, [], 0)
    return res

def combinationSum3(k, n):
    ''' Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
        Only numbers 1 through 9 are used.
        Each number is used at most once.
        Return a list of all possible valid combinations. The list must not contain the same combination twice, 
        and the combinations may be returned in any order.
    '''
	# helper
    def backtrack(nums, path, res, k, n):
        if len(path) == k and sum(path) == n: 
            res.append(path[::])

        for i in range(len(nums)):
            newNums =   nums[i+1:]
            path += [nums[i]] 
            backtrack(newNums, path, res, k, n) # - recursive call will make sure I reach the leaf 
            path.pop() # -- NOTE [3]

    nums    = [ i for i in range(1, 10) ] 
    res     = []
    backtrack( nums, [], res, k, n )
    return res

def generateParenthesis(n):
    ''' Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. 
    '''
    def backtracking(nOpen, nClose, path):
        if n == nClose:  # Found a valid n pairs of parentheses
            res.append(path)
            return

        if nOpen < n:  # Number of opening bracket up to `n`
            backtracking(nOpen + 1, nClose, path + "(")
        if nClose < nOpen:  # Number of closing bracket up to opening bracket
            backtracking(nOpen, nClose + 1, path + ")")

    res = []
    backtracking(0, 0, "")
    return res

def letterCombinations(digits):
    ''' Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
        that the number could represent. Return the answer in any order.
        A mapping of digit to letters (just like on the telephone buttons) is given below. 
        Note that 1 does not map to any letters. 
    '''
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return list(mapping[digits[0]])
    prev        = letterCombinations(digits[:-1])
    additional  = mapping[digits[-1]]
    return [s + c for s in prev for c in additional]