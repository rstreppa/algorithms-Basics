# -*- coding: utf-8 -*-
""" 
@date:          Wed Jan 12 22:00:42 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Algorithms/twoPointers.py
"""
from twoPointers import isPairSum, pairSum, findTriplets_hash, findTriplets
from twoPointers import removeDuplicates, removeDuplicates2, isPalindrome, isPalindrome2, reorderList
from twoPointers import swap, reverse, maxArea
from doublyLinkedList import DoublyLinkedList
from linkedList import LinkedList

def main():
    print('###############################')
    # array declaration
    arr = [2, 3, 5, 8, 9, 10, 11]
     
    # value to search
    val = 17
     
    print(isPairSum(arr, len(arr), val))
    
    print('###############################')
    llist = DoublyLinkedList()
    for item in arr:
        llist.append(item)
    pairSum( llist.head, val )
    print('###############################')  
    arr = [0, -1, 2, -3, 1]
    n = len(arr)
    findTriplets_hash(arr, n)
    print('###############################') 
    findTriplets(arr, n)
    print('###############################')
    nums    = [0,0,1,1,1,2,2,3,3,4]
    k       = removeDuplicates( nums )
    print(k)
    print(nums[:k])
    nums = [1,1,2]
    k       = removeDuplicates( nums )
    print(k)
    print(nums[:k])
    nums    = [0,0,1,1,1,2,2,3,3,4]
    print('######## removeDuplicates2 #######################')
    k       = removeDuplicates2( nums )
    print(k)
    print(nums[:k])
    print('###############################')
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(4)
    llist.push(20) 
    print( isPalindrome(llist.head) ) 
    print( isPalindrome2(llist.head) )
    print('###############################')
    llist = LinkedList()
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4) 
    llist.push(3)
    llist.push(2) 
    llist.push(1)
    llist.printList()
    print('###############################')
    reorderList(llist.head)
    llist.printList()
    print('###############################')
    arr = [1,2,3,4,5,6]
    swap(arr,0,3)
    print(arr)
    reverse(arr)
    print(arr)
    print('###############################')
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))
    print('###############################')