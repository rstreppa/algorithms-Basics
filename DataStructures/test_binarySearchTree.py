# -*- coding: utf-8 -*-
""" 
@date:          Thu Jan 13 22:47:26 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Data_Structures/BinarySearchTree/binarySearchTree.py
"""

from binarySearchTree import Node, insert, search, search_iterative, minValueNode, deleteNode, isBST, inOrderSuccessor
from binarySearchTree import Nodep, insertp, inOrderSuccessorp, lca, lcaIterative, lcap

def test_BST():
    root    = Node(8)
    root    = insert(root, 3)
    root    = insert(root, 10)
    root    = insert(root, 1)
    root    = insert(root, 6)
    root    = insert(root, 14)
    root    = insert(root, 4)
    root    = insert(root, 7)
    root    = insert(root, 13)
    return root 

def test_BSTp():
    root    = Nodep(8)
    root    = insertp(root, 3)
    root    = insertp(root, 10)
    root    = insertp(root, 1)
    root    = insertp(root, 6)
    root    = insertp(root, 14)
    root    = insertp(root, 4)
    root    = insertp(root, 7)
    root    = insertp(root, 13)
    return root    


def main():
    print('###################')
    root    = test_BST()
    r = search(root, 7)
    print(r.key)
    print('###################')
    print(search_iterative(root, 7))
    print(search_iterative(root, 18))
    print('###################')
    m = minValueNode(root)
    print(m.key)
    print('###################')
    r = deleteNode(root, 8)
    print(r.key)
    print('###################')
    print(isBST(root, 1, 20))
    print(isBST(root, 1, 10))
    print('###################')
    root    = test_BST()
    print('###################')
    r = inOrderSuccessor(root, Node(3))
    print(r.key)
    print('###################')
    root    = test_BSTp()
    r = inOrderSuccessorp( root.left.right ) # 6
    print(r.key)
    r = inOrderSuccessorp( root.left.left )  # 1
    print(r.key)
    print('###################')
    root    = test_BST()
    r = lca(root, 4, 13)
    print(r.key)
    r = lca(root, 1, 6)
    print(r.key)
    r = lcaIterative(root, 4, 13)
    print(r.key)
    r = lcaIterative(root, 1, 6)
    print(r.key)
    print('###################')
    root    = test_BSTp()
    r = lcap(root, root.left.right.left, root.right.right.left)
    print(r.key)
    r = lcap(root, root.left.left, root.left.right)
    print(r.key)
    print('###################')