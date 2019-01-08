#pragma once
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <queue>
#include <map>
#include <set>


using namespace std;

const int ALPHABET_SIZE = 26;

class Trie
{
public:
	Trie* character[ALPHABET_SIZE];
	bool isLeaf;
public:
	Trie();
	void insert(string key);
	bool deletion(Trie*& trie, string key);
	bool search(string key);
	bool haveChildren(Trie const* trie);
};


Trie::Trie()
{
	for (unsigned int i = 0; i < ALPHABET_SIZE; ++i)
		character[i] = nullptr;
	isLeaf = false;
}

// Iterative function to insert a key in the Trie
void Trie::insert(string key)
{
	// start from root node
	Trie* curr = this;
	for (unsigned int i=0; i<key.length(); ++i)
	{
		// create a new node if path doesn't exists
		if (curr->character[key[i]] == nullptr)
			curr->character[key[i]] = new Trie();

		// go to next node
		curr = curr->character[key[i]];
	}

	// mark current node as leaf
	curr->isLeaf = true;
}

// Iterative function to search a key in Trie. It returns true
// if the key is found in the Trie, else it returns false
bool Trie::search(string key)
{
	// return false if Trie is empty
	if (this == nullptr)
		return false;

	Trie* curr = this;
	for (unsigned int i=0; i<key.length(); ++i)
	{
		// go to next node
		curr = curr->character[key[i]];

		// if string is invalid (reached end of path in Trie)
		if (curr == nullptr)
			return false;
	}

	// if current node is a leaf and we have reached the
	// end of the string, return true
	return curr->isLeaf;
}

// returns true if given node has any children
bool Trie::haveChildren(const Trie* curr)
{
	for (unsigned int i=0; i<ALPHABET_SIZE; ++i)
		if (curr->character[i])
			return true;					// child found
	return false;
}

// Recursive function to delete a key in the Trie
bool Trie::deletion(Trie*& trie, string key)
{
	// return if Trie is empty
	if (trie == nullptr)
		return false;

	// if we have not reached the end of the key
	if (key.length())
	{
		// recurse for the node corresponding to next character in the key
		// and if it returns true, delete current node (if it is non-leaf)
		if (trie && 
			trie->character[key[0]] &&
			deletion(trie->character[key[0]], key.substr(1)) &&
			trie->isLeaf == false)
		{
			if (!haveChildren(trie))
			{
				delete trie;
				trie = nullptr;
				return true;
			}
			else 
			{
				return false;
			}
		}
	}

	// if we have reached the end of the key
	if (key.length() == 0 && trie->isLeaf)
	{
		// if current node is a leaf node and don't have any children
		if (!haveChildren(trie))
		{
			// delete current node
			delete trie;
			trie = nullptr;

			// delete non-leaf parent nodes
			return true;
		}
		// if current node is a leaf node and have children
		else
		{
			// mark current node as non-leaf node (DON'T DELETE IT)
			trie->isLeaf = false;

			// don't delete its parent nodes
			return false;
		}
	}
	return false;
}

/* 
Given a list of strings words representing an English Dictionary, find the longest word 
in words that can be built one character at a time by other words in words.If there is more 
than one possible answer, return the longest word with the smallest lexicographical order.
*/

string longestWord(vector<string>& words)
{
	string res = "";
	int mxLen = 0;
	unordered_set<string> s(words.begin(), words.end());
	queue<string> q;
	for (string word : words)
		if (word.size() == 1) q.push(word);

	while (!q.empty())
	{
		string t = q.front();
		q.pop();
		if (t.size() > mxLen)
		{
			mxLen = t.size();
			res = t;
		}
		else if (t.size() == mxLen)
		{
			res = min(res, t);
		}

		for (char c = 'a'; c <= 'z'; ++c)
		{
			t.push_back(c);
			if (s.find(t) != s.end()) 
				q.push(t);
			t.pop_back();
		}
	}
	return res;
}


/*
Given a non - empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest.If two words have the same frequency, 
then the word with the lower alphabetical order comes first.
*/

typedef function<bool(pair<string, int>, pair<string, int>)> Comparator;
Comparator compFunctor = [](pair<string, int> elem1, pair<string, int> elem2)
{
	if (elem1.second > elem2.second)
		return true;
	else if (elem1.second == elem2.second && elem1.first < elem2.first)
		return true;
	else
		return false;
};

vector<string> topKFrequent(vector<string>& words, int k)
{
	vector<string> v;
	map<string, int> map;
	for (auto word : words)
	{
		if (map.find(word) == map.end())
			map.insert(pair<string, int>(word, 1));
		else
			map[word]++;
	}
	set<pair<string, int>, Comparator> set(map.begin(), map.end(), compFunctor);                 
	for (auto elem : set)
		v.push_back(elem.first);
	vector<string>::const_iterator first = v.begin();
	vector<string>::const_iterator last = v.begin() + k;
	vector<string> res(first, last);

	return res;
}

