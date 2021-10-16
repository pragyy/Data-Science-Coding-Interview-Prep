"""

You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.

"""

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        
        add = 0
        
        for x in items:
            if ruleKey == "type":
                if x[0] == ruleValue:
                    add += 1
            elif ruleKey == "color":
                if x[1] == ruleValue:
                    add += 1
            elif ruleKey == "name":
                if x[2] == ruleValue:
                    add += 1
                    
        return add
