#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#
from typing import List
# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        index = 0
        le = len(words)
        accumulate = 0
        n = 0
        line = []
        res = []
        while index < le:
            word = words[index]
            accumulate += len(word)
            n += 1
            line.append(word)
            if accumulate + n > maxWidth + 1:
                div = (maxWidth - accumulate + len(word))//(n-2 if n>2 else 1)
                if (maxWidth - accumulate + len(word)) != 0:
                    mod = (maxWidth - accumulate + len(word))%(n-2 if n>2 else (maxWidth - accumulate + len(word)))
                else:
                    mod = 0
                line.pop()
                #print(div, mod,line,n)
                s = ''
                for i in range(len(line)):
                    s += line[i]
                    if i < mod:
                        s += ' '*(div+1)
                    else:
                        if i != len(line) - 1:
                            s += ' '*div
                if len(line) == 1:
                    s += ' '*(maxWidth - len(s))
                res.append(s)
                #print(res)
                accumulate, n = 0,0
                line = []
                continue
            index += 1
            #print(index, line)
        if index == le and len(line)>0:
            s = ''
            s += ' '.join(line)
            s += ' '*(maxWidth -len(s))
            res.append(s)
        #print(res)
        return res

# @lc code=end

solution = Solution()
solution.fullJustify(words = ["Listen","to","many,","speak","to","a","few."]
, maxWidth = 6)
#[
#   "This    is    an",
#   "example  of text",
#    "justification.  "
#]
