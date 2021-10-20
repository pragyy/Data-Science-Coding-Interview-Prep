"""
Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.
"""

class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        n = len(arr)
        
        sum = 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    diff1 = abs(arr[i]-arr[j])
                    diff2 = abs(arr[j]-arr[k])
                    diff3 = abs(arr[i]-arr[k])
                    
                    if diff1<= a and diff2<=b and diff3<=c:
                        sum += 1
            else:
                continue
                
        return sum
