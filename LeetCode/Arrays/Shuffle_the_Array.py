"""

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

"""

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        # size of half the array
        n = len(nums)/2
        
        new_nums = []
        for i in range(n):
            new_nums.append(nums[i])
            new_nums.append(nums[n+i])
            
        return new_nums
