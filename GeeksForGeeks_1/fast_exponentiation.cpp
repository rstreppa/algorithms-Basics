#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

// Exponentiation by squaring.
// This is the standard method for doing modular exponentiation for huge numbers 
// in asymmetric cryptography.
// modular exponentiation
// 5^13 //Starting Problem
// 5 ^ 1 1 0 1 //Convert "13" to binary.
// 5 ^ 2 ^ 2 ^ 2 * 5 ^ 2 ^ 2 * 5

unsigned long long ipow(long base, long exp)
{
	unsigned long long result = 1;
	for (;;)
	{
		if (exp & 1)				// odd exponent: 10001 & 00001 = 1
			result *= base;			
		exp >>= 1;					// lose least significant bit
		if (!exp)					// if 0 break
			break;
		base *= base;				// square base 
	}

	return result;
}

unsigned long long ipow_other(long base, long t)
{
	unsigned long long result = 1;
	vector<int> binary;
	long twoth = 2;
	while (t>0)
	{
		if (t%twoth == 0)
			binary.push_back(0);
		else
		{
			binary.push_back(1);
			t -= twoth / 2;
		}
		twoth = (2 * twoth);
	}

	for (int i = 0; i<binary.size(); i++)
	{
		if (binary[i] == 1)
		{
			result *= base;
		}
		base *= base;
	}
	return result;
}

int main(int argc, char* argv[])
{
	int base = 98 + 26;
	long t = 818638958430279427;
	// cout << ipow(base, t) << endl;
	cout << ipow_other(base, t) << endl;
	int kkk;
	cin >> kkk;
	return kkk;
}




