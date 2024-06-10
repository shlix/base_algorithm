#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
from typing import List
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        le = len(gas)
        index = 0
        remain = 0
        for i in range(le):
            remain += gas[i] - cost[i]
            if remain < 0 and i != le-1:
                index = i + 1
                remain = 0
            if remain >= 0 and i == le - 1:
                for j in range(index):
                    remain += gas[j] - cost[j]
                    if remain < 0:
                        return -1
                return index
        return -1       

# @lc code=end

solu = Solution()
solu.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
solu.canCompleteCircuit([2,3,4], [3,4,3])