#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

from typing import List
# @lc code=start
class Solution:

    #空间复杂度为O（N）
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        le = len(nums)
        pre = [1]*le
        suf = [1]*le
        res = []
        for i in range(le):
            pre[i] = pre[i - 1] * nums[i - 1] if i>0 else 1
            suf[le - i - 1] = 1 if i==0 else nums[le - i] * suf[le - i]
        #print(pre,suf)
        for i in range(le):
            res.append(pre[i]*suf[i])
        #print(res)
        return res
    
    #空间复杂度为O（1）
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        le = len(nums)
        res = [1]*le
        
        for i in range(le):
            res[i] = res[i-1]*nums[i-1] if i>0 else 1
        
        r = 1
        for i in reversed(range(le)):
            res[i] *= r
            r *= nums[i]
        return res


solu = Solution()
solu.productExceptSelf([1,2,3,4,5])
# @lc code=end