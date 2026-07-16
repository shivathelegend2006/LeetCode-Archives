class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #backtrakinggg
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []
        def backtrack(i,curr):
            if len(curr) == len(digits): 
                res.append(curr)
                return

            letters = phone_map[digits[i]]
            for l in letters:
                backtrack(i+1,curr+l)

        backtrack(0,"")
        return res