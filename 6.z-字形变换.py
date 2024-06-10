#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        lis = ['' for i in range(min(numRows, len(s)))]
        flag = False
        row = 0
        for cha in s:
            lis[row] += cha
            if row == 0 or row == numRows-1:
                flag = not flag
            row += 1 if flag else -1
        re = ''
        for i in lis:
            re += i
        return re
    
    # review 06.09
    def convert2(self, s: str, numRows: int) -> str:
        sl = len(s)
        if sl==1 or numRows==1:
            return s
        circle = 2*numRows-2
        round = sl//(circle)
        mod = sl%(circle)
        res = ''
        #print(circle,round,mod)
        for i in range(numRows):
            #print('i: ',i)
            for j in range(round):
                #print('j: ',j)
                #print(i + j * circle)
                res += s[i + j * circle]
                if i>0 and i<numRows-1:
                    #print(2*numRows -i + j * circle-2)
                    res += s[2*numRows -i + j * circle-2]
            if mod > i:
                #print(i + (round) * circle)
                res += s[i + (round) * circle]
                if mod >= 2*numRows -i-1 and i>0 and i<numRows-1:
                    #print('rrr',2*numRows -i-1 + (round) * circle-2)
                    res += s[2*numRows -i + (round) * circle-2]
        #print(res)
        return res

solu = Solution()
solu.convert('ABCDE', 4)
# @lc code=end

