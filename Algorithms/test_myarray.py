# -*- coding: utf-8 -*-
""" 
@date:          Fri Jan 21 20:41:07 2022
@author:        rstreppa ( roberto.strepparava@gmail.com )
@company:       https://github.com/rstreppa
@type:          test
@description:   test file for script C:/Users/rober/OneDrive/Documents/Library/Programming/Algorithms/myarray.py
"""

from myarray import containsDuplicate, missingNumber, findDisappearedNumbers 
from myarray import singleNumber, singleNumber2, canAttendMeetings, search
from myarray import nextGreatestLetter, peakIndexInMountainArray, peakIndexInMountainArray2
from myarray import construct2DArray, productExceptSelf,productExceptSelf2
from myarray import findDuplicate, findDuplicate2, findDuplicates, findDuplicates2
from myarray import setZeroes, spiralOrder, rotate
from myarray import numPairsDivisibleBy60, canThreePartsEqualSum
from myarray import longestConsecutive, maxScoreSightseeingPair, heightChecker
from myarray import sumOfDigits, duplicateZeros, prefixesDivBy5, allCellsDistOrder, diagonalSort, maxScoreIndices
from myarray import numOfSubarrays, numTimesAllBlue, maxSumTwoNoOverlap, maxSumTwoNoOverlap2
from myarray import maxSatisfied, sampleStats, twoSumLessThanK, numSteps, getWays
from myarray import longestArithSeqLength, lengthOfLIS, lengthOfLIS2, numberOfArithmeticSlices

