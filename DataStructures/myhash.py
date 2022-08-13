# -*- coding: utf-8 -*-
""" 
@date:          Tue Feb  1 21:06:46 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   implementation and simple prolperties of hash table
"""

import math
from collections import Counter


def largestUniqueNumber(A):
    ''' Given an array of integers A, return the largest integer that only occurs once.
        If no integer occurs once, return -1. 
    '''
    d = {}
    for elem in A:
        d[elem] = d.get(elem, 0) + 1
    arr = []
    for k, v in d.items():
        if v == 1:
            arr.append(k)
    return -1 if not arr else sorted(arr)[-1]

def countCharacters(words, chars):
    ''' You are given an array of strings words and a string chars.
        A string is good if it can be formed by characters from chars (each character can only be used once).
        Return the sum of lengths of all good strings in words.
    ''' 
    d = {}
    for c in chars:
        d[c] = d.get(c, 0) + 1
 
    def check(word, chars, d):
        if len(word) > len(chars):
            return False
        temp = {}
        for c in word:
            temp[c] = temp.get(c, 0) + 1
            if c not in d.keys() or d[c] < temp[c]:
                return False
        return True

    return sum(len(word) for word in words if check(word, chars, d))       
        
def calculateTime(keyboard, word):
    ''' There is a special keyboard with all keys in a single row.
        You have given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25), 
        initially your finger is at index 0. 
        To type a character, you have to move your finger to the index of the desired character. 
        The time taken to move your finger from index i to index j is |i – j|.
        You want to type a string word. Write a program to calculate how much time it takes to type it with one finger.
    '''
    res     = 0
    d       = {}
    for i, c in enumerate(keyboard):
        d[c] = i
    j = 0 
    for c in word:
        res += abs(d[c]-j)
        j   = d[c]
    return res

def uniqueOccurrences(arr):
    ''' Given an array of integers arr, return true 
        if the number of occurrences of each value in the array is unique, or false otherwise.
    '''        
    d = {}
    for elem in arr:
        d[elem] = d.get(elem, 0) + 1
        
    occurrences = []
    for k, v in d.items():
        occurrences.append(v)
    
    dd = {}
    for elem in occurrences:
        dd[elem] = dd.get(elem, 0) + 1
        
    for k, v in dd.items():
        if v > 1:
            return False
    return True

def canFormArray( arr, pieces ):

    """

    :type arr: List[int]

    :type pieces: List[List[int]]

    :rtype: bool

 

    1640. Check Array Formation Through Concatenation

    You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct.

    Your goal is to form arr by concatenating the arrays in pieces in any order.

    However, you are not allowed to reorder the integers in each array pieces[i].

    Return true if it is possible to form the array arr from pieces. Otherwise, return false.

    """

    s = {}

    for piece in pieces:

        s[piece[0]] = piece

    index = 0

    while index < len(arr): 

        if arr[index] not in s:

            return False

        piece = s[arr[index]]

        for i,e in enumerate(piece):

            if i+index >= len(arr):

                return False

            if arr[i+index]!=e:

                return False

        index += len(piece)

    return True

def countKDifference(nums, k):

    """

    :type nums: List[int]

    :type k: int

    :rtype: int

 

    2006. Count Number of Pairs With Absolute Difference K

    Easy

    Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

    """

    res = 0

    d   = {}

    for x in nums:

        if x-k in d:

            res += d[x-k]

        if x+k in d:

            res += d[x+k]

        d[x] = d.get(x, 0) + 1           

    return res       

def kthDistinct(arr, k):

    """

    :type arr: List[str]

    :type k: int

    :rtype: str

 

    2053. Kth Distinct String in an Array

    Easy

 

    A distinct string is a string that is present only once in an array.

    Given an array of strings arr, and an integer k, return the kth distinct string present in arr.

    If there are fewer than k distinct strings, return an empty string "".

    Note that the strings are considered in the order in which they appear in the array.

    """

    a = []

    for i in arr:

        if arr.count(i) == 1:

            a.append(i)

    for i in range(0,len(a)):

        if i + 1 == k:

            return a[i]

    return ""       

 
def mostFrequent(nums, key):

    """

    :type nums: List[int]

    :type key: int

    :rtype: int

 

    2190. Most Frequent Number Following Key In an Array

    Easy

    You are given a 0-indexed integer array nums. You are also given an integer key, which is present in nums.

 

    For every unique integer target in nums, count the number of times target immediately follows an occurrence of key in nums.

    In other words, count the number of indices i such that:

 

    0 <= i <= nums.length - 2,

    nums[i] == key and,

    nums[i + 1] == target.

    Return the target with the maximum count. The test cases will be generated such that the target with maximum count is unique.       

    """

 

    n = len(nums)

    d = {}

    maxcount = 0

    for i in range(n-1):

        if nums[i] == key:

            d[nums[i+1]] = d.get(nums[i+1], 0) + 1

            maxcount = max(maxcount, d[nums[i+1]])

               

    for k, v in d.items():

        if v == maxcount:

            return k

def smallestCommonElement( mat ):
    ''' 1198. Find Smallest Common Element in All Rows
        Given a matrix mat where every row is sorted in increasing order, return the smallest common element in all rows.        
        If there is no common element, return -1
    '''
    setList = []
    for row in mat:
        setList.append( set(row) )
    s = setList[0]
    for i,ss in enumerate(setList, 1):
        s = s.intersection(ss)
    
    if len(s) == 0:
        return  -1
    else:
        return min(s)
    
