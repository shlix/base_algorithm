#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
from typing import List
# @lc code=start
class Solution:
    #滑动窗口
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        le = len(nums)
        res = le + 1
        i = 0
        j = 0
        tmp = 0
        while j < le and i <= j:
            tmp += nums[j]
            if tmp < target:
                j += 1
            else:
                res = min(res, j - i + 1)
                tmp -= (nums[i] + nums[j])
                i += 1
        return res if res<le + 1 else 0
    

# @lc code=end

#[2,3,1,2,4,3]