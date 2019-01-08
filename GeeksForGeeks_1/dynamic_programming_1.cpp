#include <iostream>
#include <vector>
#include <algorithm>    // std::max


using namespace std;

unsigned long long cache[1000] = {0, };
const long mod = 1000000007;


// dynamic programming for factorial with modulus
long long factorial(int N)
{
	if (N == 1)
		return 1;
	if (cache[N] != 0)
		return cache[N];
	return cache[N] = N * factorial(N - 1) % mod;
}

// Fibonacci recursion: slow
unsigned long long fib_rec(int N)
{
	if (N < 2)
		return 1;
	return fib_rec(N - 1) + fib_rec(N - 2);
}

// Fibonacci dynamic programming: fast
unsigned long long fib_dp(int N)
{
	if (N == 1)
		return 1;
	if (N == 2)
		return 1;
	cache[0] = 1;
	cache[1] = 1;
	if (cache[N] != 0)
		return cache[N];
	return cache[N] = fib_dp(N-1) + fib_dp(N-2);
}

// Fibonacci dynamic programming iterative
unsigned long long fib_dp_iter(int N)
{
	vector<unsigned long long> fibresult(N, 0);
	fibresult[0] = 1;
	fibresult[1] = 1;
	for (int i = 2; i<N; i++)
		fibresult[i] = fibresult[i-1] + fibresult[i-2];
	return fibresult[N-1];
}

/*
Sub-problem: DPn be the number of ways to write N as the sum of 1, 3, and 4.
Finding recurrence: Consider one possible solution, n = x1 + x2 + ... xn. 
If the last number is 1, the sum of the remaining numbers should be n - 1. 
So, number of sums that end with 1 is equal to DPn-1.. 
Take other cases into account where the last number is 3 and 4. 
The final recurrence would be:

DPn = DPn-1 + DPn-3 + DPn-4.

Take care of the base cases. DP0 = DP1 = DP2 = 1, and DP3 = 2.
*/

long sum_of_1_3_4(int N)
{
	vector<long> DP(N+1, 0);
	DP[0] = DP[1] = DP[2] = 1; DP[3] = 2;
	for (unsigned int i = 4; i <= N; i++)
		DP[i] = DP[i - 1] + DP[i - 3] + DP[i - 4];
	return DP[N];
}

/*
"Imagine you have a collection of N wines placed next to each other on a shelf. For simplicity, 
let's number the wines from left to right as they are standing on the shelf with integers from 1 to N, 
respectively. The price of the ith wine is pi. (prices of different wines can be different).

Because the wines get better every year, supposing today is the year 1, on year y 
the price of the ith wine will be y*pi, i.e. y-times the value that current year.

You want to sell all the wines you have, but you want to sell exactly one wine per year, 
starting on this year. One more constraint - on each year you are allowed to sell only either 
the leftmost or the rightmost wine on the shelf and you are not allowed to reorder the wines on the shelf 
(i.e. they must stay in the same order as they are in the beginning).

You want to find out, what is the maximum profit you can get, if you sell the wines in optimal order?"

So, for example, if the prices of the wines are (in the order as they are placed on the shelf, 
from left to right): p1=1, p2=4, p3=2, p4=3. The optimal solution would be to sell the wines in the order 
p1, p4, p3, p2 for a total profit 1 * 1 + 3 * 2 + 2 * 3 + 4 * 4 = 29.

If the prices of the wines are: p1=2, p2=3, p3=5, p4=1, p5=4. 
The greedy strategy would sell them in the order p1, p2, p5, p4, p3 
for a total profit 2 * 1 + 3 * 2 + 4 * 3 + 1 * 4 + 5 * 5 = 49.

But, we can do better if we sell the wines in the order p1, p5, p4, p2, p3 for a total profit 
2 * 1 + 4 * 2 + 1 * 3 + 3 * 4 + 5 * 5 = 50.
*/

/*
int N; // read-only number of wines in the beginning
int p[N]; // read-only array of wine prices
int cache[N][N]; // all values initialized to -1 (or anything you choose)

int profit(int be, int en) {
	if (be > en)
		return 0;
	// these two lines save the day
	if (cache[be][en] != -1)
		return cache[be][en];
	int year = N - (en - be + 1) + 1;
	// when calculating the new answer, don't forget to cache it
	return cache[be][en] = max(
		profit(be + 1, en) + year * p[be],
		profit(be, en - 1) + year * p[en]);
}
*/

/*
Objective:  The maximum subarray problem is the task of finding the contiguous subarray 
within a one-dimensional array of numbers which has the largest sum.

MS(i)  is maximum sum ending at index i
To calculate the solution for any element at index “i” has two options
EITHER added to the solution found till “i-1“th index
OR start a new sum from the index “i“.
MS(i) = Max[MS(i-1) + A[i] , A[i]]
*/

// maximum subarray dynamic programming iterative
int maxSub_iter(const vector<int>& a)
{
	vector<int> MS(a.size() + 1, 0);
	MS[0] = 0;
	for (int j = 1; j <MS.size(); j++) 
		MS[j] = max(MS[j-1] + a[j-1], a[j-1]);
	
	int maxMS = MS[0];
	for (int j = 1; j <MS.size(); j++)
		if (maxMS<MS[j])
			maxMS = MS[j];
	return maxMS;
}

// maximum subarray dynamic programming recursive
int maxSub_recursive(vector<int>& a)
{
	if (a.size() == 1)
		return a[0];
	cache[0] = a[0];
	if (cache[a.size()] != 0)
		return cache[a.size()];
	vector<int>::const_iterator first = a.begin();
	vector<int>::const_iterator last = a.end()-1;
	vector<int> newa(first, last);
	return cache[a.size()] = max(maxSub_recursive(newa) + a.back(), a.back());
}

