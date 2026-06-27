# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isEqual(self, a, b):
        self.res = True
        self.BFS(a, b)
        return self.res

    def BFS(self, a, b):
        if not a and not b:
            return
        if not a or not b:
            self.res = False
            return
        if a.val != b.val:
            self.res = False
            return
        self.BFS(a.left, b.left)
        self.BFS(a.right, b.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = [root]
        while q:
            for _ in range(len(q)):
                node = q.pop(0)
                if self.isEqual(node, subRoot):
                    return True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return False