# -*- coding: utf-8 -*-
""" 
@date:          Sat Feb  5 20:22:13 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   simple problems involving greedy algorithms
"""

def largestSumAfterKNegations(A, K):
    ''' Given an integer array nums and an integer k, modify the array in the following way:
        choose an index i and replace nums[i] with -nums[i].
        You should apply this process exactly k times. You may choose the same index i multiple times.
        Return the largest possible sum of the array after modifying it in this way.
    '''
    A.sort()
    remain = K
    for i in range(K):
        if A[i] >= 0:
            break
        A[i] = -A[i]
        remain -= 1
    return sum(A) - (remain%2)*min(A)*2   

def twoCitySchedCost(costs):
    ''' A company is planning to interview 2n people. 
        Given the array costs where costs[i] = [aCosti, bCosti], 
        the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
        Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
        
        This arrangement may not divide the candidates evenly. 
        The problem requires you to allocate candidates to each city evenly.
    '''
    #we want to select half people go to A and half people go to B which minimize the total cost
    #we can sort the array by cost1 - cost2
    #it is cheaper for anyone in first half than anyone from second half to buy ticket to city A
    #and vice versa
    #O(nlogn) time and O(1) space

    costs.sort(key = lambda x: x[0] - x[1])  
    res = 0
    for i in range(len(costs)//2):
        res += costs[i][0]
        res += costs[len(costs)-1-i][1]   
    return res    
  
def shortestWay(source, target):
    ''' From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).
        Given two strings source and target, return the minimum number of subsequences of source 
        such that their concatenation equals target. If the task is impossible, return -1.
        
        Brute force: 
        define a starting index i for string source, with an initialized value of 0. 
        Then we loop through each character in the target:
        If the character exists in source after position i (e.g. exists at position j where j>i), 
        we move on to the next character, and set i to the value of j;
        If the character does not exists in source after position i, and i is 0, we return -1 as we cannot form target by using source.
        If the character does not exists in source after position i, and i is not 0, 
        we increment the output count by 1, and set i to 0, and then repeat from step 1.            
    '''
    i = 0
    res = 1
    for c in target:
        i = source.find(c, i)
        if i == -1:
            i = source.find(c)
            if i == -1:
                return -1
            res += 1
        i += 1
    return res

def shortestWay2(source, target):
    ''' Iterate through the source to move pointer in target as much as possible.
        After one iteration, res++.
        If we could come to the end of target, return res.
        If go through one iteration, the pointer in target is not changed, then return -1.
        Time Compleixty: O(n + res * m). n = target.length(). m = source.length().
        Space: O(1).
    '''
    if not source or not target:
        return -1
         
    if len(target) == 0:
        return 0

    res = 0
    m   = len(source)
    n   = len(target)
    cur = 0
    while cur < n:
        temp = cur
        for i in range(m):
            if cur >= n:
                break
            if source[i] == target[cur]:
                cur += 1
        if temp == cur:
            return -1 
        res += 1 
        
    return res

def canJump(nums):
    ''' You are given an integer array nums. You are initially positioned at the array's first index, 
        and each element in the array represents your maximum jump length at that position.
        Return true if you can reach the last index, or false otherwise.
    
        if you think from the front, it can't be a greedy solution
        however, if you think from the back, it IS greedy, why?
        
        when you are at index i, you can jump to index i + nums[i]
        so backwardly, the first goal is jumping to the index, target == len(nums) - 1
        if you find a index i, s.t. i + nums[i] >= len(nums) - 1, which means that as long as we can somehow greedily 
        find a index j, s.t. j + nums[j] >= i, then we can sure we can jump from j to i.
        So we simply change target to i, and continuously doing backward!!
        And in the end, since we are in the index 0 at the begining, and we keep updating our goal to i,
        which means that if we (somehow) can jump to 0, which we already did, then we must be able to jump to len(nums) - 1!!        
    '''
    target = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= target:
            target = i
    return target == 0    