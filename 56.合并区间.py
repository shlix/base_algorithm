#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from typing import List
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key = lambda i:(i[0],i[1]))
        le = len(intervals)
        res = [intervals[0]]
        for i in range(1,le):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res



# @lc code=end

#输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
#输出：[[1,6],[8,10],[15,18]]
#区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6]