# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #find balance factor at each node and then add them to find the maximu of all;
        self.maxd = 0
        def h(node):
            
            if not node:
                return 0
            
            lefth = h(node.left)
            righth = h(node.right)
            self.maxd = max(self.maxd, lefth + righth)

            return 1 + max(lefth,righth)

        h(root)
        return self.maxd
