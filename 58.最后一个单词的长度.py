#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord1(self, s: str) -> int:
        res = 0
        last = 0
        for i in s:
            if i != ' ':
                res += 1
            else:
                res = 0
            last = res if res>0 else last
        return last
    #反序，剪枝
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for i in reversed(s):
            if i == ' ':
                if res>0:
                    return res
                continue
            else:
                res += 1
        return res

# @lc code=end

