#pragma once
#include <iostream>

using namespace std;

struct Node 
{
	int data;
	Node* next;
	Node* prev;
	Node(int data);
};

Node::Node(int data)
{
	this->data = data;
	this->next = nullptr;
	this->prev = nullptr;
}

class DLL
{
	Node* head;
	void push(int data);
	void insert(Node* prev, int data);
	void append(int data);
	void deleteNode(Node* del);
	void reverse();
};

void DLL::push(int data)
{
	Node* temp = new Node(data);
	if (head == nullptr)
		head = temp;
	else
	{
		temp->next = head;
		head->prev = temp;
		head = temp;
	}
}

void DLL::append(int data)
{
	Node* temp = new Node(data);
	if (head == nullptr)
		head = temp;
	else 
	{
		Node* curr = head;
		while (curr)
			curr = curr->next;
		curr->next = temp;
		temp->prev = curr;
	}

}

void DLL::insert(Node* prev, int data)
{
	Node* temp = new Node(data);
	if (prev == nullptr)
		return;
	temp->next = prev->next;
	prev->next = temp;
	temp->prev = prev;
	if(temp->next)
		temp->next->prev = temp;
}

void DLL::deleteNode(Node* del)
{
	if (head == nullptr || del == nullptr)
		return;
	if (head == del)
		head = head->next;
	if (del->next)		// not the last node
		del->next->prev = del->prev;
	if (del->prev)		// not the first node
		del->prev->next = del->next;
	delete del;
}

void DLL::reverse()
{
	if (head == nullptr)
		return;
	Node* current = head;
	Node* temp = nullptr;
	while (current)
	{
		Node* temp = current->prev;
		current->prev = current->next;
		current->next = temp;
		current = current->prev;
	}
	head = temp->prev;
}