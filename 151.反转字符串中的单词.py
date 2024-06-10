#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        res = ''
        for i in reversed(s):
            if i != ' ':
                stack.append(i)
            else:
                if len(stack) != 0:
                    stack.reverse()
                    res += ''.join(stack)+" "
                    stack = []
        if len(stack) != 0:
            stack.reverse()
            res += ''.join(stack) + ' '
        return res[0:len(res)-1]

# @lc code=end

