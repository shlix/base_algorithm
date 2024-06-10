#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num:int) -> str:
        lis = [['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],\
               ['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
        res = ""
        for i in lis:
            #print(i)
            if num==0:
                break
            t = num//i[1]
            res += i[0]*t
            num -= t*i[1]
        return res

# @lc code=end
solu = Solution()
solu.intToRoman(3749)

