# -*- coding: utf-8 -*-
""" 
@date:          Sat Jan 22 12:21:35 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   simple problems involving dynamic programming
"""
import sys


def climbStairs(n):
    ''' You are climbing a staircase. It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
        Basically it's a fibonacci.
        Base cases:
        if n <= 0, then the number of ways should be zero.
        if n == 1, then there is only way to climb the stair.
        if n == 2, then there are two ways to climb the stairs. One solution is one step by another; 
        the other one is two steps at one time.
        
        The key intuition to solve the problem is that given a number of stairs n, 
        if we know the number ways to get to the points [n-1] and [n-2] respectively, 
        denoted as n1 and n2 , then the total ways to get to the point [n] is n1 + n2. 
        Because from the [n-1] point, we can take one single step to reach [n]. 
        And from the [n-2] point, we could take two steps to get there.
        
        The solutions calculated by the above approach are complete and non-redundant. 
        The two solution sets (n1 and n2) cover all the possible cases on how the final step is taken. 
        And there would be NO overlapping among the final solutions constructed from these two solution sets, 
        because they differ in the final step.        
    '''
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


def maxProfit(prices):
    ''' 
        You are given an array prices where prices[i] is the price of a given stock on the ith day.
        You want to maximize your profit by choosing a single day to buy one stock and choosing a different 
        day in the future to sell that stock.
        Return the maximum profit you can achieve from this transaction. 
        If you cannot achieve any profit, return 0
        
        The logic to solve this problem is same as "max subarray problem" using Kadane's Algorithm
        Find a contiguous subarray giving maximum profit. If the difference falls below 0, reset it to zero.
        Suppose we have original array:
        [a0, a1, a2, a3, a4, a5, a6]
        
        what we are given here(or we calculate ourselves) is:
        [b0, b1, b2, b3, b4, b5, b6]
        
        where,
        b[i] = 0, when i == 0
        b[i] = a[i] - a[i - 1], when i != 0
        
        suppose if a2 and a6 are the points that give us the max difference (a2 < a6)
        then in our given array, we need to find the sum of sub array from b3 to b6.    
        b3 = a3 - a2
        b4 = a4 - a3
        b5 = a5 - a4
        b6 = a6 - a5        
        adding all these, all the middle terms will cancel out except two
        i.e.       
        b3 + b4 + b5 + b6 = a6 - a2       
        a6 - a2 is the required solution.       
        so we need to find the largest sub array sum to get the most profit                      
    '''
    diffs = list()
    for i in range(1,len(prices)):
        diffs.append( prices[i] - prices[i-1] )
    
    # max subarray problem using Kadane algorithm
    n                       = len(diffs)
    dp                      = [0] * n
    dp[0]                   = diffs[0]
    for i in range(1, n):
        dp[i] = max( dp[i-1] + diffs[i], diffs[i])
    return max( max( dp ), 0 )

def maxProfitI(prices):
    '''     Best Time to Buy and Sell Stocks I
            Say you have an array, A, for which the ith element is the price of a given stock on day i.
            If you were only permitted to complete at most one transaction (i.e, buy one and sell one share of the stock), 
            design an algorithm to find the maximum profit.
            Return the maximum possible profit.    
    '''
    if len(prices) == 0:
        return 0
    else:
        max_profit = 0
        min_price = prices[0]
        for i in range(len(prices)):
            profit = prices[i] - min_price
            max_profit = max(profit, max_profit)
            min_price = min(min_price, prices[i])

        return max_profit

def maxSubArray(nums):
    ''' Given an integer array nums, find the contiguous subarray (containing at least one number) 
        which has the largest sum and return its sum. 
        So this is actually a dynamic programming problem. 
        If dp[i] represents the largest sum of all subarrays ending with index i, 
        then its value should be the larger one between nums[i] 
        (without using prefix) and dp[i-1] + nums[i] (using prefix with largest sum plus current number)
    '''
    n                       = len(nums)
    dp                      = [0] * n
    dp[0]                   = nums[0]
    for i in range(1, n):
        dp[i] = max( dp[i-1] + nums[i], nums[i])
    return max( dp )
    
