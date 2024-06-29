#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#
from typing import List
from itertools import product
# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[0 for j in range(9)] for i in range(9)]
        column = [[0 for j in range(9)] for i in range(9)]
        block = [[[0 for k in range(9)] for i in range(3)] for j in range(3)]
        for i,j in product(range(9), range(9)):
            ele = board[i][j]
            if ele != '.':
                ele = int(ele) - 1
                #print(i,j,ele)
                row[i][ele] += 1
                column[j][ele] += 1
                block[i//3][j//3][ele] += 1
                if row[i][ele] > 1 or column[j][ele] > 1 or block[i//3][j//3][ele] > 1:
                    return False
        return True

# @lc code=end

