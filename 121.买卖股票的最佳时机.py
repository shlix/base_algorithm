#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]*len(prices)
        low = prices[0]
        for i in range(1,len(prices)):
            dp[i] = max(dp[i-1], prices[i] - low)
            if prices[i] < low:
                low = prices[i]
            #print(dp,low)
        return max(dp)
            
# @lc code=end
solu = Solution()
print(solu.maxProfit([7,1,5,3,6,4]))
