#pragma once
#include <stack>

using namespace std;

template<typename T>
class Queue 
{
private:
	stack<T> inbox;
	stack<T> outbox;
public:
	Queue() {}
	~Queue() {}
	Queue(const Queue& other) = default;
	Queue& operator=(const Queue& other) = default;
	void queue(const T& item);
	T deque();
};

template<typename T>
void Queue<T>::queue(const T& item)
{
	inbox.push(item);
}

template<typename T>
T Queue<T>::deque()
{
	if (outbox.empty())
	{
		while (!inbox.empty())
		{
			T tmp = inbox.top();
			inbox.pop();
			outbox.push(tmp);
		}
	}
	T res = outbox.top();
	outbox.pop();
	return res;
}

