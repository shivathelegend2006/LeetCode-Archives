class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def classify(a,b,x):
            if x == "+":
                return a+b
            elif x == "*":
                return a*b
            elif x == "-":
                return a-b
            else:
                return int(a/b)

        stack = []
        for i in range(len(tokens)):
            x = tokens[i]
            if  x not in {"+", "-", "*", "/"}:
                stack.append(int(x))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(classify(b,a,x))

        return stack[-1]