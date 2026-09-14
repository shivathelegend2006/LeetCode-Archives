import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        locks = [0]*numCourses
        adj = defaultdict(list)

        for c, p in prerequisites:
            adj[p].append(c)
            locks[c] += 1

        q = collections.deque()
        for i in range(numCourses):
            if locks[i] == 0:
                q.append(i)

        res = []
        while q:
            curr = q.popleft()
            res.append(curr)

            for n in adj[curr]:
                locks[n] -= 1
                if locks[n] == 0:
                    q.append(n)

        if len(res) == numCourses:
            return res
        else:
            return []