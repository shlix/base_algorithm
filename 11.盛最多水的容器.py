#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        volume = 0
        while(i != j):
            volume = max(volume, min(height[i], height[j])*(j - i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return volume
# @lc code=end

