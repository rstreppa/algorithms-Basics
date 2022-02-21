# -*- coding: utf-8 -*-
""" 
@date:          Fri Jan 21 20:40:11 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   miscellaneous arrays problems
"""
from functools import reduce

def containsDuplicate(nums):
    ''' Given an integer array nums, return true if any value appears at least twice in the array, 
        and return false if every element is distinct.     
    '''
    numsSet = set(nums)
    if len(numsSet) < len(nums):
        return True
    else:
        return False
    
def missingNumber(nums):
    ''' Given an array nums containing n distinct numbers in the range [0, n], 
        return the only number in the range that is missing from the array. 
    '''
    return sum(range(len(nums)+1)) - sum(nums)
        
def findDisappearedNumbers(nums):
    ''' Given an array nums of n integers where nums[i] is in the range [1, n], 
        return an array of all the integers in the range [1, n] that do not appear in nums.
    '''
    return list( set(range(1, len(nums)+1)).difference(set(nums)) )

def singleNumber(nums):
    ''' Given a non-empty array of integers nums, every element appears twice except for one. 
        Find that single one.
        You must implement a solution with a linear runtime complexity and use only constant extra space.
    '''
    d = dict()
    for i in nums:
        d[i] = d.get(i, 0) + 1
    for k, v in d.items():
        if v == 1:
            return k
        
    return -1
    
 
def singleNumber2(nums):
    ''' https://hackernoon.com/xor-the-magical-bit-wise-operator-24d3012ed821
        Solution using XOR
        
        Bitwise XOR ( ^ ) like the other operators (except ~) 
        also take two equal-length bit patterns. 
        If both bits in the compared position of the bit patterns are 0 or 1, 
        the bit in the resulting bit pattern is 0, otherwise 1.
    '''
    res = 0
    for num in nums:
        res ^= num
    return res

def canAttendMeetings( intervals ):
    ''' Given an array of meeting time intervals consisting of start and end times [s1, e1], [s2, e2], ... , 
        determine if a person could attend all meetings.
        For example,
        Given [ [0, 30], [5, 10], [15, 20] ],
        return false.
        If a person can attend all meetings, there must not be any overlaps between any meetings. 
        After sorting the intervals, we can compare the current end and next start.    
    '''
    new_intervals = sorted( intervals, key=lambda x: x[0] )
    for i in range(1,len(new_intervals)):
        if new_intervals[i-1][1] > new_intervals[i][0]: # end of previous overlaps with stgart of current 
            return False
    return True            
        
def search(nums, target):
    ''' Given an array of integers nums which is sorted in ascending order, and an integer target, 
        write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
        You must write an algorithm with O(log n) runtime complexity.
    '''    
    n       = len(nums)
    low     = 0
    high    = n-1
    while low < high:
        mid = low + (high-low)//2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid-1
        else:
            low = mid+1         
    return -1

def nextGreatestLetter(letters, target):
    ''' Given a characters array letters that is sorted in non-decreasing order 
        and a character target, return the smallest character in the array that is larger than target.
        Note that the letters wrap around.
    '''
    n = len(letters)
    if n == 0:
        return None
    
    low = 0
    high = n - 1
    # If it can not be found, must be the first element (wrap around)
    result = 0 
    
    while low <= high:
        mid = low + (high-low) // 2
        if letters[mid] > target:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return letters[result]

def peakIndexInMountainArray(arr):
    ''' Let's call an array arr a mountain if the following properties hold:
        arr.length >= 3
        There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... arr[i-1] < arr[i]
        arr[i] > arr[i+1] > ... > arr[arr.length - 1]
        Given an integer array arr that is guaranteed to be a mountain, 
        return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
    '''
    n       = len(arr)
    low     = 0
    high    = n - 1
    while low < high:
        mid = low + (high-low)//2
        if (arr[mid] > arr[mid-1]) and (arr[mid] > arr[mid+1]):
            return mid
        elif arr[mid] > arr[mid-1]:
            low = mid + 1
        elif arr[mid] < arr[mid-1]:
            high = mid - 1
        elif arr[mid] > arr[mid+1]:
            high = mid + 1
        else:
            low = mid - 1
    
def peakIndexInMountainArray2(arr):
    ''' easier solution: In each iteration, we check the mid: if it's smaller than the next element, 
        it's on the left side of the mountain and we have to continue searching in the right side of mid. 
        So low = mid+1. Otherwise, high = mid-1. 
    '''
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < arr[mid+1]:
            low = mid+1
        else:
            high = mid-1
    return low

