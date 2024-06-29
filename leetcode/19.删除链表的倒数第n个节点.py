#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # need 2 traversal
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        le = 1
        i = 1
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while(cur.next):
            le += 1
            cur = cur.next
        cur = dummy
        while(cur.next):
            if i == le - n + 1:
                cur.next = cur.next.next
                break
            i += 1
            cur = cur.next
        return dummy.next
    # only 1 traversal
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        cur2 = dummy
        i = 0
        while cur.next:
            if i < n:
                cur = cur.next
            else:
                cur = cur.next
                cur2 = cur2.next
            i += 1
        cur2.next = cur2.next.next
        return dummy.next
# @lc code=end

