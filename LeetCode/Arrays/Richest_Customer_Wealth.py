"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the jth bank. 
Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

"""

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        amount = []
        
        #iterating over the 2D array
        for rows in accounts:
            add = 0
            for col in rows:
                add += col
            amount.append(add) # appending the total amount for each customer
            
        return (max(amount)) # return the max amount
