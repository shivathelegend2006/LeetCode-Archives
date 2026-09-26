# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p1 = []
        q1 = []
        def dfs(root,t,l):
            
            if not root:
                return None

            if root.val == t:
                
                return l
            
            l.append(root)
            if dfs(root.left,t,l) or dfs(root.right,t,l):

                return l

            l.pop()
            return None

        p1 = dfs(root,p.val,[])
        q1 = dfs(root,q.val,[])
        p1.append(p)
        q1.append(q)
        if p in q1: return p
        if q in p1: return q

        i, j = 0,0
        curr = 0

        while True:
            if  (i < len(p1)) and (j < len(q1)) and p1[i].val == q1[j].val:
                curr = p1[i]
                i += 1
                j += 1
                continue
            else:
                break

        return curr