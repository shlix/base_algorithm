#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        lis = ['' for i in range(min(numRows, len(s)))]
        flag = False
        row = 0
        for cha in s:
            lis[row] += cha
            if row == 0 or row == numRows-1:
                flag = not flag
            row += 1 if flag else -1
        re = ''
        for i in lis:
            re += i
        return re

# @lc code=end

