#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List
class Solution:
    # 暴力方法
    def generateParenthesis1(self, n: int) -> List[str]:
        res = []
        def isValid(combination):
            lis = []
            for i in combination:
                if lis and lis[-1] == '(' and i == ')':
                    lis.pop()
                else:
                    if i == ')':
                        return False
                    lis.append(i)
            return True if len(lis)==0 else False

        def backtrack(combination, l1, l2):
            if l1 == 0 and l2 == 0:
                if isValid(combination):
                    res.append(combination)
            elif l1 == 0:
                backtrack(combination+")", l1, l2 - 1)
            elif l2 == 0:
                backtrack(combination+'(', l1 - 1, l2)
            else:
                backtrack(combination+'(', l1 - 1, l2)
                backtrack(combination+")", l1, l2 - 1)
        backtrack('', n, n)
        return res
    
    # 优化方法
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(combination, l1, l2):
            if l1 == 0 and l2 == 0:
                res.append(combination)
            if l2 > l1:
                backtrack(combination+")", l1, l2 - 1)
            if l1 > 0 :
                backtrack(combination+'(', l1 - 1, l2)
        backtrack('', n, n)
        return res
#solu = Solution()
#print(solu.generateParenthesis(3))
# @lc code=end

