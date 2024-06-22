#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        if s is None or s=='':
            return 0
        char_set = list(s[0])  #TODO char_set可以使用dict，减少查找耗时
        res_index = [0,0]
        i = 0
        j = 1
        while(i <= j and j < len(s)):
            if s[j] not in char_set:
                char_set.append(s[j])
                if j-i > res_index[1] - res_index[0]:
                    res_index = [i, j]
                j += 1
            else:
                char_set.pop(0)
                i += 1
        return res_index[1]-res_index[0]+1
    
    #review 24.06.17
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0,0
        se = set()
        res = 0
        while i<=j and j <len(s):
            #print(i,j)
            if s[j] not in se:
                se.add(s[j])
                j += 1
            else:
                se.remove(s[i])
                i += 1
            #print(se)
            res = max(res,j-i)
        return res
            
solu = Solution()
print(solu.lengthOfLongestSubstring('a'))
# @lc code=end

