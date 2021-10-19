"""

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

"""

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        
        str1 = ''.join(word1)
        str2 = ''.join(word2)
        
        if str1 == str2:
            return True
        else:
            return False
