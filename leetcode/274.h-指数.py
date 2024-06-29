#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#
from typing import List
# @lc code=start
class Solution:
    #直接排序方法
    def hIndex1(self, citations: List[int]) -> int:
        citations.sort()
        le = len(citations)
        hindex = 0
        for i in range(le):
            if le - i >= citations[i]:
                hindex = max(hindex, citations[i])
            else:
                hindex = max(hindex,le-i)
                break
        return hindex
    # 不排序，统计
    def hIndex(self, citations: List[int]) -> int:
        le = len(citations)
        count = [0] * (le+1)
        index = 0
        for i in range(le):
            if citations[i] > le:
                count[le] += 1
            else:
                count[citations[i]] += 1
        for i in range(le,0,-1):
            index += count[i]
            if index >= i:
                return i
        return 0


# @lc code=end

