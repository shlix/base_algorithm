#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    #微观统计-局部与整体的关系，一旦某个局部出现最多的数在该区域占比没有超过50%，那么去除该区域不影响整体求解
    def majorityElement(self, nums: List[int]) -> int:
        t = nums[0]
        c = 0
        for i in nums:
            c += 1 if i==t else -1
            if c < 0:
                t = i
                c = 1
        return t
# @lc code=end

