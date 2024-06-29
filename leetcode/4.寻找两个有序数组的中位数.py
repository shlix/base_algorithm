#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m>n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        if n == 0:
            raise ValueError
        imin, imax, half = 0, m, (m+n+1)//2
        while(imin<=imax):
            i = (imax+imin)//2
            print(i)
            j = half - i
            if(i<m and nums1[i]<nums2[j-1]):
                imin = i+1
            elif(i>0 and nums2[j]<nums1[i-1]):
                imax = i-1
            else:
                if i==0:
                    maxofleft = nums2[j-1]
                elif j == 0:
                    maxofleft = nums1[i-1]
                else:
                    maxofleft = max(nums1[i-1], nums2[j-1])
                if (m+n)%2==1:
                    return maxofleft
                if i==m:
                    minofright = nums2[j]
                elif j==n:
                    minofright = nums1[i]
                else:
                    minofright = min(nums1[i], nums2[j])
                return (minofright+maxofleft)/2.0
#nums1, nums2=[1,3], [2]
#solu = Solution()
#print(solu.findMedianSortedArrays(nums1, nums2))
# @lc code=end

