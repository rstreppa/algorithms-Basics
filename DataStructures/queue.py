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
        In case of Linear queue, we did not had the head and tail pointers because we used python List for implementing it. But in case of a circular queue, as the size of the queue is fixed, hence we will set a maxSize for our list used for queue implementation.

        A few points to note here are:

        In case of a circular queue, head pointer will always point to the front of the queue, and tail pointer will always point to the end of the queue.
        Initially, the head and the tail pointers will be pointing to the same location, this would mean that the queue is empty.
        Circular queue python

        New data is always added to the location pointed by the tail pointer, and once the data is added, tail pointer is incremented to point to the next available location.
        Circular queue python

        In a circular queue, data is not actually removed from the queue. Only the head pointer is incremented by one position when dequeue is executed. As the queue data is only the data between head and tail, hence the data left outside is not a part of the queue anymore, hence removed.
        Circular queue python

        The head and the tail pointer will get reinitialised to 0 every time they reach the end of the queue.
        Circular queue python

        Also, the head and the tail pointers can cross each other. In other words, head pointer can be greater than the tail. Sounds odd? This will happen when we dequeue the queue a couple of times and the tail pointer gets reinitialised upon reaching the end of the queue.
        Circular queue python

        Another very important point is keeping the value of the tail and the head pointer within the maximum queue size. In the diagrams above the queue has a size of 8, hence, the value of tail and head pointers will always be between 0 and 7. This can be controlled either by checking everytime whether tail or head have reached the maxSize and then setting the value 0 or, we have a better way, which is, for a value x if we divide it by 8, the remained will never be greater than 8, it will always be between 0 and 7, which is exactly what we want.
        If you want to see a Queue operating in realtime, checkout this animation.

        Algorithm for Circular Queue
        Initialize the queue, with size of the queue defined (maxSize), and head and tail pointers.
        enqueue: Check if the number of elements is equal to maxSize - 1:
        If Yes, then return Queue is full
        If No, then add the new data element to the location of tail pointer and increment the tail pointer.
        dequeue: Check if the number of elements in the queue is zero:
        If Yes, then return Queue is empty
        If No, then increment the head pointer.
        size:
        If, tail >= head, size = tail - head
        But if, head > tail, then size = maxSize - (head - tail)
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
