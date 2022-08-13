# -*- coding: utf-8 -*-
""" 
@date:          Sun Jan 30 12:59:51 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   implementation and simple properties of trie data structure
"""

ALPHABET_SIZE = 26

 
class TrieNode:
    def __init__(self):
        self.children      = [None] * ALPHABET_SIZE 
        self.isEndOfWord   = False      # isEndOfWord is true if the node represents end of a word



def insert(root, key):
    ''' If not present, inserts key into trie 
        If the key is prefix of trie node, just marks leaf node 
    '''

    pCrawl = root
    for i in range(len(key)):
        index = ord(key[i]) - ord('a') 
        if not pCrawl.children[index]: 
            pCrawl.children[index] = TrieNode()
        pCrawl = pCrawl.children[index]

	# mark last node as leaf 
    pCrawl.isEndOfWord = True


 
def search(root, key):
    ''' Returns true if key presents in trie, else false '''
    pCrawl = root
    for i in range(len(key)):
        index = ord(key[i]) - ord('a')
        if not pCrawl.children[index]:
            return False
        pCrawl = pCrawl.children[index]
        
    return pCrawl and pCrawl.isEndOfWord

def indexPairs( text, words):
    ''' 
    	1065. Index Pairs of a String
	Easy
	Given a text string and a list of sdtrings words, return alll index pairs [i,j]
        so that substring text[i]...text[j] is in the list of words
    '''
    result = []
    for i in range(len(text)):
       for j in range(i+1,len(text)+1):
          if text[i:j] in words:
             result.append([i,j-1])
    return result

def indexPairs2( text, words):
    ''' 
    	1065. Index Pairs of a String
	Easy
    	Given a text string and a list of strings words, return alll index pairs [i,j]
        so that substring text[i]...text[j] is in the list of words
        Using TrieNode
    '''
    trie    = TrieNode()
    for word in words:
        insert(trie, word)	# O(KL) K number of words, L max length of a word
    
    solutions = []
    def trie_search(i):
        node    = trie
        j       = i
        while node and j < len(text) and ( ord(text[j]) - ord('a') ) in node.children:
            index   = ord(text[j]) - ord('a')
            node    = node.children[index]
            if node.isEndOfWord:
                solutions.append([i,j])
    
    for i in range(len(text)):
        trie_search(i)		# O(NL) N length text, L max length of a word
        
    return solutions
