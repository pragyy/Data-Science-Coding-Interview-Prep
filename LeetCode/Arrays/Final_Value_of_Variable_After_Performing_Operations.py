"""
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.
"""

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for ele in operations:
            if ele == "--X":
                x = x-1
            elif ele == "X--":
                x = x-1
            elif ele == "X++":
                x = x+1
            else:
                x = x+1
                
        return x
