# -*- coding: utf-8 -*-
""" 
@date:          Tue Jan 11 21:56:07 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Data_Structures/Queue/queue.py
"""

from queue import Queue

def main():
    q = Queue(maxsize = 10)
    q.put( 1 )
    q.put( 2 )
    q.put( 3 )
    q.put( 4 )
    q.put( 5 )
    print(q.qsize())
    print('######################')
    print(q.get())
    print(q.get())
    print(q.get())    
    print("\nEmpty: ", q.empty()) 
    print(q)
    print('######################')