def construct2DArray(original, m, n):
    ''' You are given a 0-indexed 1-dimensional (1D) integer array original, 
        and two integers, m and n. 
        You are tasked with creating a 2-dimensional (2D) array with m rows and n columns 
        using all the elements from original.
        The elements from indices 0 to n - 1 (inclusive) of original should form the first row 
        of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) 
        should form the second row of the constructed 2D array, and so on.
        Return an m x n 2D array constructed according to the above procedure, 
        or an empty 2D array if it is impossible.
    '''
    N       = len(original)
    if N != m*n:
        return []
    
    res     = []
    row     = 0
    for i in range(n):
        res.append( original[ row: row+m ] )
        row += m
        
    return res

def productExceptSelf(nums):
    ''' Given an integer array nums, return an array answer such that answer[i] 
        is equal to the product of all the elements of nums except nums[i].
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
        You must write an algorithm that runs in O(n) time and without using the division operation. 
    '''      
    res = []
    for i in range(len(nums)):
        product = reduce( lambda x, y: x*y, nums[:i] + nums[i+1:], 1 )
        res.append(product)
    return res

def productExceptSelf2(nums):
    ''' O(n) solution '''
    # Left is an array containing the left products i.e: left[i] = nums[0] * .... * nums[i-1]  * nums[i]
    # Right is an array containing the array products i.e: right[i] = nums[i] * nums[i+1]  * .... * nums[len(nums)]
    left    = [1] * len(nums)
    right   = [1] * len(nums)
    res     = [1] * len(nums)
    
    for i in range(1, len(nums)):
        left[i]     = left[i-1] * nums[i-1]
        
    for i in range( len(nums) -2, -1, -1 ):
        right[i]    = right[i+1] * nums[i+1]
        
    for i in range(len(nums)):
        res[i]      = left[i] * right[i]
        
    return res

def findDuplicate(nums):
    ''' Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
        There is only one repeated number in nums, return this repeated number.
        You must solve the problem without modifying the array nums and uses only constant extra space.
    '''
    d = dict()
    for i in nums:
        d[i] = d.get(i, 0) + 1
    for k, v in d.items():
        if v == 2:
            return k
        
    return -1

def findDuplicate2(nums):
    ''' If there is no duplicate in the array, we can map each indexes to each numbers in this array. 
        In other words, we can have a mapping function f(index) = number
        For example, let's assume nums = [2,1,3], then the mapping function is 0->2, 1->1, 2->3.
        If we start from index = 0, we can get a value according to this mapping function, 
        and then we use this value as a new index and, again, we can get the other new value according to this new index. 
        We repeat this process until the index exceeds the array. 
        Actually, by doing so, we can get a sequence. Using the above example again, the sequence we get is 0->2->3. 
        (Because index=3 exceeds the array's size, the sequence terminates!)
         However, if there is duplicate in the array, the mapping function is many-to-one.
         For example, let's assumenums = [2,1,3,1], then the mapping function is 0->2, {1,3}->1, 2->3. 
         Then the sequence we get definitely has a cycle. 0->2->3->1->1->1->1->1->........ 
         The starting point of this cycle is the duplicate number.

        According to Floyd's algorithm, first step, if a cycle does exist, and you advance the tortoise one node each unit of time 
        but the hare two nodes each unit of time, then they will eventually meet. 
        This is what the first while loop does. The first while loop finds their meeting point.
        Second step, take tortoise or hare to the start point of the list (i.e. let one of the animal be 0) 
        and keep the other one staying at the meeting point. Now, advance both of the animals one node each unit of time, 
        the meeting point is the starting point of the cycle. This is what the second while loop does. The second while loop finds their meeting point.
    '''
    if len(nums) > 1:
        slow     = nums[0] 
        fast      = nums[nums[0]]
        while slow != fast: 
            slow = nums[slow] 
            fast = nums[nums[fast]]

        fast = 0;
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
            return slow
        return -1   
    
def findDuplicates(nums):
    ''' Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, 
        return an array of all the integers that appears twice.
        You must write an algorithm that runs in O(n) time and uses only constant extra space.
    '''
    res     = []
    d       = {}
    for elem in nums:
        d[elem]     = d.get(elem, 0) + 1
    for k, v in d.items():
        if v > 1:
            res.append(k)           
    return res

