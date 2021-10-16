"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

"""

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        
        for i in range(len(nums)):
            add = 0
            for j in range(len(nums)):
                if nums[j] < nums[i] and j!=i:
                    add += 1
            res.append(add)
            
        return res
