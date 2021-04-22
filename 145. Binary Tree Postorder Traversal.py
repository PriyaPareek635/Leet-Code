# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        def postorder(root,value):
            if root:
                postorder(root.left,value)
                postorder(root.right,value)
                value.append(root.val)
                
            return value
        return postorder(root,value=[])
