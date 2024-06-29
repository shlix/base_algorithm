#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
from typing import List
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = dp[i-1] + nums[i] if dp[i-1]>=0 else nums[i]
        return max(dp)
# @lc code=end

#solution = Solution()
#print(solution.maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]))
