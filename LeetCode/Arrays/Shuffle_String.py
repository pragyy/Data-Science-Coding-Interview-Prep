"""

Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

"""

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        #intializing an empty arrayy same as the size of s
        final_string = [0] * len(s)
        
        # looping and assigning value as per the value in indices
        for i in range(len(indices)):
            final_string[indices[i]] = s[i]
        
        # joining all list elements into string
        res = "".join(final_string)
        
        return res
