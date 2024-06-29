#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_s = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(val, self.min)
        self.min_s.append(self.min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_s.pop()
        if len(self.min_s) != 0:
            self.min = self.min_s[-1]
        else:
            self.min = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_s[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

