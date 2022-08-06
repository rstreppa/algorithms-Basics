# -*- coding: utf-8 -*-
""" 
@date:          Fri Jan 21 20:40:11 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          lib
@description:   miscellaneous arrays problems
"""
from functools import reduce
import bisect


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
        if new_intervals[i-1][1] > new_intervals[i][0]: # end of previous overlaps with stgrt of current 
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


def removeDuplicates(nums):
    """
    26. Remove Duplicates from Sorted Array
    Easy
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
    The relative order of the elements should be kept the same.
    Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
    More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
    It does not matter what you leave beyond the first k elements.
    Return k after placing the final result in the first k slots of nums.
    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.   
    
    :type nums: List[int]
    :rtype: int
    """
    n   = len(nums)
    if n == 0:
        return nums
    i   = 1
    while i < n:
        if nums[i] == nums[i-1]:
            nums.pop(i)
            n   -= 1
        else:
            i   += 1
    return n




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
    ''' 
        48. Rotate Image
        Medium
        You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
        You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
        DO NOT allocate another 2D matrix and do the rotation.
        here give a common method to solve the image rotation problems.
        clockwise rotate: first reverse up to down, then swap the symmetry
        anticlockwise rotate: first reverse left to right, then swap the symmetry
    '''
    n       = len(matrix)

    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for r in range(n):
        matrix[r].reverse()
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


