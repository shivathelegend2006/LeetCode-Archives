class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        tree = [[] for i in range(n)]

        for i in range(1, n):
            tree[parent[i]].append(i)
        
        ans = [1]*n
        last_seen = {}

        def dfs(u):
            ch = s[u]
            prev = last_seen.get(ch)

            last_seen[ch] = u
            for child in tree[u]:
                dfs(child)

            last_seen[ch] = prev
            if u != 0:
                target = prev if prev is not None else parent[u]
                ans[target] += ans[u]

        dfs(0)
        return ans