/*
Longest Common Subsequence
Given two sequences, find the length of longest subsequence present in both of them. 
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. 
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. 
So a string of length n has 2^n different possible subsequences.

1) Optimal Substructure:
Let the input sequences be X[0..m-1] and Y[0..n-1] of lengths m and n respectively. 
And let L(X[0..m-1], Y[0..n-1]) be the length of LCS of the two sequences X and Y. 
Following is the recursive definition of L(X[0..m-1], Y[0..n-1]).

If last characters of both sequences match (or X[m-1] == Y[n-1]) then
L(X[0..m-1], Y[0..n-1]) = 1 + L(X[0..m-2], Y[0..n-2])

If last characters of both sequences do not match (or X[m-1] != Y[n-1]) then
L(X[0..m-1], Y[0..n-1]) = MAX ( L(X[0..m-2], Y[0..n-1]), L(X[0..m-1], Y[0..n-2]) )

*/

// A Naive recursive implementation of LCS problem
// Returns length of LCS for X[0..m-1], Y[0..n-1]
// Time complexity of the above naive recursive approach is O(2^n) in worst case 
// and worst case happens when all characters of X and Y mismatch i.e., length of LCS is 0.
int lcs(char* X, char* Y, int m, int n)
{
	if (m == 0 || n == 0)
		return 0;
	if (X[m - 1] == Y[n - 1])
		return 1 + lcs(X, Y, m - 1, n - 1);
	else
		return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n));
}

// Dynamic Programming C/C++ implementation of LCS problem
// Returns length of LCS for X[0..m-1], Y[0..n-1] */
int lcs_dp(char* X, char* Y, int m, int n)
{
	int** L = new int*[m + 1];
	for (unsigned int i = 0; i < m + 1; ++i)
		L[i] = new int[n + 1];

	/* Following steps build L[m+1][n+1] in bottom up fashion. Note
	that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1] */
	for (unsigned int i = 0; i <= m; i++)
	{
		for (unsigned int j = 0; j <= n; j++)
		{
			if (i == 0 || j == 0)
				L[i][j] = 0;

			else if (X[i - 1] == Y[j - 1])
				L[i][j] = L[i - 1][j - 1] + 1;

			else
				L[i][j] = max(L[i - 1][j], L[i][j - 1]);
		}
	}

	/* L[m][n] contains length of LCS for X[0..n-1] and Y[0..m-1] */
	return L[m][n];
}

// Given a sequence, find the length of the longest palindromic subsequence in it.
// Let X[0..n - 1] be the input sequence of length n 
// and L(0, n - 1) be the length of the longest palindromic subsequence of X[0..n - 1].
// If last and first characters of X are same, then L(0, n - 1) = L(1, n - 2) + 2.
// Else L(0, n - 1) = MAX(L(1, n - 1), L(0, n - 2)).

// Returns the length of the longest palindromic subsequence in seq recursive
int lps(char* seq, int i, int j)
{
	// Base Case 1: If there is only 1 character 
	if (i == j)
		return 1;

	// Base Case 2: If there are only 2 characters and both are same 
	if (seq[i] == seq[j] && i + 1 == j)
		return 2;

	// If the first and last characters match 
	if (seq[i] == seq[j])
		return lps(seq, i + 1, j - 1) + 2;

	// If the first and last characters do not match 
	return max(lps(seq, i, j - 1), lps(seq, i + 1, j));
}

// Returns the length of the longest palindromic subsequence in seq, Dynamic programming 
int lps(char* str)
{
	int n = strlen(str);
	int j, cl;
	int L[n][n];  // Create a table to store results of subproblems 


	// Strings of length 1 are palindrome of lentgh 1 
	for (int i = 0; i < n; i++)
		L[i][i] = 1;

	// Build the table. Note that the lower diagonal values of table are 
	// useless and not filled in the process.  
	// cl is length of substring 
	for (cl = 2; cl <= n; cl++)
	{
		for (int i = 0; i<n - cl + 1; i++)
		{
			j = i + cl - 1;
			if (str[i] == str[j] && cl == 2)
				L[i][j] = 2;
			else if (str[i] == str[j])
				L[i][j] = L[i + 1][j - 1] + 2;
			else
				L[i][j] = max(L[i][j - 1], L[i + 1][j]);
		}
	}
	return L[0][n - 1];
}


int main(int argc, char* argv[])
{
	cout << factorial(5)   << endl;
	cout << factorial(500) << endl;

	cout << fib_dp(500) << endl;
	cout << fib_dp_iter(500) << endl;

	cout << sum_of_1_3_4(5) << endl;
	cout << sum_of_1_3_4(50) << endl;

	vector<int> a = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
	cout << maxSub_iter(a) << endl;			// right
	cout << maxSub_recursive(a) << endl;	// wrong

	char X[] = "AGGTAB";
	char Y[] = "GXTXAYB";

	int m = strlen(X);
	int n = strlen(Y);

	printf("Length of LCS is %d", lcs(X, Y, m, n));
	cout << endl;
	printf("Length of LCS is %d", lcs_dp(X, Y, m, n));
	cout << endl;

	char seq[] = "GEEKSFORGEEKS";
	int n = strlen(seq);
	printf("The length of the LPS is %d", lps(seq, 0, n - 1));

	int kkk;
	cin >> kkk;
	return kkk;
}

