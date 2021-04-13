# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        def preorder(root,value):
            if root:
                value.append(root.val)
                preorder(root.left,value)
                preorder(root.right,value)
            return value
        return preorder(root,value=[])
