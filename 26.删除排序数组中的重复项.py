#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        while i <= j and j < len(nums)-1:
            if nums[j] != nums[j+1]:
                i += 1
                nums[i] = nums[j+1]
            j += 1
        return i + 1

#solu = Solution()
#print(solu.removeDuplicates([1,1,2,2,2,3,3,4]))
# @lc code=end

