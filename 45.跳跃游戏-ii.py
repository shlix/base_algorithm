#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
from typing import List
# @lc code=start
class Solution:
    #dp解法
    def jump1(self, nums: List[int]) -> int:
        le = len(nums)
        dp = [0] + [1e8]*(le-1)
        for i in range(le):
            for j in range(nums[i]):
                if i + j + 1 > le-1:
                    break
                dp[i + j + 1] = min(dp[i]+1, dp[i + j + 1])
        return dp[-1]
    
    #贪心解法
    def jump(self, nums: List[int]) -> int:
        le = len(nums)
        far = 0
        end =0
        step = 0
        for i in range(le-1):
            far = max(far, i + nums[i])
            if i==end:
                end = far
                step += 1
        return step



# @lc code=end

