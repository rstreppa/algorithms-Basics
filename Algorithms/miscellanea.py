# -*- coding: utf-8 -*-
""" 
@date:          Sat Jan 15 18:09:43 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   miscellaneous Algorithm problems
"""
import sys
import math

def search_id(arr, n, x):
    ''' Function for getting index of first element which is greater than or equal to x = A[ i ]'''
    # Initialise starting index and ending index
    low = 0
    high = n

    # Till low is less than high
    while low < high:

        mid = low + int((high - low) / 2)

        # If X is less than or equal
        # to arr[mid], then find in
        # left subarray
        if x <= arr[mid]:
            high = mid

        # If X is greater arr[mid]
        # then find in right subarray
        else:
            low = mid + 1

    # Return the lower_bound index
    return low

def longestIncreasingSubsequence_divideConquer( a, n ):
    ''' Find the longest increasing subsequence of a given array of integers, A.
        In other words, find a subsequence of array in which the subsequence’s elements 
        are in strictly increasing order, and in which the subsequence is as long as possible. 
        This subsequence is not necessarily contiguous, or unique.
        In this case, we only care about the length of the longest increasing subsequence.
        Divide and Conquer algo:
            https://www.codesdope.com/blog/article/longest-increasing-subsequence/
    '''
    temp = []

    # position array will store the index of
    # element stored at ith position in temp
    # array
    position = []

    # initialize temp array with INT_MAX
    # as all values in array a will be smaller than
    # INT_MAX
    for i in range(n):
        temp.append(sys.maxsize)

    # Variable to track position of last element
    # in temp array
    pt = 0

    temp[0] = a[0]
    position.append(0)

    for i in range(1, n):

        # append a[i] if it is greater
        # then last value in temp array
        if temp[pt] < a[i]:
            temp[pt + 1] = a[i]
            position.append(i)
            pt = pt + 1
        else:

            # if a[i] is greater, put it in appropriate position
            # such that temp[ind-1]<a[i]
            ind = search_id(temp, n, a[i])

            temp[ind] = a[i]

            position[ind] = i

    # Number of elements in temp array is
    # is the length of longest increasing subsequence
    print("Length of longest increasing subsequence", pt + 1)

    return pt+1


def lengthOfLIS(self, nums):
    """
    300. Longest Increasing Subsequence
    Medium
    Given an integer array nums, return the length of the longest 
    strictly increasing subsequence.

    A subsequence is a sequence that can be derived from an array by deleting some 
    or no elements without changing the order of the remaining elements. 
    For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].        
        
    Watch this video https://www.youtube.com/watch?v=cjWnW0hdF1Y
    Exploit brute force
    It is natural to start from the end as there are no values/indices after
    for each index backwards you will check all indices after, so O(n^2) 
        
    :type nums: List[int]
    :rtype: int
    """
    n           = len(nums)
    dp          = [1] * n
        
    for i in range( n-1, -1, -1 ):
        for j in range( i+1, n ):
            if nums[i] < nums[j]:
                dp[i]   = max( dp[i], 1 + dp[j] )
                    
    return max( dp )


def maxProfit(prices):
   """      Say you have an array, A, for which the ith element is the price of a given stock on day i.
           Design an algorithm to find the maximum profit.
           You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
           However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).   
           Algo:
               https://www.tutorialcup.com/leetcode-solutions/best-time-to-buy-and-sell-stock-ii-leetcode-solution.htm
   
            As we don’t have any restrictions on the number of transactions so we will think of a greedy algorithm here. 
            So every time we will buy a stock at a minimum price and sell it at a maximum price. 
            We can summarize it as, at each minima we will buy a stock and at each maxima, 
            we will sell a stock.  This is explained in the figure given below. 
            It is a plot between the stock price and the days.
            We can make it simpler if we observe that a maxima is formed when small values 
            are added to minima. So in spite of tracking every minima and maxima 
            to calculate the maximum profit, we can directly add those values to our profit 
            for which we found a positive slope that is prices[i]>prices[i-1]. 
            The addition of all such values will give us maximum profit.
    """
   ans = 0
   for i in range(1,len(prices)):
      if prices[i] - prices[i-1] >0:
         ans+=(prices[i] - prices[i-1])
   return ans

