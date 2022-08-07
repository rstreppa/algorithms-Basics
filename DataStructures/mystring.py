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

def multiply(self, num1, num2):
    """
        43. Multiply Strings
        Medium
        Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
        Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
        
        So this isn’t a very difficult problem, but if you just do the regular multiplication, you can figure it out. Figure below:
        The basic idea is as follows:
        (1) can first flip the string, that is, start from the low order calculation.
        (2) use an array to maintain the final result, updating it every time you multiply it, but pay attention to the carry case () pay attention 
            to the two  points, the same bit to add the carry, from low to high multiplication is carried. )
        (3) finally, the 0 in front of the array is discarded and converted to string output.            
        
        
        :type num1: str
        :type num2: str
        :rtype: str
    """
    res = [0] * (len(num1) + len(num2))  # Initialization, array to hold the product.
    pos = len(res) - 1

    for n1 in reversed(num1):
        tempPos = pos
        for n2 in reversed(num2):
            res[tempPos] += int(n1) * int(n2)
            res[tempPos - 1] += res[tempPos] // 10  # Offset
            res[tempPos] %= 10  # fractional remainder
            tempPos -= 1
        pos -= 1

    st = 0
    while st < len(res) - 1 and res[st] == 0:  # How many zeros are in front of a statistic?
        st += 1
    return ''.join(map(str, res[st:])) # Remove the 0, then turn it into a string, and return

def numberOfLines(self, widths, s):
    """
        806. Number of Lines To Write String
        Easy
        You are given a string s of lowercase English letters and an array widths denoting how many pixels wide each lowercase English letter is. 
        Specifically, widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.

        You are trying to write s across several lines, where each line is no longer than 100 pixels. 
        Starting at the beginning of s, write as many letters on the first line such that the total width does not exceed 100 pixels. 
        Then, from where you stopped in s, continue writing as many letters as you can on the second line. Continue this process until you have written all of s.

        Return an array result of length 2 where:

        result[0] is the total number of lines.
        result[1] is the width of the last line in pixels.
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
    """
    lines = 1
    total = 0
    for c in s:
        total += widths[ord(c) - ord('a')]
        if total > 100:
            lines += 1
            total = widths[ord(c) - ord('a')]
    return [lines, total]            
