#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(a, b):
            tmp = nums[a]
            nums[a] = nums[b]
            nums[b] = tmp
        tmp = 'mark'
        index = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                for j in range(i, len(nums)):
                    if nums[i-1]<nums[j] and (j==len(nums)-1 or nums[i-1]>=nums[j+1]):
                        swap(i-1, j)
                index = i
                break
        nums[index:] = [nums[i] for i in range(len(nums)-1, index-1, -1)]
#nums = [1,5,8,4,7,6,5,3,1]
#solu = Solution()
#solu.nextPermutation(nums)
#print(nums)
# @lc code=end

