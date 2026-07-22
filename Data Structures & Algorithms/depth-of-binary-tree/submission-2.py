# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def solve(node, depth):
            # base case
            if not node:
                return depth
            # recursive case
            return max(solve(node.left, depth+1), solve(node.right, depth+1))
        return solve(root, 0)