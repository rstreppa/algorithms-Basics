# -*- coding: utf-8 -*-
""" 
@date:          Wed Jan 12 21:58:43 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   two pointer algorithm examples and problems
"""
from functools import reduce

# https://leetcode.com/articles/two-pointer-technique/

def isPairSum(A, N, X):
    
    # sort Array
    A = sorted( A )
 
    # represents first pointer
    i = 0
 
    # represents second pointer
    j = N - 1
 
    while(i < j):
       
        # If we find a pair
        if (A[i] + A[j] == X):
            return True
 
        # If sum of elements at current
        # pointers is less, we move towards
        # higher values by doing i += 1
        elif(A[i] + A[j] < X):
            i += 1
 
        # If sum of elements at current
        # pointers is more, we move towards
        # lower values by doing j -= 1
        else:
            j -= 1
    return False
 
def pairSum( head, x ):
    
    first   = head 
    second  = head 
       
    while second.next:
        second = second.next
        
    found = False
    
    while first and second and ( first != second ) and ( second.next != first ):
        if ( first.data + second.data == x ):
            found = True
            print( "(",  first.data, ", ", second.data, ")" )
            first  = first.next
            second = second.prev
        elif ( first.data + second.data < x ):
            first = first.next
        else:
            second = second.prev
    
    if not found:
        print("No pair found")
        
def findTriplets_hash(arr, n):
    ''' function to print triplets with 0 sum '''
    found = False
    for i in range(n - 1):

        # Find all pairs with sum 
        # equals to "-arr[i]" 
        s = set()
        for j in range(i + 1, n):
            x = -(arr[i] + arr[j])
            if x in s:
                print(x, arr[i], arr[j])
                found = True
            else:
                s.add(arr[j])
    if found == False:
        print("No Triplet Found")    

def findTriplets(arr, n):
    ''' function to print triplets with 0 sum: two pointer technique '''

    found = False

    # sort array elements
    arr.sort()

    for i in range(0, n-1):
    
        # initialize left and right
        l = i + 1
        r = n - 1
        x = arr[i]
        while (l < r):
        
            if (x + arr[l] + arr[r] == 0):
                # print elements if it's sum is zero
                print(x, arr[l], arr[r])
                l+=1
                r-=1
                found = True
            

            # If sum of three elements is less
            # than zero then increment in left
            elif (x + arr[l] + arr[r] < 0):
                l+=1

            # if sum is greater than zero than
            # decrement in right side
            else:
                r-=1
        
    if (found == False):
        print(" No Triplet Found")

def threeSum(nums):
    """
    15. 3Sum
    Medium
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.
    
    Hash map solution: same idea as preceding but slightly different to pass test cases
    The problem wants to find all ABC so that A+B+C=0. We can use two for-loop to find out all the combinations of A, B. In each combination, we look for C.
    If we again use a for-loop to find C, the time complexity would be O(N3). Therefore we need to reduce the time to find C.
    It’s natural to think of dictionary, because it has a O(1) time for lookup a value. However, how can we make sure we don’t find duplicates?
    # Avoid duplicates:
    we can solve case #2 and #3 together. If we build a dictionary like this:
    
    key = A, value = largest index of A.
    
    then we can rule out the values occurred before the second pointer, or itself.    

    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res     = set()
    nums    = sorted(nums)
    n       = len(nums)
    d       = {}
    for i in range(n):
        d[nums[i]]  = i
    for i in range(n):
        if i !=0 and nums[i] == nums[i-1]:
            continue
        twoSum  = -nums[i]
        for j in range(i+1, n):
            target = twoSum - nums[j]
            if target in d and d[target] > j:
                res.add( (-twoSum, nums[j], target ) )
    return res
        
def threeSumClosest(nums, target):
    """
    16. 3Sum Closest
    Medium
    Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
    Return the sum of the three integers.
    You may assume that each input would have exactly one solution.    

    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # two pointers I would say it's the way to go
    nums    = sorted(nums)
    n       = len(nums)
    res     = sys.maxsize
    for i in range(0, n-1):
        l       = i+1
        r       = n-1
        while l < r:
            val = nums[i] + nums[l] + nums[r]
            if val < target:
                l += 1
            else:
                r -= 1
            if abs(val-target) < abs(res-target):
                res = val
    return res        
        

