#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    # two-pointers method, 暴力法
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        le = len(needle)
        if not needle:
            return 0
        while i<=j and j<len(haystack):
            if haystack[j] == needle[j-i]:
                j += 1
            else:
                i += 1
                j = i
            if le == j - i:
                return i
        return -1
    # todo robin karp method
# @lc code=end

