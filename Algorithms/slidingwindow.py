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
