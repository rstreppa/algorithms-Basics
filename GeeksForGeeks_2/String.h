#pragma once
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <unordered_map>

using namespace std;

vector<string> split(const string s, char c = ' ')
{
	vector<string> res;
	const char* str = s.c_str();
	do
	{
		const char* begin = str;
		while (*str != c && *str)
			str++;
		res.push_back(string(begin, str));
	} while (*str++);
	return res;
}

// Given an input string, reverse the string word by word.
// Could you do it in - place without allocating extra space ?
string reverseWordByWord(string s)
{
	string res = "";
	vector<string> v = split(s);
	unsigned int n = v.size();
	for (unsigned int i = 0; i < n / 2; ++i)
		swap(v[i], v[n - 1 - i]);
	for (auto str : v)
	{
		res += str;
		res += ' ';
	}
	return res;
}




/*
The API : int read4(char *buf) reads 4 characters at a time from a file.
The return value is the actual number of characters read.For example,
it returns 3 if there is only 3 characters left in the file.
By using the read4 API, implement the function int read(char *buf, int n)
that reads n characters from the file.
Note :
The read function will only be called once for each test case.
*/
/*
Understand the problem:
This seemingly easy coding question has some tricky edge cases. When read4 returns
less than 4, we know it must reached the end of file. However, take note that read4
returning 4 could mean the last 4 bytes of the file.

To make sure that the buffer is not copied more than n bytes, copy the remaining bytes
(n – readBytes) or the number of bytes read, whichever is smaller.
*/

// Forward declaration of the read4 API.
int read4(char* buf)
{
	return 0;
}

int read(char* buf, int n)
{
	bool eof = false;
	int charsRead = 0;
	char buf4[4];	// or char* buf4 = new char[4]; 

	while (!eof && charsRead < n)
	{
		int size = read4(buf4);
		eof = size < 4;

		if (charsRead + size > n)
			size = n - charsRead;

		for (unsigned int i = 0; i < size; i++)
			buf[charsRead++] = buf4[i];
	}
	return charsRead;
}


// same as above but The read function may be called multiple times 
/*
Thoughts
The difference between this question and the first version is that the read() function will be called multiple times.
The trouble here will be as the following example if using the first version solution:
file: “abcdefg”
read(3) read(2) read(2) should be “abc” “de” “fg”
but using first version solution it will print “abc” “ef” “”

This is because when you use read4() to read, the pointer to read file has already moved to “e”
after the first call of read4(). So it’s not correct any more.
In order to solve, we need to persist the characters that has been already read by using read4
but it’s not put into the result of read().

Summary:
This problem is not very hard, but requires thinking of every corner cases.
To sum up, the key of the problem is to put the char buf4[4] into global, and maintains two more global variables:
-- offset : the starting position in the buf4 that a read() should start from.
-- bytesLeftInBuf4 : how many elements left in the buf4.

One corner case to consider is when is the eof should be true? In the previous question,
it is true only if bytesFromRead4 < 4. However, in this question, since we might have some bytes left the buf4,
even if it is not end of the file, we may mistakely consider the eof as true.
So the condition to set eof is true is bytesFromRead4 < 4 && bytesLeftInBuf4 == 0

Another corner case we need to consider is: if the bytesFromRead4 + bytesRead > n,
the actual bytes to copy is n - bytesRead.
For example, the file is "abcde", and read(2), in this case, the bytesFromRead4 = 4,
but we should only copy 2 bytes from the buf4. So be very careful about this case.

At the end, we need to update the global offset and bytesLeftInBuf4, as well as the local bytesRead.

Do execrise more about this question, this is really classical.
*/
class Solution {
	bool m_fEof = false;
	char* m_buf4 = new char[4];
	int m_lastPos = 0;
	int m_cBytesLastRead = 0;

	int read(char* buf, int n)
	{
		int curPos = 0;
		while (curPos < n)
		{
			if (m_lastPos == m_cBytesLastRead)
			{
				m_cBytesLastRead = read4(m_buf4);
				m_fEof = m_cBytesLastRead < 4;
				m_lastPos = 0;
			}

			int cBytesToRead = min(n - curPos, m_cBytesLastRead - m_lastPos);
			for (int i = m_lastPos; i<m_lastPos + cBytesToRead; i++)
				buf[curPos++] = m_buf4[i];

			m_lastPos += cBytesToRead;

			if (m_fEof)
				break;
		}

		return curPos;
	}
};

/*
451. Sort Characters By Frequency
Given a string, sort it in decreasing order based on the frequency of characters.
*/
string frequencySort(string s)
{
	string res = "";
	priority_queue<pair<int, char>> q;
	unordered_map<char, int> m;
	for (char c : s)
		++m[c];
	for (auto a : m)
		q.push({ a.second, a.first });
	while (!q.empty())
	{
		auto t = q.top();
		q.pop();
		res.append(t.first, t.second);
	}
	return res;
}

// Function to find and print longest 
// substring without repeating characters. 
string findLongestSubstring(string str)
{
	int i;
	int n = str.length();

	// starting point of current substring. 
	int st = 0;

	// length of current substring. 
	int currlen;

	// maximum length substring without repeating  
	// characters. 
	int maxlen = 0;

	// starting index of maximum length substring. 
	int start;

	// Hash Map to store last occurrence of each 
	// already visited character. 
	unordered_map<char, int> pos;

	// Last occurrence of first character is index 0; 
	pos[str[0]] = 0;

	for (i = 1; i < n; i++) {

		// If this character is not present in hash, 
		// then this is first occurrence of this 
		// character, store this in hash. 
		if (pos.find(str[i]) == pos.end())
			pos[str[i]] = i;

		else {
			// If this character is present in hash then 
			// this character has previous occurrence, 
			// check if that occurrence is before or after 
			// starting point of current substring. 
			if (pos[str[i]] >= st) {

				// find length of current substring and 
				// update maxlen and start accordingly. 
				currlen = i - st;
				if (maxlen < currlen) {
					maxlen = currlen;
					start = st;
				}

				// Next substring will start after the last 
				// occurrence of current character to avoid 
				// its repetition. 
				st = pos[str[i]] + 1;
			}

			// Update last occurrence of 
			// current character. 
			pos[str[i]] = i;
		}
	}

	// Compare length of last substring with maxlen and 
	// update maxlen and start accordingly. 
	if (maxlen < i - st) {
		maxlen = i - st;
		start = st;
	}

	// The required longest substring without 
	// repeating characters is from str[start] 
	// to str[start+maxlen-1]. 
	return str.substr(start, maxlen);
}

/*
8. String to Integer (atoi)
Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary 
until the first non-whitespace character is found. Then, starting from this character, 
takes an optional initial plus or minus sign followed by as many numerical digits as possible, 
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, 
which are ignored and have no effect on the behavior of this function.
*/
int myAtoi(string str)
{
	if (str.empty()) 
		return 0;
	int sign = 1, base = 0, i = 0, n = str.size();
	while (i < n && str[i] == ' ') 
		++i;
	if (str[i] == '+' || str[i] == '-') 
		sign = (str[i++] == '+') ? 1 : -1;

	while (i < n && str[i] >= '0' && str[i] <= '9')
	{
		if (base > INT_MAX / 10 || (base == INT_MAX / 10 && str[i] - '0' > 7))
			return (sign == 1) ? INT_MAX : INT_MIN;
		base = 10 * base + (str[i++] - '0');
	}
	return base * sign;
}
