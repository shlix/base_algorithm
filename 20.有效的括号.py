#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid1(self, s: str) -> bool:
        stack = []
        k_v = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        for i in s:
            if stack and k_v.get(i, '-') == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        return False
    # review 06.29
    def isValid(self ,s:str) -> bool:
        stack = []
        k_v = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        for i in s:
            if i in k_v and stack and stack[-1] == k_v[i]:
                stack.pop()
            else:
                stack.append(i)
        return not stack
#so = Solution()
#print(so.isValid('()'))
# @lc code=end

