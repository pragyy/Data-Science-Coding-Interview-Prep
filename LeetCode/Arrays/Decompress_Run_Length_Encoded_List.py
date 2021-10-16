"""
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.

"""

class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(nums),2):
            freq = nums[i]
            val = nums[i+1]
            
            # appending the vals as per its frequency
            temp = []
            for j in range(freq):
                temp.append(val)
            
            # appending to the final list
            res.extend(temp)
            
        return res
