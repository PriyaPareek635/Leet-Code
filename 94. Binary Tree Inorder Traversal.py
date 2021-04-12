# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        l = []
        if root:
            self.traverse(root, l)
        return l
        
    def traverse(self, node, l):
        if (node.left):
            self.traverse(node.left, l)
        l.append(node.val)
        if (node.right):
            self.traverse(node.right, l)   
        
