# -*- coding: utf-8 -*-
""" 
@date:          Thu Jan 20 21:03:40 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   implmentation and simple properties of graphs
"""

from collections import defaultdict

class AdjNode:
    ''' A class to represent the adjacency list of the node '''
    def __init__(self, data):
        self.vertex = data
        self.next   = None

class Graph:
    ''' A class to represent a graph. A graph is the list of the adjacency lists.
        Size of the array will be the no. of the vertices "V"'''
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
 

    def add_edge(self, src, dest):
        ''' Function to add an edge in a directed graph'''
        # Adding the node to the source node
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        ''' Function to print the graph '''
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")
            
class Graph2: 
    ''' This class represents a directed graph using adjacency list representation'''
    def __init__(self, vertices):
 
        # default dictionary to store graph
        self.graph  = defaultdict(list)
        self.V      = vertices # No. of vertices'
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self, s):
        ''' BFS traversal from a given source vertex. BFS(int s) traverses vertices reachable from s. 
            Similar to level order traversal of a binary tree
        '''
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        ''' The function to do DFS traversal. It uses recursive DFSUtil() 
            Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a tree. 
            The only catch here is, unlike trees, graphs may contain cycles (a node may be visited twice). 
            To avoid processing a node more than once, use a boolean visited array. 
            The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) 
            and explores as far as possible along each branch before backtracking. 
            So the basic idea is to start from the root or any arbitrary node and mark the node 
            and move to the adjacent unmarked node and continue this loop until there is no unmarked adjacent node. 
            Then backtrack and check for other unmarked nodes and traverse them. Finally, print the nodes in the path.
            Algorithm: 
            Create a recursive function that takes the index of the node and a visited array.
        '''
        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)

    def DFSUtil2(self, s, visited):
        ''' prints all not yet visited vertices reachable from s '''
         
        # Create a stack for DFS
        stack = []
     
        # Push the current source node.
        stack.append(s)
     
        while (len(stack) != 0):
             
            # Pop a vertex from stack and print it
            s = stack.pop()
     
            # Stack may contain same vertex twice.
            # So we need to print the popped item only
            # if it is not visited.
            if (not visited[s]):
                print(s, end = " ")
                visited[s] = True
     
            # Get all adjacent vertices of the
            # popped vertex s. If a adjacent has not 
            # been visited, then push it to the stack.
            i = 0
            while i < len(self.graph[s]):
                if (not visited[self.graph[s][i]]):
                    stack.append(self.graph[s][i])
                i += 1
     
    def DFS2(self):
        ''' prints all vertices in DFS manner 
            The only difference between iterative DFS and recursive DFS is that 
            the recursive stack is replaced by a stack of nodes.
            This is similar to BFS, the only difference is queue is replaced by stack.
        '''
         
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
        for i in range(self.V):
            if (not visited[i]):
                self.DFSUtil2(i, visited)

    
    def topologicalSortUtil(self, v, visited, stack):
        ''' A recursive function used by topologicalSort '''
 
        # Mark the current node as visited.
        visited[v] = True
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Push current vertex to stack which stores result
        stack.append(v)

    def topologicalSort(self):
        ''' The function to do Topological Sort. It uses recursive topologicalSortUtil() 
            In DFS, we print a vertex and then recursively call DFS for its adjacent vertices. 
            In topological sorting, we need to print a vertex before its adjacent vertices. 
            In topological sorting, we use a temporary stack. We don’t print the vertex immediately, 
            we first recursively call topological sorting for all its adjacent vertices, 
            then push it to a stack. Finally, print contents of the stack. 
            Note that a vertex is pushed to stack only when all of its adjacent vertices 
            (and their adjacent vertices and so on) are already in the stack. 
        '''
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
        stack = []
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        # Print contents of the stack
        print(stack[::-1])  # return list in reverse order

 
