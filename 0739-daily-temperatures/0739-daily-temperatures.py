class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        t = temperatures
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and t[stack[-1]] < temp:
                prev = stack.pop()
                res[prev] = i- prev
            stack.append(i)

        return res
            
        