def main():
    print('#### containsDuplicate #########################')
    nums = [1,2,3,4]
    print(containsDuplicate(nums))
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(containsDuplicate(nums))
    print('#### missingNumber #########################')
    nums = [3,0,1]
    print(missingNumber(nums))
    nums = [9,6,4,2,3,5,7,0,1]
    print(missingNumber(nums))
    print('#### findDisappearedNumbers #########################')
    nums = [4,3,2,7,8,2,3,1]
    print(findDisappearedNumbers(nums))
    nums = [1,1]
    print(findDisappearedNumbers(nums))
    print('#### singleNumber #########################')
    nums = [2,2,1]
    print(singleNumber(nums))
    nums = [4,1,2,1,2]
    print(singleNumber(nums))
    nums = [1]
    print(singleNumber(nums))
    print('#### singleNumber2 #########################')
    nums = [2,2,1]
    print(singleNumber2(nums))
    nums = [4,1,2,1,2]
    print(singleNumber2(nums))
    nums = [1]
    print(singleNumber2(nums))
    print('#### canAttendMeetings #########################')
    intervals = [ [0, 30], [5, 10], [15, 20] ]
    print(canAttendMeetings(intervals))
    intervals = [[7,10],[2,4]]
    print(canAttendMeetings(intervals))
    print('#### search #########################')
    nums = [-1,0,3,5,9,12]
    target = 9
    print(search(nums, target))
    nums = [-1,0,3,5,9,12]
    target = 2
    print(search(nums, target))
    print('#### nextGreatestLetter #########################')
    letters     = ["c","f","j"] 
    target      = "a"
    print(nextGreatestLetter(letters, target))
    letters     = ["c","f","j"]
    target      = "c"
    print(nextGreatestLetter(letters, target))
    letters     = ["c","f","j"]
    target      = "d"
    print(nextGreatestLetter(letters, target))
    print('#### peakIndexInMountainArray #########################')
    arr = [0,1,0]
    print(peakIndexInMountainArray(arr))
    arr = [0,2,1,0]
    print(peakIndexInMountainArray(arr))
    arr = [0,10,5,2]
    print(peakIndexInMountainArray(arr))
    print(peakIndexInMountainArray2([0,1,0]))
    print(peakIndexInMountainArray2([0,2,1,0]))
    print(peakIndexInMountainArray2([0,10,5,2]))
    print('#### construct2DArray #########################')
    print(construct2DArray([1,2,3,4], 2, 2))
    print(construct2DArray([1,2,3], 1, 3))
    print(construct2DArray([1,2], 1, 1))
    print('#### productExceptSelf #########################')
    print(productExceptSelf([1,2,3,4]))
    print(productExceptSelf([-1,1,0,-3,3]))
    print(productExceptSelf2([1,2,3,4]))
    print(productExceptSelf2([-1,1,0,-3,3]))
    print('#### findDuplicate #########################')
    print(findDuplicate([1,3,4,2,2]))
    print(findDuplicate([3,1,3,4,2]))
    print(findDuplicate2([1,3,4,2,2]))
    print(findDuplicate2([3,1,3,4,2]))
    print('#### findDuplicates findDuplicates2 #########################')
    print(findDuplicates([4,3,2,7,8,2,3,1]))
    print(findDuplicates([1,1,2]))
    print(findDuplicates([1]))
    print(findDuplicates2([4,3,2,7,8,2,3,1]))
    print(findDuplicates2([1,1,2]))
    print(findDuplicates2([1]))
    print('#### setZeroes #########################')
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print(setZeroes(matrix))
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print(setZeroes(matrix))
    print('#### spiralOrder #########################')
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(spiralOrder(matrix))
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(spiralOrder(matrix))
    print('#### rotate #########################')
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(rotate(matrix))
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    print(rotate(matrix))
    print('#### numPairsDivisibleBy60 #########################')
    print(numPairsDivisibleBy60([30,20,150,100,40]))
    print(numPairsDivisibleBy60([60,60,60]))
    print('#### canThreePartsEqualSum #########################')
    print(canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
    print(canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
    print(canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))
    print('#### longestConsecutive #########################')
    print(longestConsecutive([100,4,200,1,3,2]))
    print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print('#### maxScoreSightseeingPair #########################')
    print(maxScoreSightseeingPair([8,1,5,2,6]))
    print(maxScoreSightseeingPair([1,2]))
    print('#### heightChecker #########################')
    print(heightChecker([1,1,4,2,1,3]))
    print(heightChecker([5,1,2,3,4]))
    print('#### sumOfDigits #########################')
    print(sumOfDigits([34,23,1,24,75,33,54,8]))
    print(sumOfDigits([99,77,33,66,55]))
    print('#### duplicateZeros #########################')
    print(duplicateZeros([1,0,2,3,0,4,5,0]))
    print(duplicateZeros([1,2,3]))
    print('#### prefixesDivBy5 #########################')
    print(prefixesDivBy5([0,1,1]))
    print(prefixesDivBy5([1,1,1]))
    print('#### allCellsDistOrder #########################')
    print(allCellsDistOrder(1,2,0,0))
    print(allCellsDistOrder(2,2,0,1))
    print(allCellsDistOrder(2,3,1,2))
    print('#### diagonalSort #########################')
    print(diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
    print(diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]))
    print('#### maxScoreIndices #########################')
    print( maxScoreIndices([0,0,1,0]) )
    print( maxScoreIndices([0,0,0]) )
    print( maxScoreIndices([1,1]) )
    print('#### numOfSubarrays #########################')
    print( numOfSubarrays( [2,2,2,2,5,5,5,8], 3, 4 ) )
    print( numOfSubarrays( [11,13,17,23,29,31,7,5,2,3], 3, 5 ) )
    print('#### numTimesAllBlue #########################')
    print( numTimesAllBlue( [3,2,4,1,5] ) )
    print( numTimesAllBlue( [4,1,2,3] ) )
    print('#### maxSumTwoNoOverlap #########################')
    print( maxSumTwoNoOverlap( [0,6,5,2,2,5,1,9,4], 1, 2 ) )
    print( maxSumTwoNoOverlap( [3,8,1,3,2,1,8,9,0], 3, 2 ) )
    print( maxSumTwoNoOverlap( [2,1,5,6,0,9,5,0,3,8], 4, 3 ) )
    print( maxSumTwoNoOverlap2( [0,6,5,2,2,5,1,9,4], 1, 2 ) )
    print( maxSumTwoNoOverlap2( [3,8,1,3,2,1,8,9,0], 3, 2 ) )
    print( maxSumTwoNoOverlap2( [2,1,5,6,0,9,5,0,3,8], 4, 3 ) )
    print('#### maxSatisfied #########################')
    print( maxSatisfied( [1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3 ) )
    print( maxSatisfied( [1], [0], 1 ) )
    print('#### sampleStats #########################')
    print( sampleStats([0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
) )
    print(sampleStats([0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
))
    print('#### twoSumLessThanK #########################')
    print( twoSumLessThanK([34,23,1,24,75,33,54,8], 60) )
    print( twoSumLessThanK([10,20,30], 15) )
    print('#### numSteps #########################')
    print( numSteps( "1101" ) )
    print( numSteps( "10" ) )
    print( numSteps( "1" ) )
    print('#### getWays #########################')
    print( getWays( 4, [1, 2, 3] ) )
    print( getWays( 10, [2, 5, 3, 6 ] ) )
    print('#### longestArithSeqLength #########################')
    print( longestArithSeqLength([3,6,9,12]) )
    print( longestArithSeqLength([9,4,7,2,10]) )
    print( longestArithSeqLength([20,1,15,3,10,5,8]) )
    print('#### lengthOfLIS #########################')
    print( lengthOfLIS( [10,9,2,5,3,7,101,18] ) )
    print( lengthOfLIS( [0,1,0,3,2,3] ) )
    print( lengthOfLIS( [7,7,7,7,7,7,7] ) )
    print( lengthOfLIS2( [10,9,2,5,3,7,101,18] ) )
    print( lengthOfLIS2( [0,1,0,3,2,3] ) )
    print( lengthOfLIS2( [7,7,7,7,7,7,7] ) )
    print('#### numberOfArithmeticSlices #########################')
    print( numberOfArithmeticSlices([1,2,3,4]) )
    print( numberOfArithmeticSlices([1]) )