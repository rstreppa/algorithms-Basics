# -*- coding: utf-8 -*-
""" 
@date:          Sun Jan 30 13:00:45 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Data_Structures/Trie/trie.py
"""

from  trie import TrieNode, insert, search, indexPairs, indexPairs2

def main():
    print('#### insert search #########################')
    keys = ["the","a","there","anaswe","any",
            "by","their"]
    output = ["Not present in trie",
              "Present in trie"]
    # Trie object
    t = TrieNode()
   
    # Construct trie
    for key in keys:
        insert(t, key)

    print("{} ---- {}".format("the",output[search(t, "the")]))
    print("{} ---- {}".format("these",output[search(t, "these")]))
    print("{} ---- {}".format("their",output[search(t, "their")]))
    print("{} ---- {}".format("thaw",output[search(t, "thaw")]))
    print('#### indexPairs #########################')
    print(indexPairs("ababa", ["aba","ab"]))
    
    t = TrieNode()
    for word in ["aba","ab"]:
        insert(t, word)
    print(indexPairs2("ababa", ["aba","ab"]))