def longestArithSeqLength(A):
    """
        1027. Longest Arithmetic Subsequence
        Medium
        Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
        Recall that a subsequence of an array nums is a list nums[i1], nums[i2], ..., nums[ik] with 0 <= i1 < i2 < ... < ik <= nums.length - 1, 
        and that a sequence seq is arithmetic if seq[i+1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
        
        Dynamic programming solution 
        
        https://www.youtube.com/watch?v=-NIlLdVKBFs
        
        :type nums: List[int]
        :rtype: int
    """
    
    n       = len(A)
    if 0 == n:
        return 0
    res     = 0
    dp      = [ {} for i in range(n) ]
    for i in range(n):
        for j in range(0,i):
            diff            = A[i]-A[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + 1
            else:
                dp[i][diff] = 2
            res             =max( res, dp[i][diff] )
    return res


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
    
    # def bin2num(arr):
    #     result = 0
    #     while(arr):
    #         result += 2*arr.pop()
    #     return result
    
    # def bin2num(arr):
    #     mult   = 1
    #     result = arr.pop()
    #     while(arr):
    #         mult   *= 2
    #         result += mult*arr.pop()
    #     return result

    def bin2num(arr):
        res = 0
        while arr:
            res = 2*res + arr.pop()
        return res
     
    
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

def maxScoreIndices(nums):

    """

    :type nums: List[int]

    :rtype: List[int]

 

    2155. All Divisions With the Highest Score of a Binary Array

    Medium

    You are given a 0-indexed binary array nums of length n. nums can be divided at index i (where 0 <= i <= n) into two arrays (possibly empty)

    numsleft and numsright:

 

    numsleft has all the elements of nums between index 0 and i - 1 (inclusive), while numsright has all the elements of nums

    between index i and n - 1 (inclusive).

    If i == 0, numsleft is empty, while numsright has all the elements of nums.

    If i == n, numsleft has all the elements of nums, while numsright is empty.

    The division score of an index i is the sum of the number of 0's in numsleft and the number of 1's in numsright.

 

    Return all distinct indices that have the highest possible division score. You may return the answer in any order.

 

    O(3N)

    """

    left = 0

    right = nums.count(1)

    value = [left + right]

    for i in nums:

        if i == 0:

            left += 1

        else:

            right -= 1

        value.append(left + right)

    max_val = max(value)

    return [i for i,v in enumerate(value) if v == max_val]           

def numOfSubarrays( arr, k, threshold ):
    ''' 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
        Medium
        Given an array of integers arr and two integers k and threshold, 
        return the number of sub-arrays of size k and average greater than or equal to threshold.
    
        Sliding window, make sure you don't exceed time limit
    '''
    ans = 0
    
    i, j, subarrsum = 0, 0, 0 
    
    while j < len(arr):
        subarrsum += arr[j]
        
        if j-i+1<k:
            j += 1
        else:
            if subarrsum >= k*threshold:
                ans += 1
                                
            subarrsum -= arr[i]
            j += 1
            i += 1
    return ans
   
def numTimesAllBlue(flips):
    ''' 1375. Number of Times Binary String Is Prefix-Aligned
        Medium
        Share
        You have a 1-indexed binary string of length n where all the bits are 0 initially. 
        We will flip all the bits of this binary string (i.e., change them from 0 to 1) one by one. 
        You are given a 1-indexed integer array flips where flips[i] indicates that the bit at index i will be flipped in the ith step.      
        A binary string is prefix-aligned if, after the ith step, all the bits in the inclusive range [1, i] 
        are ones and all the other bits are zeros.        
        Return the number of times the binary string is prefix-aligned during the flipping process.
        
        Bascially deep meaning is that column b is reaarange of column A.
        Reading all it means when to reach step x we need to flip all the <=x numbers.
    '''    
    count = 0
    maxi = 0
    for i,v in enumerate(flips):
        maxi = max(v,maxi)          
        if maxi == i+1:
            count += 1
        
    return count

def maxSumTwoNoOverlap(nums, firstLen, secondLen):
    ''' 1031. Maximum Sum of Two Non-Overlapping Subarrays
        Medium
        Given an integer array nums and two integers firstLen and secondLen, 
        return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.       
        The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.       
        A subarray is a contiguous part of an array.
    ''' 
    res1 = 0 
    n    = len(nums)
    for i in range(n-firstLen-secondLen):
        for j in range(i+firstLen, n-secondLen):
            res1 = max( res1, sum(nums[i:i+firstLen])+sum(nums[j:j+secondLen]) )
    res2 = 0 
    for i in range(n-firstLen-secondLen):
       for j in range(i+secondLen, n-firstLen):
           res2 = max( res2, sum(nums[i:i+secondLen])+sum(nums[j:j+firstLen]) )

    return max(res1, res2) 

def maxSumTwoNoOverlap2(nums, firstLen, secondLen):
    '''  O(N) dynamic programming solution '''
    dp = [0] * (len(nums) + 1)
    res1, res2, res = -1, -1, -1

    for i in range(1, len(dp)):
        dp[i] = dp[i - 1] + nums[i - 1]

        if i >= firstLen + secondLen:
            res1 = max(res1, dp[i - secondLen] - dp[i - secondLen - firstLen])
            res2 = max(res2, dp[i - firstLen] - dp[i - firstLen - secondLen])

            first_second = res1 + dp[i] - dp[i - secondLen]
            second_first = res2 + dp[i] - dp[i - firstLen]
            res = max(res, first_second, second_first)

    return res    
       
def maxSatisfied(customers, grumpy, minutes):
    ''' 1052. Grumpy Bookstore Owner
        Medium
        There is a bookstore owner that has a store open for n minutes. 
        Every minute, some number of customers enter the store. You are given an integer array customers of length n 
        where customers[i] is the number of the customer that enters the store at the start of the ith minute 
        and all those customers leave after the end of that minute.      
        On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 
        if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.       
        When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.       
        The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.       
        Return the maximum number of customers that can be satisfied throughout the day.
        
         Idea:
        Without secret technique sum:
        = totalSatisfied - totalGrumpy
        
        With secret technique sum:
        = totalSatisfied - totalGrumpy + maxSaved
        
        maxSaved = the max sum of k minute sliding window       
    '''
    totalSatisfied, totalGrumpy = 0, 0
    windowStart, maxSaved, currSaved = 0, 0, 0

    for windowEnd in range(len(customers)):
        totalSatisfied += customers[windowEnd]
        totalGrumpy += customers[windowEnd] * grumpy[windowEnd]
        currSaved += customers[windowEnd] * grumpy[windowEnd]
        if windowEnd - windowStart + 1 > minutes:
            currSaved -= customers[windowStart] * grumpy[windowStart]
            windowStart += 1
        maxSaved = max(maxSaved, currSaved)

    return totalSatisfied - totalGrumpy + maxSaved 

def sampleStats(count):
    ''' 1093. Statistics from a Large Sample
        Medium
        You are given a large sample of integers in the range [0, 255]. Since the sample is so large, 
        it is represented by an array count where count[k] is the number of times that k appears in the sample.
        
        Calculate the following statistics:
        
        minimum: The minimum element in the sample.
        maximum: The maximum element in the sample.
        mean: The average of the sample, calculated as the total sum of all elements divided by the total number of elements.
        median:
        If the sample has an odd number of elements, then the median is the middle element once the sample is sorted.
        If the sample has an even number of elements, then the median is the average of the two middle elements once the sample is sorted.
        mode: The number that appears the most in the sample. It is guaranteed to be unique.
        Return the statistics of the sample as an array of floating-point numbers [minimum, maximum, mean, median, mode]. 
        Answers within 10-5 of the actual answer will be accepted.
    '''
    mn,mx,mode,max_freq,sm,total=float('+inf'),float('-inf'),0,0,0,0
    arr=[]
    for i,el in enumerate(count):
        if el>0: 
            mn=min(mn,i)
            mx=max(mx,i)
        if el>max_freq:
            mode=i
            max_freq=el
        sm+=el*i
        total+=el
        arr.append(total)
    median1=bisect.bisect(arr,(total-1)//2)
    median2=bisect.bisect(arr,total//2)
    return [mn,mx,sm/total,(median1+median2)/2,mode]  

def twoSumLessThanK( A, K):
    ''' 1099. Two Sum Less Than K 
        Given an array A of integers and integer K, return the maximum S such that 
        there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

        Approach 1: Two Point
    '''
    res = -1
    A   = sorted(A)
    i   = 0 
    j   = len(A)-1
    while(i<j):
        if A[i]+A[j] >= K:
            j -= 1
        else:
            res = A[i]+A[j]
            i += 1
    return res
        
    
def numSteps(s):
    ''' 1404. Number of Steps to Reduce a Number in Binary Representation to One
        Medium
        Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
        
        If the current number is even, you have to divide it by 2.
        
        If the current number is odd, you have to add 1 to it.
        
        It is guaranteed that you can always reach one for all test cases.
    '''
    #s = s[::-1]
    n = 0 
    for c in s:
        n = 2*n+int(c)
        
    res = 0 
    while n > 1:
        if  n%2 == 0:
            n /= 2 
        else:
             n += 1
        res += 1 
    return res

def getWays(n, c):
    ''' Given an amount and the denominations of coins available, determine how many ways change can be made for amount. 
        There is a limitless supply of each coin type.
    '''
    def dfs( total, coins , coin_num, lookup ):        

        if total == 0:
            return 1
        elif total < 0:
            return 0
        elif coin_num <= 0:
            return 0
        
        key = (total, coin_num)
        
        if key not in lookup:
            lookup[key] = dfs( total, coins, coin_num-1, lookup ) + dfs( total-coins[coin_num-1], coins, coin_num, lookup )
            
        return lookup[key]

    lookup = {}
    coin_num = len(c)
    lookup = {}
    return dfs( n, c, coin_num, lookup )


def longestArithSeqLength(nums):
    ''' 1027. Longest Arithmetic Subsequence
        Medium
        Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
        
        Recall that a subsequence of an array nums is a list nums[i1], nums[i2], ..., nums[ik] 
        with 0 <= i1 < i2 < ... < ik <= nums.length - 1, and that a sequence seq is arithmetic 
        if seq[i+1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
    '''
    n = len(nums)
    max_len = 1
    dp = [ [ 1 for i in range(1002) ] for j in range(n+1) ]
    for i in range(n):
        for j in range(i+1, n):
            dif = nums[j] - nums[i] + 500
            dp[j][dif] = dp[i][dif] +1
            max_len = max( max_len, dp[j][dif] )
    return max_len



def lengthOfLIS(nums):
    ''' 300. Longest Increasing Subsequence
        Medium
        Given an integer array nums, return the length of the longest strictly increasing subsequence.        
        A subsequence is a sequence that can be derived from an array by deleting some or no elements 
        without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
        Time O(n^2) / Memory O(n)
    '''
    dp=[1]*len(nums)
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[j]<nums[i]: dp[i]=max(dp[i],1+dp[j])
    return max(dp)
   
def lengthOfLIS2(nums):
    ''' Time O(nlog n) / Memory O(n) '''
    ans=[]
    for i in range(len(nums)):
        if not ans or nums[i]>ans[-1]: 
            ans.append(nums[i])
        else: 
            idx = bisect.bisect_left(ans,nums[i]) 
            ans[idx] = nums[i]
    return len(ans)    
    
def numberOfArithmeticSlices(nums):
    ''' 413. Arithmetic Slices
        Medium
        An integer array is called arithmetic if it consists of at least three elements and 
        if the difference between any two consecutive elements is the same.
        
        For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
        Given an integer array nums, return the number of arithmetic subarrays of nums.
        
        A subarray is a contiguous subsequence of the array.
    '''    
    diff_arr = [0]*(len(nums)-1)
    
    for i in range(1,len(nums)):
        diff_arr[i-1] = nums[i]-nums[i-1]
        
        
    ans = 0
    count_sum = 1
    
    for i in range(1,len(diff_arr)):
        
        if diff_arr[i] == diff_arr[i-1]:
            ans += count_sum
            count_sum += 1
        else:
            count_sum = 1
            
    return ans   

def nextPermutation(self, nums):
    """
        31. Next Permutation
        Medium
        A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

        For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
        The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
        More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
        then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, 
        the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

        For example, the next permutation of arr = [1,2,3] is [1,3,2].
        Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
        While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
        Given an array of integers nums, find the next permutation of nums.

        The replacement must be in place and use only constant extra memory.
        nums = [4,5,3,2,1]
        Step 1: scan from right to left and stop at 4 because it less than 5. Here, index = 0
        Step 2: Again scan from right to left and stop at 5 because it is greater than 4. Here, j = 1
        Step 3: Swap the elements at index and j. The array will become [5,4,3,2,1].
        Step 4: Reverse the array after index. The array will become [5,1,2,3,4]
        
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
    """    
    def reverse(nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


    # Length of the array
    n = len(nums)
    # Index of the first element that is smaller than
    # the element to its right.
    index = -1
    # Loop from right to left
    for i in range(n - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            index = i - 1
            break
    # Base condition
    if index == -1:
        reverse(nums, 0, n - 1)
        return
    j = n - 1
    # Again swap from right to left to find first element
    # that is greater than the above find element
    for i in range(n - 1, index, -1):
        if nums[i] > nums[index]:
            j = i
            break
    # Swap the elements
    nums[index], nums[j] = nums[j], nums[index]
    # Reverse the elements from index + 1 to the nums.length
    reverse(nums, index + 1, n - 1)

def merge(nums1, m, nums2, n):
    """
        88. Merge Sorted Array
        Easy
        You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
        and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

        Merge nums1 and nums2 into a single array sorted in non-decreasing order.

        The final sorted array should not be returned by the function, but instead be stored 
        inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m
        elements denote the elements that should be merged, and the last n elements are set to 0 
        and should be ignored. nums2 has a length of n.        
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    while m > 0 and n > 0:
		if nums1[m - 1] >= nums2[n - 1]:
			nums1[m + n - 1] = nums1[m - 1]
			m -= 1
		else:
			nums1[m + n - 1] = nums2[n - 1]
			n -= 1

    for i in range(0, n):
		nums1[i] = nums2[i]

    return nums1

def islandPerimeter(grid):
    """
    463. Island Perimeter
    Easy
    You are given row x col grid representing a map where grid[i][j] = 1 represents land 
    and grid[i][j] = 0 represents water.

    Grid cells are connected horizontally/vertically (not diagonally). 
    The grid is completely surrounded by water, and there is exactly one island 
    (i.e., one or more connected land cells).

    The island doesn't have "lakes", meaning the water inside isn't connected to the water 
    around the island. One cell is a square with side length 1. The grid is rectangular, 
    width and height don't exceed 100. Determine the perimeter of the island.
        
    We can improve that to just checking two neighbors. As we right and down in the grid 
    to traverse it, we can only keep a check of left and up cells to a land cell. 
    We can assume that every land cell contributes ‘4’ to the perimeter of the island. 
    But if a land cell shares its side(s) with any other cell, we will subtract 2 from it
    (one for its shared side and one as the other cell shares a side too). 
    The time complexity of both the solutions is the same but we somewhat improve on grounds
    of operation in this approach.
        
    :type grid: List[List[int]]
    :rtype: int
    """
    res     = 0
    n       = len(grid)
    m       = len(grid[0])
        
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                res     += 4
                if i > 0 and grid[i-1][j] == 1:
                    res -= 2
                if j > 0 and grid[i][j-1] == 1:
                    res -= 2
                    
    return res

def findMaxConsecutiveOnes(nums):
    """
        485. Max Consecutive Ones
        Easy
        Given a binary array nums, return the maximum number of consecutive 1's in the array.

        Easy but not too much, look carefully at it and absorb the pattern - avoid double loop liek the plague - 
            
        :type nums: List[int]
        :rtype: int
    """
        
    count_global    = 0
    count_cur       = 0
    for i in nums:
        if i == 1:
            count_cur += 1
        else:
            if count_cur > count_global:
                count_global = count_cur
            count_cur = 0
    return max(count_global, count_cur)

    def nextGreaterElement(self, nums1, nums2):
        """
            496. Next Greater Element I
            Easy
            The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
            You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
            For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
            If there is no next greater element, then the answer for this query is -1.
            Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
            
            Monotonic stack solution in O(n+m)
            
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
        """
        res     = []
        s       = []
        d       = {}
        
        for elem in nums2:
            #put in table the pair <value, next greater> until stack empty or elem < stack.peek()
            while s and elem > s[-1]:
                d[s.pop()] = elem
            #push in stack
            s.append(elem)
        
        #put in table the pairs of remaining element in stack
        while s:
            d[s.pop()] = -1
        
        #populate answer list with result in table
        for elem in nums1:
            if elem in d:
                res.append(d[elem])
        
        return res

    def nextGreaterElement(self, nums1, nums2):
        """
            496. Next Greater Element I
            Easy
            The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
            You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
            For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
            If there is no next greater element, then the answer for this query is -1.
            Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
            
            Naive solution in O(n*m)
            
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
        """
        res         = [-1] * len(nums1)
        nums1Idx    = { n: i for i, n in enumerate(nums1) }
        d       = {}
   
        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx         = nums1Idx[nums2[i]]
                    res[idx]    = nums2[j]
                    break
               
        return res
