# -*- coding: utf-8 -*-
""" 
@date:          Thu Jan 13 22:45:17 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   implementation and simple properties of BST
"""

class Node:
    ''' Building block of a binary search tree '''
    def __init__( self, key = None ):
        self.key    = key
        self.left   = None
        self.right  = None
        
class Nodep:
    ''' Building block of a binary search tree with parent pointer '''
    def __init__( self, key = None ):
        self.key    = key
        self.left   = None
        self.right  = None
        self.parent = None
    

def insert(root, key):
    ''' A utility function to insert a new node with given key in BST '''

    # If the tree is empty, return a new node
    if not root:
        return Node(key)

	# Otherwise, recur down the tree
    if key < root.key:
        root.left = insert(root.left, key) 
    elif key > root.key:
        root.right = insert(root.right, key)

	# return the (unchanged) node pointer
    return root


def search(root, key):
    ''' search a given key in a given BST '''
	# Base Cases: root is nullptr or key is present at root 
    if not root or root.key == key: 
        return root

	# Key is greater than root's key 
    if key > root.key: 
        return search(root.right, key)

	# Key is smaller than root's key 
    return search(root.left, key)

def search_iterative(root, key):
    # Iterative function to search a given key in root
    
    # traverse the tree and search for the key
    while root:
        #if given key is less than the current node, go to left subtree else go to right subtree
        if key < root.key:
            root = root.left 
        elif key > root.key:
            root = root.right
		# if key is found return True
        else:
            return True

	# we reach here if the key is not present in the BST
    return False

def minValueNode(root):
    ''' Given a non-empty binary search tree, return the node with minimum
        key value found in that tree. Note that the entire tree does not
        need to be searched.'''

    current = root

	# loop down to find the leftmost leaf */
    while current.left:
        current = current.left

    return current 

def deleteNode(root, key):
    ''' Given a binary search tree and a key, this function deletes the key
        and returns the new root '''

	# base case 
    if not root:
        return root

    # If the key to be deleted is smaller than the root's key, then it lies in left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
	# If the key to be deleted is greater than the root's key, then it lies in right subtree 
    elif key > root.key:
        root.right = deleteNode(root.right, key)
	# if key is same as root's key, then This is the node to be deleted 
    else:
		# node with only one child or no child 
        if not root.left: 
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp

		# node with two children: Get the inorder successor (smallest in the right subtree) i.e. smallest of the larger ones 
        temp = minValueNode(root.right)

		# Copy the inorder successor's content to this node 
        root.key = temp.key

		# Delete the inorder successor 
        root.right = deleteNode(root.right, temp.key)

    return root

def isBST(root, minKey, maxKey):
    ''' Function to determine if given Binary Tree is a BST or not by keeping a
        valid range (starting from [MIN_VALUE, MAX_VALUE]) and keep shrinking
        it down for each node as we go down recursively '''

	# base case
    if not root:
        return True

	# if node's value fall outside valid range
    if root.key < minKey or root.key > maxKey:
        return False

    # recursively check left and right subtrees with updated range
    return isBST(root.left, minKey, root.key) and isBST(root.right, root.key, maxKey)


def inOrderSuccessor(root, n):
    ''' Recursive function to find inorder successor for given node in a BST '''

    # Step 1 of the above algorithm
    if n.right is not None:
        return minValueNode(n.right)
 
    # Step 2 of the above algorithm
    succ=Node(None)
     
     
    while(root):
        if(root.key<n.key):
            root=root.right
        elif(root.key>n.key):
            succ=root
            root=root.left
        else:
            break
    return succ

def insertp(root, key):
    ''' A utility function to insert a new node with given key in BST with parent pointer '''
    
    # If the tree is empty, return a new node
    if not root: 
        return Nodep(key)
  
    #Otherwise, recur down the tree
    if key < root.key:
        root.left           = insertp(root.left, key)
        root.left.parent    = root

    elif key > root.key:
        root.right = insertp(root.right, key)
        root.right.parent = root
  
    # return the (unchanged) node pointer */
    return root

def inOrderSuccessorp(root):
    ''' Recursive function to find inorder successor for given node in a BST using parent pointer
        If right subtree of node is not NULL, then succ lies in right subtree. Do the following. 
        Go to right subtree and return the node with minimum key value in the right subtree.
        If right subtree of node is NULL, then succ is one of the ancestors. Do the following. 
        Travel up using the parent pointer until you see a node which is left child of its parent. 
        The parent of such a node is the succ.
    '''
    
    if root.right:
        return( minValueNode( root.right ) )
    
    parent = root.parent
    while parent: 
        if root != parent.right:
            break
        root    = parent
        parent  = parent.parent
    return parent

def lca(root, n1, n2):
    ''' A recursive python program to find LCA least common ancestor of two nodes n1 and n2'''
    # Base Case
    if not root:
        return root

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.key > n1 and root.key > n2):
        return lca(root.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA
    # lies in right 
    if(root.key < n1 and root.key < n2):
        return lca(root.right, n1, n2)

    return root

def lcaIterative(root, n1, n2):
    ''' An iterative python program to find LCA least common ancestor of two nodes n1 and n2'''
    while root:
        # If both n1 and n2 are smaller than root,
        # then LCA lies in left
        if root.key > n1 and root.key > n2:
            root = root.left
        
        # If both n1 and n2 are greater than root, 
        # then LCA lies in right
        elif root.key < n1 and root.key < n2:
            root = root.right

        else:
            break

    return root

def lcap(root, n1, n2):
    ''' An iterative python program to find LCA least common ancestor of two nodes n1 and n2  
        using Parent Pointer.
        1 Create an empty hash table.
        2 Insert n1 and all of its ancestors in hash table.
        3 Check if n2 or any of its ancestors exist in hash table, if yes return the first existing ancestor.
    '''
    # Create a map to store ancestors of n1
    ancestors = dict()
  
    # Insert n1 and all its ancestors in map
    while n1: 
        ancestors[n1] = True
        n1 = n1.parent
  
    # Check if n2 or any of its ancestors is in map.
    while n2:
       if ancestors.get(n2, None):
           return n2
       n2 = n2.parent
  
    return None