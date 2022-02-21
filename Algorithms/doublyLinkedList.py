# -*- coding: utf-8 -*-
""" 
@date:          Mon Jan  3 21:53:17 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   module to handle simple operations on doubly linked lists
"""

class Node:
    ''' Building block of a doubly linked list '''
    def __init__( self, data = None ):
        self.data   = data
        self.prev   = None
        self.next   = None

class DoublyLinkedList:
    ''' Doubly linked list as collection of linked data and pointers to next Node and previous Node '''
    def __init__( self ):
        self.head   = None


    def printList( self ):
        ''' Function to print linked list '''
        temp    = self.head 
        
        while temp:
            print( temp.data )
            temp = temp.next
       
        return

    def push( self, data ):
        ''' Adding a node at the front of the list '''
        
        temp        = Node(data)
        
        if self.head is None:
            self.head = temp
            return
        
        temp.next       = self.head 
        temp.prev       = None
        self.head.prev  = temp
        self.head       = temp
        return
            
    def append( self, data ):
        ''' appends a new node at the end '''
        temp        = Node( data )
        if self.head is None:
            self.head = temp
            return
        
        last        = self.head
        while last.next:
            last    = last.next
        last.next   = temp
        temp.prev   = last
        return
        
    def insert( self, prev, data ):
       ''' Given a node prev, insert after it '''
       temp         = Node( data )
       
       temp.next    = prev.next
       prev.next    = temp
       temp.prev    = prev
       if temp.next:        # Change previous of new_nodes's next node
           temp.next.prev = temp
       return
                
    def insertAt( self, i, data ):
        ''' Given a node index, insert after it '''
        temp        = Node( data )
        prev        = self.head
        for k in range( 1, i+1 ):
            prev    = prev.next
        
        temp.next   = prev.next
        prev.next   = temp
        temp.prev   = prev
        if temp.next:        # Change previous of new_nodes's next node
            temp.next.prev = temp
        return

    def delete( self, dele ):        
        ''' Function to delete a node in a Doubly Linked List. '''
        
        if ( self.head is None ) or ( dele is None ):   # Base Case
            return
        
        if self.head == dele:   # If node to be deleted is head node
            self.head       = dele.next 
              
        if dele.next:   # Change next only if node to be deleted is NOT the last node
            dele.next.prev  = dele.prev
            
        if dele.prev:   # Change prev only if node to be deleted is NOT the first node
            dele.prev.next  = dele.next

        return            
    
    def deleteAt( self, i ):
        ''' Given a position, deletes the node at the given position '''

        if ( self.head is None ) or ( i <= 0 ):   # Base Case
            return
        
        curr        = self.head
        k           = 1 
        
        while ( curr ) and ( k < i ):
            curr    = curr.next
            k       += 1
            
        if curr is None:
            return
        
        self.delete( curr )
        return
        
        