def fourSum(nums, target):
    """
    18. 4Sum
    Medium
    Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target
    You may return the answer in any order.
    
    Easy two pointer technique
    Notice that you remove duplicate solutions by returning a set
    
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    # two pointer I would say
    nums    = sorted(nums)
    n       = len(nums)
    res     = set()
    for i in range( 0, n-2 ):
        for j in range( i+1, n-1 ):
            l   = j+1
            r   = n-1
            while l < r:
                if nums[i] + nums[j] + nums[l] + nums[r] == target:
                    res.add( ( nums[i], nums[j], nums[l], nums[r] ) )
                    l += 1
                    r -= 1
                elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
    return res
    
    
    
def removeDuplicates( nums ):
    ''' Remove Duplicates from Sorted Array  in-place such that each unique element appears only once. 
        The relative order of the elements should be kept the same. 
        you must instead have the result be placed in the first part of the array nums. 
        More formally, if there are k elements after removing the duplicates, 
        then the first k elements of nums should hold the final result. 
        It does not matter what you leave beyond the first k elements.'''
    count   = 1
    N       = len(nums)
    i       = 0
    elem    = nums[0]
    for j in range(1, N):
        if nums[j]  == elem:
            continue
        else:
            elem = nums[j]
            i += 1
            nums[i] = elem
            count += 1
            
    return count
        
def removeDuplicates2( nums ):
    if len(nums) == 0: return 0
    if len(nums) == 1: return 1
    
    # nums = [0,0,1,1,1,2,2,3,3,4]
    j = 1 # slower pointer, only move when meet unique number
    for i in range(1, len(nums)): # faster pointer, i will iterate over all element in nums
        if nums[i] != nums[i-1]: # when nums[i] is a unique number, assign it to nums[j]
            nums[j] = nums[i]
            j += 1
    # after for loop, i = 9, j = 5, nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
    # we can see the nums[:5] is the unique number list we want 
    return j

def isPalindrome(head):
    '''Given the head of a singly linked list, return true if it is a palindrome.'''
    arr = []
    arr.append(head.data)
    while head.next:
        head = head.next
        arr.append(head.data)
    return arr == arr[::-1]
    
    
def isPalindrome2(head):
    ''' We can use fast slow pointer to find the middle point and reverse the first half or second half to compare with the other half. '''
    slow    = head
    fast    = head
    stack   = []
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next 
    
    if fast:
        slow = slow.next
    
    while slow:
        top = stack.pop()
        if slow.data != top :
            return False
        slow = slow.next 
        
    return True
    
    
def removeNthFromEnd(head, n):
    """
    19. Remove Nth Node From End of List
    Medium
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    
    We are given a linked list and a number n, and we are required to remove the nth from the end of the list. 
    Since we are removing the nth node, we need to link next pointer of (n - 1)th node to the (n + 1)th node.
    Once we remove the node, we need to return the head of the modified list.
    
    Initialize two pointers slow and fast, pointing to the head of the linked list.
    Move fast pointer n steps ahead.
    Now, move both slow and fast one step at a time unless fast reaches to the end. The fast pointer will definitely reach to the end before slow because it is ahead.
    When we fast pointer reaches to the end, the slow pointer will be n steps behind it i.e., n steps behind the end of the list.
    At that point, we will remove the node and link it to the next of current node.    
        
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    # Two pointers - fast and slow
    slow = head
    fast = head
    # Move fast pointer n steps ahead
    for i in range(0, n):
        if not fast.next:
            # If n is equal to the number of nodes, delete the head node
            if i == n - 1:
                head = head.next
            return head
        fast = fast.next
    # Loop until fast node reaches to the end
    # Now we will move both slow and fast pointers
    while fast.next:
        slow = slow.next
        fast = fast.next
    # Delink the nth node from last
    if slow.next:
        slow.next = slow.next.next
    return head    
    
    
def reorderList(head):
    ''' You are given the head of a singly linked-list. The list can be represented as:
        L0 → L1 → … → Ln - 1 → Ln
        Reorder the list to be on the following form:
        
        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
        You may not modify the values in the list's nodes. Only nodes themselves may be changed.
    '''
    if not head:
        return
    
    # split
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    head1, head2 = head, slow.next
    slow.next = None
    
    # reverse second half  
    cur, pre = head2, None
    while cur:
        nex = cur.next      # Store next
        cur.next = pre      # Reverse current node's pointer 
        
        pre = cur           # Move pointers one position ahead
        cur = nex
    
    # merge
    cur1, cur2 = head1, pre
    while cur2:
        nex1, nex2 = cur1.next, cur2.next   # Store next
        
        cur1.next = cur2                    # Intertwine pointers  
        cur2.next = nex1
        
        cur1, cur2 = nex1, nex2             # Move pointers one position ahead
   

