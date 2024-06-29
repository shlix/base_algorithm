#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
from typing import List
# @lc code=start
class Solution:
    #贪心算法
    def maxProfit1(self, prices: List[int]) -> int:
        le = len(prices)
        low = -1
        up = 0
        res = 0
        if le==1:
            return res
        for i in range(0,le):
            if (i not in [0,le-1] and prices[i] <= prices[i-1] and prices[i] < prices[i+1]) \
                or (i==0 and prices[i] < prices[i+1]):
                low = prices[i] if low<0 else min(low, prices[i])
                #print('low', low)
            if (i not in [0,le-1] and prices[i] >= prices[i-1] and prices[i] > prices[i+1]) \
                or (i==le-1 and prices[i] >= prices[i-1]):
                up = prices[i]
                #print('up', up)
                if low >= 0:
                    res += up-low
                    #print(up-low)
                    low = -1
        return res
    #贪心优化版本
    def maxProfit2(self, prices: List[int]) -> int:
        res = 0
        le = len(prices)
        for i in range(1, le):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res

    #动态规划
    def maxProfit(self, prices: List[int]) -> int:
        dp0 = 0
        dp1 = -prices[0]
        for i in range(len(prices)):
            dp0 = max(dp0, dp1+prices[i])
            dp1 = max(dp1, dp0-prices[i])
        return dp0
# @lc code=end

so = Solution()
so.maxProfit([1,9,6,9,1,7,1,1,5,9,9,9])
