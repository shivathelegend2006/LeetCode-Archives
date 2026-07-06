# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_hash = {value:index for index, value in enumerate(inorder)}

        self.pre_indx = 0

        def builder(left,right,self):
            if left > right:
                return None

            root_val = preorder[self.pre_indx]
            root = TreeNode(root_val)

            self.pre_indx += 1
            mid = inorder_hash[root_val]

            root.left = builder(left,mid-1,self)
            root.right = builder(mid+1,right,self)

            return root

        return builder(0,len(inorder)-1,self)