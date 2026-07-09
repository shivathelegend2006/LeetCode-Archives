"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        hash = {}
        def dfs(curr):
            if curr in hash:
                return hash[curr]
            clone = Node(curr.val)
            hash[curr] = clone

            for n in curr.neighbors:
                clone.neighbors.append(dfs(n))

            return clone
        return dfs(node)
        