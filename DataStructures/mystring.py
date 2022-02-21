# -*- coding: utf-8 -*-
""" 
@date:          Mon Jan 31 22:11:03 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   simple properties of string
"""

def confusingNumber(N):
    ''' Given a number N, return true if and only if it is a confusing number, which satisfies the following condition:
        We can rotate digits by 180 degrees to form new digits. 
        When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. 
        When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid. 
        A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.
    '''
    d = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6',
    }
    
    q = []
    
    S = str(N)
    
    for c in reversed(S):
        if c not in d:
            return False
        q.append(d[c])
    
    return False if ''.join(q) == S else True

def countLetters(S):
    ''' Given a string s, return the number of substrings that have only one distinct letter. 
        a string with k consecutive chars has ```k*(k+1)/2``` combinations
    '''
    # count = 0
    # for i in range(len(S)):
    #     for j in range(i+1, len(S)+1):
    #         sub = S[i:j]
    #         s   = set(sub)
    #         if len(s) == 1:
    #             count += 1
    # return count

    count   = 1
    total   = 0
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            total += count * (count + 1) // 2
            count = 1
        else:
            count += 1
    total += count * (count + 1) // 2 # add last substring
    return total