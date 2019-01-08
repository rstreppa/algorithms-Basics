#pragma once
#include <iostream>
#include <vector>
#include <queue>

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
	q.push({src, -1});

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
				q.push({u, node.v});
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
