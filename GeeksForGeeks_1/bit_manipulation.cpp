#include <stdio.h>
#include <iostream>

using namespace std;

int findOdd(int arr[], int n);

// 7) Count set bits in integer
int countSetBits(int x);
// 8) Find log base 2 of 32 bit integer
int log2(int x);
// 9) Checking if given 32 bit integer is power of 2
int isPowerof2(int x);
void myswap(int& a, int& b);

int main(int argc, char* argv[])
{
	/* & (bitwise AND) | (bitwise OR) ^ (bitwise XOR) << (left shift) >> (right shift) ~ (bitwise NOT) */
	unsigned char a = 5, b = 9;			// a = 5(00000101), b = 9(00001001) 
	printf("a = %d, b = %d\n", a, b);
	printf("a&b = %d\n", a&b);			// The result is 00000001 
	printf("a|b = %d\n", a | b);		// The result is 00001101 
	printf("a^b = %d\n", a^b);			// The result is 00001100 
	printf("~a = %d\n", a = ~a);		// The result is 11111010 
	printf("b<<1 = %d\n", b << 1);		// The result is 00010010  
	printf("b>>1 = %d\n", b >> 1);		// The result is 00000100  

	// 1) The left shift and right shift operators should not be used for negative numbers 
	// 2) The bitwise XOR operator is the most useful operator from technical interview perspective
	int arr[] = { 12, 12, 14, 90, 14, 14, 14 };
	int n = sizeof(arr) / sizeof(arr[0]);
	printf("The odd occurring element is %d ", findOdd(arr, n));
	cout << endl;
	// 3) The bitwise operators should not be used in place of logical operators.
	// 4) The left-shift and right-shift operators are equivalent to multiplication and division by 2 respectively.
	// 5) The & operator can be used to quickly check if a number is odd or even
	// The value of expression (x & 1) would be non-zero only if x is odd, otherwise the value would be zero.
	int x = 29;
	(x & 1) ? printf("Odd") : printf("Even");
	cout << endl;
	// 6) The ~ operator should be used carefully

	// 1) Clear all bits from LSB to ith bit
	// int x = 29; 00011101) and we want to clear LSB to 3rd bit, total 4 bits
	int i = 3;
	auto mask = ~((1 << i + 1) - 1);	// mask = 16(00010000), mask = 16-1 = 15(00001111), ~mask 11110000 
	x &= mask;							// 16 (00010000)
	cout << x << endl;

	// 2) Clearing all bits from MSB to i-th bit
	auto mask2 = (1 << i) - 1;
	x &= mask2;
	cout << x << endl;

	// 5) Upper case English alphabet to lower case
	char ch = 'A';		// (01000001)
	auto mask3 = ' ';	// (00100000)
	ch |= mask3;		// ‘a’(01100001)
	cout << ch << endl;

	// 6) Lower case English alphabet to upper case
	ch &= '_';			// ‘a’(01100001) & '_'(11011111) =  ‘A’ (01000001)
	cout << ch << endl;

	// 7) Count set bits in integer
	int y = 29;
	cout << countSetBits(y) << endl;
	
	// 8) Find log base 2 of 32 bit integer
	cout << log2(y) << endl;
	
	// 9) Checking if given 32 bit integer is power of 2
	cout << isPowerof2(y) << endl;

	// 6) Convert binary code directly into an integer in C++
	auto number = 0b011;
	cout << number << endl;

	// 7) The Quickest way to swap two numbers :
	int p = 4;
	int q = 3;
	cout << p << ", " << q << endl;
	myswap(p, q);
	cout << p << ", " << q << endl;

	int kkk;
	cin >> kkk;
	return kkk;
}

// Function to return the only odd occurring element 
int findOdd(int arr[], int n)

{
	int res = 0;
	for (int i = 0; i < n; ++i)
		res ^= arr[i];
	return res;
}

int countSetBits(int x)
{
	int count = 0;
	while (x)
	{
		x &= (x - 1);
		count++;
	}
	return count;
}

int log2(int x)
{
	int res = 0;
	while (x >>= 1)
		res++;
	return res;
}

int isPowerof2(int x)
{
	return (x && !(x & x - 1));
	/*	Logic: All the power of 2 have only single bit set e.g. 16 (00010000).
	If we minus 1 from this, all the bits from LSB to set bit get toggled,
	i.e., 16 - 1 = 15 (00001111).Now if we AND x with(x - 1) and the result is 0
	then we can say that x is power of 2 otherwise not.
	We have to take extra care when x = 0.
	*/
}

void myswap(int& a, int& b)
{
	a ^= b;
	b ^= a;
	a ^= b;
	/*
		// Code to swap 'x' and 'y' 
		x = x * y;  // x now becomes 50 
		y = x / y;  // y becomes 10 
		x = x / y;  // x becomes 5 
	*/
}

//bit reversal function
uint32_t reverseBits(uint32_t n)
{
	uint32_t tmp = 0;         //  Assign num to the tmp 

	for (int iLoop = 0; iLoop < 31; iLoop++)
		if ((n & (1 << iLoop))) // check set bits of num
			tmp |= 1 << (31 - iLoop); //putting the set bits of num in tmp
	return tmp;
}

//left rotate n by d bits
#define INT_BITS 32
int leftRotate(unsigned n, unsigned d) 
{ 
	/* In n<<d, last d bits are 0. To put first 3 bits of n at
	last, do bitwise or of n<<d with n >>(INT_BITS - d) */
	return (n << d) | (n >> (INT_BITS - d));
}