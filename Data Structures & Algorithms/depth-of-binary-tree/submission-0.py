# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recurse_maxDepth(v):
            if not root:
                return 0 #??
            else:
                left = recurse_maxDepth(v.left) if v.left else 0
                right = recurse_maxDepth(v.right) if v.right else 0
                return 1 + max(left,right)
        
        return recurse_maxDepth(root)