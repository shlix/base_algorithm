#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class DoubleLinkedList:
    def __init__(self, key: int, value:int):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.dic = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dic:
            cur = self.dic[key]
            self.update(cur)

            return cur.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.dic:
            cur = DoubleLinkedList(key, value)
            if len(self.dic) == self.capacity:
                self.delete()
            self.add(cur)
            self.dic[key] = cur
        else:
            cur = self.dic[key]
            cur.value = value
            self.update(cur)

            
    def update(self,cur: DoubleLinkedList) -> None:
        if cur == self.head:
            return
        pre = cur.pre
        next = cur.next

        if pre:
            pre.next = next
        if next:
            next.pre = pre
        else:
            self.tail = pre

        cur.pre = None
        cur.next = self.head
        self.head.pre = cur

        self.head = cur
    
    def add(self, cur) -> None:
        if not self.tail:
            self.head = cur
            self.tail = cur
        else:
            cur.next = self.head
            self.head.pre = cur
            self.head = cur

    def delete(self) -> None:
        self.dic.pop(self.tail.key)
        if not self.tail or not self.tail.pre:
            self.head = None
        if self.tail.pre:
            self.tail.pre.next = None
        self.tail = self.tail.pre



# Your LRUCache object will be instantiated and called as such:
#obj = LRUCache(2)
#param_1 = obj.get(key)
#obj.put(key,value)
# @lc code=end