def numDecodings(s):
    ''' Ways to Decode
        A message containing letters from A-Z is being encoded to numbers using the following mapping:
         'A' -> 1
         'B' -> 2
         ...
         'Z' -> 26
         Given an encoded message A containing digits, determine the total number of ways 
         to decode it modulo 10**9 + 7.
    Step 1: Declare and initialize a 1D array of size n with zero.
    Step 2: Check if we can decode the string which starts and ends both at (n-1)th index( Base case ).
    Step 3: Run a loop and check at every step if we can use the ith index element as one digit valid number or merge it with (i+1)th index element to form a valid number of two digit.
    1.	If s[i]!=’0’, then dp[i]+=dp[i+1]
    2.	If s[i]==’1’, then dp[i]+=dp[i+2]
    3.	If s[i]==’2’ and s[i+1]<=’6’, then dp[i]+=dp[i+2]  
    Step 4: Return dp[0].
    '''
    n = len(s)
    dp = [0] * (n+1)
    dp[n] = 1
    if s[n-1]!='0':     # if the last chararcter is not zero then we have one way to decode it
        dp[n-1]=1
        
    for i in range(n-2, -1, -1):
        if s[i] != '0':
            dp[i]+=dp[i+1]
            
        if s[i] == '1':
            dp[i]+=dp[i+2]
        
        if s[i] == '2':
            if s[i+1] <= '6':
                dp[i]+=dp[i+2]

    return dp[0]   
    
def numberOfPaths_recursive(m, n):
    '''Count all possible paths from top left to bottom right of a mXn matrix '''
    # If either given row number is first
    # or given column number is first
    if(m == 1 or n == 1):
        return 1

    # If diagonal movements are allowed
    # then the last addition
    # is required.
    return numberOfPaths_recursive(m-1, n) + numberOfPaths_recursive(m, n-1)

def binomialCoeff(n, k):
    ''' simple recursive implementation '''
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
 
    # Recursive Call
    return binomialCoeff(n-1, k-1) + binomialCoeff(n-1, k)

def binomialCoef_dp(n, k):
    ''' A Dynamic Programming based Python Program that uses table C[][] to calculate the Binomial Coefficient'''
    C = [[0 for x in range(k+1)] for x in range(n+1)]
 
    # Calculate value of Binomial
    # Coefficient in bottom up manner
    for i in range(n+1):
        for j in range(min(i, k)+1):
            # Base Cases
            if j == 0 or j == i:
                C[i][j] = 1     # C(n,0) = C(n,n) = 1
 
            # Calculate value using
            # previously stored values
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
 
    return C[n][k]
 


def numberOfPaths_math(m, n):
    '''Count all possible paths from top left to bottom right of a mXn matrix '''
    return binomialCoeff( m+n-2, m-1 )


def numberOfPaths_dp(m, n):
    ''' Count all possible paths from top left to bottom right of a mXn matrix 
        So this problem has both properties 
        1) Overlapping Subproblems 
        2) Optimal Substructure 
        of a dynamic programming problem. Like other typical Dynamic Programming(DP) problems, 
        recomputations of same subproblems can be avoided by constructing a temporary array 
        count[][] in bottom up manner using the above recursive formula.
    '''
    # Create a 2D table to store
    # results of subproblems
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

def uniquePathsWithObstacles(A):
    ''' Given a grid of size m * n, let us assume you are starting at (1, 1) and your goal is to reach (m, n). At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).
        Now consider if some obstacles are added to the grids.
        Approach:
        * Create a 2D matrix of the same size as the given matrix to store the results.
        * Traverse through the created array row-wise and start filling the values in it.
        * If an obstacle is found, set the value to 0.
        * For the first row and column, set the value to 1 if an obstacle is not found.
        * Set the sum of the right and the upper values if an obstacle is not present at that corresponding position in the given matrix
        * Return the last value of the created 2d matrix                  
    '''
    # create a 2D-matrix and initializing with value 0
    paths = [[0]*len(A[0]) for i in A]
     
    # initializing the left corner if no obstacle there
    if A[0][0] == 0:
        paths[0][0] = 1
     
    # initializing first column of the 2D matrix
    for i in range(1, len(A)):
         
        # If not obstacle
        if A[i][0] == 0:
            paths[i][0] = 1 # paths[i-1][0]
             
    # initializing first row of the 2D matrix
    for j in range(1, len(A[0])):
         
        # If not obstacle
        if A[0][j] == 0:
            paths[0][j] = 1 # paths[0][j-1]
             
    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
 
            # If current cell is not obstacle
            if A[i][j] == 0:
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
 
    # returning the corner value of the matrix
    return paths[-1][-1]

