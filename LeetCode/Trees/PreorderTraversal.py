# Definition for a binary tree node.
#class TreeNode(object):
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return
        
        res = []
        stack = []
        
        while stack or root:
            if root:
                stack.append(root)
                res.append(root.val)    
                root = root.left     
            else:
                node = stack.pop()
                root = node.right
        return res
