#pragma once
#include <stack>
#include <queue>
#include <string>
#include <iostream>

using namespace std;

template<typename T>
class Queue
{
private: 
	stack<T> inbox;
	stack<T> outbox;
public:
	void queue(T item);
	T deque();
};

template<typename T>
void Queue<T>::queue(T item)
{
	inbox.push(item);
}

template<typename T>
T Queue<T>::deque()
{
	T res;
	if (outbox.empty())
	{
		while (!inbox.empty())
		{
			outbox.push(inbox.top());
			inbox.pop();
		}
	}
	res = outbox.top();
	outbox.pop();
	return res;
}


// This function uses queue data structure to print binary numbers 
void generatePrintBinary(int n)
{
	// Create an empty queue of strings 
	queue<string> q;

	// Enqueue the first binary number 
	q.push("1");

	// This loops is like BFS of a tree with 1 as root 
	// 0 as left child and 1 as right child and so on 
	while (n--)
	{
		// print the front of queue 
		string s1 = q.front();
		q.pop();
		cout << s1 << "\n";

		string s2 = s1;  // Store s1 before changing it 

		// Append "0" to s1 and enqueue it 
		q.push(s1.append("0"));

		// Append "1" to s2 and enqueue it. Note that s2 contains 
		// the previous front 
		q.push(s2.append("1"));
	}
}

