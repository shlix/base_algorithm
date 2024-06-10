#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#
from typing import List
# @lc code=start
class Solution:
    #贪心算法，左右约束分开计算，取最大值
    def candy1(self, ratings: List[int]) -> int:
        le = len(ratings)
        left = [1] * le
        right = 1
        res = 0
        for i in range(1,le):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
        #print(left)
        for i in range(le-1, -1, -1):
            if i<le-1 and ratings[i] > ratings[i+1]:
                right += 1
            else:
                right = 1
            #print(right)
            res += max(right, left[i])
        return  res
    #贪心算法，空间复杂度降低为O(1)
    def candy(self, ratings: List[int]) -> int:
        le = len(ratings)
        up_len,low_len,pre = 1,1,1
        res = 1
        for i in range(1,le):
            if ratings[i] >= ratings[i-1]:
                low_len = 0
                pre = 1 if ratings[i] == ratings[i-1] else pre + 1
                #print(pre)
                res += pre
                up_len = pre
            else:
                low_len += 1
                if low_len == up_len:
                    #pass
                    low_len += 1
                #print(low_len)
                res += low_len
                pre = 1
        #print(res)
        return res


# @lc code=end
solu = Solution()
solu.candy([1,2,3,10,9,8,7,6,5,4,3,2,1])

