#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for i in magazine:
            dic[i] = dic.get(i, 0) + 1
        for i in ransomNote:
            if i in dic and dic.get(i) > 0:
                dic[i] -= 1
            else:
                return False
        return True
# @lc code=end
