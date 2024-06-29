#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
from typing import List
# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        last = -100
        for ele in nums:
            #print(last,ele,res)
            if ele == last + 1:
                last = ele
                if ele == nums[-1]:
                    res[-1] += '->'+str(last)
                continue
            if res and res[-1] != str(last):
                res[-1] += '->'+str(last)
            res.append(str(ele))
            last = ele
        return res
            
# @lc code=end
sol = Solution()
sol.summaryRanges([0,2,3,4,6,8,9])

