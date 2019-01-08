#pragma once
#include <iostream>

using namespace std;

struct Node
{
	int data;
	Node* next;
	Node();
	Node(int data);
};

Node::Node()
{
}

Node::Node(int data)
{
	this->data = data;
	this->next = nullptr;
}

struct CLL
{
	Node* head;
	CLL();

	bool isEmpty();							// function to check whether Linked list is empty
	Node* getLastNode();					// retrieve the last node of the CLL, starting from head
	void push(int data);					// function to add Node at front, return position 
	void insert(int i, int data);			// add Node at position i	
	void append(int data);					// function to add Node at the End of list, return position
	int length();							// length of the CLL
	Node* searchKey(int key);				// function to search a value
	void deleteKey(int key);				// function to delete any Node
};

CLL::CLL()
{
	head = nullptr;
}

bool CLL::isEmpty()
{
	return head == nullptr ?  true : false;
}

Node* CLL::getLastNode()
{
	Node* temp = head;
	if (temp == nullptr)
		return temp;
	else
	{
		while (temp->next != head)
			temp = temp->next;
		return temp;
	}
}

void CLL::push(int data)
{
	// 1. allocate node 2. put in the data
	Node* temp = new Node(data);
	// 3. Make next of new node as head (as in singly linked list)
	temp->next = head;
	
	// 4. Get the Last Node and make its next point to new Node
	if (head == nullptr)
		temp->next = temp;		// 4a. only one node CLL points to itself
	else
	{	
		Node* prev = head;
		while (prev->next != head)
			prev = prev->next;
		prev->next = temp;
	}

	// 5. move the head to point to the new node
	head = temp;
}

void CLL::append(int data)
{
	// 1. allocate node 2. put in the data
	Node* temp = new Node(data);
	
	// 3a. only one node CLL points to itself
	if (head == nullptr)
	{
		temp->next = temp;
		head = temp;
	}
	else // 3b. make new node be pointed by last and pointring to head
	{
		Node* prev = head;
		while (prev->next != head)
			prev = prev->next;
		prev->next = temp;
		temp->next  = head;
		// 4. do not channge head
	}	
}

void CLL::insert(int i, int data)
{
	Node* temp = new Node(data);
	Node* prev = head;
	for (unsigned int k = 1; k <= i; ++k)
		prev = prev->next;
	temp->next = prev->next;
	prev->next = temp;
}

int CLL::length()
{
	int res = 0;
	if (head == nullptr)
		return res;
	else
	{
		Node* prev = head;
		do 
		{
			res++;
			prev = prev->next;
		} while (prev->next != head);
		return res;
	}
}

Node* CLL::searchKey(int key)
{
	if (head == nullptr)
		return head;
	else
	{
		Node* prev = head;
		while (prev->data != key)
		{
			prev = prev->next;
			if (prev->next == head)
				return nullptr;
		}
		return prev;
	}
}

void CLL::deleteKey(int key)
{
	if (head == nullptr)
		return;
	
	Node* temp = head;
	Node* prev;

	if (temp->data == key)
	{
		head = temp->next;
		delete temp;
		return;
	}
	
	while (temp->next != head && temp->data != key)
	{
		prev = temp;
		temp = temp->next;
	}

	if (temp->next == head)
		return;

	prev->next = temp->next;
	delete temp;
}

