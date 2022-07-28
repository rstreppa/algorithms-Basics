# -*- coding: utf-8 -*-
""" 
@date:          Tue Jul 26 19:57:50 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   Implementation and simple properties of sliding window algorithm
"""

def solve(arr, queries):
    ''' 
        https://www.hackerrank.com/challenges/queries-with-fixed-length/problem?isFullScreen=true
        Really look at the problem
        It's min_{0<=i<=n-d} max_{i<=j<=i+d} a_j
        Instead of nested min max you keep a sliding window updating max and min in one run O(n)
        Textbook example really!!!
        
        Consider an -integer sequence, . We perform a query on  by using an integer, , to calculate the result of the following expression:
        In other words, if we let , then you need to calculate .

        Given  and  queries, return a list of answers to each query.
        Example

        The first query uses all of the subarrays of length : . The maxima of the subarrays are . The minimum of these is .

        The second query uses all of the subarrays of length : . The maxima of the subarrays are . The minimum of these is .

        Return .
    '''
    # Write your code here
    res     = []
    for d in queries:
        maxnum  = max(arr[:d])
        minnum  = maxnum
        
        # main logic
        for i in range( d, len(arr) ):
            # if element goes out of window
            if arr[i-d] == maxnum:
                maxnum = max(arr[i-d+1:i+1])
            # new element is greater than maxnum
            elif arr[i] > maxnum:
                maxnum = arr[i]
    
            # update overall minimum
            if maxnum < minnum:
                minnum = maxnum
            
        res.append(minnum)
    
    return res


def lengthOfLongestSubstring(s):
    """
    3. Longest Substring Without Repeating Characters
    Medium
    Given a string s, find the length of the longest substring without repeating characters.
    Are you thinking what I am thinking 🤔? Yes, this is a classic example of a problem that can be solved using the legendary technique - Sliding Window Algorithm.

    Following are the steps that we will follow -

    Have two pointers which will define the starting index start and ending index end of the current window. Both will be 0 at the beginning.
    Declare a Set that will store all the unique characters that we have encountered.
    Declare a variable maxLength that will keep track of the length of the longest valid substring.
    Scan the string from left to right one character at a time.
    If the character has not encountered before i.e., not present in the Set the we will add it and increment the end index. The maxLength will be the maximum of Set.size() and existing maxLength.
    If the character has encounter before, i.e., present in the Set, we will increment the start and we will remove the character at start index of the string.
    Steps #5 and #6 are moving the window.
    After the loop terminates, return maxLength

    :type s: str
    :rtype: int
    """
    # sliding window technique
    n   = len(s)    
    i   = 0
    j   = 0
    res = 0
    ss  = set()
    while i <= j and j < n:
        if s[j] not in ss:
            ss.add( s[j] )
            length  = j-i+1   # alternatively length = len(ss)
            res     = max( res, length )
            j       += 1
        else:
            ss.remove(s[i])
            i += 1
    return res




