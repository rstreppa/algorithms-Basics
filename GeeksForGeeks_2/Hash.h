#pragma once
#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <unordered_map>
#include <algorithm>
#include <unordered_set>

using namespace std;

// Structure for a binary tree node 
struct Node
{
	int key;
	Node* left; 
	Node* right;
	Node(int key);
};

Node::Node(int key)
{
	this->key   = key;
	this->left  = nullptr;
	this->right = nullptr;
}

// Utility function to store vertical order in map 'm' 
// 'hd' is horizontal distance of current node from root. 
// 'hd' is initally passed as 0 
void getVerticalOrder(Node* root, int hd, map<int, vector<int>>& m)
{
	// Base case 
	if (root == nullptr)
		return;

	// Store current node in map 'm' 
	m[hd].push_back(root->key);

	// Store nodes in left subtree 
	getVerticalOrder(root->left, hd-1, m);

	// Store nodes in right subtree 
	getVerticalOrder(root->right, hd + 1, m);
}

// The main function to print vertical oder of a binary tree 
// with given root 
void printVerticalOrder(Node* root)
{
	// Create a map and store vertical oder in map using 
	// function getVerticalOrder() 
	map<int, vector<int>> m;
	int hd = 0;
	getVerticalOrder(root, hd, m);

	// Traverse the map and print nodes at every horigontal 
	// distance (hd) 
	for (map<int, vector<int>>::iterator it = m.begin(); it != m.end(); it++)
	{
		for (int i = 0; i<it->second.size(); ++i)
			cout << it->second[i] << " ";
		cout << endl;
	}
}

/* Return true if arr2 is a subset of arr1 */
bool isSubset_naive(vector<int> arr1, vector<int> arr2)
{
	int i = 0;
	int j = 0;
	for (i = 0; i < arr2.size(); i++)
	{
		for (j = 0; j < arr1.size(); j++)
		{
			if (arr2[i] == arr1[j])
				break;
		}

		/* If the above inner loop was
		not broken at all then arr2[i]
		is not present in arr1[] */
		if (j == arr1.size())
			return false;
	}

	/* If we reach here then all
	elements of arr2[] are present
	in arr1[] */
	return true;
}

/* Standard Binary Search function*/
int binarySearch(vector<int> arr, int low, int high, int x) 
{ 
  if(high >= low) 
  { 
    int mid = (low + high)/2;  /*low + (high - low)/2;*/
   
    /* Check if arr[mid] is the first occurrence of x. 
        arr[mid] is first occurrence if x is one of the following 
        is true: 
        (i)  mid == 0 and arr[mid] == x 
        (ii) arr[mid-1] < x and arr[mid] == x 
     */
    if(( mid == 0 || x > arr[mid-1]) && (arr[mid] == x)) 
      return mid; 
    else if(x > arr[mid]) 
      return binarySearch(arr, (mid + 1), high, x); 
    else
      return binarySearch(arr, low, (mid -1), x); 
  } 
 return -1; 
}

void exchange(int& a, int& b)
{
	int temp;
	temp = a;
	a = b;
	b = temp;
}

int partition(vector<int> A, int si, int ei)
{
	int x = A[ei];
	int i = (si - 1);
	int j;

	for (j = si; j <= ei - 1; j++)
	{
		if (A[j] <= x)
		{
			i++;
			exchange(A[i], A[j]);
		}
	}
	exchange(A[i + 1], A[ei]);
	return (i + 1);
}

/* Implementation of Quick Sort
A[] --> Array to be sorted
si  --> Starting index
ei  --> Ending index
*/
void quickSort(vector<int> A, int si, int ei)
{
	int pi;    /* Partitioning index */
	if (si < ei)
	{
		pi = partition(A, si, ei);
		quickSort(A, si, pi - 1);
		quickSort(A, pi + 1, ei);
	}
}

bool isSubset_sorting(vector<int> arr1, vector<int> arr2)
{
	int i = 0;
	int m = arr1.size();
	quickSort(arr1, 0, m - 1);
	for (i = 0; i<arr2.size(); i++)
	{
		if (binarySearch(arr1, 0, m - 1, arr2[i]) == -1)
			return false;
	}

	/* If we reach here then all elements of arr2[]
	are present in arr1[] */
	return true;
}

/* Return true if arr2 is a subset of arr1 */
bool isSubset_hash(vector<int> arr1, vector<int> arr2)
{
	set<int> hset;

	// hset stores all the values of arr1 
	for (int i = 0; i < arr1.size(); i++)
	{
		if (hset.find(arr1[i]) == hset.end())
			hset.insert(arr1[i]);
	}

	// loop to check if all elements of arr2 also 
	// lies in arr1 
	for (int i = 0; i < arr2.size(); i++)
	{
		if (hset.find(arr2[i]) == hset.end())
			return false;
	}
	return true;
}



