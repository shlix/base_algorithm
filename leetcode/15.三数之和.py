#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List
# @lc code=start
class Solution:
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        
        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans
    #review 24.06.12
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 首先对数组进行排序
        res = []
        n = len(nums)

        for i in range(n):
            # 跳过重复的元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1  # 双指针初始化

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    # 跳过重复的 left 元素
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 跳过重复的 right 元素
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return res
# @lc code=end
sol = Solution()
sol.threeSum([-1,0,1,2,-1,-4])

#[-1,0,1,2,-1,-4]
#[-4,-1,-1,0,1,2]