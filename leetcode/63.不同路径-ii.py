#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
from typing import List
from itertools import product
# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0]*n for i in range(m)]
        if obstacleGrid[0][0]==1:
            return 0
        else:
            dp[0][0] = 1
        for i in range(0,m):
            for j in range(0,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i==0 and j>0:
                        dp[i][j] = dp[i][j-1]
                    if j==0 and i>0:
                        dp[i][j] = dp[i-1][j]
                    if i!=0 and j!=0:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

    #use math method,多个障碍物时如何修改？
    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:
        def getC(m,n):
            if m<=1 or n<=1:
                return 1
            up = 1
            low = 1
            for i in range(m-1):
                up *= (m+n-2-i)
                low *= i+1
            return int(up/low)
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        x,y = -1,-1
        for i,j in product(range(m),range(n)):
            if obstacleGrid[i][j] == 1:
                x, y = i, j
                break
        if x==-1:
            return getC(m,n)
        
        return getC(m,n) - getC(x+1,y+1)*getC(m-x,n-y)
# @lc code=end
#so = Solution()
#print(so.uniquePathsWithObstacles([[0,1],[1,0]]))