def longestWPI(hours):
    ''' 1124. Longest Well-Performing Interval
        Medium
        We are given hours, a list of the number of hours worked per day for a given employee.       
        A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.        
        A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.       
        Return the length of the longest well-performing interval.
    '''
    res     = 0
    d       = {}   
    mysum   = 0
    
    for i, h in enumerate(hours):
        mysum += 1 if h > 8 else -1 # adding 1 for tiring and -1 for not tiring
        if mysum > 0:               # if starting from 0 index to i, net tiring is more than non-tiring days
            res = i+1               # storing i+1 since 0-based indexing in array
        else:                       # if number of non-tiring days is equal to or more than tiring days
            if mysum-1 in d:        # since we need positive sum(i.e. tiring days > non-tiring days), 
                                    # that can only reside between appearance of sum and sum-1
                res = max(res,i-d[sum-1])
        if mysum not in d:          # marking occurence index of every sum (cumulative) if not already marked
            d[sum] = i
            
    return res
    
def countPairs(deliciousness):
    ''' 1711. Count Good Meals
        Medium
        A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.       
        You can pick any two different foods to make a good meal.       
        Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, 
        return the number of different good meals you can make from this list modulo 109 + 7.        
        Note that items with different indices are considered different even if they have the same deliciousness value.
       
        O(n) | Python |  similar to 2Sum| HashMap
    '''    
    res1=0
    res2=0
    good_pairs = Counter(deliciousness)
    powers=[]
    
    for i in range(0,22):
        powers.append(2**i)
        
    for num in good_pairs:
        for power in powers:
            if (power-num) in good_pairs:
                if((power-num)!=num):
                    res1=res1+good_pairs[power-num]*good_pairs[num]
                if((power-num)==num and good_pairs[num]!=1):
                    res2=res2+math.comb(good_pairs[num],2)
    return int((res1/2)+res2)%(10**9+7)         

def maxOperations(nums, k):
    ''' 1679. Max Number of K-Sum Pairs
        Medium
        You are given an integer array nums and an integer k.        
        In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.       
        Return the maximum number of operations you can perform on the array.
    '''
    res = 0
    d   = {}            
         
    for e in nums:
        if k-e in d and d[k-e] > 0:
            d[k-e] -= 1
            res    += 1
        else:
            d[e] = d.get(e, 0) + 1
        
    return res
    
def countNicePairs(nums):
    ''' 1814. Count Nice Pairs in an Array
        Medium
        You are given an array nums that consists of non-negative integers. 
        Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. 
        A pair of indices (i, j) is nice if it satisfies all of the following conditions:      
        0 <= i < j < nums.length
        nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.
    '''
    def rev(x):
        arr = []
        res = 0
        while x:
            arr.append( x%10 )
            x /= 10
        arr = arr[::-1]
        for e in arr:
            res = 10*res + e
        return res  
   
    res = 0
    d   = {}
    for num in nums:
        
        reversed_num = int(str(num)[::-1])
        
        looking_for = num - reversed_num
        
        res += d.get(looking_for, 0)
        
        d[looking_for] = d.get(looking_for, 0) + 1
    
    return res %1000000007     

def findJudge(self, n, trust):
    """
        997. Find the Town Judge
        Easy
        In a town, there are n people labeled from 1 to n. 
        There is a rumor that one of these people is secretly the town judge.

        If the town judge exists, then:

        The town judge trusts nobody.
        Everybody (except for the town judge) trusts the town judge.
        There is exactly one person that satisfies properties 1 and 2.
        You are given an array trust where trust[i] = [ai, bi] representing that the person
        labeled ai trusts the person labeled bi.

        Return the label of the town judge if the town judge exists and can be identified, 
        or return -1 otherwise.
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
    """
    d       = defaultdict(set)
    dnot    = defaultdict(set)
    for edge in trust:
        u, v    = edge
        d[v].add(u)
        dnot[u].add(v)
     
    for i in range( 1, n+1 ):
        if len( d[i] ) == n-1 and len( dnot[i] ) == 0:
            return i
    return -1

def commonChars(self, words):
    """
        1002. Find Common Characters
        Easy
        Given a string array words, return an array of all characters that show up in all strings within the words
        (including duplicates). You may return the answer in any order.        
        :type words: List[str]
        :rtype: List[str]
    """
    res         = Counter( words[0] )
    for word in words:
        res     &= Counter( word )
    return list( res.elements() )        

def countCharacters(self, words, chars):
    """
        1160. Find Words That Can Be Formed by Characters
        Easy
        You are given an array of strings words and a string chars.
        A string is good if it can be formed by characters from chars (each character can only be used once).
        Return the sum of lengths of all good strings in words.        

        :type words: List[str]
        :type chars: str
        :rtype: int
    """
    res             = 0
    flag            = True

    charDict        = Counter(chars)
        
    for word in words:
        wordDict    = Counter(word)

        for k , v in wordDict.items():
            if k in charDict and v<= charDict[k]:
                continue
            else:
                flag = False
                break
        
        if flag:
            res     += len(word)
        else:
            flag    = True
    

    return res        
