# -*- coding: utf-8 -*-
""" 
@date:          Sun Jan  9 13:57:59 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   module to handle simple operations on binary trees
"""

class Node:
    ''' Building block of a binary tree '''
    def __init__( self, data = None ):
        self.data   = data
        self.left   = None
        self.right  = None


def postOrder( root ):
    ''' Given a binary tree, print its nodes according to the "bottom-up" postorder traversal. '''
    if root is None:
        return 
    
    postOrder( root.left )
    postOrder( root.right )
    print( str( root.data ) + " ", end='')
    
def inOrder( root ):
    ''' Given a binary tree, print its nodes in inorder '''
    if root is None:
        return 
    
    inOrder( root.left )
    print( str( root.data ) + " ", end='')
    inOrder( root.right )

def inOrder_stack( root ):
    ''' Iterative function for inorder tree traversal  '''
    # Set current to root of binary tree
    current = root
    stack = [] # initialize stack
    done = 0
     
    while True:
         
        # Reach the left most Node of the current Node
        if current is not None:
             
            # Place pointer to a tree node on the stack
            # before traversing the node's left subtree
            stack.append(current)
         
            current = current.left    
        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done
        elif(stack):
            current = stack.pop()
            print(current.data, end=" ") # Python 3 printing
         
            # We have visited the node and its left
            # subtree. Now, it's right subtree's turn
            current = current.right
 
        else:
            break
      
    print()
    
    
def preOrder( root ):
    ''' Given a binary tree, print its nodes in preorder '''
    if root is None:
        return
    
    print( str( root.data ) + " ", end='')
    preOrder( root.left )
    preOrder( root.right )
 
def height( root ):
    ''' Compute the "height" of a tree -- the number of
        nodes along the longest path from the root node
        down to the farthest leaf node. '''
    
    if root is None:
        return 0
    else:
        return max( height( root.left ), height( root.right ) ) + 1
    
def givenLevel( root, level ):
    ''' Print nodes at a given level '''
    if root is None:
        return
    if level == 1:
        print( root.data, end = ' ' )
    elif level > 1:
        givenLevel( root.left, level-1 )
        givenLevel( root.right, level-1 )
        
def levelOrder( root ):
    ''' Function to print level order traversal a tree '''
    for i in range( 1, height(root) + 1):
        givenLevel( root, i )

def levelOrder_queue( root ):
    ''' Iterative method to find height of B inary Tree '''
    # Base Case
    if root is None:
        return

    # Create an empty queue
    # for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)
    
    while(len(queue) > 0):

        # Print front of queue and
        # remove it from queue
        print(queue[0].data, end='')
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

def maxDepth( root ):
    ''' Compute the "maxDepth" of a tree -- the number of
        nodes along the longest path from the root node
        down to the farthest leaf node.'''
    if root is None:
        return 0
    else: 
        return max( maxDepth(root.left), maxDepth(root.right) ) + 1 
    
def diameter( root ):
    ''' Function to get diameter of a binary tree '''
    if root is None:
        return 0 
    
    # get the height of left and right sub-trees
    lheight     = height(root.left)
    rheight     = height(root.right)
    
    #get the diameter of left and right sub-trees
    ldiameter  = diameter(root.left)
    rdiameter  = diameter(root.right)

	# Return max of following three
	# 1) Diameter of left subtree
	# 2) Diameter of right subtree
	# 3) Height of left subtree + height of right subtree + 1 */
    return max(lheight + rheight + 1, max(ldiameter, rdiameter))
    