class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #think, just use kruskalss, if u w=find a cycle, return the edge
        parent = [i for i in range(len(edges)+1)]

        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])

            return parent[n]

        for u , v in edges:
            parent_u = find(u)
            parent_v = find(v)

            if parent_u == parent_v:
                return [u,v]
            
            parent[parent_v] = parent_u
        return []