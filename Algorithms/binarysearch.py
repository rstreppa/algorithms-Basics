# -*- coding: utf-8 -*-
""" 
@date:          Sat Feb  5 14:35:12 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   simple binary search problems
"""

import bisect
import math

def fixedPoint(A):
    ''' Given an array A of distinct integers sorted in ascending order, 
        return the smallest index i that satisfies A[i] == i.  Return -1 if no such i exists.
    '''
    
    low, high = 0, len(A)-1
    while low <= high:
        mid = low + (high-low)//2
        if A[mid] >= mid:
            high = mid-1
        else:
            low = mid+1
    return low if A[low] == low else -1

def numSmallerByFrequency(queries, words):
    ''' Let the function f(s) be the frequency of the lexicographically smallest character 
        in a non-empty string s. For example, if s = "dcce" then f(s) = 2 because 
        the lexicographically smallest character is 'c', which has a frequency of 2.
        You are given an array of strings words and another array of query strings queries. 
        For each query queries[i], count the number of words in words such that f(queries[i]) < f(W) for each W in words.
        Return an integer array answer, where each answer[i] is the answer to the ith query.
    '''
    def f(word):
        s = {}
        for c in word:
            s[c]    = s.get(c, 0) + 1
        res     = 0
        char    = 1000
        for k, v in s.items():
            if ord(k) < char:
                char    = ord(k)
                res     = s[k]
        return  res
    
    res = []
    for i, query in enumerate(queries):
        count = 0
        for word in words:
            if f(query) < f(word):
                count += 1
        res.append(count)
    return res

def numSmallerByFrequency2(queries, words):
    ''' bisect solution '''
    words_freq = sorted( word.count( min( word ) ) for word in words )
    return [ len( words ) - bisect.bisect_right( words_freq, query.count( min( query ) ) ) for query in queries ]    

def findMissing(arr):
    ''' Given an array that represents elements of arithmetic progression in order. 
        One element is missing in the progression, find the missing number. 
    '''
    n       = len(arr)
    diff    = ( arr[n-1] - arr[0] ) // n
    low     = 0 
    high    = n-1
    
    def check(arr, d, x):
        return arr[x] != arr[0] + d*x

    while low <= high:
        mid = low + (high - low) // 2
        if check(arr, diff, mid):
            high = mid-1
        else:
            low = mid+1
    return arr[0] + diff*low
    
def findSpecialInteger(arr):
    ''' Given an integer array sorted in non-decreasing order, 
        there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
    '''
    d = {}
    n = len(arr)
    for elem in arr:
        d[elem] = d.get(elem, 0) + 1
    for k, v in d.items():
        if float(v)/n > 0.25:
            return k 
    return -1 

def findSpecialInteger2(arr):
    ''' using binary search '''
    n           = len(arr)
    low         = 0
    high        = n-1  
    mid         = low + (high - low) // 2
    return arr[mid]    
        
def findTheDistanceValue(arr1, arr2, d):
    ''' Given two integer arrays arr1 and arr2, and the integer d, 
        return the distance value between the two arrays.
        The distance value is defined as the number of elements arr1[i] 
        such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
        
        Sort arr2 in ascending order. and do two binary searches for each element to determine the range of [a-d, a+d], 
        if that range is empty we increase the counter
        Time complexity: O(mlogm + nlogm)
        Space complexity: O(1)
    '''
    res     = 0
    arr2.sort()
    l       = len(arr2)
    for num in arr1:
        index   = bisect.bisect_left(arr2, num)
        min_dist = float('inf')
        if index > 0:
            min_dist = min(min_dist, abs(num-arr2[index-1]))
        if index < l:
            min_dist = min(min_dist, abs(num-arr2[index]))
        if min_dist > d:
            res += 1 
    return res

def findKthPositive(arr, k):
    ''' Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
        Find the kth positive integer that is missing from this array. 
        Example: [2, 3, 4, 7, 11]. Aim: find the 5-th missing number. 
        We need to start finding from the number 7. This is very natural to think.
        The index of 7 is what we want to get using Binary Search. 
        After that, we need to compute how many numbers are missing before 7, that is, 7 - 3(index of 7) - 1 = 3. 
        So the left missing number is 5 - 3 = 2. 
        So just start from 7, and count 2 more, which gives 7 + 2 = 9.
        
        Finally, to write like left + 1 < right is the standard writing method that ACM players always use. 
        This has a benefit that, it will never happen
        the case of crossing border. But the side effect is that, after Binary Search, either left or right can be the result both. 
        So we need to judge after while loop. Although this is a side effect, but it is like a template when we judge it at last. 
        So I can say, the benefit > side effect when
        we use left + 1 < right. Otherwise, writing left <= right or left < right will make you confused in many problems.
    '''
    left    = 0
    right   = len(arr) - 1
    
    while left + 1 < right:
        
        mid = left + (right - left) // 2
        
        # the missing number until i-th number
        if arr[mid] - mid - 1 < k:
            left = mid
        else:
            right = mid - 1
    
    if arr[right] - right - 1 < k:
        return arr[right] + (k - (arr[right] - right - 1))
    elif arr[left] - left - 1 < k:
        return arr[left] + (k - (arr[left] - left - 1))
    else:
        return k    