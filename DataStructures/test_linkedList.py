# -*- coding: utf-8 -*-
""" 
@date:          Sun Jan  2 16:21:58 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Data_Structures/LinkedList/linkedList.py
"""

from linkedList import Node, LinkedList, mergeTwoLists, getDecimalValue


def test_LinkedList():
    l1              = LinkedList()
    l1.head         = Node('Mon')
    e2              = Node('Tue')
    e3              = Node('Wed')
    l1.head.next    = e2    # link first Node to second Node
    e2.next         = e3    # link secodn node to third Node
    return l1
    

def main():
    print('###################')
    l = test_LinkedList() 
    print(l)
   
    print('###################')
    l.printList()
    
    print('###################')   
    l.push('Sun')
    l.printList()
   
    print('###################')
    prev = l.head.next.next   # Tue
    l.insert(prev, 'TueEvening')
    l.printList()
   
    print('###################')
    l.insertAt( 3 , 'TueNight' )
    l.printList()
   
    print('###################')
    l.append( 'Thur' )
    l.printList()
   
    print('###################')
    l.deleteKey( 'Sun' )
    l.printList()
   
    print('###################')
    l.deleteKey( 'TueEvening' )
    l.printList()
    
    print('###################')
    l.deleteAt( 0 )
    l.printList()
    
    print('###################')
    l.deleteAt( 2 )
    l.printList()
   
    print('###################')
    l.deleteAt( 20 )
    l.printList()

    print('###################')
    print( l.length() )

    print('###################')
    l = test_LinkedList()
    l.push('Sun')
    l.append( 'Thur' )
    l.swap( 'Sun', 'Thur' )
    l.printList()
    l.swap( 'Sun', 'Tue' )
    l.printList()
    
    print('###################')
    l = test_LinkedList()
    l.push('Sun')
    l.append( 'Thur' )
    l.printList()
    l.reverse()
    l.printList()
    
    print('###################')
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(10)     
    # Create a loop for testing
    llist.head.next.next.next.next = llist.head    
    
    if( llist.detectLoop() ):
        print("Loop found")
    else:
        print("No Loop ")
    
    if( l.detectLoop() ):
        print("Loop found")
    else:
        print("No Loop ")
        
    print('###################')
    if( llist.detectloopFloyd() ):
        print("Loop found")
    else:
        print("No Loop ")
    
    if( l.detectloopFloyd() ):
        print("Loop found")
    else:
        print("No Loop ")
    
    print('###################')
    l.rotate(3)
    l.printList()
    print('###################')
    l.rotate(2)
    l.printList()
    print('#### hasCycle #########################')
    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(10)     
    # Create a loop for testing
    llist.head.next.next.next.next = llist.head 
    print(llist.hasCycle())
    print(llist.hasCycle2())
    print('#### middleNode #########################')
    l = LinkedList()
    l.push(5)
    l.push(4) 
    l.push(3)
    l.push(2)
    l.push(1)
    print(l.middleNode().data)
    g = LinkedList()
    g.push(6)
    g.push(5) 
    g.push(4)
    g.push(3)
    g.push(2)
    g.push(1)
    print(g.middleNode().data)
    print('#### isPalindrome #########################')
    l = LinkedList()
    l.push(1)
    l.push(2) 
    l.push(2)
    l.push(1)
    print( l.isPalindrome() )
    g = LinkedList()
    g.push(2)
    g.push(1)
    print( g.isPalindrome() )
    h = LinkedList()
    h.push(1)
    h.push(2) 
    h.push(3)
    h.push(2)
    h.push(1)
    print( h.isPalindrome() )
    print('#### removeElements #########################')
    l = LinkedList()
    for data in [1,2,6,3,4,5,6][::-1]:
        l.push(data)
    l.removeElements(6)
    l.printList()
    g = LinkedList()
    for data in [][::-1]:
        g.push(data)
    g.removeElements(1)
    g.printList()
    h = LinkedList()
    for data in [7,7,7,7][::-1]:
        h.push(data)
    h.removeElements(7)
    h.printList()
    print('#### deleteDuplicates #########################')
    l = LinkedList()
    for data in [1,1,2][::-1]:
        l.push(data)
    l.deleteDuplicates()
    l.printList()
    g = LinkedList()
    for data in [1,1,2,3,3][::-1]:
        g.push(data)
    g.deleteDuplicates()
    g.printList()
    print('#### mergeTwoLists #########################')
    l1 = LinkedList()
    for data in [1,2,4][::-1]:
        l1.push(data)
    l2 = LinkedList()
    for data in [1,3,4][::-1]:
        l2.push(data)
    head = mergeTwoLists(l1.head, l2.head)
    l3   = LinkedList()
    l3.head = head
    l3.printList()

    l1 = LinkedList()
    for data in [][::-1]:
        l1.push(data)
    l2 = LinkedList()
    for data in [][::-1]:
        l2.push(data)
    head = mergeTwoLists(l1.head, l2.head)
    l3   = LinkedList()
    l3.head = head
    l3.printList()
    
    l1 = LinkedList()
    for data in [][::-1]:
        l1.push(data)
    l2 = LinkedList()
    for data in [0][::-1]:
        l2.push(data)
    head = mergeTwoLists(l1.head, l2.head)
    l3   = LinkedList()
    l3.head = head
    l3.printList()
    print('#### getDecimalValue #########################')
    l = LinkedList()
    for data in [1,0,1][::-1]:
        l.push(data)
    print(getDecimalValue(l.head))
    l = LinkedList()
    for data in [0][::-1]:
        l.push(data)
    print(getDecimalValue(l.head))
    l = LinkedList()
    for data in [1,0,1,0][::-1]:
        l.push(data)
    print(getDecimalValue(l.head))
    