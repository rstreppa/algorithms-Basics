#pragma once
#include <iostream>
#include <queue>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <stack>
#include <unordered_map>

using namespace std;

/* Binary Tree: */ 
struct Node
{
	int data;
	Node *left;
	Node *right;
	Node(int data);
};

Node::Node(int data)
{
	this->data  = data;
	this->left  = nullptr;
	this->right = nullptr;
}

/* Given a binary tree, print its nodes according to the "bottom-up" postorder traversal. */
void printPostorder(Node* root)
{
	if (root == nullptr)
		return;
	// first recur on left subtree 
	printPostorder(root->left);
	// then recur on right subtree 
	printPostorder(root->right);
	// now deal with the node 
	cout << root->data << " ";
}

/* Given a binary tree, print its nodes in inorder*/
void printInorder(Node* root)
{
	if (root == nullptr)
		return;

	/* first recur on left child */
	printInorder(root->left);

	/* then print the data of node */
	cout << root->data << " ";

	/* now recur on right child */
	printInorder(root->right);
}

/* Given a binary tree, print its nodes in preorder*/
void printPreorder(Node* root)
{
	if (root == nullptr)
		return;

	/* first print data of node */
	cout << root->data << " ";

	/* then recur on left sutree */
	printPreorder(root->left);

	/* now recur on right subtree */
	printPreorder(root->right);
}

/* Compute the "height" of a tree -- the number of
nodes along the longest path from the root node
down to the farthest leaf node.*/
int height(Node* root)
{
	if (root == nullptr)
		return 0;
	else
		return max(height(root->left), height(root->right)) + 1;
}

/* Print nodes at a given level */
void printGivenLevel(Node* root, unsigned int level)
{
	if (root == nullptr)
		return;
	if (level == 1)
		cout << root->data << endl;
	else if (level > 1)
	{
		printGivenLevel(root->left, level - 1);
		printGivenLevel(root->right, level - 1);
	}
}

/* Function to print level order traversal a tree*/
void printLevelOrder(Node* root)
{
	for (unsigned int i = 1; i <= height(root); i++)
		printGivenLevel(root, i);
}

// Iterative method to find height of Bianry Tree 
void printLevelOrder_queue(Node* root)
{
	// Base Case 
	if (root == nullptr)  
		return;

	// Create an empty queue for level order traversal 
	queue<Node*> q;

	// Enqueue Root and initialize height 
	q.push(root);

	while (q.empty() == false)
	{
		// Print front of queue and remove it from queue 
		Node* temp = q.front();
		cout << temp->data << " ";
		q.pop();

		/* Enqueue left child */
		if (temp->left)
			q.push(temp->left);

		/*Enqueue right child */
		if (temp->right)
			q.push(temp->right);
	}
}

/* Function to get diameter of a binary tree */
int diameter(Node* root)
{
	/* base case where tree is empty */
	if (root == nullptr)
		return 0;

	/* get the height of left and right sub-trees */
	int lheight = height(root->left);
	int rheight = height(root->right);

	/* get the diameter of left and right sub-trees */
	int ldiameter = diameter(root->left);
	int rdiameter = diameter(root->right);

	/* Return max of following three
	1) Diameter of left subtree
	2) Diameter of right subtree
	3) Height of left subtree + height of right subtree + 1 */
	return max(lheight + rheight + 1, max(ldiameter, rdiameter));
}

/* Iterative function for inorder tree traversal */
void inOrder(Node* root)
{
	stack<Node*> s;
	Node* curr = root;
	while (curr || s.empty() == false)
	{
		/* Reach the left most Node of the curr Node */
		while (curr)
		{
			/* place pointer to a tree node on the stack before traversing the node's left subtree */
			s.push(curr);
			curr = curr->left;
		}

		/* Current must be NULL at this point */
		curr = s.top();
		s.pop();

		cout << curr->data << " ";

		/* we have visited the node and its left subtree.  Now, it's right subtree's turn */
		curr = curr->right;
	} /* end of while */
}

/* Compute the "maxDepth" of a tree -- the number of
nodes along the longest path from the root node
down to the farthest leaf node.*/
int maxDepth(Node* root)
{
	if (root == nullptr)
		return 0;
	else
		return max(maxDepth(root->left), maxDepth(root->right)) + 1;
}

