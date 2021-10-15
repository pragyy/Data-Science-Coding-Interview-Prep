"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = []
        
        # initializing the first element
        running_sum.append(nums[0])
        
        # looping to calculate running/cumulative sum
        for i in range(1,len(nums)):
            running_sum.append(nums[i]+running_sum[i-1]) 
            
        return running_sum