def findDuplicates2(nums):
    ''' when find a number i, flip the number at position i-1 to negative. 
        if the number at position i-1 is already negative, i is the number that occurs twice.
    '''
    res = []
    for x in nums:
        if nums[abs(x)-1] < 0:
            res.append(abs(x))
        else:
            nums[abs(x)-1] *= -1
    return res

def setZeroes(matrix):
    ''' Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
        You must do it in place. 
    '''
    rows        = len(matrix)
    columns     = len(matrix[0])
    zeros       = []
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 0:
                zeros.append([i,j])
    for zero in zeros:
        for i in range(rows):
            matrix[i][zero[1]] = 0
        for j in range(columns):
            matrix[zero[0]][j] = 0          
    
    return matrix
        
def spiralOrder(matrix):
    ''' Given an m x n matrix, return all elements of the matrix in spiral order.
        This is a very simple and easy to understand solution. I traverse right and increment rowBegin, 
        then traverse down and decrement colEnd, then I traverse left and decrement rowEnd, and finally I traverse up and increment colBegin.
        the conditions to check borders are all the same. len(res) < n * m
    '''
    res = []
    if len(matrix) == 0:
        return res
    row_begin = 0
    col_begin = 0
    row_end = len(matrix)-1 
    col_end = len(matrix[0])-1
    while (row_begin <= row_end and col_begin <= col_end):
        for i in range(col_begin,col_end+1):
            res.append(matrix[row_begin][i])
        row_begin += 1
        for i in range(row_begin,row_end+1):
            res.append(matrix[i][col_end])
        col_end -= 1
        if (row_begin <= row_end):
            for i in range(col_end,col_begin-1,-1):
                res.append(matrix[row_end][i])
            row_end -= 1
        if (col_begin <= col_end):
            for i in range(row_end,row_begin-1,-1):
                res.append(matrix[i][col_begin])
            col_begin += 1
    return res
       
def rotate(matrix):
    ''' You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
        You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
        DO NOT allocate another 2D matrix and do the rotation.
        here give a common method to solve the image rotation problems.
        clockwise rotate: first reverse up to down, then swap the symmetry
        anticlockwise rotate: first reverse left to right, then swap the symmetry
    '''
    n           = len(matrix)
    matrix      = matrix[::-1]
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

