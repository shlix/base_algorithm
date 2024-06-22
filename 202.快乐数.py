#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
import math
# @lc code=start
class Solution:
    #最简单的方法，另外两种方法待定
    def isHappy(self, n: int) -> bool:
        se = set()
        return Solution.recursion(se, n)
    
    @staticmethod
    def recursion(se, n) -> bool:
        if n in se:
            return False
        else:
            se.add(n)
            re = 0
            for i in str(n):
                re += int(math.pow(int(i),2))
            if re == 1:
                return True
            return Solution.recursion(se, re)
# @lc code=end
sol = Solution()
sol.isHappy(2)
