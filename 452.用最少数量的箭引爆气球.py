#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#
from typing import List
from copy import deepcopy
# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x:(x[0],x[1]))
        #print(points)
        arrow = points[0]
        res = 1
        for ele in points:
            #print(ele,arrow)
            #print(arrow[1],ele[0])
            if arrow[1] >= ele[0]:
                arrow = [max(arrow[0], ele[0]),min(arrow[1], ele[1])]
            else:
                arrow = deepcopy(ele)
                res += 1
        return res

        
# @lc code=end
#输入：points = [[10,16],[2,8],[1,6],[7,12]]
#输出：2
#解释：气球可以用2支箭来爆破:
#-在x = 6处射出箭，击破气球[2,8]和[1,6]。
#-在x = 11处发射箭，击破气球[10,16]和[7,12]。
