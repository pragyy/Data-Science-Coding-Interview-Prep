"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x: x[0])
        
        res = []
        res.append(intervals[0])
        for interval in intervals:
            if interval[0] <= res[-1][1]:
                res[-1][1] = interval[1]
            else:
                res.append(interval)
            
        return(res)
      
   """
   Time complexity = O(n)
   Space Complexity = O(n)
   """
