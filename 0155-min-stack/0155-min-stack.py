class MinStack:
# we need to append 2 values at a time my guy
    def __init__(self):
        self.stack = []


    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append((value,value))
        else:
            minn = min(value,self.stack[-1][1])
            self.stack.append((value,minn))


    def pop(self) -> None:
        self.stack.pop()
    

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

#now all vlaues remebers which is the minium when they were added 
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()