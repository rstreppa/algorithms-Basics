# -*- coding: utf-8 -*-
""" 
@date:          Sat Jan 22 10:36:03 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   simple bit manipulation problems
"""

import operator
import math

def singleNumber(nums):
    ''' https://hackernoon.com/xor-the-magical-bit-wise-operator-24d3012ed821
        Solution using XOR
        
        Bitwise XOR ( ^ ) like the other operators (except ~) 
        also take two equal-length bit patterns. 
        If both bits in the compared position of the bit patterns are 0 or 1, 
        the bit in the resulting bit pattern is 0, otherwise 1.
    '''
    res = 0
    for num in nums:
        res ^= num
    return res

def isPowerof2(x):
    ''' Logic: All the power of 2 have only single bit set e.g. 16 (00010000).
    	If we minus 1 from this, all the bits from LSB to set bit get toggled,
        ., 16 - 1 = 15 (00001111).Now if we AND x with(x - 1) and the result is 0
	    then we can say that x is power of 2 otherwise not.
	    We have to take extra care when x = 0.
    '''
    return x and operator.not_( operator.and_( x, x-1 ) ) 

def log2(x):
    ''' log2 by right shift''' 
    res = 0
    while x:
        x   = operator.rshift(x, 1)
        res += 1
    return res-1

def myswap(a, b):
    ''' swap using XOR logic without extra variable ''' 
    a ^= b
    b ^= a
    a ^= b
    return a, b

def power2( n ):
    ''' power of 2 by left shift''' 
    return operator.lshift(1, n)

def rightmostOne(n):
    ''' Return the rightmost 1 in the binary representation of a number. 
        The property is, the difference between a binary number n and n-1 is 
        all the bits on the right of the rightmost 1 are flipped including the rightmost 1. 
    '''
    return n ^ operator.and_(n, n-1)
 
    
def binaryArray(n):
    ''' return an array of the binary representation of a number'''
    binary = []
    while n:
        binary.append( n % 2 )
        n   = math.floor( n / 2 )
    return binary[::-1]  
  
def countBits(n):
    ''' Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
        ans[i] is the number of 1's in the binary representation of i
    '''
    res = []
    for i in range(n+1):
        res.append(sum(binaryArray(i)))
    return res

def countBits2(n):
    ''' Can you do it in linear time O(n) and possibly in a single pass? 
        All whole numbers can be represented by 2N (even) and 2N+1 (odd).
        For a given binary number, multiplying by 2 is the same as adding a zero at the end 
        (just as we just add a zero when multiplying by ten in base 10).
        Since multiplying by 2 just adds a zero, then any number and its double will have the same number of 1's. 
        Likewise, doubling a number and adding one will increase the count by exactly 1. Or:        
        countBits(N) = countBits(2N)
        countBits(N)+1 = countBits(2N+1)
        Thus we can see that any number will have the same bit count as half that number, 
        with an extra one if it's an odd number. We iterate through the range of numbers 
        and calculate each bit count successively in this manner:    
    ''' 
    dp      = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = dp[i//2] + i%2
    return dp
    