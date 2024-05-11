#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
from typing import List
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[:2] = nums[:2]
        for i in range(2,n):
            dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        return max(dp)
# @lc code=end