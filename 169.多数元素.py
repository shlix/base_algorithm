#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from typing import List
# @lc code=start
class Solution:
    #微观统计-局部与整体的关系，一旦某个局部出现最多的数在该区域占比没有超过50%，那么去除该区域不影响整体求解
    def majorityElement1(self, nums: List[int]) -> int:
        t = nums[0]
        c = 0
        for i in nums:
            c += 1 if i==t else -1
            if c < 0:
                t = i
                c = 1
        return t

    def majorityElement(self, nums: List[int]) -> int:
        le = len(nums)
        k = nums[0]
        n = 0
        for i in range(1,le):
            if n < 0:
                k = nums[i]
            if nums[i] != k:
                n -= 1
            else:
                n += 1
        return k


# @lc code=end