// This function creates clone by copying key and left and right pointers 
// This function also stores mapping from given tree node to clone. 
Node* copyLeftRightNode(Node* root, map<Node*, Node*>& mymap)
{
	if (root == nullptr)
		return nullptr;

	Node* clone = new Node(root->data);
	mymap[root] = clone;
	clone->left = copyLeftRightNode(root->left, mymap);
	clone->right = copyLeftRightNode(root->right, mymap);
	return clone;
}

// This function makes the clone of given tree. It mainly uses copyLeftRightNode() 
Node* clone(Node* root)
{
	if (root == nullptr)
		return nullptr;
	map<Node*, Node*> mymap;
	Node* clone = copyLeftRightNode(root, mymap);
	return clone;
}

/* Function to find index of value in arr[start...end]
The function assumes that value is present in in[] */
int search(vector<int> arr, int strt, int end, int value)
{
	for (unsigned int i = strt; i <= end; ++i) 
	{
		if (arr[i] == value)
			return i;
	}
}

/* Recursive function to construct binary of size
len from Inorder traversal in[] and Preorder traversal
pre[]. Initial values of inStrt and inEnd should be
0 and len -1. The function doesn't do any error
checking for cases where inorder and preorder
do not form a tree */
Node* buildTree(vector<int> in, vector<int> pre, int inStrt, int inEnd, unordered_map<int, int>& mp)
{
	static int preIndex = 0;

	if (inStrt > inEnd)
		return nullptr;

	/* Pick current node from Preorder traversal using preIndex and increment preIndex */
	int curr = pre[preIndex++];
	Node* tNode = new Node(curr);

	/* If this node has no children then return */
	if (inStrt == inEnd)
		return tNode;

	/* Else find the index of this node in Inorder traversal */
	int inIndex = mp[curr];

	/* Using index in Inorder traversal, construct left and
	right subtress */
	tNode->left = buildTree(in, pre, inStrt, inIndex - 1, mp);
	tNode->right = buildTree(in, pre, inIndex + 1, inEnd, mp);

	return tNode;
}

// This function mainly creates an unordered_map, then calls buildTree() 
Node* buldTreeWrap(vector<int> in, vector<int> pre, int len)
{
	// Store indexes of all items so that we we can quickly find later 
	unordered_map<int, int> mp;
	for (unsigned int i = 0; i < len; i++)
		mp[in[i]] = i;

	return buildTree(in, pre, 0, len - 1, mp);
}

/* Get width of a given level */
unsigned int getWidth(Node* root, int level)
{
	if (root == nullptr)
		return 0;

	if (level == 1)
		return 1;

	else if (level > 1)
		return getWidth(root->left, level-1) + getWidth(root->right, level-1);
}

/* Function to get the maximum width of a binary tree*/
unsigned int getMaxWidth(Node* root)
{
	int maxWidth = 0;

	/* Get width of each level and compare
	the width with maximum width so far */
	for (unsigned int i = 1; i <= height(root); i++)
	{
		unsigned int width = getWidth(root, i);
		if (width > maxWidth)
			maxWidth = width;
	}
	return maxWidth;
}

// Function to find the maximum width of the tree using level order traversal 
unsigned int maxWidth(Node* root)
{
	// Base case 
	if (root == nullptr)
		return 0;

	// Initialize result 
	unsigned int result = 0;

	// Do Level order traversal keeping track of number of nodes at every level. 
	queue<Node*> q;
	q.push(root);
	while (!q.empty())
	{
		// Get the size of queue when the level order traversal for one level finishes 
		unsigned int count = q.size();

		// Update the maximum node count value 
		result = max(count, result);

		// Iterate for all the nodes in the queue currently 
		while (count--)
		{
			// Dequeue an node from queue 
			Node* temp = q.front();
			q.pop();

			// Enqueue left and right children of 
			// dequeued node 
			if (temp->left)
				q.push(temp->left);
			if (temp->right)
				q.push(temp->right);
		}
	}
	return result;
}

void printKDistant(Node* root, int k)
{
	if (root == nullptr)
		return;

	if (k == 0)
	{
		cout << root->data << " ";
		return;
	}
	else
	{
		printKDistant(root->left, k-1);
		printKDistant(root->right, k-1);
	}
}

