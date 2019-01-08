#pragma once

class BinaryTree 
{
private:
	struct TreeNode 
	{
		int value;
		TreeNode* left;
		TreeNode* right;
	};
	TreeNode* root;
	void insert(TreeNode* current, TreeNode* parent, int value);

public:
	BinaryTree();
	void insertNode(int value);
};

BinaryTree::BinaryTree()
{
	root = nullptr;
}

void BinaryTree::insert(TreeNode* current, TreeNode* parent, int value)
{
	if (current == nullptr)
	{
		TreeNode* newnode = new TreeNode;
		newnode->value = value;
		newnode->left  = nullptr;
		newnode->right = nullptr;
		if (parent->value > newnode->value)
			parent->left = newnode;
		else
			parent->right = newnode;
	}
	else if (current->value > value)
	{
		insert(current->left, current, value);
	}
	else
	{
		insert(current->right, current, value);
	}
}

void BinaryTree::insertNode(int value)
{
	if (root == nullptr)
	{
		root = new TreeNode;
		root->value = value;
		root->left  = nullptr;
		root->right = nullptr;
	}
	else
	{
		if (root->value > value)
			insert(root->left, root, value);
		else
			insert(root->right, root, value);
	}
}