def swap( arr, i, j):
    ''' swap characters in string '''
    temp     = arr[i]
    arr[i]   = arr[j]
    arr[j]   = temp
    
def reverse(arr):
    ''' reverse an array using two pointers '''
    i, j = 0, len(arr)-1
    while i<j:
        swap(arr, i, j)
        i += 1 
        j -= 1
        
def maxArea(height):
    ''' 11. Container With Most Water You are given an integer array height of length n. 
        There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
        Find two lines that together with the x-axis form a container, such that the container contains the most water.
        Return the maximum amount of water a container can store.'''
    res = 0  
    
    i, j = 0, len(height)-1
    while i < j:
        water = (j-i) * min(height[i], height[j])
        if water > res:
            res = water 
        if height[i+1] >= height[i]:
            i+=1
        elif height[j-1] >= height[j]:
            j-=1
        else:
            i+=1 
            j-=1 
            
    return res

def twoSum(nums, target):
    ''' Given an array of integers nums and an integer target, return indices of the two numbers 
        such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order
    '''
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n] = i

def sortedSquares(nums):
    ''' 
        977. Squares of a Sorted Array
        Given an integer array nums sorted in non-decreasing order, 
        return an array of the squares of each number sorted in non-decreasing order. 
        Squaring each element and sorting the new array is very trivial, 
        could you find an O(n) solution using a different approach?
    '''
    n       = len(nums)
    l       = 0
    r       = n-1
    res     = []
    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            res.append(nums[l]**2)
            l   += 1
        else:
            res.append(nums[r]**2)
            r   -= 1
    return res[::-1]


def backspaceCompare(s, t):
    ''' Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
        '#' means a backspace character.
        Note that after backspacing an empty text, the text will continue empty.
    '''
    def back(res, c):
        ''' add chars if not back space # '''
        if c != '#': 
            res.append(c)
        elif res: 
            res.pop()
        return res 
    
    return reduce(back, s, []) == reduce(back, t, []) 

def backspaceCompare2(S, T):
    ''' Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
        '#' means a backspace character.
        Note that after backspacing an empty text, the text will continue empty.
        Two pointeres technique
    ''' 
    back = lambda res, c: res[:-1] if c == '#' else res + c
    return reduce(back, S, "") == reduce(back, T, "")

def backspaceCompare3(S, T):
    ''' Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
        '#' means a backspace character.
        Note that after backspacing an empty text, the text will continue empty.
        Two pointeres technique
    ''' 
    i, j = len(S) - 1, len(T) - 1
    backS = backT = 0
    while True:
        while i >= 0 and (backS or S[i] == '#'):
            backS += 1 if S[i] == '#' else -1
            i -= 1
        while j >= 0 and (backT or T[j] == '#'):
            backT += 1 if T[j] == '#' else -1
            j -= 1
        if not (i >= 0 and j >= 0 and S[i] == T[j]):
            return i == j == -1
        i, j = i - 1, j - 1


def maxProfit(self, prices):
    """
    121. Best Time to Buy and Sell Stock
    Easy
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    you cannot take max(prices) - min(prices) as time goes forward and they could be reversed
    
    Two Pointer technique: l = buy r = sell
    
    when prices(l) > prices(r) you are going to update the pointers and have l point to the smaller value
    when prices(l) < prices(r) we just update the right pointer
    
    O(n) time O(1) spoace because we just used two pointers and no extra space
    
    :type prices: List[int]
    :rtype: int
    """
    
    l               = 0     # l = buy
    r               = 1     # r = sell
    res             = 0     # max profit
    
    while r < len(prices):
        # profitable transaction?
        if prices[l] < prices[r]:
            profit  = prices[r] - prices[l]
            res     = max( res, profit )    # potentially update the max
        else:
            l       = r     # switch left to right since right is lower
        r           += 1    # always increment right pointer regardless
            
    return res