def isCycleExist(n, graph):
    ''' This function returns true if there is a cycle in directed graph, else returns false. 
        Steps involved in detecting cycle in a directed graph using BFS.
        Step-1: Compute in-degree (number of incoming edges) for each of the vertex present in the graph 
                and initialize the count of visited nodes as 0.
        Step-2: Pick all the vertices with in-degree as 0 and add them into a queue (Enqueue operation)
        Step-3: Remove a vertex from the queue (Dequeue operation) and then. 
        
        Increment count of visited nodes by 1.
        Decrease in-degree by 1 for all its neighboring nodes.
        If in-degree of a neighboring nodes is reduced to zero, then add it to the queue.
        Step 4: Repeat Step 3 until the queue is empty.
        Step 5: If count of visited nodes is not equal to the number of nodes in the graph has cycle, otherwise not.                   
    '''
 
    # Create a vector to store indegrees of all
    # vertices. Initialize all indegrees as 0.
    in_degree=[0]*n
 
    # Traverse adjacency lists to fill indegrees of
    # vertices. This step takes O(V+E) time
    for i in range(n):
        for j in graph[i]:
            in_degree[j]+=1
     
    # Create an queue and enqueue all vertices with
    # indegree 0
    queue=[]
    for i in range(len(in_degree)):
        if in_degree[i]==0:
            queue.append(i)
     
    # Initialize count of visited vertices
    cnt=0
 
    # One by one dequeue vertices from queue and enqueue
    # adjacents if indegree of adjacent becomes 0
    while(queue):
 
        # Extract front of queue (or perform dequeue)
        # and add it to topological order
        nu=queue.pop(0)
 
        # Iterate through all its neighbouring nodes
        # of dequeued node u and decrease their in-degree
        # by 1
        for v in graph[nu]:
            in_degree[v]-=1
 
            # If in-degree becomes zero, add it to queue
            if in_degree[v]==0:
                queue.append(v)
        cnt+=1
 
    # Check if there was a cycle
    if cnt==n:
        return False
    else:
        return True
         
def validPath(n, edges, source, destination):
    ''' 
        1971. Find if Path Exists in Graph
        There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). 
        The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] 
        denotes a bi-directional edge between vertex ui and vertex vi. 
        Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
        You want to determine if there is a valid path that exists from vertex source to vertex destination.
        Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, 
        or false otherwise.
        # Time:  O(|V| + |E|)
        # Space: O(|V| + |E|)
        # dfs solution
    '''
      
    adj     = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    visited = set()

    def dfs(s, visited):
        if s == destination:
            return True
        else:
            visited.add(s)
            return any([dfs(neighbor, visited) for neighbor in adj[s] if neighbor not in visited])

    return dfs(source, visited)  

def validPath2(n, edges, start, end):
    ''' 
        1971. Find if Path Exists in Graph
        # Time:  O(|V| + |E|)
        # Space: O(|V| + |E|)
        # bfs solution
    '''
    # if the edges list is empty then return False
    if len(edges) in [0,1]:
        return True
    
    # build the adjacency list
    adj = defaultdict(list)
    for x,y in edges:
        adj[x].append(y)
        adj[y].append(x)
        
    
    # Edge case: check if either of the vertex is not in the graph
    if not start in adj or not end in adj:
        return False
    
    visited = [False] * (len(adj)*2)
    queue = [start]
    
    found = False
    
    while queue:
        node = queue.pop(0)  # take out the node which we want to process
        
        # mark it as visited
        visited[node] = True
        
        if end in adj[node]:
            found = True
            break
        
        # add all the neighbours to the queue for processing
        for val in adj[node]:
            if visited[val] == False: # only add the node if it is not visited
                queue.append(val)
            
    return found

