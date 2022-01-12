# -*- coding: utf-8 -*-
""" 
@date:          Sun Jan  9 13:58:48 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Data_Structures/BinaryTree/binaryTree.py
"""


from binaryTree import Node, postOrder, inOrder, preOrder, height, givenLevel, levelOrder, levelOrder_queue, inOrder_stack, maxDepth, diameter

def main():
    # Driver code to build binary tree
    root            = Node(1)
    root.left       = Node(2)
    root.right      = Node(3)
    root.left.left  = Node(4)
    root.left.right = Node(5)    

    print('###################')
    postOrder( root )
    print()
    print('###################')
    inOrder( root )
    print()
    print('###################')
    print( inOrder_stack( root ) )
    print('###################')
    preOrder( root )
    print('###################')
    print( height( root ) )
    print('###################')
    givenLevel(root, 3)
    print()
    givenLevel(root, 2)
    print()
    givenLevel(root, 1)
    print()
    givenLevel(root, 0)
    print('###################')
    levelOrder( root )
    print('###################')
    levelOrder_queue( root )
    print('###################')
    print( maxDepth( root ) )
    print('###################')
    print( diameter( root ) )