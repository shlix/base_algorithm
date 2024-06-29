#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
from typing import List
from itertools import product
from copy import deepcopy
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        if m+n==0:
            return 0
        dp = deepcopy(matrix)
        res = 0
        for i,j in product(range(m), range(n)):
            dp[i][j] = int(matrix[i][j])
            if dp[i][j]>res:
                res = dp[i][j]
            if matrix[i][j]=='0' or i==0 or j==0 or dp[i-1][j-1]==0:
                continue
            dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + 1
            if dp[i][j]>res:
                res = dp[i][j]
            #print(dp)
        return res*res

# @lc code=end
solu = Solution()
solu.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])


