# -*- coding: utf-8 -*-
""" 
@date:          Mon Jan  3 21:53:17 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Data_Structures/LinkedList/doublyLinkedList.py
"""

from doublyLinkedList import DoublyLinkedList

def main():
    # Start with empty list
    llist = DoublyLinkedList()
     
    # Insert 6. So the list becomes 6->None
    llist.append(6)
     
    # Insert 7 at the beginning.
    # So linked list becomes 7->6->None
    llist.push(7)
     
    # Insert 1 at the beginning.
    # So linked list becomes 1->7->6->None
    llist.push(1)
     
    # Insert 4 at the end.
    # So linked list becomes 1->7->6->4->None
    llist.append(4)
     
    # Insert 8, after 7.
    # So linked list becomes 1->7->8->6->4->None
    llist.insert(llist.head.next, 8)

    print('###################')
    llist.printList() 
    
    # So linked list becomes 1->7->8->2->6->4->None
    llist.insertAt(2, 2)
    llist.printList()
    
    print('###################')
    llist.delete(llist.head)
    llist.delete(llist.head.next)
    llist.delete(llist.head.next)
    llist.printList()
    print('###################')
    llist.deleteAt(2)
    llist.printList()