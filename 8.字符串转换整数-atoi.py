#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        num = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        op = {'+', '-'}
        num_str = ''
        str = str.strip()
        if not str or (str[0] not in num and str[0] not in op):
            return 0
        for i in range(1, len(str)):
            if str[i] not in num:
                num_str = str[0:i]
                break
        if len(num_str) == 0:
            num_str = str
        if len(num_str) == 1 and num_str[0] in op:
            return 0
        import math
        res = int(num_str)
        max_int = int(math.pow(2, 31))
        if res < max_int and res >= -max_int:
            return res
        elif res >= max_int:
            return max_int-1
        else:
            return -max_int
solu = Solution()
print(solu.myAtoi('+1'))
        
# @lc code=end

