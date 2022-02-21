# -*- coding: utf-8 -*-
""" 
@date:          Thu Jan 20 21:08:43 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Data_Structures/Graph/graph.py
"""

from graph import AdjNode, Graph, Graph2, isCycleExist, validPath, validPath2, DisjSet, earliestAcq



def main():
    print('#### Driver program to the above Graph class #########################')
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.print_graph()
    print('#### Driver program to the Graph2 and BFS algo #########################')
    g = Graph2(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print ("Following is Breadth First Traversal (starting from vertex 2)")
    print()
    g.BFS(2)
    print()
    print('#### Driver program to the Graph2 and isCycleExist algo #########################')
    h=Graph2(6)
    h.addEdge(0,1)
    h.addEdge(1,2)
    h.addEdge(2,0)
    h.addEdge(3,4)
    h.addEdge(4,5)
     
    if isCycleExist(h.V,h.graph):
        print("Yes")
    else:
        print("No")
    print ("Depth First Traversal (or Search) for a graph (starting from vertex 2)")    
    g.DFS(2)
    print()
    print ("Depth First Traversal (or Search) for a graph (starting from vertex 2) iterative method ")
    g.DFS2()
    print()
    print ("Topological sort for a graph recursive method ")
    g.topologicalSort()
    print('#### validPath #########################')
    print(validPath(3, [[0,1],[1,2],[2,0]], 0, 2))
    print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))
    print(validPath2(3, [[0,1],[1,2],[2,0]], 0, 2))
    print(validPath2(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))
    print('#### DisjSet #########################')
    obj = DisjSet(5)
    obj.Union(0, 2)
    obj.Union(4, 2)
    obj.Union(3, 1)
    if obj.find(4) == obj.find(0):
        print('Yes')
    else:
        print('No')
    if obj.find(1) == obj.find(0):
        print('Yes')
    else:
        print('No') 
    print('#################### earliestAcq #########################')   
    logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]] 
    N = 6
    print(earliestAcq(logs, N))