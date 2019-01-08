#pragma once

#include <iostream>
#include <vector>
#include <stack>
#include <string>

using namespace std;


class Stack
{
private:
	char* a;
	int t;
public:
	Stack(unsigned int size);
	bool empty();
	void push(char b);
	void pop();
	char top();
};


Stack::Stack(unsigned int size)
{
	a = new char[size];
	t = -1;			// empty stack
}

bool Stack::empty()
{
	return t < 0;
}

void Stack::push(char b)
{
	a[++t] = b;
}

void Stack::pop()
{
	if (empty())
	{
		cout << "Empty Stack" << endl;
		return;
	}

	cout << a[t--];
}

char Stack::top()
{
	return a[t];
}

void reverse_1(string& s)
{
	reverse(s.begin(), s.end());
}

void reverse_2(string& s)
{
	for (unsigned int l = 0, unsigned int h = s.length() - 1; l < h; l++, h--)
		swap(s[l], s[h]);
}

void reverse_3(string& s)
{
	unsigned int l = s.length();
	stack<char> stack;
	for (unsigned int i = 0; i < l; ++i)
		stack.push(s[i]);
	unsigned int index = 0;
	while (!stack.empty())
	{
		s[index++] = stack.top();
		stack.pop();
	}
}


// Below is a recursive function  
// that inserts an element 
// at the bottom of a stack. 


void insert_at_bottom(char x, stack<char>& stack)
{
	if (stack.size() == 0)
		stack.push(x);
	else
	{
		// All items are held in Function Call 
		// Stack until we reach end of the stack 
		// When the stack becomes empty, the 
		// st.size() becomes 0, the above if  
		// part is executed and the item is  
		// inserted at the bottom 
		char a = stack.top();
		stack.pop();
		insert_at_bottom(x, stack);

		// push allthe items held in  
		// Function Call Stack 
		// once the item is inserted 
		// at the bottom 
		stack.push(a);
	}
}

void rev(stack<char> st)
{
	if (st.size() > 0)
	{
		// Hold all items in Function  
		// Call Stack until we 
		// reach end of the stack  
		char x = st.top();
		st.pop();
		rev(st);
		// Insert all the items held 
		// in Function Call Stack 
		// one by one from the bottom  
		// to top. Every item is 
		// inserted at the bottom  
		insert_at_bottom(x, st);
	}
}


void reverse_4(string& s)
{
	unsigned int l = s.length();
	stack<char> stack;
	for (unsigned int i = 0; i < l; ++i)
		stack.push(s[i]);
	rev(stack);
	for (unsigned int i = 0; i < l; ++i)
	{
		s[i] = stack.top();
		stack.pop();
	}
}


