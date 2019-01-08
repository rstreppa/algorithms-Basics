#pragma once
#include <vector>
#include <algorithm>
#include <set>


using namespace std;

vector<vector<int>> combinations(vector<int> v, unsigned int k)
{
	vector<vector<int>> res;
	size_t n = v.size();

	vector<bool> mask(n, false);
	fill(mask.end() - k, mask.end(), true);
	do
	{
		vector<int> r;
		for (unsigned int i = 0; i < n; ++i)
			if (mask[i])
				r.push_back(v[i]);
		res.push_back(r);
	} while (next_permutation(mask.begin(), mask.end())); // SORTED permutations, hence correct number of combinations
	
	return res;
}

int nChoosek(int n, int k) 
{
	if (k > n) 
		return 0;
	if (k > n/2) 
		k = n - k;
	int res = 1;
	for (int i = 0; i < k; ++i)
		res = res*(n - i) / (i + 1);
	return res;
}

vector<int> pascalRow(int n) 
{
	vector<int> res;
	for (int i = 0; i <= n; ++i) 
	{
		if (i == 0 || i == n) 
			res.push_back(1);
		else res.push_back(nChoosek(n, i));
	}
	return res;
}

vector<int> pascalRow_2(int n)
{
	vector<int> res(n + 1);
	res[0] = 1;
	for (int i = 1; i <= n; ++i)
		for (int j = i; j >= 1; --j)
			res[j] += res[j - 1];
	return res;
}

/*
46. Permutations
Given a collection of distinct integers, return all possible permutations.
*/
vector<vector<int> > permute(vector<int>& num)
{
	vector<vector<int>> res;
	permuteDFS(num, 0, res);
	return res;
}
void permuteDFS(vector<int> &num, int start, vector<vector<int>> &res)
{
	if (start >= num.size()) 
		res.push_back(num);
	for (int i = start; i < num.size(); ++i)
	{
		swap(num[start], num[i]);
		permuteDFS(num, start + 1, res);
		swap(num[start], num[i]);
	}
}

/*
47. Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
*/
vector<vector<int>> permuteUnique(vector<int>& nums)
{
	set<vector<int>> res;
	permute_repeat(nums, 0, res);
	return vector<vector<int>>(res.begin(), res.end());
}
void permute_repeat(vector<int> &nums, int start, set<vector<int>> &res)
{
	if (start >= nums.size()) res.insert(nums);
	for (int i = start; i < nums.size(); ++i)
	{
		if (i != start && nums[i] == nums[start])
			continue;
		swap(nums[i], nums[start]);
		permute_repeat(nums, start + 1, res);
		swap(nums[i], nums[start]);
	}
}

