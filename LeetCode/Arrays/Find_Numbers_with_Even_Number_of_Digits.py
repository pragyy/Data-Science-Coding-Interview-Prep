"""
Given an array nums of integers, return how many of them contain an even number of digits.
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        res = 0
        
        for x in nums:
            dig = 0
            while x>0:
                dig += 1
                x = x//10     
            
            if dig % 2 == 0:
                res += 1
                
        return res
