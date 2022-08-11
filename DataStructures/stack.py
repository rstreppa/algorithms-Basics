# -*- coding: utf-8 -*-
""" 
@date:          Tue Jan 11 21:52:32 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   implementation and simple properties of a stack 
"""

from collections import deque
from queue import LifoQueue


class Stack():
    def __init__( self ):
        self.stack = []
    
    def push( self, data ):
        '''Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)'''
        self.stack.append( data )
    
    def pop( self ):
        ''' Deletes the topmost element of the stack – Time Compl exity: O(1)'''
        return self.stack.pop()
   
    def size( self ):
        ''' Returns the size of the stack – Time Complexity: O(1) '''
        return len( self.stack )
    
    def top( self ):
        ''' Returns a reference to the topmost element of the stack – Time Complexity: O(1) '''
        return self.stack[-1]
    
    def empty( self ):
        ''' Returns whether the stack is empty – Time Complexity: O(1) '''
        if self.size() == 0:
            return True
        else:
            return False
    def print( self ):
        for elem in self.stack:
            print( elem, end=' ')
            
class Stack2():
    def __init__( self ):
        ''' stack implementation using collections.deque'''
        self.stack = deque()
        
    def push( self, data ):
        '''Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)'''
        self.stack.append( data )
    
    def pop( self ):
        ''' Deletes the topmost element of the stack – Time Compl exity: O(1)'''
        return self.stack.pop()
   
class Stack3():
    def __init__( self ):
        ''' stack implementation using queue module '''
        self.stack = LifoQueue(maxsize=100)
        
    def push( self, data ):
        '''Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)'''
        self.stack.put( data )
    
    def pop( self ):
        ''' Deletes the topmost element of the stack – Time Compl exity: O(1)'''
        return self.stack.get()
   
    def size( self ):
        ''' Returns the size of the stack – Time Complexity: O(1) '''
        return self.qsize()
           
def reverseStackUsingTwoStacks( S ):
    ''' Function to reverse a stack using two stacks '''
    
    # Two additional stacks
    A = Stack()
    B = Stack()
        
    # Transfer all elements
    # from the stack S to A
    while S.size() > 0:
        A.push(S.top())
        S.pop()
        
    # Transfer all elements
    # from the stack A to B
    while A.size() > 0:
        B.push(A.top())
        A.pop() 

    # Transfer all elements
    # from the stack B to S
    while B.size() > 0:
        S.push(B.top())
        B.pop()
        
def transfer( s1, s2, n ):
    ''' Function to transfer elements of the stack s1 to the stack s2 '''
    
    for i in range(n):
        # Store the top element
        # in a temporary variable
        temp = s1.top()
 
        # Pop out of the stack
        s1.pop()
 
        # Push it into s2
        s2.push(temp)
        
def reverse_stack_by_using_extra_stack(s, n):
    ''' Function to reverse a stack using another stack '''

    s2 = Stack()
     
    for i in range(n):
 
        # Store the top element
        # of the given stack
        x = s.top()
 
        # Pop that element
        # out of the stack
        s.pop()
 
        transfer(s, s2, n - i - 1)
        s.push(x)
        transfer(s2, s, n - i - 1)

def insertAtBottom(stack, item):
    ''' Below is a recursive function that inserts an element at the bottom of a stack.'''
    if stack.empty():
        stack.push( item )
    else:
        temp = stack.pop()
        insertAtBottom(stack, item)
        stack.push( temp )
    
def reverse(stack):
    ''' Below is the function that reverses the given stack using insertAtBottom()'''
    if not stack.empty():
        temp = stack.pop()
        reverse(stack)
        insertAtBottom(stack, temp)

def isValid(self, s):
    """
    20. Valid Parentheses
    Easy
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

    Easy to solve using a stack

    :type s: str
    :rtype: bool
    """
    stack = []
    for c in s:
        if not stack:
            stack.append(c)
        elif    ( c == ')' and stack[-1] == '(' ) or \
                ( c == ']' and stack[-1] == '[' ) or \
                ( c == '}' and stack[-1] == '{' ):
            stack.pop()
        else:
            stack.append(c)
    if not stack:
        return True
    else:
        return False
  
def dailyTemperatures(self, temperatures):
    """
    739. Daily Temperatures
    Medium
    Given an array of integers temperatures represents the daily temperatures, return an array
    answer such that answer[i] is the number of days you have to wait after the ith day to get a
    warmer temperature. If there is no future day for which this is possible, 
    keep answer[i] == 0 instead.
        
    Of course brute force approach would take O(n^2) time
    Lesser time complexity if we use extra memory
    [73, 74, 75, 71]
    you have to remmeber the previous temperature: a list but stack is more intutitive
    because if we keep track of the indices we don't need 73 any more and we can pop it
        
    so if it is increasing it's really easy you keep on putting 1s and popping from the stack
    if it is decreasing you keep adding to the stack
        
    Monotonic stack decreasing order not strictly (allow equals) 
    Beginner's friendly problem
        
    for the unpopped values the default is zero, for the popped it's the differnece in indices
        
    O(n) time O(n) memory
    :type temperatures: List[int]
    :rtype: List[int]
    """
        
    res                         = [0] * len(temperatures)
    stack                       = []    # pair [temperature, index]  
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd    = stack.pop()
            res[stackInd]       = i - stackInd
        stack.append( [t,i] )
    return res
