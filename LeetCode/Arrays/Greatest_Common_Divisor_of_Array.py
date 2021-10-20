"""
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
"""

class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        x = max(nums)
        y = min(nums)
        
        while(y):
            x, y = y, x % y
  
        return x
