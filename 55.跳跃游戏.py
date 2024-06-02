#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

from typing import List
# @lc code=start
class Solution:
    #原始DP解法
    def canJump1(self, nums: List[int]) -> bool:
        le = len(nums)
        dp = [True] + [False]*(le-1)
        for i in range(le):
            if dp[i]:
                for j in range(nums[i]):
                    if i + j + 1 < le:
                        dp[i + j + 1] = True
                    else:
                        return True
        return dp[-1]

    #时间复杂度优化，最远可达到位置（到达位置能超过len(nums), 则能到最后一个位置）
    def canJump(self, nums: List[int]) -> bool:
        le = len(nums)
        res = 0
        for i in range(le-1):
            res = max(res, i + nums[i])
            if res == i and nums[i] == 0:
                return False
        return True if res >=le-1 else False

# @lc code=end

