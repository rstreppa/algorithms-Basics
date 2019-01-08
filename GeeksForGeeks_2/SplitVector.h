#pragma once
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Utility function to print a vector
template<typename T>
void print(const vector<T>& v)
{
	for (auto &i : v)
		cout << i << ' ';
	cout << '\n';
}

// Split a vector into sub-vectors of size n in C++
vector<vector<int>> split(const vector<int>& v, unsigned int n)
{
	// create vectyor of vectors to store the sub-vectors
	vector<vector<int>> res;

	// determine number of sub-vectors of size n: correct even in the case n = 1 
	unsigned int size = (v.size() - 1) / n + 1;

	// each iteration of this loop process next set of n elements
	// and store it in a vector at k'th index in vec
	for(int k = 0; k < size; ++k)
	{
		// get range for next set of n elements
		auto start_itr = next(v.cbegin(), k*n);
		auto end_itr   = next(v.cbegin(), (k+1)*n);

		// code to handle the last sub-vector as it might
		// contain less elements
		if ((k+1)*n > v.size()) 
			end_itr = v.end();

		// copy elements from the input range to the sub-vector
		vector<int> temp(start_itr, end_itr);
		res.push_back(temp);
	}
	return res;
}

// Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
// For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is[1, 6, 2, 5, 3, 4].

void wiggleSort(vector<int> &nums)
{
	unsigned int n = nums.size();
	sort(nums.begin(), nums.end());
	if (nums.size() <= 2) 
		return;
	for (unsigned int i = 1; i < n / 2; i += 2)
		swap(nums[i], nums[n - 1 - i]);
}