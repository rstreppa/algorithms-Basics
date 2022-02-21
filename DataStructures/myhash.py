# -*- coding: utf-8 -*-
""" 
@date:          Tue Feb  1 21:06:46 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   implementation and simple prolperties of hash table
"""

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
