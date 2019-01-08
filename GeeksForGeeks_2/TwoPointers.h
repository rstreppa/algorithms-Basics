#pragma once
#include <vector>
#include <stack>
using namespace std;

/*
26. Remove Duplicates from Sorted Array
Easy
Given a sorted array nums, remove the duplicates in - place such that each element 
appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying 
the input array in - place with O(1) extra memory.
*/

int removeDuplicates(vector<int>& nums)
{
	if (nums.empty())
		return 0;
	int pre = 0, cur = 0, n = nums.size();
	while (cur < n)
	{
		if (nums[pre] == nums[cur])
			++cur;
		else
			nums[++pre] = nums[cur++];
	}
	return pre + 1;
}

/*
75. Sort Colors
Medium
Given an array with n objects colored red, white or blue, sort them in - place 
so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.
*/
void sortColors(vector<int>& nums)
{
	int n = nums.size();
	int bound0 = 0, bound2 = n - 1;
	for (int i = 0; i <= bound2; i++)
	{
		while (nums[i] == 2 && bound2 > i)
		{
			swap(nums[i], nums[bound2]);
			bound2--;
		}
		while (nums[i] == 0 && bound0 < i)
		{
			swap(nums[i], nums[bound0]);
			bound0++;
		}
	}
}

/*
234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome
*/
struct ListNode 
{
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(nullptr) {}
};



bool isPalindrome(ListNode* head)
{
	if (!head || !head->next)
		return true;
	ListNode *slow = head, *fast = head;
	stack<int> s;
	s.push(head->val);
	while (fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		s.push(slow->val);
	}
	if (!fast->next) s.pop();
	while (slow->next)
	{
		slow = slow->next;
		int tmp = s.top(); s.pop();
		if (tmp != slow->val)
			return false;
	}
	return true;
}

/*
86. Partition List
Given a linked list and a value x, partition it such that all nodes less than x
come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
*/
ListNode* partition(ListNode* head, int x)
{
	ListNode* dummy1 = new ListNode(0);
	ListNode* dummy2 = new ListNode(0);
	ListNode* curr2 = dummy2;
	dummy1->next = head;
	head = dummy1;

	while (head->next)
	{
		if (head->next->val<x)   // skip node
			head = head->next;
		else
		{  // remove node from dummy1 and insert to the tail of dummy2
			curr2->next = head->next;
			head->next = head->next->next;
			curr2 = curr2->next;
			curr2->next = nullptr;
		}
	}

	head->next = dummy2->next;
	head = dummy1->next;
	delete dummy1;
	delete dummy2;
	return head;
}
