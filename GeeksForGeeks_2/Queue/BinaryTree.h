#pragma once
#include <cmath>
#include<queue>

// Data structure to store a Binary Tree node
struct Node
{
	int key;
	Node *left, *right;
};

// Recursive function to calculate height of given binary tree
int height(Node* root)
{
	// Base case: empty tree has height 0
	if (root == nullptr)
		return 0;

	// recurse for left and right subtree and consider maximum depth
	return max(height(root->left), height(root->right)) + 1;
}


// Iterative function to calculate height of given binary tree
// by doing level order traversal of the tree
int height(Node *root)
{
	// empty tree has height 0
	if (root == nullptr)
		return 0;

	// create an empty queue and enqueue root node
	queue<Node*> queue;
	queue.push(root);

	Node* front = nullptr;
	int height = 0;

	// run till queue is not empty
	while (!queue.empty())
	{
		// calculate number of nodes in current level
		int size = queue.size();

		// process every node of current level and enqueue their
		// non-empty left and right child to queue
		while (size--)
		{
			front = queue.front();
			queue.pop();

			if (front->left)
				queue.push(front->left);

			if (front->right)
				queue.push(front->right);
		}

		// increment height by 1 for each level
		height++;
	}

	return height;
}
