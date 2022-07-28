# -*- coding: utf-8 -*-
""" 
@date:          Sun Jan  2 15:55:17 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   module to handle simple operations on singly linked lists
"""

class Node:
    ''' Building block of a singly linked list '''
    def __init__( self, data = None ):
        self.data   = data
        self.next   = None
        
class LinkedList:
    ''' Simply linked list as collection of linked data and pointers to next Node '''
    def __init__( self ):
        self.head   = None
        
    def printList( self ):
        ''' Function to print linked list '''
        temp    = self.head 
        
        while temp is not None:
            print( temp.data )
            temp = temp.next
       
        return

    def push( self, data ):
        ''' push data at beginning '''
        
        temp        = Node( data ) 
        temp.next   = self.head
        self.head   = temp
        
        return
   
    def insert( self, prev, data ):
       ''' Given a node prev, insert after it '''
       temp         = Node( data )
       temp.next    = prev.next
       prev.next    = temp
       return
   
    def insertAt( self, i, data ):
        ''' Given a node index, insert after it '''
        temp        = Node( data )
        prev        = self.head
        for k in range( 1, i+1 ):
            prev    = prev.next
        
        temp.next    = prev.next
        prev.next    = temp
        return
        
    def append( self, data ):
        ''' Add a node at the end '''
        temp        = Node( data )
        last        = self.head
        while last.next is not None:
            last    = last.next
        last.next   = temp
        return
    
    def deleteKey( self, key ):
        ''' Given a ‘key’, delete the first occurrence of this key in linked list '''
        
        temp        = self.head
        
        if ( temp is not None ) and ( temp.data == key ): # remove head
            self.head   = temp.next
            temp        = None
            return
        
        while ( temp is not None ) and ( temp.data != key ): # traverse the list
            prev    = temp 
            temp    = temp.next 
            
        if temp is None:    # end of the list, no key
            return           
            
        prev.next   = temp.next     # Unlink the node from linked list
        return
                
            
    def deleteAt( self, i ):
        ''' Given a position, deletes the node at the given position '''

        if self.head is None:       # empty list
            return
        
        temp        = self.head     # store head
        
        if i == 0:                  # head needs be removed
            self.head = temp.next
            return

        for k in range( i ):      # traverse the list up until i-1 
            if temp is None:
                return
            prev    = temp
            temp    = temp.next
        
        if temp is None:            # end of the list
            return

        prev.next   = temp.next     # Unlink the node from linked list
        return
        
    def length( self ):
        ''' Counts no. of nodes in linked list, iterative '''
        res         = 0
        
        if self.head is None:       # empty list
            return res
        
        temp        = self.head
        while temp is not None:
            res     += 1
            temp    = temp.next
        
        return res
        
    def swap( self, x, y ):
        ''' swaps the nodes rather than swapping the field from the nodes '''
        
        if self.head is None:   # Nothing to do if empty list
            return
        
        if x == y:              # Nothing to do if x and y are same
            return
        
        prevX       = None
        currX       = self.head     # search for x        
        while ( currX is not None ) and ( currX.data != x ):
            prevX   = currX
            currX   = currX.next
            
        prevY       = None
        currY       = self.head     # search for y       
        while ( currY is not None ) and ( currY.data != y ):
            prevY   = currY
            currY   = currY.next
        
        if ( currX is None ) or ( currY is None ): # If either x or y is not present, nothing to do 
            return
        
        if prevX is not None:   # If x is not head of linked list
            prevX.next  = currY 
        else:
            self.head   = currY
        
        if prevY is not None:  # If y is not head of linked list
            prevY.next  = currX 
        else:
            self.head   = currX
            
            
        temp            = currY.next    # Swap next pointers
        currY.next      = currX.next 
        currX.next      = temp
        
        return
    
    def reverse( self ):
        ''' Reverse a linked list by changing links between nodes. Iterative Method '''
               
        prev            = None 
        curr            = self.head 
        nextPtr         = None
        
        while curr is not None:
            nextPtr     = curr.next     # Store next
            curr.next   = prev          # Reverse current node's pointer 
            
            prev        = curr          # Move pointers one position ahead
            curr        = nextPtr
       
        self.head       = prev 
        return

    def detectLoop( self ):
        ''' Returns true if there is a loop in linked list else returns false '''
        s       = set()
        temp    = self.head
        
        while temp is not None:
            # If we have already has
            # this node in hashmap it
            # means their is a cycle
            # (Because you we encountering
            # the node second time).
            if temp in s:
                return True
             
        # If we are seeing the node for
        # the first time, insert it in hash
            s.add( temp )
            temp = temp.next
 
        return False
        
    def detectloopFloyd( self ):
        ''' Returns true if there is a loop in linked list. Floyd’s Cycle-Finding Algorithm '''
        
        slow        = self.head 
        fast        = self.head 
        
        while slow and fast and fast.next:
            slow    = slow.next 
            fast    = fast.next.next
            if slow == fast:
                return True
            
        return False
            
            
    def rotate( self, k ):
        ''' Rotate a Linked List counter-clockwise by k nodes. '''
            
        if k == 0:
            return
        
        curr            = self.head 
        count           = 1
        
        while ( count < k ) and curr:
            curr        = curr.next 
            count       += 1
            
        if curr is None:
            return
        
        kthNode         = curr 
        
        while curr.next:
            curr        = curr.next 
            
        curr.next       = self.head 
        self.head       = kthNode.next 
        kthNode.next    = None
        return
        
    def hasCycle(self):
        ''' Given head, the head of a linked list, determine if the linked list has a cycle in it. '''
        if not self.head or not self.head.next:
            return False
        
        visited = set()
        curr    = self.head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr    = curr.next 
        return False
            
    def hasCycle2(self): 
        ''' Use Floyd slow + fast pointers '''
        if not self.head or not self.head.next:
            return False
        slow    = self.head 
        fast    = self.head
        
        while slow and fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False
                   
    def middleNode(self):
        ''' Given the head of a singly linked list, return the middle node of the linked list. 
            If there are two middle nodes, return the second middle node.
        '''
        if not self.head or not self.head.next:
            return self.head
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
               
        return slow
    
    def isPalindrome(self):
        if not self.head or not self.head.next:
            return True
        
        stack = list()
        slow = self.head
        fast = self.head
        curr = self.head
        
        # midpoint
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Push the second half into the stack
        stack.append(slow.data)
        
        while slow.next:
            slow = slow.next
            stack.append(slow.data) 
        
        # comparison
        while stack:
            if stack.pop() != curr.data:
                return False
            curr = curr.next
                 
        return True
   
    def removeElements(self, val):
        ''' Given the head of a linked list and an integer val, 
            remove all the nodes of the linked list that has Node.val == val, and return the new head.
        '''
        while self.head and self.head.data == val:
            self.head = self.head.next
        
        curr = self.head
        while curr and curr.next:
            if curr.next.data == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return self.head
        
    def deleteDuplicates(self):
        ''' Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
            Return the linked list sorted as well. 
        '''
        if not self.head:
            return self.head
        
        curr = self.head 
        while curr and curr.next:
            if curr.data == curr.next.data:
                curr.next = curr.next.next      # careful NOT curr = curr.next.next
            else:
                curr = curr.next
        
        return self.head
        
