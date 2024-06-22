#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
from typing import List
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = {}
        for i in range(len(strs)):
            order = "".join(sorted(strs[i]))
            dic[order] = dic.get(order,len(res))
            #print(i,dic,res)
            if len(res) > dic[order]:
                res[dic[order]].append(strs[i])
            else:
                res.append([strs[i]])
        return res
# @lc code=end
sol = Solution()
sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])


#输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#输出: [["bat"],["nat","tan"],["ate","eat","tea"]