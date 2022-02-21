# -*- coding: utf-8 -*-
""" 
@date:          Wed Feb 16 20:06:27 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   Implementation and simple properties of a binary heap
"""

import heapq


class BinHeap:
    ''' https://runestone.academy/ns/books/published/pythonds/Trees/BinaryHeapImplementation.html '''
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    def percolateUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2  
          
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percolateUp(self.currentSize)
        
    def percolateDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
            
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percolateDown(1)
        return retval
    
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percolateDown(i)
            i = i - 1

def lastStoneWeight(stones):
    ''' 1046. Last Stone Weight
        You are given an array of integers stones where stones[i] is the weight of the ith stone.
        We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. 
        The result of this smash is:
        If x == y, both stones are destroyed, and
        If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
        At the end of the game, there is at most one stone left.       
        Return the smallest possible weight of the left stone. If there are no stones left, return 0.
    '''
    max_heap = [-x for x in stones]
    heapq.heapify(max_heap)
    for i in range(len(stones)-1):
        x, y = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
        heapq.heappush(max_heap, -abs(x-y))
    return -max_heap[0]

def minStoneSum(piles, k):
    ''' 1962. Remove Stones to Minimize the Total
        You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, 
        and an integer k. You should apply the following operation exactly k times:       
        Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
        Notice that you can apply the operation on the same pile more than once.        
        Return the minimum possible total number of stones remaining after applying the k operations.
    '''    
    for i, x in enumerate(piles):
        piles[i] = -x
    heapq.heapify(piles)
    for i in range(k):
        heapq.heappush(piles, heapq.heappop(piles)//2)
    return -sum(piles)    