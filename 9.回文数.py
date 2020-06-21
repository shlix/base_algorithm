#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# @lc code=start
class Solution:
    # 将int转为str后处理
    def isPalindrome1(self, x: int) -> bool:
        s = str(x)
        for i in range(0, len(s)//2 + 1):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
    # 保留int格式处理
    def isPalindrome(self, x: int) -> bool:
        num_lis = []
        if x < 0:
            return False
        if x == 0:
            return True
        while x:
            num_lis.append(x%10)
            x = x // 10
        for i in range(0, len(num_lis)//2 + 1):
            if num_lis[i] != num_lis[len(num_lis)-i-1]:
                return False
        return True

# @lc code=end