/* If target is present in tree, then prints the ancestors
and returns true, otherwise returns false. */
bool printAncestors(Node* root, int target)
{
	/* base cases */
	if (root == nullptr)
		return false;

	if (root->data == target)
		return true;

	/* If target is present in either left or right subtree of this node, then print this node */
	if (printAncestors(root->left, target) ||
		printAncestors(root->right, target))
	{
		cout << root->data << " ";
		return true;
	}

	/* Else return false */
	return false;
}

/* A utility function to check whether trees with roots as root1 and
root2 are identical or not */
bool areIdentical(Node* root1, Node* root2)
{
	/* base cases */
	if (root1 == nullptr && root2 == nullptr)
		return true;

	if (root1 == nullptr || root2 == nullptr)
		return false;

	/* Check if the data of both roots is same and data of left and right
	subtrees are also same */
	return (root1->data == root2->data   &&
		areIdentical(root1->left, root2->left) &&
		areIdentical(root1->right, root2->right));
}

/* This function returns true if S is a subtree of T, otherwise false */
bool isSubtree(Node* T, Node* S)
{
	/* base cases */
	if (S == nullptr)
		return true;

	if (T == nullptr)
		return false;

	/* Check the tree with root as current node */
	if (areIdentical(T, S))
		return true;

	/* If the tree with root as current node doesn't match then
	try left and right subtrees one by one */
	return isSubtree(T->left, S) || isSubtree(T->right, S);
}

void helperInvert(Node* p) 
{

	Node* temp = p->left;
	p->left    = p->right;
	p->right   = temp;

	if (p->left)
		helperInvert(p->left);

	if (p->right)
		helperInvert(p->right);
}

Node* invertTree(Node* root) 
{
	if (root) 
		helperInvert(root);
	return root;
}

Node* invertTree_iter(Node* root) 
{
	queue<Node*> queue;

	if (root)
		queue.push(root);

	while (!queue.empty()) 
	{
		Node* p = queue.front();
		queue.pop();
		if (p->left)
			queue.push(p->left);
		if (p->right)
			queue.push(p->right);

		Node* temp = p->left;
		p->left    = p->right;
		p->right   = temp;
	}

	return root;
}

// Flatten a Binary Tree to a Linked List in place
// recursive soltion
void flatten(Node* root)
{
	if (!root || !root->left && !root->right)
		return;

	// if root->left exists then we have to make it root->right 
	if (root->left)
	{
		// move left recursively 
		flatten(root->left);

		// store the node root->right 
		Node* tmpRight = root->right;
		root->right = root->left;
		root->left = nullptr;

		// find the position to insert 
		// the stored value    
		Node* t = root->right;
		while (t->right)
			t = t->right;

		// insert the stored value 
		t->right = tmpRight;
	}

	// now call the same function 
	// for root->right 
	flatten(root->right);
}

// Flatten a Binary Tree to a Linked List in place
// iterative soltion using queue
void flatten(Node* root)
{
	queue<Node*> queue;

	if (root)
		queue.push(root);

	while(!queue.empty())
	{
		Node* p = queue.front();
		queue.pop();
		if (p->left)
			queue.push(p->left);
		if (p->right)
			queue.push(p->right);

		Node* temp = p->right;
		p->right   = p->left;
		p->left = nullptr;
		while (p->right)
			p = p->right;
		p->right = temp;
	}
}

// Recursive function to print all paths from leaf to root node
void printLeafToRootPaths(Node* root, vector<int>& path)
{
	// base case
	if (!root)
		return;

	// include current node to path vector
	path.push_back(root->data);

	// if leaf node is found, print the path
	if (!root->left && !root->right)
		printPath(path);

	// recurse for left and right subtree
	printLeafToRootPaths(root->left, path);
	printLeafToRootPaths(root->right, path);

	// remove current node after left and right subtree are done
	path.pop_back();
}

// Main function to print all paths from leaf to root node
void printLeafToRootPaths(Node* root)
{
	// vector to store left to root path
	vector<int> path;

	// call recursive function
	printLeafToRootPaths(root, path);
}

void printPath(const vector<int>& path)
{
	for (int i = path.size() - 1; i > 0; i--)
		cout << path.at(i) << " -> ";

	cout << path.at(0) << endl;
}