class LinkedList
{
	struct Node
	{
		int data;
		Node* next;
		Node(int d)
		{
			data = d;
			next = nullptr;
		}
	};

	Node* head; // head of list 

			   /* Linked list Node*/

	/* Inserts a node at start of linked list */
	void push(int new_data)
	{
		/* 1 & 2: Allocate the Node &
		Put in the data*/
		Node* temp = new Node(new_data);

		/* 3. Make next of new Node as head */
		temp->next = head;

		/* 4. Move the head to point to new Node */
		head = temp;
	}

	void append(int new_data)
	{
		if (head == nullptr)
		{
			Node* n = new Node(new_data);
			head = n;
			return;
		}
		Node* n1 = head;
		Node* n2 = new Node(new_data);
		while (n1->next)
			n1 = n1->next;

		n1->next = n2;
		n2->next = nullptr;
	}

	/* A utilty function that returns true if data is
	present in linked list else return false */
	bool isPresent(int data)
	{
		Node* t = head;
		while (t)
		{
			if (t->data == data)
				return true;
			t = t->next;
		}
		return false;
	}

	LinkedList getIntersection(Node* head1, Node* head2)
	{
		set<int> hset;
		Node* n1 = head1;
		Node* n2 = head2;
		LinkedList result;

		// loop stores all the elements of list1 in hset 
		while (n1)
		{
			if (hset.find(n1->data) == hset.end())
			{
				hset.insert(n1->data);
			}
			else
			{
				hset.insert(n1->data);
			}
			n1 = n1->next;
		}

		//For every element of list2 present in hset 
		//loop inserts the element into the result 
		while (n2)
		{
			if (hset.find(n2->data) != hset.end())
			{
				result.push(n2->data);
			}
			n2 = n2->next;
		}
		return result;
	}

	LinkedList getUnion(Node* head1, Node* head2)
	{
		// HashMap that will store the  
		// elements of the lists with their counts 
		unordered_map<int, int> hmap;
		Node* n1 = head1;
		Node* n2 = head2;
		LinkedList result;

		// loop inserts the elements and the count of  
		// that element of list1 into the hmap 
		while (n1)
		{
			if (hmap.find(n1->data) != hmap.end())
			{
				int val = hmap[n1->data];
				hmap.insert(pair<int, int>(n1->data, val + 1));
			}
			else
			{
				hmap.insert(pair<int, int>(n1->data, 1));
			}
			n1 = n1->next;
		}

		// loop further adds the elements of list2 with  
		// their counts into the hmap  
		while (n2)
		{
			if (hmap.find(n2->data) != hmap.end())
			{
				int val = hmap[n2->data];
				hmap.insert(pair<int, int>(n2->data, val + 1));
			}
			else
			{
				hmap.insert(pair<int, int>(n2->data, 1));
			}
			n2 = n2->next;
		}

		// Eventually add all the elements 
		// into the result that are present in the hmap 
		for (unordered_map<int, int>::iterator it = hmap.begin(); it != hmap.end(); ++it)
			result.append(it->first);
		return result;
	}
};

// Function to check if array has 2 elements  
// whose sum is equal to the given value 
bool hasArrayTwoCandidates(vector<int> A, int sum)
{
	int l, r;

	/* Sort the elements */
	sort(A.begin(), A.end());

	/* Now look for the two candidates in
	the sorted array*/
	l = 0;
	r = A.size() - 1;
	while (l < r)
	{
		if (A[l] + A[r] == sum)
			return true;
		else if (A[l] + A[r] < sum)
			l++;
		else // A[i] + A[j] > sum 
			r--;
	}
	return false;
}

void printPairs(vector<int> arr, int sum)
{
	unordered_set<int> s;
	for (int i = 0; i < arr.size(); i++)
	{
		int temp = sum - arr[i];

		if (temp >= 0 && s.find(temp) != s.end())
			cout << "Pair with given sum " << sum <<
			" is (" << arr[i] << ", " << temp <<
			")" << endl;

		s.insert(arr[i]);
	}
}

void printItinerary(map<string, string> dataSet)
{
	// To store reverse of given map 
	map<string, string> reversemap;
	map<string, string>::iterator it;

	// To fill reverse map, iterate through the given map 
	for (it = dataSet.begin(); it != dataSet.end(); it++)
		reversemap[it->second] = it->first;

	// Find the starting point of itinerary 
	string start;

	for (it = dataSet.begin(); it != dataSet.end(); it++)
	{
		if (reversemap.find(it->first) == reversemap.end())
		{
			start = it->first;
			break;
		}
	}

	// If we could not find a starting point, then something wrong with input 
	if (start.empty())
	{
		cout << "Invalid Input" << endl;
		return;
	}

	// Once we have starting point, we simple need to go next, 
	//next of next using given hash map 
	it = dataSet.find(start);
	while (it != dataSet.end())
	{
		cout << it->first << "->" << it->second << endl;
		it = dataSet.find(it->second);
	}
}