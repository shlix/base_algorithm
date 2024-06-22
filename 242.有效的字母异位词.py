#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i], 0) + 1
            dic[t[i]] = dic.get(t[i], 0) - 1
        for k,v in dic.items():
            if v != 0:
                return False
        return True
# @lc code=end

