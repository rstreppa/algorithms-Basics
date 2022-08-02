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
    ''' 
    	98. Validate Binary Search Tree
       	Medium
    	Function to determine if given Binary Tree is a BST or not by keeping a
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
    ''' 
    	235. Lowest Common Ancestor of a Binary Search Tree
	Easy
    	A recursive python program to find LCA least common ancestor of two nodes n1 and n2
    '''
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
    ''' 
    	235. Lowest Common Ancestor of a Binary Search Tree
	Easy
	An iterative python program to find LCA least common ancestor of two nodes n1 and n2
    '''
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

def generateTrees(self, n):
    """
        95. Unique Binary Search Trees II
        Medium
        Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. 
        Return the answer in any order.       
    
        Remember that a BST has in the left nodes all numbers less than root and right node all numbers grater than root
        Also the root must be inside the inner loop as it changes with l and r
        :type n: int
        :rtype: List[TreeNode]
    """
    def dfs( nums ):
        if not nums:
            return [ None ]
        
        res         = []
        
        for i in range( len( nums ) ):
            left    = dfs( nums[:i] )
            right   = dfs( nums[i+1:] )
            for l in left:
                for r in right:
                    root        = TreeNode( nums[i] )
                    root.left   = l
                    root.right  = r
                    res.append( root )
        return res
    
    
    nums    = list( range( 1, n+1 ) )
    return dfs( nums )

def numTrees(self, n):
    """
        96. Unique Binary Search Trees
        Medium
        Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
        Careful: if you use the same approach as problem 95, which requires you to list the trees, you get Time Limit Exceeded!
        
        The answer is Catalan numbers C_{n+1} = C_0*C_n + C_1*C_{n-1} + ... + C_n*C_0
        https://brilliant.org/wiki/catalan-numbers/
        Beacuse for eacch number you multiply the number of left and right subtrees which are obtained by splitting below and above root 
        It's an iteraitve Dynamic Programming solution
        :type n: int
        :rtype: int
    """
    dp      = [1] * (n+1) # you will count also tree with 0 nodes and tree with n nodes
    
    # 0 nodes -> 1 tree
    # 1 node  -> 1 tree
    
    for nodes in range( 2, n+1 ):
        total   = 0
        for root in range( 1, nodes + 1 ):
            left    = root - 1
            right   = nodes - root
            total   += dp[left] * dp[right]
        dp[nodes]   = total
    return dp[n]

class Solution(object):
    def recoverTree(self, root):
        """
            99. Recover Binary Search Tree
            Medium
            You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. 
            Recover the tree without changing its structure.
            :type root: TreeNode
            :rtype: None Do not return anything, modify root in-place instead.
        """
        
        def swap( x, y ):
            temp = x.val
            x.val = y.val
            y.val = temp

        def inorder(root):
            if not root:
                return

            inorder(root.left)

            if self.pred and root.val < self.pred.val:
                self.y = root
                if not self.x:
                    self.x = self.pred
                else:
                    return
            self.pred = root

            inorder(root.right)

        self.pred   = None
        self.x      = None  # 1st wrong node
        self.y      = None  # 2nd wrong node
        inorder(root)
        swap(self.x, self.y)

class Solution(object):
    def recoverTree2(self, root):
        """
            99. Recover Binary Search Tree
            Medium
            You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. 
            Recover the tree without changing its structure.
	    
	    Easier solution that captures the essence of the problem: inorder traversal of the BST 
            :type root: TreeNode
            :rtype: None Do not return anything, modify root in-place instead.
        """
        
        self.temp = []
        
        def dfs( node ):	# in order traversal
            if not node:    return
            dfs( node.left )
            self.temp.append( node )
            dfs( node.right )
            
        dfs( root )
        
        srt = sorted( n.val for n in self.temp )
        
        for i in range( len( srt ) ):
            self.temp[i].val = srt[i]

def sortedArrayToBST(self, nums):
    """
        108. Convert Sorted Array to Binary Search Tree
        Easy
        Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
        A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
        :type nums: List[int]
        :rtype: TreeNode
    """
    
    def buildBST(nums):
        n           = len(nums)
        if n == 0:
            return
        i           = n // 2
        root        = TreeNode( nums[i] )
        root.left   = buildBST( nums[:i] )
        root.right  = buildBST( nums[i+1:] )
        return root
        
    return buildBST(nums)        

class Solution(object):
    def sortedListToBST(self, head):
        """
            109. Convert Sorted List to Binary Search Tree
            Medium
            Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
            For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node 
            never differ by more than 1.
            
            Easy once you have solved 108. Convert Sorted Array to Binary Search Tree
            
            :type head: Optional[ListNode]
            :rtype: Optional[TreeNode]
        """
        
        if not head:
            return None
        if not head.next:
            return TreeNode( head.val )
        
        slow    = fast  = head
        prev    = None
        while fast and fast.next:
            prev    = slow
            slow    = slow.next
            fast    = fast.next.next
            
        prev.next   = None
        root        = TreeNode( slow.val )
        root.left   = self.sortedListToBST( head )
        root.right  = self.sortedListToBST( slow.next )
        
        return root

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):
    """
        173. Binary Search Tree Iterator
        Medium
        Implement the BSTIterator class that represents an iterator over the in-order traversal 
        of a binary search tree (BST):
        BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. 
        The root of the BST is given as part of the constructor. 
        The pointer should be initialized to a non-existent number smaller than any element in the BST.
        boolean hasNext() Returns true if there exists a number in the traversal 
        to the right of the pointer, otherwise returns false.
        int next() Moves the pointer to the right, then returns the number at the pointer.
        Notice that by initializing the pointer to a non-existent smallest number, 
        the first call to next() will return the smallest element in the BST.
        You may assume that next() calls will always be valid. That is, there will be at least a next
        number in the in-order traversal when next() is called.    
    """

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack  = []
        while root:
            self.stack.append( root )
            root    = root.left

    def next(self):
        """
        :rtype: int
        """
        res         = self.stack.pop()
        curr        = res.right
        while curr:
            self.stack.append( curr )
            curr    = curr.left
        return res.val
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

def kthSmallest(root, k):
    """
        230. Kth Smallest Element in a BST
        Medium
        Given the root of a binary search tree, and an integer k, return the kth smallest value 
        (1-indexed) of all the values of the nodes in the tree.
            
        Easy to solve with a stack 
            
        :type root: TreeNode
        :type k: int
        :rtype: int
    """
    curr    = root
    s       = []
        
    while True:
        if curr:
            s.append( curr )
            curr    = curr.left
        elif s:
            curr    = s.pop()
            k       -= 1
            if  k == 0:
                return curr.val
            curr    = curr.right
        else:
            break
	
class Solution(object):
    def kthSmallest2(self, root, k):
        """
            230. Kth Smallest Element in a BST
            Medium
            Given the root of a binary search tree, and an integer k, return the kth smallest value 
            (1-indexed) of all the values of the nodes in the tree.
            
            Recursive solution
            
            :type root: TreeNode
            :type k: int
            :rtype: int
        """
        self.count  = 0
        self.res    = 0
        self.dfs( root, k)
        return self.res
    
    def dfs( self, root, k ):
        if root.left:
            self.dfs( root.left, k )
        
        self.count  += 1
        if self.count == k:
            self.res = root.val
            return
        
        if root.right:
            self.dfs( root.right, k )


def verifyPreorder(preorder):
    '''
    	255. Verify Preorder Sequence in Binary Search Tree (Python)
	Medium
	Stack .
	Description
	Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
	You may assume each number in the sequence is unique.
		
	Methodology
	Kinda simulate the traversal, keeping a stack of nodes (just their values) of which we’re still in the left subtree. 
	If the next number is smaller than the last stack value, then we’re still in the left subtree of all stack nodes, 
	so just push the new one onto the stack. But before that, pop all smaller ancestor values, as we must now be in their right subtrees 
	(or even further, in the right subtree of an ancestor). Also, use the popped values as a lower bound, since being in their right subtree 
	means we must never come across a smaller number anymore.
    '''
    if not preorder: 
	return True
    min_val 	= float('-inf')
    s 		= []
    for elem in preorder:
        if elem < min_val: 
	    return False
        while s and s[-1] < elem:
            min_val = s.pop()
        s.append(elem)
    return True
