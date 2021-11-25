"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        new_strs = [''.join(sorted(word)) for word in strs]
        
        hashmap = {key:[] for key in new_strs}
        for idx in range(len(new_strs)):
            if new_strs[idx] in hashmap:
                hashmap[str(new_strs[idx])].append(strs[idx])
        return(hashmap.values())
      
"""
Time Complexity - O(3n)
Space Complexity - O(n)
