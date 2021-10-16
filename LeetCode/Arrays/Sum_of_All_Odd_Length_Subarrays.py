"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.
"""

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        sum = 0
        l = len(arr)
        
        for i in range(l):
     
            # Add to the sum for each contribution of the arr[i]
            sum += ((((i + 1) * (l - i) + 1) // 2) * arr[i])
     
        # Return the final sum
        return sum
