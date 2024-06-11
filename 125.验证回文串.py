#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j =0, len(s)-1
        while i <= j:
            if (s[i].isalpha() or s[i].isdigit()) and (s[j].isalpha() or s[j].isdigit()):
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                    continue
                else:
                    return False
            
            if not s[i].isalpha() and not s[i].isdigit():
                i += 1
            if not s[j].isalpha() and not s[j].isdigit():
                j -= 1
        return True

# @lc code=end

solu = Solution()
solu.isPalindrome("0p")
