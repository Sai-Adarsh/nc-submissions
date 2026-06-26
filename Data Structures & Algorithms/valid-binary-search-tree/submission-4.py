# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return
        self.res = True
        res = []
        def BFS(root):
            if not root:
                return
            BFS(root.left)
            res.append(root.val)
            if len(res) > 1 and res[-1] <= res[-2]:
                self.res = False
                return
            BFS(root.right)
        BFS(root)
        return self.res