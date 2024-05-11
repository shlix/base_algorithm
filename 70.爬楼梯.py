#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        f = [0]*(n+1)
        if n==1:
            return 1
        f[0],f[1] = 1,1
        for i in range(2, n+1):
            print(i,f)
            f[i] = f[i-1] + f[i-2]
        return f[n]
solu = Solution()
print(solu.climbStairs(9))

# @lc code=end

