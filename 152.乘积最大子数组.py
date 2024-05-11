#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
from typing import List
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        big,small = [-1]*n,[1]*n
        big[0],small[0] = nums[0],nums[0]
        for i in range(1,n):
            big[i] = max(big[i-1]*nums[i],small[i-1]*nums[i],nums[i])
            small[i] = min(big[i-1]*nums[i],small[i-1]*nums[i],nums[i])
        print(big)
        return max(big)
            
solu = Solution()
solu.maxProduct([0.1,-0.3,1,-1,0.8,-0.9,-4,1])
# @lc code=end