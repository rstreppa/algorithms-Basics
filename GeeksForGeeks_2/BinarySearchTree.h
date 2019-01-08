#pragma once
#include <iostream>
#include <queue>
#include <map>
#include <vector>
#include <set>
#include <stack>

using namespace std;

/* Binary Tree: */
struct Node
{
	int key;
	Node *left;
	Node *right;
	Node(int key);
};

Node::Node(int key)
{
	this->key = key;
	this->left = nullptr;
	this->right = nullptr;
}

// search a given key in a given BST 
Node* search(Node* root, int key)
{
	// Base Cases: root is nullptr or key is present at root 
	if (root == nullptr || root->key == key)
		return root;

	// Key is greater than root's key 
	if (key > root->key)
		return search(root->right, key);

	// Key is smaller than root's key 
	return search(root->left, key);
}

// Iterative function to search a given key in root
bool search_iterative(Node *root, int key)
{
	// traverse the tree and search for the key
	while (root)
	{
		// if given key is less than the current node, go to left
		// subtree else go to right subtree

		if (key < root->key)
			root = root->left;
		else if (key > root->key)
			root = root->right;
		// if key is found return true
		else
			return true;
	}

	// we reach here if the key is not present in the BST
	return false;
}




/* A utility function to insert a new node with given key in BST */
Node* insert(Node* root, int key)
{
	/* If the tree is empty, return a new node */
	if (root == nullptr) 
		return new Node(key);

	/* Otherwise, recur down the tree */
	if (key < root->key)
		root->left = insert(root->left, key);
	else if (key > root->key)
		root->right = insert(root->right, key);

	/* return the (unchanged) node pointer */
	return root;
}

/* Given a non-empty binary search tree, return the node with minimum
key value found in that tree. Note that the entire tree does not
need to be searched. */
Node* minValueNode(Node* root)
{
	Node* current = root;

	/* loop down to find the leftmost leaf */
	while (current->left)
		current = current->left;

	return current;
}

/* Given a binary search tree and a key, this function deletes the key
and returns the new root */
Node* deleteNode(Node* root, int key)
{
	// base case 
	if (root == nullptr) 
		return root;

	// If the key to be deleted is smaller than the root's key, 
	// then it lies in left subtree 
	if (key < root->key)
		root->left = deleteNode(root->left, key);
	// If the key to be deleted is greater than the root's key, 
	// then it lies in right subtree 
	else if (key > root->key)
		root->right = deleteNode(root->right, key);
	// if key is same as root's key, then This is the node 
	// to be deleted 
	else
	{
		// node with only one child or no child 
		if (root->left == nullptr)
		{
			Node* temp = root->right;
			delete root;
			return temp;
		}
		else if (root->right == nullptr)
		{
			Node* temp = root->left;
			delete root;
			return temp;
		}

		// node with two children: Get the inorder successor (smallest 
		// in the right subtree) i.e. smallest of the larger ones 
		Node* temp = minValueNode(root->right);

		// Copy the inorder successor's content to this node 
		root->key = temp->key;

		// Delete the inorder successor 
		root->right = deleteNode(root->right, temp->key);
	}
	return root;
}

// Function to determine if given Binary Tree is a BST or not by keeping a
// valid range (starting from [MIN_VALUE, MAX_VALUE]) and keep shrinking
// it down for each node as we go down recursively
bool isBST(Node* root, int minKey, int maxKey)
{
	// base case
	if (root == nullptr)
		return true;

	// if node's value fall outside valid range
	if (root->key < minKey || root->key > maxKey)
		return false;

	// recursively check left and right subtrees with updated range
	return isBST(root->left, minKey, root->key) && isBST(root->right, root->key, maxKey);
}

// Returns true if given tree is BST. 
bool isBST(Node* root, Node* l = nullptr, Node* r = nullptr)
{
	// Base condition 
	if (root == nullptr)
		return true;

	// if left node exist then check it has 
	// correct data or not i.e. left node's data 
	// should be less than root's data 
	if (l and root->key < l->key)
		return false;

	// if right node exist then check it has 
	// correct data or not i.e. right node's data 
	// should be greater than root's data 
	if (r and root->key > r->key)
		return false;

	// check recursively for every node. 
	return isBST(root->left, l, root) && isBST(root->right, root, r);
}

/* Given a non-empty binary search tree,
return the minimum data value found in that
tree. Note that the entire tree does not need
to be searched. */
int minValue(Node* root) 
{
	Node* current = root;

	/* loop down to find the leftmost leaf */
	while (current->left)
		current = current->left;

	return current->key;
}

Node* minNode(Node* root)
{
	Node* current = root;

	/* loop down to find the leftmost leaf */
	while (current->left)
		current = current->left;

	return current;
}

