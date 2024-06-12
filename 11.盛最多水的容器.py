#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
from typing import List
# @lc code=start
class Solution:
    def maxArea1(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        volume = 0
        while(i != j):
            volume = max(volume, min(height[i], height[j])*(j - i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return volume
    # review 0611
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        res = 0
        while i < j:
            res = max(res, min(height[i], height[j])*(j-i))
            if height[i]>height[j]:
                j -= 1
            else:
                i += 1
        return res

# @lc code=end
# [1,8,6,2,5,4,8,3,7]
