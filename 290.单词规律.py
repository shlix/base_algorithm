#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        slist = s.strip().split(' ')
        if len(pattern) != len(slist):
            return False
        for i in range(len(pattern)):
            #print(i,pattern[i],slist[i],dic)
            if pattern[i] in dic and dic[pattern[i]] != slist[i]:
                return False
            dic[pattern[i]] = slist[i]
        dic = {}
        for i in range(len(pattern)):
            #print(i,pattern[i],slist[i],dic)
            if slist[i] in dic and dic[slist[i]] != pattern[i]:
                return False
            dic[slist[i]] = pattern[i]
        return True

# @lc code=end
sol = Solution()
sol.wordPattern('abba', 'dog cat cat dog')
