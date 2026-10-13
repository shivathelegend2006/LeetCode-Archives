# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if not root: 
            return []
        q = deque([root])
        res = []
        while q:
            current = []

            for i in range(len(q)):
                node = q.popleft()
                current.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            res.append(current)

        return res[::-1]
            
