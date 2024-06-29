#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
from typing import List
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for s in nums:
            if s-1 in nums:
                continue
            cur = s + 1
            while cur in nums:
                cur += 1
            res = max(cur-s, res)
        return res

# @lc code=end

#input: [100,4,200,1,3,2]
#output: 4, [1,2,3,4]

