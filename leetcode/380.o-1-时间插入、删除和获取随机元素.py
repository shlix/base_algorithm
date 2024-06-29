#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

#变长数组可以在 O(1) 的时间内完成获取随机元素操作，但是由于无法在 O(1) 的时间内判断元素是否存在，因此不能在 O(1) 的时间内完成插入和删除操作。哈希表可以在 O(1) 的时间内完成插入和删除操作，但是由于无法根据下标定位到特定元素，因此不能在 O(1) 的时间内完成获取随机元素操作。为了满足插入、删除和获取随机元素操作的时间复杂度都是 O(1)，需要将变长数组和哈希表结合，变长数组中存储元素，哈希表中存储每个元素在变长数组中的下标。

import random
# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.lis = []
        self.se = {}

    def insert(self, val: int) -> bool:
        if val in self.se:
            return False
        else:
            #print('insert',self.lis,self.se)
            self.lis.append(val)
            self.se[val] = len(self.lis) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.se:
            #print('delete',self.lis,self.se)
            self.lis[self.se[val]] = self.lis[-1]
            self.se[self.lis[-1]] = self.se[val]
            self.lis.pop()
            self.se.pop(val)
            
            return True
        else:
            return False

    def getRandom(self) -> int:
        ele = random.choice(self.lis)
        return ele



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