def numPairsDivisibleBy60(time):
    ''' You are given a list of songs where the ith song has a duration of time[i] seconds.
        Return the number of pairs of songs for which their total duration in seconds is divisible by 60. 
        Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
    '''
    count       = 0
    remainders  = [0] * 60
    for t in time:
        remainders[ t%60 ] += 1
    
    i           = 1
    j           = 59
    while i < j:
        count += remainders[i] * remainders[j]
        i += 1 
        j -= 1
    # for group 0 and group 30
    count +=(remainders[0]*(remainders[0]-1)//2)+(remainders[30]*(remainders[30]-1)//2)
    return count

def canThreePartsEqualSum(arr):
    ''' Given an array of integers arr, return true if we can partition the array 
        into three non-empty parts with equal sums.
        Formally, we can partition the array if we can find indexes i + 1 < j 
        with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] 
              == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])
    '''
    N       =len(arr)
    third   =sum(arr)//3
    if(third*3!=sum(arr)):
        return False
    running_sum     = 0
    parts           = 0
    for i in range(N):
        running_sum+=arr[i]
        if(running_sum==third):
            running_sum=0
            parts+=1
    if(parts==3):
        return True
    return False

    # i   = 1
    # j   = len(arr) - 2
    # while i < j:
    #     if sum(arr[:i+1]) == sum(arr[i+1:j]) and sum(arr[i+1:j]) == sum(arr[j:]):
    #         return True
    #     i += 1 
    #     j -= 1
    # return  False
    
def longestConsecutive(nums):
    ''' Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
        You must write an algorithm that runs in O(n) time.
    
        First turn the input into a set of numbers. That takes O(n) and then we can ask in O(1) whether we have a certain number.
        
        Then go through the numbers. If the number x is the start of a streak (i.e., x-1 is not in the set), 
        then test y = x+1, x+2, x+3, ... and stop at the first number y not in the set. 
        The length of the streak is then simply y-x and we update our global best with that. 
        Since we check each streak only once, this is overall O(n)
    '''
    nums = set(nums)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
    return best    

def maxScoreSightseeingPair(values):
    ''' You are given an integer array values where values[i] represents the value of the ith sightseeing spot. 
        wo sightseeing spots i and j have a distance j - i between them.
        The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: 
        the sum of the values of the sightseeing spots, minus the distance between them.
        Return the maximum score of a pair of sightseeing spots.
        
        Idea: Pick up the first element of array and start traversing the array. 
        Now we know that distance value will increase by 1 or alternatively the effective value of first element will decrease by 1. 
        So, keep on finding the max value till the moment the effective value of first element is lesser than current element. 
        Update the first element to current element and proceed with algorithm for the current element, ie, 
        reducing its effective value by 1 and finding max.
    '''
    n       = len(values)
    f       = values[0]
    res     = 0
    for i in range(1, n):
        f   -= 1
        res = max(res, f + values[i])
        if f < values[i]: 
            f = values[i]
    return res       
    
def heightChecker(heights):
    ''' A school is trying to take an annual photo of all the students. 
        The students are asked to stand in a single file line in non-decreasing order by height. 
        Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
        You are given an integer array heights representing the current order that the students are standing in. 
        Each heights[i] is the height of the ith student in line (0-indexed).
        Return the number of indices where heights[i] != expected[i].
    '''    
    expected    = sorted(heights)
    count       = 0
    for i, j in zip(expected, heights):
        if i != j:
            count += 1
    return count    
    
def sumOfDigits(A):
    ''' Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.
        Return 0 if S is odd, otherwise return 1 
    '''
    minimal = min(A)
    sumof   = 0
    while(minimal):
        sumof   += minimal % 10
        minimal = minimal // 10
    if sumof % 2 == 0:
        return 1
    else:
        return 0
        
def duplicateZeros(arr):
    ''' Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
        Note that elements beyond the length of the original array are not written. 
        Do the above modifications to the input array in place and do not return anything. 
    '''    
    left = 0
    while left < len(arr):
        if arr[left] == 0:
            arr.pop()
            arr.insert(left,0)
            left+=2
        else:
            left+=1   
    return arr

def prefixesDivBy5(nums):
    ''' You are given a binary array nums (0-indexed).
        We define xi as the number whose binary representation is the subarray nums[0..i] 
        (from most-significant-bit to least-significant-bit).
        For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
        Return an array of booleans answer where answer[i] is true if xi is divisible by 5.
    '''
    res     = []
    
    def bin2num(arr):
        result = 0
        while(arr):
            result += 2*arr.pop()
        return result
    
    for i in range(len(nums)):
       arr  = nums[:i+1] 
       x    = bin2num(arr)
       if x % 5 == 0:
           res.append( True )
       else:
           res.append( False )
    
    return res            
            
def allCellsDistOrder(rows, cols, rCenter, cCenter):
    ''' 1030. Matrix Cells in Distance Order
        You are given four integers row, cols, rCenter, and cCenter. 
        There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).
        Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) 
        from the smallest distance to the largest distance. 
        You may return the answer in any order that satisfies this condition.
        The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.
    '''
    result  = []
    for i in range(rows):
        for j in range(cols):
            result.append( ( abs(i-rCenter) + abs(j-cCenter), [i,j] ) )
    result = sorted( result, key = lambda x: x[0] )
    res = [ e[1] for e in result ]        
    return res

def diagonalSort(mat):
    ''' 1329. Sort the Matrix Diagonally
        A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row 
        or leftmost column and going in the bottom-right direction until reaching the matrix's end. 
        For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, 
        includes cells mat[2][0], mat[3][1], and mat[4][2].

        Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
    '''
    def pickDiagonals(row,col,mat,R,C):
        diagonal=[]
        while(row<R and col<C):
            diagonal.append(mat[row][col])
            row+=1
            col+=1
        return diagonal

    def arrangeDiagonal(row,col,diagonal,mat,R,C):
        while(row<R and col<C):
            mat[row][col]=diagonal.pop(0)
            row+=1
            col+=1

    R=len(mat)
    C=len(mat[0])

    for row in range(R-2,-1,-1):
        diagonal=pickDiagonals(row,0,mat,R,C)
        diagonal.sort()
        arrangeDiagonal(row,0,diagonal,mat,R,C)

    for col in range(1,C-1):
        diagonal=pickDiagonals(0,col,mat,R,C)
        diagonal.sort()
        arrangeDiagonal(0,col,diagonal,mat,R,C)

    return mat    
    