// This function finds predecessor and successor of key in BST. 
// It sets pre and suc as predecessor and successor respectively 
void findPreSuc(Node* root, Node*& pre, Node*& suc, int key)
{
	// Base case 
	if (root == nullptr)  
		return;

	// If key is present at root 
	if (root->key == key)
	{
		// the maximum value in left subtree is predecessor 
		if (root->left)
		{
			Node* tmp = root->left;
			while (tmp->right)
				tmp = tmp->right;
			pre = tmp;
		}

		// the minimum value in right subtree is successor 
		if (root->right)
		{
			Node* tmp = root->right;
			while (tmp->left)
				tmp = tmp->left;
			suc = tmp;
		}
		return;
	}

	// If key is smaller than root's key, go to left subtree 
	if (key < root->key)
	{
		suc = root;
		findPreSuc(root->left, pre, suc, key);
	}
	else // go to right subtree 
	{
		pre = root;
		findPreSuc(root->right, pre, suc, key);
	}
}

// Recursive function to find inorder successor for given key in a BST
// Note that successor 'succ' is passed by reference to the function
void findSuccessor(Node* root, Node*& succ, int key)
{
	// base case
	if (root == nullptr)
		return;

	// if node with key's value is found, the successor is minimum value
	// node in its right subtree (if any)
	if (root->key == key)
	{
		if (root->right)
			succ = minNode(root->right);
	}
	// if given key is less than the root node, recuse for left subtree
	else if (key < root->key)
	{
		// update successor to current node before recursing in left subtree
		succ = root;
		findSuccessor(root->left, succ, key);
	}
	// if given key is more than the root node, recurse for right subtree
	else
		findSuccessor(root->right, succ, key);
}

// Recursive function to find Lowest Common Ancestor of given nodes
// x and y where both x and y are present in the Binary Search Tree
Node* LCARecursive(Node* root, int x, int y)
{
	// base case: empty tree
	if (root == nullptr)
		return nullptr;

	// if both x and y is smaller than root, LCA exists in left subtree
	if (max(x, y) < root->key)
		return LCARecursive(root->left, x, y);

	// if both x and y is greater than root, LCA exists in right subtree
	else  if (min(x, y) > root->key)
		return LCARecursive(root->right, x, y);
	// if one key is greater (or equal) than root and one key is smaller
	// (or equal) than root, then the current node is LCA
	return root;
}

/* Function to find LCA of n1 and n2. The function assumes that both
n1 and n2 are present in BST */
Node* LCAIterative(Node* root, int n1, int n2)
{
	while (root)
	{
		// If both n1 and n2 are smaller than root, then LCA lies in left 
		if (n1 < root->key && n2 < root->key)
			root = root->left;

		// If both n1 and n2 are greater than root, then LCA lies in right 
		else if (n1 > root->key && n2 > root->key)
			root = root->right;

		else break;
	}
	return root;
}

/*
// traverse the binary tree and store its keys in a set
set<int> set;
extractKeys(root, set);

// put back keys present in set in their correct order in BST
auto it = set.begin();
convertToBST(root, it);

// print the BST
inorder(root);
*/

// Function to perform in-order traversal of the tree
void inorder(Node* root)
{
	if (root == nullptr)
		return;

	inorder(root->left);
	cout << root->key << " ";
	inorder(root->right);
}

// Function to traverse the binary tree and store its keys in a set
void extractKeys(Node *root, set<int>& set)
{
	// base case
	if (root == nullptr)
		return;

	extractKeys(root->left, set);
	set.insert(root->key);
	extractKeys(root->right, set);
}

// Function to put back keys in set in their correct order in BST
// by doing in-order traversal
void convertToBST(Node *root, set<int>::iterator it)
{
	if (root == nullptr)
		return;

	convertToBST(root->left, it);

	root->key = *it;
	it++;

	convertToBST(root->right, it);
}

struct ListNode
{
	int data;
	ListNode* next;
	ListNode(int data);
};

ListNode::ListNode(int data)
{
	this->data = data;
	this->next = nullptr;
}

Node* sortedListToBST(ListNode* head)
{
	if (!head)
		return nullptr;
	if (!head->next)
	{
		Node* root = new Node(head->data);
		return root;
	}
	ListNode* slow = head;
	ListNode* fast = head;
	ListNode* prev = nullptr;

	while (fast && fast->next)
	{
		prev = slow;
		slow = slow->next;
		fast = fast->next->next;
	}

	Node* root = new Node(slow->data);
	prev->next = nullptr;
	slow = slow->next;
	root->left  = sortedListToBST(head);
	root->right = sortedListToBST(slow);

	return root;
}

/*
173. Binary Search Tree Iterator
Implement an iterator over a binary search tree (BST). 
Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.
*/
class BSTIterator {
public:
	BSTIterator(Node* root)
	{
		while (root)
		{
			s.push(root);
			root = root->left;
		}
	}

	/** @return whether we have a next smallest number */
	bool hasNext()
	{
		return !s.empty();
	}

	/** @return the next smallest number */
	int next()
	{
		Node* n = s.top();
		s.pop();
		int res = n->key;
		if (n->right)
		{
			n = n->right;
			while (n)
			{
				s.push(n);
				n = n->left;
			}
		}
		return res;
	}
private:
	stack<Node*> s;
};