def sumRange(nums, left, right):
    ''' Given an integer array nums, handle multiple queries of the following type:
        Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
    '''
    return sum(nums[left:right+1])

def minWindow(S, T):
    ''' Given strings S and T, find the minimum (contiguous) substring W of S, 
        so that T is a subsequence of W.
        If there is no such window in S that covers all characters in T, 
        return the empty string "". 
        If there are multiple such minimum-length windows, return the one with the left-most starting index.
        
        We can have the brute force solution where we consider every substring of S and check whether it contains T. Amongst those substrings, our answer will be the one of the shortest length and smallest index. But it’s time complexity would be O(S³) (number of substrings * length of substring).
        But this can be solved elegantly using DP,
        dp[i][j]: the start position of Minimum Window Subsequence for S[:i] and T[:j]    
    '''
    m       = len(S)
    n       = len(T)
    dp      = [[-1 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    length  = float('inf')
    ans     = ""
    for i in range(1, m+1):
        for j in range(1, n+1):
            if S[i-1] == T[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j]
            if dp[i][n] != -1 and i - dp[i][n] < length:
                length = i - dp[i][n]
                ans = S[dp[i][n]:i]
    return ans

def findTargetSumWays(nums, S):
    ''' You are given an integer array nums and an integer target.
        You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer 
        in nums and then concatenate all the integers.
        For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them 
        to build the expression "+2-1".
        Return the number of different expressions that you can build, which evaluates to target.
        
        Read this to understand DP
        https://leetcode.com/problems/target-sum/discuss/455024/DP-IS-EASY!-5-Steps-to-Think-Through-DP-Questions.
    '''
    def dp(nums, target, index, curr_sum):

        if (index, curr_sum) in memo:
            return memo[(index, curr_sum)]

    	# Base Cases
        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0 
        
    	# Decisions
        positive = dp(nums, target, index-1, curr_sum + nums[index])
        negative = dp(nums, target, index-1, curr_sum + -nums[index])
        
        memo[(index, curr_sum)] = positive + negative
        return positive + negative    


    index       = len(nums) - 1
    curr_sum    = 0
    memo        = {}
    return dp(nums, S, index, curr_sum)


def rob(nums):
    ''' You are a professional robber planning to rob houses along a street. 
        Each house has a certain amount of money stashed, the only constraint stopping you 
        from robbing each of them is that adjacent houses have security systems connected and it will 
        automatically contact the police if two adjacent houses were broken into on the same night.
        Given an integer array nums representing the amount of money of each house, 
        return the maximum amount of money you can rob tonight without alerting the police.
    
        This particular problem and most of others can be approached using the following sequence:
        Find recursive relation
        Recursive (top-down)
        Recursive + memo (top-down)
        Iterative + memo (bottom-up)
        Iterative + N variables (bottom-up)
        
        https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
    '''
    def dfs( nums, i ):
        if i < 0:
            return 0 
        if dp[i] >= 0:
            return dp[i]
        res     = max( dfs(nums, i-2) + nums[i], dfs(nums, i-1) )    
        dp[i]   = res 
        return res
        
     
    dp = [-1] * (len(nums)+1)
    
    return dfs( nums, len(nums)-1)

def coinChange(coins, amount):
    ''' 322. Coin Change
        Medium
        You are given an integer array coins representing coins of different denominations 
        and an integer amount representing a total amount of money.        
        Return the fewest number of coins that you need to make up that amount. 
        If that amount of money cannot be made up by any combination of the coins, return -1.   
        You may assume that you have an infinite number of each kind of coin.
    '''
    memo = dict()
    memo[0] = 0

    def dp(coins, target): 
        if target in memo:
            return memo[target]
        if target<0:
            return -1
        res = float('inf')
        for coin in coins:
            if dp(coins, target-coin) == -1:
                continue
            res = min(res, dp(coins, target-coin)+1)
        memo[target] = res
        return res
    return dp(coins, amount) if dp(coins, amount)<float('inf') else -1

def coinChange2(coins, amount):
    ''' iterative DP solution '''
    dp = [float('inf') for _ in range(1+amount)]
    dp[0] = 0 

    for i in range(1, 1+amount): 
        for coin in coins:
            if i-coin>=0: 
                dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[amount] if dp[amount]<float('inf') else -1   


def coinChange3(coins, amount):
    ''' recursive DP solution that I actually understand 
        Unfortunately it solves a different problem, namely not the min
    '''
    
    # Function to find the total number of distinct ways to get a change of `target`
    # from an unlimited supply of coins in set `S`
    def count(S, n, target, lookup):
     
        # if the total is 0, return 1 (solution found)
        if target == 0:
            return 1
     
        # return 0 (solution does not exist) if total becomes negative,
        # no elements are left
        if target < 0 or n < 0:
            return 0
     
        # construct a unique key from dynamic elements of the input
        key = (n, target)
     
        # if the subproblem is seen for the first time, solve it and
        # store its result in a dictionary
        if key not in lookup:
     
            # Case 1. Include current coin `S[n]` in solution and recur
            # with remaining change `target-S[n]` with the same number of coins
            include = count(S, n, target - S[n], lookup)
     
            # Case 2. Exclude current coin `S[n]` from solution and recur
            # for remaining coins `n-1`
            exclude = count(S, n - 1, target, lookup)
     
            # assign total ways by including or excluding current coin
            lookup[key] = include + exclude
     
        # return solution to the current subproblem
        return lookup[key]    
    
    
    lookup = {}
    return count(coins, len(coins) - 1, amount, lookup)
  

def coinChange4(coins, amount):
    ''' recursive DP solution that I actually understand 
        This time it solves the real problem
        Recursive top-down approach
    '''
    def dfs( coins, target, lookup ):

         if target < 0:
             return -1

         if target == 0:
             return 0

         minVal = sys.maxint

         if target not in lookup:
             for coin in coins:
                 tempRes = dfs( coins, target - coin, lookup )
                 
                 if tempRes >= 0 and tempRes < minVal:
                     minVal = 1+tempRes

             if minVal == sys.maxint:
                 lookup[target] = -1
             else:
                 lookup[target] = minVal

         return lookup[target]

    lookup = {}
    return dfs( coins, amount, lookup )


  
def uniquePaths(m, n):
    """
        62. Unique Paths
        Medium
        There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
        The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
        The robot can only move either down or right at any point in time.       
        Given the two integers m and n, return the number of possible unique paths that the robot 
        can take to reach the bottom-right corner.

        Dynamic Programming Recursive
    """

    def dfs( m, n, lookup ):
        if m == 1 or n == 1:
            return 1
        key = (m, n)
        if key not in lookup:
            lookup[key] = dfs(m-1, n, lookup ) + dfs(m, n-1, lookup )
        return lookup[key]

    lookup = {}
    return  dfs( m, n, lookup )

def uniquePaths2(m, n):
    """ 
        Dynamic Programming Iterative
	
        Count all possible paths from top left to bottom right of a mXn matrix
        So this problem has both properties
        1) Overlapping Subproblemss
        2) Optimal Substructure

        of a dynamic programming problem. Like other typical Dynamic Programming(DP) problems,
        recomputations of same subproblems can be avoided by constructing a temporary array
        count[][] in bottom up manner using the above recursive formula.

    """

    # Create a 2D table to store results of subproblems
    # one-liner logic to take input for rows and columns
    # mat = [[int(input()) for x in range (C)] for y in range(R)]

    count = [[0 for x in range(n)] for y in range(m)]
    
    # Count of paths to reach any
    # cell in first column is 1
    for i in range(m):
        count[i][0] = 1

    # Count of paths to reach any
    # cell in first column is 1
    for j in range(n):
        count[0][j] = 1

    # Calculate count of paths for other
    # cells in bottom-up
    # manner using the recursive solution
    for i in range(1, m):
        for j in range(1, n):            
            count[i][j] = count[i-1][j] + count[i][j-1]

    return count[m-1][n-1]


