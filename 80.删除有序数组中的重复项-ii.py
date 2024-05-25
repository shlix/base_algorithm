#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates1(self, nums: List[int]) -> int:
        le = len(nums)
        k,f = 0,0
        for i in range(le):
            #print(nums,i,k,f)
            if nums[i] == nums[k] and k < i:
                f += 1
                if f<2:
                    k += 1
                    nums[k] = nums[i]
            if nums[i] != nums[k]:
                f = 0
                k += 1
                nums[k] = nums[i]
        return k + 1
    def removeDuplicates(self, nums: List[int]) -> int:
        le = len(nums)
        if le <= 2:
            return le
        slower = 2
        for i in range(2,le):
            #print(nums,i,slower)
            if nums[i] != nums[slower-2]:
                nums[slower] = nums[i]
                slower += 1
        return slower


# @lc code=end

solution = Solution()
print(solution.removeDuplicates([0,0,1,1,1,1,2,3,3]))