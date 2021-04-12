# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        
        new = []
        def helper(root):
            if not root:
                return([])
            return(helper(root.left)+[root.val]+helper(root.right))

        new = helper(root)
        for i in range(len(new)-1):
            if(new[i]>=new[i+1]):
                return(False)
        return(True)
        
