#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [[1]+[0]*(n-1) if i!=0 else [1]*n for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
    #use math method
    def uniquePaths(self, m: int, n: int) -> int:
        up = 1
        low = 1
        for i in range(m-1):
            up *= (m+n-2-i)
            low *= i+1
        return int(up/low)
        
# @lc code=end
#solution = Solution()
#print(solution.uniquePaths_math(3,7))