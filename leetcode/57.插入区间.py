#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
from typing import List
# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        f = False
        if not intervals:
            return [newInterval]
        for i,ele in enumerate(intervals):
            if not f and newInterval[0] <= ele[1] and newInterval[1] >= ele[0]:
                res.append([min(ele[0],newInterval[0]), max(newInterval[1], ele[1])])
                f = True
                continue
            if res and res[-1][1] >= ele[0]:
                res[-1][1] = max(ele[1], res[-1][1])
            else:
                res.append(ele)
            if not f and i<len(intervals)-1 and newInterval[0]>ele[1] and newInterval[1]< intervals[i + 1][0]:
                res.append(newInterval)
                f = True
        if not f:
            return intervals + [newInterval] if newInterval[0] > intervals[-1][0] else [newInterval] + intervals
        return res

# @lc code=end

#输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
#输出：[[1,5],[6,9]]