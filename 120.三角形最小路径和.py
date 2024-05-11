#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
from typing import List
from itertools import product
# @lc code=start
class Solution:
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[1000]*n for i in range(n)]
        dp[0][0] = triangle[0][0]
        res = 100000
        for i,j in product(range(0,n), range(0,n)):
            if i < j:
                continue
            if j>0:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            elif i!=0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            if i == n-1 and res > dp[i][j]:
                res = dp[i][j]
        #print(dp)
        return res
    #原数组上操作
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        #dp = [100]*n
        res = 100000
        for i,j in product(range(n), range(n)):
            if i < j:
                continue
           #print(i,j)
            if j>0 and i != j:
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
            elif i!=0 and i!=j:
                triangle[i][j] += triangle[i-1][j]
            if i==j and i>0:
                #print(i,j)
                triangle[i][j] += triangle[i-1][j-1]
            if i == n-1 and res > triangle[i][j]:
                res = triangle[i][j]
        #print(triangle)
        return res

        
# @lc code=end

so = Solution()
so.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])