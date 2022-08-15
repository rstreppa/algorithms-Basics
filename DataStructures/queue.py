# -*- coding: utf-8 -*-
""" 
@date:          Tue Jan 11 21:55:16 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   implementation and simple properties of a queue
"""
from queue import Queue
from stack import Stack

class Queue():
    def __init__( self ):
        self.queue = []
    
    def push( self, data ):
        '''Inserts the element at the bottom of the queue – Time Complexity: O(1)'''
        self.queue.append( data )
    
    def pop( self ):
        ''' Deletes the last element of the queue – Time Compl exity: O(1)'''
        return self.queue.pop(0)
   
    def size( self ):
        ''' Returns the size of the stack – Time Complexity: O(1) '''
        return len( self.queue )
    
    def top( self ):
        ''' Returns a reference to the topmost element of the stack – Time Complexity: O(1) '''
        return self.queue[-1]
    
    def empty( self ):
        ''' Returns whether the stack is empty – Time Complexity: O(1) '''
        if self.size() == 0:
            return True
        else:
            return False
    def print( self ):
        for elem in self.queue:
            print( elem, end=' ')


def reverse( q ):
    ''' Reversing a Queue using another Queue '''
    # Size of queue
    s = q.qsize()
 
    # Second queue
    ans = Queue()
 
    for i in range(s):
 
        # Get the last element to the
        # front of queue
        for j in range(s - 1):
            x = q.get()
            q.put(x)
 
        # Get the last element and
        # add it to the new queue
        ans.put(q.get())
    return ans

def reversequeue(queue):
    ''' reverse a queue using a Stack '''
    
    # store the elements of the queue in a temporary data structure in a manner 
    # such that if we re-insert the elements in the queue they would get inserted 
    # in reverse order. The data-structure should have the property of ‘LIFO’ 
    # as the last element to be inserted in the data structure should actually 
    # be the first element of the reversed queue. The stack could help in approaching this problem.

    s = Stack() 
    while (not queue.empty()): 
        s.push(queue.queue[0]) 
        queue.get()
    while (len(s) != 0): 
        queue.put(s.top()) 
        s.pop()
    
def reverse_queue_rec(queue):
    # Base case
    if queue.empty():
        return
 
    # Dequeue current item (from front)
    item = queue.queue[0]
    queue.get()
 
    # Reverse remaining queue
    reverse_queue_rec(queue)
 
    # Enqueue current item (to rear)
    queue.put(item)  
    
# This is the CircularQueue class
class CircularQueue:
    """
    A Circular Queue is a queue data structure but circular in shape, therefore after the last position, the next place in the queue is the first position.
    https://www.studytonight.com/code/python/ds/circular-queue-in-python.php
    """
  
  # constructor for the class
  # taking input for the size of the Circular queue 
  # from user
  def __init__(self, maxSize):
    self.queue = list()
    # user input value for maxSize
    self.maxSize = maxSize
    self.head = 0
    self.tail = 0

  # add element to the queue
  def enqueue(self, data):
    # if queue is full
    if self.size() == (self.maxSize - 1):
      return("Queue is full!")
    else:
      # add element to the queue
      self.queue.append(data)
      # increment the tail pointer
      self.tail = (self.tail+1) % self.maxSize
      return True
  
  # remove element from the queue
  def dequeue(self):
    # if queue is empty
    if self.size() == 0:
      return("Queue is empty!")
    else:
      # fetch data
      data = self.queue[self.head]
      # increment head
      self.head = (self.head+1) % self.maxSize
      return data
  
  # find the size of the queue
  def size(self):
    if self.tail >= self.head:
      qSize = self.tail - self.head
    else:
      qSize = self.maxSize - (self.head - self.tail)
    # return the size of the queue
    return qSize
