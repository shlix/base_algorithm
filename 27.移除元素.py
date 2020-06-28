#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j  = 0, 0
        while i<=j and j<len(nums):
            if nums[i] == val:
                if nums[j] == val:
                    j += 1
                else:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
            else:
                i += 1
                j += 1
        return i
# @lc code=end

