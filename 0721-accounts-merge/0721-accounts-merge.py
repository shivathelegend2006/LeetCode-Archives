import collections

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        graph = collections.defaultdict(list)
        email_name = {}

        for acc in accounts:
            for email in acc[1:]:
                graph[acc[1]].append(email)
                graph[email].append(acc[1])
                email_name[email] = acc[0]

        visited = set()
        
        def dfs(email, pile):
            visited.add(email)
            pile.append(email)
            for n in graph[email]:
                if n not in visited:
                    dfs(n, pile)
            return pile

        res = []
        for email in graph:
            if email not in visited:
                res.append([email_name[email]] + sorted(dfs(email, [])))

        return res