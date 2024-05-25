#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

from typing import List
# @lc code=start
class Solution:
    #方法一未完成
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        le = len(nums)
        if k*2 > le:
            k = le - k
        for i in range(le-k):
            tmp = nums[i]
            nums[i] = nums[i+k]
            nums[i+k] = tmp
            print(nums)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        le = len(nums)
        if k>le:
            k %= le
        self.reverse(nums,0,le)
        #print(nums)
        self.reverse(nums,0,k)
        #print(nums)
        self.reverse(nums,k,le)
        #print(nums)
    def reverse(self,nums,m,n):
        for i in range(0,(n-m)//2):
            tmp = nums[m + i]
            nums[m+i] = nums[n - i-1]
            nums[n - i - 1] = tmp

# @lc code=end
solu = Solution()
nums = [1,2]
solu.rotate(nums, 3)