class DisjSet:
    ''' Disjoint Set Data Structures
        Consider a situation with a number of persons and following tasks to be performed on them.
        Add a new friendship relation, i.e., a person x becomes friend of another person y.
        Find whether individual x is a friend of individual y (direct or indirect friend)

        Example:
        
        We are given 10 individuals say,
        a, b, c, d, e, f, g, h, i, j
        
        Following are relationships to be added.
        a <-> b  
        b <-> d
        c <-> f
        c <-> i
        j <-> e
        g <-> j
        
        And given queries like whether a is a friend of d
        or not.
        
        We basically need to create following 4 groups
        and maintain a quickly accessible connection
        among group items:
        G1 = {a, b, d}
        G2 = {c, f, i}
        G3 = {e, g, j}
        G4 = {h}
        Problem : To find whether x and y belong to same group or not, i.e., to find if x and y are direct/indirect friends.
        
        Solution : Partitioning the individuals into different sets according to the groups in which they fall. 
        This method is known as disjoint set data structure which maintains collection of disjoint sets 
        and each set is represented by its representative which is one of its members.
    '''
    def __init__(self, n):
        # Constructor to create and
        # initialize sets of n items
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
  
  
    # Finds set of given item x
    def find(self, x):
          
        # Finds the representative of the set
        # that x is an element of
        if (self.parent[x] != x):
              
            # if x is not the parent of itself
            # Then x is not the representative of
            # its set,
            self.parent[x] = self.find(self.parent[x])
              
            # so we recursively call Find on its parent
            # and move i's node directly under the
            # representative of this set
  
        return self.parent[x]
  
  
    # Do union of two sets represented
    # by x and y.
    def Union(self, x, y):
          
        # Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)
  
        # If they are already in same set
        if xset == yset:
            return
  
        # Put smaller ranked item under
        # bigger ranked item if ranks are
        # different
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
  
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
  
        # If ranks are same, then move y under
        # x (doesn't matter which one goes where)
        # and increment rank of x's tree
        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1

def earliestAcq(logs, N):
    ''' In a social group, there are N people, with unique integer ids from 0 to N-1.
        We have a list of logs, where each logs[i] = [timestamp, id_A, id_B] contains a non-negative integer timestamp, 
        and the ids of two different people.
        Each log represents the time in which two different people became friends.  
        Friendship is symmetric: if A is friends with B, then B is friends with A.
        Let's say that person A is acquainted with person B if A is friends with B, or A is a friend of someone acquainted with B.
        Return the earliest time for which every person became acquainted with every other person.
        Return -1 if there is no such earliest time.
    '''
    parent = [i for i in range(N)]
    def findParent(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    count = N
    for time, a, b in sorted(logs):
        pa = findParent(a)
        pb = findParent(b)
        if pa != pb:
            count -= 1
            if count == 1:
                return time
            parent[pb] = pa
    return -1    
    
def findJudge(self, n, trust):
    """
        997. Find the Town Judge
        Easy
        In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
        If the town judge exists, then:
        The town judge trusts nobody.
        Everybody (except for the town judge) trusts the town judge.
        There is exactly one person that satisfies properties 1 and 2.
        You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
        Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
    """
    
    d       = defaultdict(set)
    dnot    = defaultdict(set)
    for edge in trust:
        u, v    = edge
        d[v].add(u)
        dnot[u].add(v)
     
    for i in range( 1, n+1 ):
        if len( d[i] ) == n-1 and len( dnot[i] ) == 0:
            return i
    return -1


def allPathsSourceTarget(graph):
    """
        797. All Paths From Source to Target
        Medium
        Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
        The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
        
         Recursive solution - see backtracking
         :type graph: List[List[int]]
        :rtype: List[List[int]]
    """
    def dfs( source, dest, graph, path, res ):
        for v in graph[source]:
            if v == dest:
                res.append(path[::]+[v])
            else:
                path    += [v]
                dfs( v, dest, graph, path, res )
                path.pop()
        
        
    n       = len(graph)
    res     = []
    dfs( 0, n-1, graph, [0], res ) 
    return res

def allPathsSourceTarget(graph):
    """
        797. All Paths From Source to Target
        Medium
        Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
        The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
        
         Iterative solution BFS with queue
         :type graph: List[List[int]]
        :rtype: List[List[int]]
    """
        
    n       = len(graph)
    res     = []
    q       = [[0]]
    dest    = n-1
    
    while q:
        temp = q.pop(0)
        if temp[-1] == dest:
            res.append(temp)
        else:
            for v in graph[temp[-1]]:
                q.append( temp + [v] )
          
    return res
