#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        import sys
        import math
        maxint = int(math.pow(2, 31))-1
        minint = -maxint-1
        rev = 0
        while(x != 0):
            pop = x%10 if x>0 else -(-x%10)
            x = x//10 if x>0 else -(-x//10)
            if rev > maxint//10 or (rev==maxint//10 and pop>maxint%10):
                return 0
            if rev < -(-minint//10) or (rev==-(-minint//10) and pop<-(-minint%10)):
                return 0
            rev = rev*10 +pop
        return rev

# @lc code=end

