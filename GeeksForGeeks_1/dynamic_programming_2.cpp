#include <iostream>
#include<vector>

using namespace std;

/*
Catalan numbers:
1) Count the number of expressions containing n pairs of parentheses which are correctly matched.
For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).

2) Count the number of possible Binary Search Trees with n keys
How many structurally unique BSTs for keys from 1..N?
We know that all node in left subtree are smaller than root and in right subtree are larger than root
so if we have ith number as root, all numbers from 1 to i-1 will be in left subtree and i+1 to N
will be in right subtree. If 1 to i-1 can form x different trees and i+1 to N can from y different trees
then we will have x*y total trees when ith number is root and we also have N choices for root also
so we can simply iterate from 1 to N for root and another loop for left and right subtree.

3) Count the number of full binary trees
(A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.

C(0) = 1; C(n+1) = Sum(k=0, ..., n) C(k)C(n-k); 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, ...
C(n) = (2n n)/(n+1) 
*/


// A recursive function to find nth catalan number 
unsigned long int catalan(unsigned int n)
{
	// Base case 
	if (n <= 1) return 1;

	// catalan(n) is sum of catalan(i)*catalan(n-i-1) 
	unsigned long int res = 0;
	for (int i = 0; i<n; i++)
		res += catalan(i)*catalan(n - i - 1);

	return res;
}

// A dynamic programming based function to find nth Catalan number 
unsigned long int catalanDP(unsigned int n)
{
	// Table to store results of subproblems 
	unsigned long int* catalan = new unsigned long int[n + 1];

	// Initialize first two values in table 
	catalan[0] = catalan[1] = 1;

	// Fill entries in catalan[] using recursive formula 
	for (int i = 2; i <= n; i++)
	{
		catalan[i] = 0;
		for (int j = 0; j<i; j++)
			catalan[i] += catalan[j] * catalan[i - j - 1];
	}

	// Return last entry 
	return catalan[n];
	// delete[] catalan;
}

// Returns value of Binomial Coefficient C(n, k) 
unsigned long int binomialCoeff(unsigned int n, unsigned int k)
{
	unsigned long int res = 1;

	// Since C(n, k) = C(n, n-k) 
	if (k > n - k)
		k = n - k;

	// Calculate value of [n*(n-1)*---*(n-k+1)] / [k*(k-1)*---*1] 
	for (int i = 0; i < k; ++i)
	{
		res *= (n - i);
		res /= (i + 1);
	}

	return res;
}

// A Binomial coefficient based function to find nth catalan number in O(n) time 
unsigned long int catalan_bin(unsigned int n)
{
	// Calculate value of 2nCn 
	unsigned long int c = binomialCoeff(2 * n, n);

	// return 2nCn/(n+1) 
	return c / (n + 1);
}

/*
How to construct all BST for keys 1..N?
The idea is to maintain a list of roots of all BSTs. 
Recursively construct all possible left and right subtrees. 
Create a tree for every pair of left and right subtree and add the tree to list. 

1) Initialize list of BSTs as empty.
2) For every number i where i varies from 1 to N, do following
......a)  Create a new node with key as 'i', let this node be 'node'
......b)  Recursively construct list of all left subtrees.
......c)  Recursively construct list of all right subtrees.
3) Iterate for all left subtrees
a) For current leftsubtree, iterate for all right subtrees
Add current left and right subtrees to 'node' and add
'node' to list.
*/

//  node structure 
struct Node
{
	int key;
	Node* left;
	Node* right;
};

// A utility function to create a new BST node 
Node* newNode(int item)
{
	Node* temp = new Node;
	temp->key = item;
	temp->left = temp->right = nullptr;
	return temp;
}

// A utility function to do preorder traversal of BST 
void preorder(Node* root)
{
	if (root != nullptr)
	{
		cout << root->key << " ";
		preorder(root->left);
		preorder(root->right);
	}
}

//  function for constructing trees 
vector<Node*> constructTrees(int start, int end)
{
	vector<Node*> list;

	/*  if start > end   then subtree will be empty so returning nullptr in the list */
	if (start > end)
	{
		list.push_back(nullptr);
		return list;
	}

	/*  iterating through all values from start to end  for constructing\
	left and right subtree recursively  */
	for (int i = start; i <= end; i++)
	{
		/*  constructing left subtree   */
		vector<Node*> leftSubtree = constructTrees(start, i - 1);

		/*  constructing right subtree  */
		vector<Node*> rightSubtree = constructTrees(i + 1, end);

		/*  now looping through all left and right subtrees and connecting them to ith root below  */
		for (int j = 0; j < leftSubtree.size(); j++)
		{
			Node* left = leftSubtree[j];
			for (int k = 0; k < rightSubtree.size(); k++)
			{
				Node* right = rightSubtree[k];
				Node* node = newNode(i);		// making value i as root 
				node->left = left;              // connect left subtree 
				node->right = right;            // connect right subtree 
				list.push_back(node);           // add this tree to list 
			}
		}
	}
	return list;
}



int main(int argc, char* argv[])
{
	// cout << catalan(20) << endl;
	cout << catalanDP(20)   << endl;
	cout << catalan_bin(20) << endl;

	// Construct all possible BSTs 
	vector<Node*> totalTreesFrom1toN = constructTrees(1, 5);

	// Printing preorder traversal of all constructed BSTs
	cout << "Preorder traversals of all constructed BSTs are \n";
	for (int i = 0; i < totalTreesFrom1toN.size(); i++)
	{
		preorder(totalTreesFrom1toN[i]);
		cout << endl;
	}


	int kkk;
	cin >> kkk;
	return kkk;
}