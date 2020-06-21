#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #采用中心扩展算法
        #TODO Manacher算法
        start, end = 0, 0
        for i in range(len(s)-1):
            le = max(self.getSpan(s, i, i), self.getSpan(s, i, i+1))
            if le > (end - start):
                start = i - (le-1)//2
                end = i + le//2
        return s[start:end+1]

    def getSpan(self, s: str, left: int, right: int) -> int:
        while(left >= 0 and right<len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1

# @lc code=end

