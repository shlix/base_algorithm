#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
from typing import List
import math 
# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        le = len(nums)
        for i in range(le):
            if nums[i] in dic and i - dic[nums[i]] <= k:
                return True
            else:
                dic[nums[i]] = i
        return False

# @lc code=end

