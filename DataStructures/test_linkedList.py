# -*- coding: utf-8 -*-
""" 
@date:          Sun Jan  2 16:21:58 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Data_Structures/LinkedList/linkedList.py
"""

from linkedList import Node, LinkedList


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
    