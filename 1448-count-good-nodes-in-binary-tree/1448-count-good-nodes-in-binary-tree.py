# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxn):
            if not node:
                return 0

            if node.val >= maxn:
                good = 1
            else:
                good = 0

            currm = max(maxn, node.val)

            left = dfs(node.left,currm)
            right = dfs(node.right,currm)

            return good + left + right

        return dfs(root,root.val)