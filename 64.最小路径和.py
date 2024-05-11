#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
from typing import List
from typing import List
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[0]*n for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(0,m):
            for j in range(0,n):
                if i==0 and j>0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                if j==0 and i>0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                if i!=0 and j!=0:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        #print(dp)
        return dp[m-1][n-1]
# @lc code=end
#so = Solution()
#print(so.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
