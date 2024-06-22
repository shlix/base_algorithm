#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        le = len(s)
        for i in range(le):
            if s[i] not in dic_s and t[i] not in dic_t:
                dic_s[s[i]] = t[i]
                dic_t[t[i]] = s[i]
            elif s[i] in dic_s and t[i] in dic_t and dic_s[s[i]] == t[i] and dic_t[t[i]] == s[i]:
                continue
            else:
                return False
        return True

# @lc code=end

