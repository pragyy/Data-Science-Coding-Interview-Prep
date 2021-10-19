"""
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
"""

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        sum = 0
        for items in words:
            for x in items:
                if x not in allowed:
                    break
            else:    
                sum += 1
                
        return sum
