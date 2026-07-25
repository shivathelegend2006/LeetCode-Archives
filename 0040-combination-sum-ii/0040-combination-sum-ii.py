class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #backtraaacking
        candidates.sort()
        res = []

        def backtrack(start, remaining, curr):
            if remaining == 0:
                res.append(list(curr))

            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i] > remaining:
                    break

                curr.append(candidates[i])

                backtrack(i+1,remaining - candidates[i],curr)
                curr.pop()

        backtrack(0,target,[])
        return res