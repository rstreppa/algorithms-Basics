#pragma once
#include <iostream>
#include <unordered_set>

using namespace std;

struct Node
{
	int data;
	Node* next;
	Node(int data);
};

Node::Node(int data)
{
	this->data = data;
	this->next = nullptr;
}

struct LinkedList 
{
	Node* head;
	LinkedList();
	void print();			// Function to print linked list
	void push(int data);	// push data at beginning
	void insert(int i, int data);	// Given a node index, insert after it
	void append(int data);	// Add a node at the end
	void deleteKey(int key);	// Given a ‘key’, delete the first occurrence of this key in linked list
	void deleteAt(int i);		// Given a position, deletes the node at the given position
	int length();				// Counts no. of nodes in linked list, iterative
	void swap(int x, int y); 	// swaps the nodes rather than swapping the field from the nodes.
	void swap2(int x, int y);	// swaps the nodes rather than swapping the field from the nodes. Simpler approach
	void reverse(); 			// Reverse a linked list by changing links between nodes. Iterative Method
	static Node* SortedMerge(Node* a, Node* b);	// Merge two sorted linked lists, Recursive plays nicely wth merge
	bool detectLoop();			// Returns true if there is a loop in linked list else returns false. 
	bool detectloopFloyd();		// Returns true if there is a loop in linked list. Floyd’s Cycle-Finding Algorithm
	void rotate(int k);			// Rotate a Linked List counter-clockwise by k nodes.
};

LinkedList::LinkedList()
{
	head = nullptr;
}

// Function to print linked list
void LinkedList::print()
{
	Node* temp = head;
	while (temp)
	{
		cout << temp->data << " ";
		temp = temp->next;
	}
}

// push data at beginning
void LinkedList::push(int data)
{
	// 1. allocate node 2. put in the data
	Node* temp = new Node(data);
	// 3. Make next of new node as head
	temp->next = head;
	// 4. move the head to point to the new node
	head = temp;
}

// push data at beginning, second way
// if you want to modify local variable of one function inside another function, 
// pass pointer to that variable.
void push(Node** head, int data)
{
	Node* temp = new Node(data);
	temp->next = *head;
	*head = temp;
} // usage push(&head, 1)

// push data at beginning, third way
Node* push(Node* head, int data)
{
	Node* temp = new Node(data);
	temp->next = head;
	return temp;
} // usage head = push(head, 1)

// Given a node prev, insert after the given prev
void insert(Node* prev, int data)
{
	Node* temp = new Node(data);
	// Make next of new node as next of prev
	temp->next = prev->next;
	// move next of prev as new node
	prev->next = temp;
}

// Given a node index, insert after it
void LinkedList::insert(int i, int data)
{
	Node* temp = new Node(data);
	Node* prev = head;
	for (unsigned int k = 1; k <= i; ++k)
		prev = prev->next;
	temp->next = prev->next;
	prev->next = temp;
}

// Add a node at the end
void LinkedList::append(int data)
{
	Node* temp = new Node(data);
	if (head == nullptr)
		head = temp;
	else
	{
		Node* last = head;
		while (last->next)
			last = last->next;
		last->next = temp;
	}
}

// Given a ‘key’, delete the first occurrence of this key in linked list
void LinkedList::deleteKey(int key)
{
	// Store head node
	Node* temp = head;
	Node* prev;
	
	// If head node itself holds the key to be deleted
	if (temp && temp->data == key)
	{
		head = temp->next;	// Changed head 
		delete temp;		// delete old head 
		return;
	}
	// Search for the key to be deleted, keep track of the 
	// previous node as we need to change 'prev->next'
	while (temp && temp->data != key)
	{
		prev = temp;
		temp = temp->next;
	}
	
	// If key was not present in linked list 
	if (temp == nullptr) 
		return;
	
	// Unlink the node from linked list 
	prev->next = temp->next;
	delete temp;					// Free memory 
}

// Given a position, deletes the node at the given position
void LinkedList::deleteAt(int i)
{
	// If linked list is empty 
	if (head == nullptr)
		return;

	// Store head node 
	Node* temp = head;

	// If head needs to be removed 
	if (i == 0)
	{
		head = temp->next;   // Change head 
		delete temp;         // free old head 
		return;
	}
	
	// Find previous node of the node to be deleted 
	for (unsigned int k = 0; temp && k<i-1; k++)
		temp = temp->next;
	
	// If position is more than number of ndoes 
	if (temp == nullptr || temp->next == nullptr)
		return;

	// temp->next is the node to be deleted 
	// Store pointer to the next of node to be deleted 
	Node* next = temp->next->next;

	// Unlink the node from linked list 
	delete temp->next;  // Free memory 
	temp->next = next;  // Unlink the deleted node from list 
}

// Counts no. of nodes in linked list, iterative
int LinkedList::length()
{
	int res = 0;
	Node* current = head;
	while (current)
	{
		res++;
		current = current->next;
	}
	return res;
}

// Counts no. of nodes in linked list, recursive
int length_rec(Node* head)
{
	// Base case 
	if (head == nullptr)
		return 0;

	// count is 1 + count of remaining list
	return 1 + length_rec(head->next);
}