def mergeTwoLists( l1, l2 ):
    ''' You are given the heads of two sorted linked lists list1 and list2.
        Merge the two lists in a one sorted list. 
        The list should be made by splicing together the nodes of the first two lists.
        Return the head of the merged linked list. 
    ''' 
    dummy = temp = Node(0)
    while l1 != None and l2 != None: #1
        if l1.data < l2.data: #2
            temp.next = l1 #3
            l1 = l1.next #4
        else: 
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    temp.next = l1 or l2  #5
    return dummy.next #6   
    
def getDecimalValue(head):
    ''' Given head which is a reference node to a singly-linked list. 
        The value of each node in the linked list is either 0 or 1. 
        The linked list holds the binary representation of a number.
        Return the decimal value of the number in the linked list.
    '''
    result = 0
    while head: 
        result = result*2 + head.data 
        head = head.next 
    return result        
   
    
def addTwoNumbers(l1, l2):
    """
    2. Add Two Numbers
    Medium
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.    
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummy   = curr = ListNode(0)
    carry   = 0
    while l1 and l2:
        curr.next   = ListNode( ( l1.val + l2.val + carry ) % 10 ) 
        carry       = ( l1.val + l2.val + carry ) // 10
        l1          = l1.next
        l2          = l2.next
        curr        = curr.next
    l       = l1 or l2      
    while l:
        curr.next   = ListNode( ( l.val + carry ) % 10 ) 
        carry       = ( l.val + carry ) // 10
        l           = l.next
        curr        = curr.next
    if carry > 0:
        curr.next   = ListNode( carry )
        
    return dummy.next    
  
