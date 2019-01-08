#pragma once
#include <iostream>
#include <vector>
#include <queue>
#include <stack>

using namespace std;

// data structure to store graph edges
struct Edge
{
	int src, dest;
};

// class to represent a graph object
class Graph
{

public:
	// No. of vertices
	int V;
	// construct a vector of vectors to represent an adjacency list
	vector<vector<int>> adjList;

	// Graph Constructor
	Graph(const vector<Edge>& edges, int V);
	void addEdge(int src, int dest);
	void addEdge(const Edge& edge);
	// Perform BFS on graph starting from vertex src and
	// returns true of cycle is found in the graph
	bool BFS(int src);
	// another BFS on graph starting from vertex s
	void BFS_2(int s);

	// A recursive function used by DFS 
	void DFSUtil(int v, vector<bool>& visited);
	// DFS traversal of the vertices reachable from v. 
	// It uses recursive DFSUtil() 
	void DFS(int v);

	bool isCyclicUtil(int v, vector<bool>& visited, vector<bool>& rs);  // used by isCyclic()
	bool isCyclic();    // returns true if there is a cycle in this graph 

	// A recursive function used by topologicalSort 
	void topologicalSortUtil(int v, vector<bool>& visited, stack<int>& stack);

	// The function to do Topological Sort. It uses recursive  
	// topologicalSortUtil() 
	void topologicalSort();
};

Graph::Graph(const vector<Edge>& edges, int V)
{
	this->V = V;
	// resize the vector to V elements of type vector<int>;
	adjList.resize(V);

	// add edges to the directed graph
	for (auto& edge : edges)
		adjList[edge.src].push_back(edge.dest);
}

void Graph::addEdge(int src, int dest)
{
	adjList[src].push_back(dest);
}

void Graph::addEdge(const Edge& edge)
{
	adjList[edge.src].push_back(edge.dest);
}

// node to store vertex and its parent info in BFS
struct Node
{
	int v;
	int parent;
};

// Perform BFS on graph starting from vertex src and
// returns true of cycle is found in the graph
bool Graph::BFS(int src)
{
	// stores vertex is discovered or not
	vector<bool> discovered(V);

	// mark source vertex as discovered
	discovered[src] = true;

	// create a queue used to do BFS and
	// push source vertex into the queue
	queue<Node> q;
	q.push({ src, -1 });

	// run till queue is not empty
	while (!q.empty())
	{
		// pop front node from queue and print it
		Node node = q.front();
		q.pop();

		// do for every edge (v -> u)
		for (int u : this->adjList[node.v])
		{
			if (!discovered[u])
			{
				// mark it discovered
				discovered[u] = true;

				// construct the queue node containing info
				// about vertex and push it into the queue
				q.push({ u, node.v });
			}
			// u is discovered and u is not a parent
			else if (u != node.parent)
			{
				// we found a cross-edge ie. cycle is found
				return true;
			}
		}
	}
	// No cross-edges found in the graph
	return false;
}

void Graph::BFS_2(int s)
{
	// Mark all the vertices as not visited 
	vector<bool> visited(V, false);

	// Create a queue for BFS 
	queue<int> queue;

	// Mark the current node as visited and enqueue it 
	visited[s] = true;
	queue.push(s);

	// 'i' will be used to get all adjacent vertices of a vertex 


	while (!queue.empty())
	{
		// Dequeue a vertex from queue and print it 
		s = queue.front();
		cout << s << " ";
		queue.pop();

		// Get all adjacent vertices of the dequeued 
		// vertex s. If a adjacent has not been visited,  
		// then mark it visited and enqueue it 
		for (vector<int>::iterator i = adjList[s].begin(); i != adjList[s].end(); ++i)
		{
			if (!visited[*i])
			{
				visited[*i] = true;
				queue.push(*i);
			}
		}
	}
}

void Graph::DFSUtil(int v, vector<bool>& visited)
{
	// Mark the current node as visited and 
	// print it 
	visited[v] = true;
	cout << v << " ";

	// Recur for all the vertices adjacent 
	// to this vertex 
	for (vector<int>::iterator i = adjList[v].begin(); i != adjList[v].end(); ++i)
		if (!visited[*i])
			DFSUtil(*i, visited);
}

// DFS traversal of the vertices reachable from v. 
// It uses recursive DFSUtil() 
void Graph::DFS(int v)
{
	// Mark all the vertices as not visited 
	vector<bool> visited(V, false);

	// Call the recursive helper function 
	// to print DFS traversal 
	DFSUtil(v, visited);
}

// This function is a variation of DFSUytil() in https://www.geeksforgeeks.org/archives/18212 
bool Graph::isCyclicUtil(int v, vector<bool>& visited, vector<bool>& recStack)
{
	if (visited[v] == false)
	{
		// Mark the current node as visited and part of recursion stack 
		visited[v] = true;
		recStack[v] = true;

		// Recur for all the vertices adjacent to this vertex 
		
		for (vector<int>::iterator i = adjList[v].begin(); i != adjList[v].end(); ++i)
		{
			if (!visited[*i] && isCyclicUtil(*i, visited, recStack))
				return true;
			else if (recStack[*i])
				return true;
		}

	}
	recStack[v] = false;  // remove the vertex from recursion stack 
	return false;
}

// Returns true if the graph contains a cycle, else false. 
// This function is a variation of DFS() in https://www.geeksforgeeks.org/archives/18212 
bool Graph::isCyclic()
{
	// Mark all the vertices as not visited and not part of recursion 
	// stack 
	vector<bool> visited(V, false);
	vector<bool> recStack(V, false);

	// Call the recursive helper function to detect cycle in different 
	// DFS trees 
	for (int i = 0; i < V; i++)
		if (isCyclicUtil(i, visited, recStack))
			return true;

	return false;
}

// A recursive function used by topologicalSort 
void Graph::topologicalSortUtil(int v, vector<bool>& visited, stack<int>& stack)
{
	// Mark the current node as visited. 
	visited[v] = true;

	// Recur for all the vertices adjacent to this vertex 
	for (vector<int>::iterator i = adjList[v].begin(); i != adjList[v].end(); ++i)
		if (!visited[*i])
			topologicalSortUtil(*i, visited, stack);

	// Push current vertex to stack which stores result 
	stack.push(v);
}

// The function to do Topological Sort. It uses recursive  
// topologicalSortUtil() 
void Graph::topologicalSort()
{
	stack<int> stack;

	// Mark all the vertices as not visited 
	vector<bool> visited(V, false);

	// Call the recursive helper function to store Topological 
	// Sort starting from all vertices one by one 
	for (int i = 0; i < V; i++)
		if (visited[i] == false)
			topologicalSortUtil(i, visited, stack);

	// Print contents of stack 
	while (!stack.empty())
	{
		cout << stack.top() << " ";
		stack.pop();
	}
}