def maxProfitIII(prices):
    '''     Best Time to Buy and Sell Stocks III
            Say you have an array, A, for which the ith element is the price of a given stock on day i.
            Design an algorithm to find the maximum profit. You may complete at most 2 transactions.
            Return the maximum possible profit.
            
            The idea is from dynamic programming, the max profit at day i is the max profit 
            before day i + max profit after day i. 
            So there is one loop O(n) to compute the max profit before each each day 
            and another loop O(n) to get the final max profit by compute the max profit after each day 
            reversely and combine the "before day" max profit.
            
            1) we compute the forward max profit and save it.  
            Forward max profit means for each day i, we want to know the max profit we can make no later than this day. Note that we only need to consider 1 transaction:
            prices[ ] = 1,2,4,2,5,7,2,4,9
            mp[ ]     =  0,1,3,3,4,6,6,6,8
            
            (2) Now what we need is two transactions rather than one, 
            easily we can see from the price list, if we are required exact 2 transactions, 
            we must finish one transaction at some day i, and do the 2nd transaction after that. 
            The max profit is the sum of max profit before day i and after day i. 
            Day i might be every day in the price list, so there is a loop in the code.
            Similar to the step(1), but in a reverse order, from the last day -1 to first, 
            we already have the max profit before day i, mp[i], and we can compute the max profit 
            every time for i to n-1 days (n is the number of days), similar to step(1).
    '''
    n = len(prices)
    if (n<2):
        return 0
    st = prices[0]
    mp=[]
    mprof = 0
    for i in range(0,n):
        if (prices[i]-st>mprof):
            mprof = prices[i]-st
        if (prices[i]<st):
            st = prices[i]
        mp.append(mprof)
    
    mprof = 0
    ed = prices[-1]
    for i in range(n-2,-1,-1):
        if (ed - prices[i] + mp[i] > mprof):
            mprof = ed - prices[i] + mp[i]
        if (prices[i]>ed):
            ed = prices[i]
    return mprof
    
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
    
def majorityElement(A):
    ''' Given an array of size n, find the majority element. The majority element is the element 
        that appears more than floor(n/2) times.
        You may assume that the array is non-empty and the majority element always exist in the array.
    '''
    n   = len(A)
    med = math.floor(n/2)
    d   = dict()

    for elem in A:
        d[elem] = d.get(elem, 0) + 1 
        
    # for i in range(n):
    #     if A[i] in d:
    #         d[A[i]] += 1
    #     else:
    #         d[A[i]] = 1

    for k, v in d.items():
        if v > med:
            return k
    
    return -1

def canCompleteCircuit(self, gas, cost):
    """
    134. Gas Station
    Medium
    There are n gas stations along a circular route, where the amount of gas 
    at the ith station is gas[i].

    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel 
    from the ith station to its next (i + 1)th station. 
    You begin the journey with an empty tank at one of the gas stations.

    Given two integer arrays gas and cost, return the starting gas station's index 
    if you can travel around the circuit once in the clockwise direction, otherwise return -1. 
    If there exists a solution, it is guaranteed to be unique
        
    watch neetcode video
    https://www.youtube.com/watch?v=lJwbPZGo05A
        
    Greedy algorithm O(n) time O(1) memory complexity 
    1) create a diff array gas - cost to see what's going on: gas is good cost is bad.  
        [-2,-2,-2,3,3] you clearly see that starting index must be 3 to do circuit
    2) Brute force solution: try every position and try to make a circle O(n^2) 
    3) sum(gas) >= sum(cost) else no solution (i.e. sum(diff) >= 0 )
    4) we are going to keep track of single variable total = 0 (and of start position)
    5) add diff[0] to total. If total ever becomes negative, we ran out of gas, meaning that that
        starting position did not work
    6) be greedy: try each position in turn if total is negative try next position and reset total to 0
    7) when you hit 3 your total becomes positive, be greedy and continue
    8) when you reach the end of the array do you have to wrap and restart? No, you don't!
        Not super intutive: since sum(diff) >= 0 a solution is guaranteed to exist
    9) greedy problems are tricky: you got to assume it works and see if it does
    10) it has to be the first index that allows you nd the array (no matter how negative the preceding)
        
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
        
    if sum(gas) < sum(cost):
        return -1
        
    # now a solution certainly exists, you have to find it
    total           = 0  
    start           = 0
        
    for i in range(len(gas)):
        total   += ( gas[i] - cost[i] )     # we are adding diff[i] to total
        # if total ever becomes negative that position not goona work
        # if total always stays positive that position is the (unique) solution
        if total < 0:
            total   = 0
            start   = i+1
        
    return start
    
    
    def myPow(x, n):
    """
        50. Pow(x, n)
        Medium
        Implement pow(x, n), which calculates x raised to the power n (i.e., xn).        
        
        Naive implementation will exceed time limit.
        Smart approach is recursve call that will compute power on the half exponent, thereby reducing to O(log n)
        :type n: int
        :rtype: float
    """
        def helper( x, n ):
            if x == 0: return 0
            if n == 0: return 1

            res = helper( x, n // 2 )
            res = res * res
            return x * res if n % 2 else res


        res     = helper( x, abs(n) )
        return res if n >= 0 else 1 / res
