#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
from typing import List
# @lc code=start
class Solution:
    #dp[i]表示偷[0:i]能获取的最大值
    def sub(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        dp = [0]*n
        dp[0],dp[1] = nums[0],max(nums[:2])
        for i in range(2,n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return max(dp)
    
    # dp[i]表示[0:i]且偷第i家能获取的最大值
    def sub2(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[:2] = nums[:2]
        for i in range(2,n):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        return max(dp)
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        return max(self.sub2(nums[:n-1]),self.sub2(nums[1:n]))
        
# @lc code=end

