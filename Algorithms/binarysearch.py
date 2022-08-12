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
    
def search(nums, target):
    """
    33. Search in Rotated Sorted Array
    Medium
    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
    such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
    For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
    Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
    You must write an algorithm with O(log n) runtime complexity. 
    
    The approach is simple if we are able to find the index from where the given array is rotated. We can follow below steps to solve this problem —
    Find the index where the array is rotated. Notice if a sorted array is rotated then the rightmost element will not be the biggest element in the array.
    Using the information in step #1, we can perform binary search to find the index where the array is rotated.
    Once we have found that index, then we can easily determine in which half (array will be divided into two halves by the pivot index) of the array 
    the target lies.
    Notice, the two halves are themselves will be sorted (this is pretty intuitive, right 😄?).
    We can then perform binary search once again in the determined half to find the index of the target element.
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # Special case
    if not nums or len(nums) == 0:
        return -1
    # Left and right pointers for the array
    left, right = 0, len(nums) - 1
    # First step is to find the pivot where the array
    # is rotated
    while left < right:
        # Middle index
        middle = left + (right - left) // 2
        # If the element at the mid is greater than
        # the element at the right then we can say that
        # the array is rotated after middle index
        if nums[middle] > nums[right]:
            left = middle + 1
        # Else, the pivot is in the left part
        else:
            right = middle
    # After the above loop is completed, then the
    # left index will point to the pivot
    pivot = left
    left, right = 0, len(nums) - 1
    # Now we will find in which half of the array,
    # our targetValue is present
    if nums[pivot] <= target and target <= nums[right]:
        left = pivot
    else:
        right = pivot
    # Now perform normal binary search
    while left <= right:
        middle = left + (right - left) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1

def findMin(self, nums):
    """
    153. Find Minimum in Rotated Sorted Array
    Medium
    Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.
    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
    Given the sorted rotated array nums of unique elements, return the minimum element of this array.
    You must write an algorithm that runs in O(log n) time.
    
    keywords sorted and O(log n) compels for a binary search, there's the twist of rotation
    
    find the pivot, find the element that breaks the order
    assuming mid is the minimum, lhs and rhs should be (at least partially) sorted: should we search left or right?
    when you rotate you put larger values on lhs
    if nums[mid] >= nums[0] thenm mid is part of the left sorted portion, which means we want to search to the right (= is edge case when mid==0)
    vice versa if nums[mid] <= nums[n-1], you want to search to the left
    this works only if rotated: if we get to a complete4ly sorted polrtion, we just take the leftmost value
    
    if nums[left] < nums[right] the portion is already sorted, you just take the leftmost and you are done

    :type nums: List[int]
    :rtype: int
    """
    n               = len(nums)
    res             = nums[0]   # you can pick anything as default, pick leftmost
    l               = 0
    r               = n-1
    while l <= r:
        if nums[l] < nums[r]:   # we are in a sorted portion, we take the leftmost
            res     = min(res, nums[l])
            break
        mid         = (r-l)//2 + l
        res         = min(res, nums[mid])
        if nums[mid] >= nums[l]:    # we want to search to the right
            l       = mid+1
        else:
            r       = mid-1
    return res


def searchRange(self, nums, target):
    """
        34. Find First and Last Position of Element in Sorted Array
        Medium
        Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
        If target is not found in the array, return [-1, -1].
        You must write an algorithm with O(log n) runtime complexity.
        
        We will use binary search algorithm to find the first and last occurrences of the target separately.

        1. For first occurrence, we will first find the index of the number and then search again in the left subarray as long as we are finding the number.
        2. For last occurrence, we will first find the index of the number and then search again in the right subarray as long as we are finding the number.

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
    """
    def findFirstOccurrence(nums, target):
        # Left snd right pointers
        left, right = 0, len(nums) - 1
        # Index of first occurrence
        firstOccurrence = -1
        # Loop until the two pointers meet
        while left <= right:
            # Middle index
            middle = left + (right - left) // 2
            # Check if we have found the value
            if target == nums[middle]:
                firstOccurrence = middle
                right = middle - 1
            # If the target is less than the element
            # at the middle index
            elif target < nums[middle]:
                right = middle - 1
            # If the target is greater than the element
            # at the middle index
            else:
                left = middle + 1
        return firstOccurrence


    def findLastOccurrence(nums, target):
        # Left snd right pointers
        left, right = 0, len(nums) - 1
        # Index of first occurrence
        lastOccurrence = -1
        # Loop until the two pointers meet
        while left <= right:
            # Middle index
            middle = left + (right - left) // 2
            # Check if we have found the value
            if target == nums[middle]:
                lastOccurrence = middle
                left = middle + 1
            # If the target is less than the element
            # at the middle index
            elif target < nums[middle]:
                right = middle - 1
            # If the target is greater than the element
            # at the middle index
            else:
                left = middle + 1
        return lastOccurrence

    return [findFirstOccurrence(nums, target), findLastOccurrence(nums, target)]
