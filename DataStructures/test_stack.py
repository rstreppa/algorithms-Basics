# -*- coding: utf-8 -*-
""" 
@date:          Tue Jan 11 21:53:45 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Data_Structures/Stack/stack.py
"""

from stack import Stack, reverseStackUsingTwoStacks, transfer, reverse_stack_by_using_extra_stack, insertAtBottom, reverse

def main():
    s = Stack()
    s.push( 1 )
    s.push( 2 )
    s.push( 3 )
    s.push( 4 )
    s.push( 5 )
    print( s.top() )
    print( s.pop() )
    s.print()
    print()
    print('######################')
    reverseStackUsingTwoStacks( s )
    s.print()
    print('######################')
    t = Stack()
    transfer( s, t, s.size() )
    t.print()
    print()
    reverse_stack_by_using_extra_stack( t, t.size() )
    t.print()
    print('######################')
    insertAtBottom(t, 5)
    t.print()
    print('######################')
    reverse( t )
    t.print()
    