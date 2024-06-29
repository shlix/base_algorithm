#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#
from typing import List
from copy import deepcopy
# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l = len(words[0])
        lw = len(words)
        ls = len(s)
        ma = {}
        count = 0
        for w in words:
            ma[w] = ma.get(w,0) + 1
        se = deepcopy(ma)
        res = []
        i, j = 0, 0
        while i <= j and j < ls:
            candidate = s[j:j + l]
            #print(i,j,se, count,candidate)
            if candidate in se and se.get(candidate) != 0:
                se[candidate] -= 1
                count += 1
                j += l
            else:
                #if j>i:
                    #se[s[i:i + l]] += 1
                    #count -= 1
                    #i += l
                #else:
                i += 1
                j = i
                se = deepcopy(ma)
                count = 0
            if count == lw:
                res.append(i)
        return res

sol = Solution()
print(sol.findSubstring("barfoothefoobarman", ["foo","bar"]))
#print(sol.findSubstring("barfoothefoobarman", ["foo","bar"]))
# @lc code=end    
#输入：s = "barfoothefoobarman", words = ["foo","bar"]
# 输出：[0,9]