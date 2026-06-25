# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = [root]
        allLevels = []

        while q:
            currLevel = None
            for _ in range(len(q)):
                node = q.pop(0)
                currLevel = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            allLevels.append(currLevel)
        return allLevels