#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binaryS(left, right):
            mid = (left+right)//2
            if left>right:
                return -1
            if target == nums[mid]:
                return mid
            if nums[mid]>=nums[left]:
                if nums[left]<=target<nums[mid]:
                    return binaryS(left, mid-1)
                else:
                    return binaryS(mid+1, right)
            else:
                if nums[mid]<target<=nums[right]:
                    return binaryS(mid+1, right)
                else:
                    return binaryS(left, mid-1)
        return binaryS(0, len(nums)-1)

solu = Solution()
print(solu.search([4,5,6,7,0,1,2], 0))
# @lc code=end

