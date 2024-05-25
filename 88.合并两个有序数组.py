#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

from typing import List
from copy import deepcopy
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m*n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m + n - 1] = nums1[m-1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        #print(nums1)
# @lc code=end

solu = Solution()
a = [0]
solu.merge(a,0, [1],1)
print(a)
