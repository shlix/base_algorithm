#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'I':1, 'V':5,'X':10, 'L':50,
            'C':100, 'D':500, 'M':1000
        }
        res = 0
        le = len(s)
        for i in range(le):
            if i < le - 1 and map[s[i]] < map[s[i+1]]:
                res -= map[s[i]]
            else:
                res += map[s[i]]
        return res


# @lc code=end

