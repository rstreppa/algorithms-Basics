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


def isKPalindrome( s, k ):
    """
        Write an efficient algorithm to check if a given string is k–palindrome or not. 
        A string is k–palindrome if it becomes a palindrome on removing at most k characters from it.
        
        Recursive solution
        The worst-case time complexity of the above solution is O(2^n), where n is the length of the input string. 
        The worst case happens when the string contains all different characters. 
        It also requires additional space for the call stack.        
    """
    # Function to check how many characters to delete to turn strings X and Y equal
    def helper(X, m, Y, n):

        # if either string is empty, remove all characters from the other string
        if m == 0 or n == 0:
            return n + m

        # ignore the last characters of both strings if they are the same
        # and recur for the remaining characters
        if X[m - 1] == Y[n - 1]:
            return helper(X, m - 1, Y, n - 1)

        # if the last character of both strings is different

        # remove the last character from the first string and recur
        x = helper(X, m - 1, Y, n)

        # remove the last character from the second string and recur
        y = helper(X, m, Y, n - 1)

        # return one more than the minimum of the above two operations
        return 1 + min(x, y)    
    
    # get reverse of X
    rev = s[::-1]
    return isKPalindrome( s, len(s), rev, len(s) ) <= 2*k

# Function to check if the given string is k–palindrome or not
def isKPalindrome(X, K):
    """
        Write an efficient algorithm to check if a given string is k–palindrome or not. 
        A string is k–palindrome if it becomes a palindrome on removing at most k characters from it.
        
        Dymnamic Programming solution 
        The problem has an optimal substructure and exhibits overlapping subproblems. 
        Since both dynamic programming properties are satisfied, we can save subproblem solutions in memory rather than computing them repeatedly. 
        The dynamic programming is demonstrated below in C++, Java, and Python, which runs in O(n^2) time:        
    """
 
    # 'Y' is a reverse of 'X'
    Y = X[::-1]
 
    n = len(X)
 
    # lookup table to store solution of already computed subproblems
    T = [[0 for x in range(n + 1)] for y in range((n + 1))]
 
    # fill the lookup table `T[][]` in a bottom-up manner
    for i in range(n + 1):
        for j in range(n + 1):
            # if either string is empty, remove all characters from the
            # other string
            if i == 0 or j == 0:
                T[i][j] = i + j
 
            # ignore the last characters of both strings if they are the same
            # and process the remaining characters
            elif X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1]
 
            # if the last character of both strings is different, consider
            # minimum by removing the last character from 'X' and 'Y'
            else:
                T[i][j] = 1 + min(T[i - 1][j], T[i][j - 1])
 
    return T[n][n] <= 2*k

def removeKdigits(self, num, k):
    """
    402. Remove K Digits
    Medium
    Share
    Given string num representing a non-negative integer num, and an integer k, 
    return the smallest possible integer after removing k digits from num.
        
    Monotonic Stack: you want to put numbers keeping them increasing and finally remove 
    from the right the larger ones
    You want to be as greedy as you can
        
    O(n) O(n)
        
    Actually best example to explain a monotonic stack
        
    watch this neecode video
    https://www.youtube.com/watch?v=cFabMOnJaq0
        
    :type num: str
    :type k: int
    :rtype: str
    """
        
    s       = []
    for c in num:
        while k > 0 and s and s[-1] > c: # keep the monotonic stack
            k   -= 1
            s.pop()
        s.append(c)
        
    s       = s[ :len(s)-k ]    # left over chars to be removed from the bottom
    res     = "".join(s)
    return str(int(res)) if res else "0"    # handle leading zeros or empty string 


def addToArrayForm(self, num, k):
    """
    989. Add to Array-Form of Integer
    Easy
    The array-form of an integer num is an array representing its digits in left to right order.

    For example, for num = 1321, the array form is [1,3,2,1].
    Given num, the array-form of an integer, and an integer k, return the array-form 
    of the integer num + k.

    Easy once you get you can exploit strings
        
    :type num: List[int]
    :type k: int
    :rtype: List[int]
    """        
    s           = "".join( str(i) for i in num )
    add         = int(s) + k
    arrStr      = str(add)
    res         = []
    for j in arrStr:
        res.append( int(j) )
    return res      