// swaps the nodes rather than swapping the field from the nodes.
void LinkedList::swap(int x, int y)
{
	// Nothing to do if x and y are same 
	if (x == y) 
		return;

	// Search for x (keep track of prev_x and curr_x 
	Node* prev_x = nullptr; 
	Node* curr_x = head;
	while (curr_x && curr_x->data != x)
	{
		prev_x = curr_x;
		curr_x = curr_x->next;
	}

	// Search for y (keep track of prev_y and curr_yy 
	Node* prev_y = nullptr;
	Node* curr_y = head;
	while (curr_y && curr_y->data != y)
	{
		prev_y = curr_y;
		curr_y = curr_y->next;
	}

	// If either x or y is not present, nothing to do 
	if (curr_x == nullptr || curr_y == nullptr)
		return;

	// If x is not head of linked list 
	if (prev_x)
		prev_x->next = curr_y;
	else // Else make y as new head 
		head = curr_y;

	// If y is not head of linked list 
	if (prev_y)
		prev_y->next = curr_x;
	else  // Else make x as new head 
		head = curr_x;

	// Swap next pointers 
	Node* temp = curr_y->next;
	curr_y->next = curr_x->next;
	curr_x->next = temp;
}

void swapPointers(Node*& a, Node*& b)
{
	Node* temp = a;
	a = b;
	b = temp;
}

void LinkedList::swap2(int x, int y)
{

	// Nothing to do if x and y are same 
	if (x == y)
		return;

	Node** a = nullptr;
	Node** b = nullptr;

	// search for x and y in the linked list 
	// and store therir pointer in a and b 
	while (head) 
	{
		if (head->data == x)
			a = &head;
		else if (head->data == y)
			b = &head;

		head = head->next;
	}

	// if we have found both a and b 
	// in the linked list swap current 
	// pointer and next pointer of these 
	if (a && b) {
		swapPointers(*a, *b);
		swapPointers(((*a)->next), ((*b)->next));
	}
}

// Reverse a linked list by changing links between nodes. Iterative Method
void LinkedList::reverse()
{
	// Initialize current, previous and next pointers 
	Node* prev = nullptr;
	Node* current = head;
	Node* next = nullptr;

	while (current)
	{
		// Store next 
		next = current->next;

		// Reverse current node's pointer 
		current->next = prev;

		// Move pointers one position ahead. 
		prev = current;
		current = next;
	}
	head = prev;
}

// Reverse a linked list by changing links between nodes. Recursive Method
void reverse_rec(Node** head_ref)
{
	Node* first;
	Node* rest;

	/* empty list */
	if (*head_ref == nullptr)
		return;

	/* suppose first = {1, 2, 3}, rest = {2, 3} */
	first = *head_ref;
	rest  = first->next;

	/* List has only one node */
	if (rest == nullptr)
		return;

	/* reverse the rest list and put the first element at the end */
	reverse_rec(&rest);
	first->next->next = first;

	/* tricky step -- see the diagram */
	first->next = nullptr;

	/* fix the head pointer */
	*head_ref = rest;
}
// Merge two sorted linked lists, Recursive plays nicely wth merge
Node* LinkedList::SortedMerge(Node* a, Node* b)
{
	Node* result = nullptr;

	/* Base cases */
	if (a == nullptr)
		return(b);
	else if (b == nullptr)
		return(a);

	/* Pick either a or b, and recur */
	if (a->data <= b->data)
	{
		result = a;
		result->next = SortedMerge(a->next, b);
	}
	else
	{
		result = b;
		result->next = SortedMerge(a, b->next);
	}
	return(result);
}

// Returns true if there is a loop in linked list else returns false.
bool LinkedList::detectLoop()
{
	
	unordered_set<Node*> s;
	Node* current = head;
	while (current)
	{
		// If this node is already present 
		// in hashmap it means there is a cycle 
		// (Because you we encountering the 
		// node for the second time). 
		if (s.find(current) != s.end())
			return true;

		// If we are seeing the node for 
		// the first time, insert it in hash 
		s.insert(current);

		current = current->next;
	}
	return false;
}

// Returns true if there is a loop in linked list. Floyd’s Cycle-Finding Algorithm
bool LinkedList::detectloopFloyd()
{
	Node* slow_p = head;
	Node* fast_p = head;

	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
		if (slow_p == fast_p)
			return true;
	}
	return false;
}

// Rotate a Linked List counter-clockwise by k nodes.
void LinkedList::rotate(int k)
{
	if (k == 0)
		return;

	// Let us understand the below code for example k = 4 and 
	// list = 10->20->30->40->50->60. 
	Node* current = head;

	// current will either point to kth or NULL after this loop. 
	//  current will point to node 40 in the above example 
	int count = 1;
	while (count < k && current)
	{
		current = current->next;
		count++;
	}

	// If current is NULL, k is greater than or equal to count 
	// of nodes in linked list. Don't change the list in this case 
	if (current == nullptr)
		return;

	// current points to kth node. Store it in a variable. 
	// kthNode points to node 40 in the above example 
	Node *kthNode = current;

	// current will point to last node after this loop 
	// current will point to node 60 in the above example 
	while (current->next)
		current = current->next;

	// Change next of last node to previous head 
	// Next of 60 is now changed to node 10 
	current->next = head;

	// Change head to (k+1)th node 
	// head is now changed to node 50 
	head = kthNode->next;

	// change next of kth node to NULL 
	// next of 40 is now NULL 
	kthNode->next = nullptr;
}

