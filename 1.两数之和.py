#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

from typing import List
# @lc code=start
class Solution:
    #Review on June 21, 2024, at 22:41—an incredibly frustrating night. 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        le = len(nums)
        for i in range(le):
            if target - nums[i] in dic and dic[target - nums[i]] != i:
                return [dic[target - nums[i]],i]
            dic[nums[i]] = i
        return []
# @lc code=end

