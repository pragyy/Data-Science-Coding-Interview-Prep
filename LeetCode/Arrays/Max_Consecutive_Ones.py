"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        ptr = 0
        count = 0
        
        for i in nums:
            if i == 1:
                ptr += 1
                
            else:
                if ptr > count:
                    count = ptr
                ptr = 0
                
        return max(count,ptr)
