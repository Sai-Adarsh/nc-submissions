# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def BFS(root):
            if not root:
                return 1
            left = BFS(root.left)
            right = BFS(root.right)
            self.res = max(self.res, left, right)
            return 1 + max(left, right)
        self.res = 0
        BFS(root)
        return self.res