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

class Nodep:
    ''' Building block of a binary tree with parent pointer '''
    def __init__( self, data = None ):
        self.data   = data
        self.left   = None
        self.right  = None
        self.parent = None


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
    ''' 
    	94. Binary Tree Inorder Traversal
	Easy    	
	Iterative function for inorder tree traversal  
    '''
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
    ''' Iterative method to find height of Binary Tree '''
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
    ''' Function to get diameter of a binary tree 
        Given the root of a binary tree, return the length of the diameter of the tree.
        The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
        This path may or may not pass through the root.
        The length of a path between two nodes is represented by the number of edges between them.
    '''
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




def depth(nodep):
    ''' A utility function to find depth of a node (distance of it from root) '''
    d = -1
    while nodep:
        d +=1
        nodep = nodep.parent
    return d   


def lcap(n1,n2):
    ''' To find LCA of nodes n1 and n2 in Binary Tree '''

    # Find depths of two nodes and differences
    d1      = depth(n1) 
    d2      = depth(n2)
    diff    = d1 - d2
  
    # If n2 is deeper, swap n1 and n2
    if diff < 0:
        temp = n1
        n1 = n2;
        n2 = temp;
        diff = -diff
  
    # Move n1 up until it reaches the same level as n2
    while diff >0:
        diff -=1
        n1 = n1.parent
  
    #Now n1 and n2 are at same levels
    while n1 and n2:
        if n1 == n2:
            return n1
        n1 = n1.parent
        n2 = n2.parent
  
    return None

def height2(root):
    ''' height of binary tree '''
    if not root:
        return 0
    return max(height(root.left),height(root.right)) + 1

def givenLevel2( root, level, res):
    ''' return nodes at a given level '''
    if not root:
        return
    if level == 1:
        res.append(root.data)
    elif level > 1:
        givenLevel2( root.left, level - 1, res)
        givenLevel2( root.right, level - 1, res)
    
def levelOrder2(root):
    ''' returns array of arrays of level order nodes '''
    res = []
    for i in range(1, height2(root)+1):
        levelArray = []
        givenLevel2( root, i, levelArray)
        res.append(levelArray)
    return res

def averageOfLevels(root):
    ''' Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. '''
    means       = []
    nodesList   = levelOrder2(root)
    for nodes in nodesList:
        count   = 0
        nodesum = 0
        for node in nodes:
            count   += 1
            nodesum += node
        means.append(nodesum/count)
    return means
    
def averageOfLevels2(root):
    ''' Let's visit every node of the tree once, keeping track of what depth we are on. 
        We can do this with a simple DFS.
        When we visit a node, info[depth] will be a two element list, keeping track 
        of the sum of the nodes we have seen at this depth, and the number of nodes we have seen. 
        This is necessary and sufficient to be able to compute the average value at this depth.
        At the end of our traversal, we can simply read off the answer.
    '''
    info = []
    def dfs(node, depth = 0):
        if node:
            if len(info) <= depth:
                info.append([0, 0])
            info[depth][0] += node.data
            info[depth][1] += 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
    dfs(root)

    return [s/float(c) for s, c in info]

def averageOfLevels3(root):
    ''' simple and clear BFS solution '''
    res     = []
    q       = []
    q.append(root)
    while(len(q)> 0):
        temp=0
        s=len(q)
        for i in range(s):
            t=q.pop(0)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
            temp    += t.data
        res.append( temp/s )
    return res 

def minDepth(root):
    ''' Given a binary tree, find its minimum depth.
        The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
        DFS
    '''
    if not root:
        return 0
    
    if not root.left:
        return minDepth(root.right) + 1
    if not root.right:
        return minDepth(root.left) + 1
    return min(minDepth(root.left),minDepth(root.right)) + 1
    
def minDepth2(root):
    ''' Given a binary tree, find its minimum depth. 
        BFS 
    '''
    if not root:
        return 0
    queue = [ (root, 1) ]
    while queue:
        node, level = queue.pop(0)
        if node:
            if not node.left and not node.right:
                return level
            else:
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
                
def isSameTree(p, q):
    ''' 
    	100. Same Tree
	Easy
	Given the roots of two binary trees p and q, write a function to check if they are the same or not.
        Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
    '''  
    if p and q:
        return p.data == q.data and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return p is q        
        
def hasPathSum(root, targetSum):
    ''' Given the root of a binary tree and an integer targetSum, return true 
        if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
        A leaf is a node with no children.
    '''    
    if not root:
         return False

    if not root.left and not root.right and root.data == targetSum:
         return True
     
    targetSum -= root.data

    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum) 
 
def traverse(root, current_path, results):
    ''' traverse a binary tree and store in path values '''
    current_path += "->" + str(root.data)
    if not root.left and not root.right:
        results.append(current_path)
        return
    if root.left:
        traverse(root.left, current_path, results)
    if root.right:
        traverse(root.right, current_path, results)

def binaryTreePaths(root):
    ''' Given the root of a binary tree, return all root-to-leaf paths in any order. 
        A leaf is a node with no children.
    '''
    results = []
    if not root:
        return results
    current_path = str(root.data)
    if not root.left and not root.right:
        results.append(current_path)
    if root.left:
        traverse(root.left, current_path, results)
    if root.right:
        traverse(root.right, current_path, results)  
    return results

def mergeTrees(root1, root2):
    ''' You are given two binary trees root1 and root2.
        Imagine that when you put one of them to cover the other, 
        some nodes of the two trees are overlapped while the others are not. 
        You need to merge the two trees into a new binary tree. 
        The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. 
        Otherwise, the NOT null node will be used as the node of the new tree.
        Return the merged tree.
    '''
    
    if root1 and root2:
        root        = Node(root1.data + root2.data)
        root.left   = mergeTrees(root1.left, root2.left)
        root.right  = mergeTrees(root1.right, root2.right)
        return root
    else:
        return root1 or root2

def areEqual( s, t):
    ''' check if two trees are equal '''
    if (not s) and (not t): 
        return True
    if (not s) or (not t): 
        return False
    
    if s.data != t.data:
        return False
    
    return areEqual(s.left, t.left) and areEqual(s.right, t.right)

def isSubtree(root, subRoot):
    ''' Given the roots of two binary trees root and subRoot, return true 
        if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
        A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
        The tree tree could also be considered as a subtree of itself.
    '''
    if not root:
        return False
    if areEqual(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

def invertTree(root):
    ''' Given the root of a binary tree, invert the tree, and return its root. '''
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
        return root
    
def invertTreeIterative(root):
    ''' Given the root of a binary tree, invert the tree, and return its root. '''
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            stack += node.left, node.right
            node.left, node.right = node.right, node.left          
    return root    
