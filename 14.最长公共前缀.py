#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        flag = True
        i = 0
        res = ''
        if len(strs) == 0:
            return res
        while(flag):
            tmp = ''
            if len(strs[0])-1 >= i:
                tmp = strs[0][i]
            else:
                flag = False
            for s in strs:
                if not (len(s)-1 >= i and s[i] == tmp):
                    flag = False
                    break
            i += 1
        return strs[0][0:i-1]
# @lc code=end

